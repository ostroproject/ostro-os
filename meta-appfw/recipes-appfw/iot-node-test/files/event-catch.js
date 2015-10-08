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

var Dumper = function (init) {
    this.buf = "";
    this.nl = false;
    this.depth = 0;

    if (init)
        for (var k in init)
            this[k] = init[k];
    
    this.indent = function (o) {
        var s = "";

        if (this.nl)
            for (var i = 0; i < this.depth; i++)
                s += "  ";

        return s + o;
    };

    this.append = function (str) {
        var n = str.length;

        this.buf += str;
        this.nl = n ? str[n - 1] == '\n' : false;
    };
    
    this.dump = function (o) {
        var k, v, e;

        switch (typeof(o)) {
        case typeof(""):
        case typeof(1):
        case typeof(1.2):
        case typeof(true):
            this.append(this.indent(o) + "\n");
            break;

        case typeof({}):
            if (o.constructor != Array) {
                this.append(this.indent("{\n"));

                this.depth++;
                for (k in o) {
                    v = o[k];
                    this.append(this.indent(k + ": "));
                    this.dump(v);
                }
                this.depth--;

                this.append(this.indent("}\n"));
            }
            else {
                this.append(this.indent("[\n"));

                this.depth++;
                for (e in o)
                    this.dump(o[e]);
                this.depth--;

                this.append(this.indent("]\n"));
            }
            break;

        default:
            this.append(this.indent("???" + o));
            break;
        }

        return this.buf;
    }
}


function parse_events(app) {
    app.events = app.evlist.split(",").map(function (s) { return s.trim(); });
    if (app.quit_event == null)
        app.quit_event = app.events[app.events.length - 1];
    else
        app.events.push(app.quit_event);
}


function parse_cmdline(app, argv) {
    var i, opt, optarg, d, libdir;

    i = 2;
    d = [];
    libdir = "";
    while (i < argv.length) {
        optstr = argv[i];
        optarg = argv[i + 1];
        
        switch (optstr) {
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

        case "--signals":
        case "-s":
            app.bridge_signals = true;
            i++;
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
    this.evlist = "hello,ahoy,aloha,goodbye";
    this.quit_event = null;
    this.bridge_signals = false;
};


/////////////////////////
// main script


var app = new App();

parse_cmdline(app, process.argv);

app.iot.onIOTEvent = function (event, event_data) {
    var d = new Dumper({ depth: 4 });

    console.log("Received events <" + event + ">");
    console.log("  with data: " + d.dump(event_data));

    if (event == app.quit_event)
        process.exit(0);
}

if (app.bridge_signals) {
    app.iot.BridgeSystemSignals();
}

process.on('SIGHUP', function () { console.log("Got SIGHUP..."); });

app.iot.SubscribeEvents(app.events);

