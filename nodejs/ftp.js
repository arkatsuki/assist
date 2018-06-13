var Client = require('ftp');

  var c = new Client();
  c.on('ready', function() {
	  console.log('ready!')
    // c.list(function(err, list) {
    //   if (err) throw err;
    //   console.dir(list);
    //   c.end();
    // });
  });
  // connect to localhost:21 as anonymous
  c.connect({
  host: '192.168.200.238',
  port: 21,
  username: 'dev-sc',
  password : 'hgHHJ?@!#'
});