/*
 * Copyright (c) 2015, Intel Corporation
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 *
 *   * Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *   * Neither the name of Intel Corporation nor the names of its contributors
 *     may be used to endorse or promote products derived from this software
 *     without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */


/////////////////////////
// parse event lists
//
function parse_events(app) {
    app.events = app.evlist.split(",").map(function (s) { return s.trim(); });
    if (app.quit_event == null) {
        app.quit_event = app.events[app.events.length - 1];
        app.events.pop();
    }
}

/////////////////////////
// parse command line
//
function parse_cmdline(app, argv) {
    var i, opt, optarg, d, libdir;

    i = 2;
    d = [];
    libdir = "";
    while (i < argv.length) {
        optstr = argv[i];
        optarg = argv[i + 1];
        
        switch (optstr) {
        case "--label":
        case "-l":
            app.label = optarg;
            i += 2;
            break;

        case "--appid":
        case "-a":
            app.appid = optarg;
            i += 2;
            break;

        case "--binary":
        case "-b":
            app.binary = optarg;
            i += 2;
            break;

        case "--user":
        case "-u":
            app.user = optarg;
            i += 2;
            break;

        case "--process":
        case "-p":
            app.process = optarg;
            i += 2;
            break;

        case "--events":
        case "-e":
            app.evlist = optarg;
            i += 2;
            break;

        case "--quit":
        case "-q":
            app.quit_event = optarg;
            i += 2;
            break;

        case "--data":
        case "-D":
            app.data = optarg;
            i += 2;
            break;

        case "--nevent":
        case "-n":
            app.nsend = optarg;
            i += 2;
            break;

        case "--interval":
        case "-I":
            app.delay = optarg;
            i += 2;
            break;

        case "--debug":
        case "-d":
            d[d.length] = optarg;
            i += 2;
            break;

        case "--libdir":
        case "-L":
            libdir = optarg;
            i += 2;
            break;

        default:
            console.log("Invalid/unknown option '" + optstr + "'");
            process.exit(0);
        }
    }

    app.iot = require(libdir ? libdir + "/iot-appfw.node" : "iot-appfw.node");
    app.iot.SetDebug(d);

    parse_events(app);
}


var App = function () {
    this.iot = null;
    this.label = null;
    this.appid = null;
    this.binary = null;
    this.user = process.env['USER'];
    this.process = 0;
    this.data = null;
    this.delay = 1000;
    this.evlist = "hello,ahoy,aloha,goodbye";
    this.quit_event = null;
    this.cnt = 0;
    this.nsend = 10;

    this.SendEvent = function (event) {
        var dst = { };

        if (this.data)
            eval("data = " + this.data);
        else
            data = {};

        if (this.label) dst.label = this.label;
        if (this.appid) dst.appid = this.appid;
        if (this.binary) dst.binary = this.binary;
        if (this.user) dst.user = this.user;
        if (this.process) dst.process = this.process;

        data.count = this.cnt;

        this.iot.SendEvent(event, dst, data);

        this.cnt++;
    };
};


/////////////////////////
// timer callback - send an event
function timer_cb () {
    var event = app.events[app.cnt % app.events.length];

    if (app.cnt > app.nsend)
        process.exit(0);

    if (app.cnt < app.nsend)
        event = app.events[app.cnt % app.events.length];
    else
        event = app.quit_event;

    app.SendEvent(event);

    setTimeout(timer_cb, app.delay);
}

/////////////////////////
// main script


var app = new App();

parse_cmdline(app, process.argv);

setTimeout(timer_cb, app.delay);
