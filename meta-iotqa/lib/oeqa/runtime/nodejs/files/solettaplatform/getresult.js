var fs = require( "fs" );

var jsonFilename = require( "path" ).resolve( __dirname, "results.json" );

var date = new Date(),
  data = "",
  caseList = [],
  setList = [],
  allList = [],
  test = {},
  testInfo = {};

exports.getTestResult = function( status, success, failure  ) {

  if ( status.result ) {
    success = "PASS";
  } else if ( !status.result ) {
    failure = "FAIL";
  }

  testInfo = {
    "message": (  status.runtime  + ": " + status.message ),
    "result": ( status.result ? success : failure ),
    "runtime": ( date.toLocaleTimeString() )
  };

  if ( setList.indexOf( status.name ) > -1 && ( "results" in test ) ) {
    test.results.push( testInfo );
    caseList.push( test );
  } else {
    setList.push( status.name );
    test = { "test": status.name, "results": [ testInfo ] };
    caseList.push( test );
    allList.push( test );
  }

  data = JSON.stringify( { "output": allList }, null, 4 );
  fs.writeFileSync( jsonFilename, data );
};
