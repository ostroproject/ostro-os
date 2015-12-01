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
from bb.runqueue import RunQueueSchedulerCompletion as BaseScheduler
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

        # Group tasks of the same kind before tasks of less important
        # kinds at the head of the queue (because earlier = lower
        # priority number = runs earlier). The ordering is rm_work
        # (run as soon as possible) > do_build >
        # do_package_write_ipk/deb/rpm > and so on, because then tasks
        # that complete a certain recipe come before tasks from other
        # recipes that would otherwise interrupt completing the
        # initial recipe.
        #
        # For example, when foo has a higher priority than bar, but
        # DEPENDS on bar, then the implicit rule (from base.bbclass)
        # is that foo's do_configure depends on bar's
        # do_populate_sysroot. When that is done, normally the tasks
        # from foo would continue to run and bar only gets completed
        # and cleaned up later. By ordering bar's task after
        # do_populate_sysroot before foo's do_configure, that problem
        # gets avoided.
        #
        # The list itself is hard-coded based on current tasks and
        # sorted topologically; should new tasks get added, the whole
        # scheme breaks again. Not all tasks listed here have to
        # exist, so it is okay to list all three potential package
        # formats.
        task_index = 0
        for task in ('do_rm_work',
                     'do_build',
                     'do_package_write_ipk',
                     'do_package_rpm',
                     'do_package_deb',
                     'do_package_qa',
                     'do_packagedata',
                     'do_package',
                     'do_populate_lic',
                     'do_populate_sysroot',
                     'do_install',
                     'do_compile',
                     'do_configure',
                     'do_patch',
                     'do_unpack',
                     'do_fetch'):
            for index in xrange(task_index, self.numTasks):
                taskid = self.prio_map[index]
                taskname = self.rqdata.runq_task[taskid]
                if taskname == task:
                    del self.prio_map[index]
                    self.prio_map.insert(task_index, taskid)
                    task_index += 1

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
