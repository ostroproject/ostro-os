# Author:       Patrick Ohly <patrick.ohly@intel.com>
# Copyright:    Copyright (C) 2015 Intel Corporation
#
# This file is licensed under the MIT license, see COPYING.MIT in
# this source distribution for the terms.

# A custom scheduler for bitbake which runs rm_work tasks more
# aggressively than the default schedule chosen by rm_work.
# To use it, add to local.conf:
#   BB_SCHEDULERS = "rmwork.RunQueueSchedulerRmWork"
#   BB_SCHEDULER = "rmwork"
# Then run:
#   PYTHONPATH=<path to the directory with rmwork.py> bitbake ...
#
# Optionally, set BB_NUMBER_COMPILE_THREADS to a number <= BB_NUMBER_THREADS
# to limit the number of compile tasks running in parallel. In other words,
# this allows to run more light tasks without overloading the machine with too
# many heavy compile tasks.

import bb
from bb.runqueue import RunQueueSchedulerSpeed as BaseScheduler
import time

class RunQueueSchedulerRmWork(BaseScheduler):
    """
    Similar to RunQueueSchedulerCompletion, but in addition, rm_work tasks
    get a priority higher than anything else and get run even when the maximum
    number of tasks is reached. Together this ensures that nothing blocks running
    the rm_work tasks once they become ready to run.
    """
    name = "rmwork"

    def __init__(self, runqueue, rqdata):
        BaseScheduler.__init__(self, runqueue, rqdata)

        self.number_compile_tasks = int(self.rq.cfgData.getVar("BB_NUMBER_COMPILE_THREADS", True) or \
                                        self.rq.number_tasks)
        if self.number_compile_tasks > self.rq.number_tasks:
            bb.fatal("BB_NUMBER_COMPILE_THREADS %d must be <= BB_NUMBER_THREADS %d" % \
                     (self.number_compile_tasks, self.rq.number_tasks))
        bb.note('BB_NUMBER_COMPILE_THREADS %d BB_NUMBER_THREADS %d' % \
                (self.number_compile_tasks, self.rq.number_tasks))

        # Extract list of tasks for each recipe, with tasks sorted
        # ascending from "must run first" (typically do_fetch) to
        # "runs last" (do_rm_work). Both the speed and completion
        # schedule prioritize tasks that must run first before the ones
        # that run later; this is what we depend on here.
        task_lists = {}
        for taskid in self.prio_map:
            fn = self.rqdata.get_task_file(taskid)
            taskname = self.rqdata.get_task_name(taskid)
            task_lists.setdefault(fn, []).append(taskname)

        # Now unify the different task lists. The strategy is that
        # common tasks get skipped and new ones get inserted after the
        # preceeding common one(s) as they are found. Because task
        # lists should differ only by their number of tasks, but not
        # the ordering of the common tasks, this should result in a
        # deterministic result that is a superset of the individual
        # task ordering.
        all_tasks = task_lists.itervalues().next()
        for recipe, new_tasks in task_lists.iteritems():
            index = 0
            old_task = all_tasks[index] if index < len(all_tasks) else None
            for new_task in new_tasks:
                if old_task == new_task:
                    # Common task, skip it. This is the fast-path which
                    # avoids a full search.
                    index += 1
                    old_task = all_tasks[index] if index < len(all_tasks) else None
                else:
                    try:
                        index = all_tasks.index(new_task)
                        # Already present, just not at the current
                        # place. We re-synchronized by changing the
                        # index so that it matches again. Now
                        # move on to the next existing task.
                        index += 1
                        old_task = all_tasks[index] if index < len(all_tasks) else None
                    except ValueError:
                        # Not present. Insert before old_task, which
                        # remains the same (but gets shifted back).
                        # bb.note('Inserting new task %s from %s after %s at %d into %s' %
                        #         (new_task, recipe,
                        #          all_tasks[index - 1] if index > 0 and all_tasks else None,
                        #          index,
                        #          all_tasks))
                        all_tasks.insert(index, new_task)
                        index += 1
        # bb.note('merged task list: %s'  % all_tasks)

        # Now reverse the order so that tasks that finish the work on one
        # recipe are considered more imporant (= come first). The ordering
        # is now so that do_rm_work[_all] is most important.
        all_tasks.reverse()

        # Group tasks of the same kind before tasks of less important
        # kinds at the head of the queue (because earlier = lower
        # priority number = runs earlier), while preserving the
        # ordering by recipe. If recipe foo is more important than
        # bar, then the goal is to work on foo's do_populate_sysroot
        # before bar's do_populate_sysroot and on the more important
        # tasks of foo before any of the less important tasks in any
        # other recipe (if those other recipes are more important than
        # foo).
        #
        # All of this only applies when tasks are runable. Explicit
        # dependencies still override this ordering by priority.
        #
        # Here's an example why this priority re-ordering helps with
        # minimizing disk usage. Consider a recipe foo with a higher
        # priority than bar where foo DEPENDS on bar. Then the
        # implicit rule (from base.bbclass) is that foo's do_configure
        # depends on bar's do_populate_sysroot. This ensures that
        # bar's do_populate_sysroot gets done first. Normally the
        # tasks from foo would continue to run once that is done, and
        # bar only gets completed and cleaned up later. By ordering
        # bar's task after do_populate_sysroot before foo's
        # do_configure, that problem gets avoided.
        task_index = 0
        # self.dump_prio('Original priorities from %s' % BaseScheduler)
        for task in all_tasks:
            for index in xrange(task_index, self.numTasks):
                taskid = self.prio_map[index]
                taskname = self.rqdata.runq_task[taskid]
                if taskname == task:
                    del self.prio_map[index]
                    self.prio_map.insert(task_index, taskid)
                    task_index += 1
        # self.dump_prio('rmwork priorities')

    def next(self):
        taskid = self.next_buildable_task()
        if taskid is not None:
            if self.rq.stats.active < self.rq.number_tasks:
                # Impose additional constraint on the number of compile tasks.
                # The reason is that each compile task itself is allowed to run
                # multiple processes, and therefore it makes sense to run less
                # of them without also limiting the number of other tasks.
                taskname = self.rqdata.runq_task[taskid]
                if taskname == 'do_compile':
                    active = [x for x in xrange(self.numTasks) if \
                              self.rq.runq_running[x] and not self.rq.runq_complete[x]]
                    active_compile = [x for x in active if self.rqdata.runq_task[x] == 'do_compile']
                    if len(active_compile) >= self.number_compile_tasks:
                        # bb.note('Not starting compile task %s, already have %d running: %s' % \
                        #         (self.describe_task(taskid),
                        #          len(active_compile),
                        #          [self.describe_task(x) for x in active]))
                        # Enabling the debug output above shows that it gets triggered even
                        # when nothing changed. Returning None here seems to trigger some kind of
                        # busy polling. Work around that for now by sleeping.
                        time.sleep(0.1)
                        return None
                return taskid

    def describe_task(self, taskid):
        result = 'ID %d: %s' % (taskid, self.rqdata.get_user_idstring(taskid))
        if self.rev_prio_map:
            result = result + (' pri %d' % self.rev_prio_map[taskid])
        return result

    def dump_prio(self, comment):
        bb.note('%s (most important first):\n%s' %
                (comment,
                 '\n'.join(['%d. %s' % (index + 1, self.describe_task(taskid)) for
                            index, taskid in enumerate(self.prio_map)])))
