function listed (id, s, m, apps) 
{
    if (s == 0) {
        for (var app in apps) {
            console.log("  " + apps[app].appid);
        }
    }

    process.exit(s);
}

args = process.argv;
libfile = args[2];
operation = args[3]
appfw = require(libfile);

if ( "-a" == operation )
    result = appfw.ListAllApplications(listed);
else if ( "-r" == operation )
    result = appfw.ListRunningApplications(listed);
else
    result = appfw.ListAllApplications(listed);

if (!result) {
    console.log("Fail to list applications");
    process.exit(1);
}


