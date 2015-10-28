
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
        case "--all":
        case "-a":
            app.which = "all";
            i++;
            break;

        case "--running":
        case "-r":
            app.which = "running";
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
}


var App = function () {
    this.iot = null;
    this.which = "all";
};


function ListCB (id, status, msg, apps) {
    console.log("Got reply for app list request " + id + "(" + status +
                ":" + msg + ")");

    if (status == 0) {
        console.log("Got a list of " + apps.length + " applications");
        for (var i in apps) {
            console.log("  " + apps[i].appid);
        }
    }

    process.exit(status);
}



/////////////////////////
// main script


var app = new App();

parse_cmdline(app, process.argv);


if (app.which == "running")
    req = app.iot.ListRunningApplications(ListCB);
else
    req = app.iot.ListAllApplications(ListCB);

if (!req) {
    console.log("Failed to query " + app.which + " applications.");
    process.exit(1);
}
else
    console.log("Got request id " + req);
    


