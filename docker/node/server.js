'use strict';
var request = require('request');
const express = require('express');
var path = require('path'),
fs = require('fs'),
bodyParser = require('body-parser')
var multer  = require('multer')
// Constants
const PORT = 8888;
const HOST = '0.0.0.0';
// App
const app = express();
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use('/static',express.static('static'));
app.use('/node_modules',express.static('node_modules'));
app.use('/css',express.static('node_modules/materialize-css/dist/css'));
app.use('/js',express.static('node_modules/materialize-css/dist/js'));
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname+'/static/index.html'));
});

var upload = multer({ dest: 'uploads/' })


app.post('/colorize',upload.single('image') ,(req, res,next) => {
 


  //console.log(req.file)
  /** RESPONSE
   
  { fieldname: 'image',
  originalname: 'f1920x960.jpeg',
  encoding: '7bit',
  mimetype: 'image/jpeg',
  destination: 'uploads/',
  filename: '0d13a5aa9acad5994a6957d9b7649996',
  path: 'uploads/0d13a5aa9acad5994a6957d9b7649996',
  size: 386996 }


  const options = {
    method: "POST",
    url: "http://127.0.0.1:5000/gen",
    port: 5000,
    headers: {
        "Content-Type": "image/jpeg"
    },
    formData : {
        "image" : fs.createReadStream(req.file.path)
    }
  };
 
  request(options, function (err, res, body) {
    if(err) console.log(err);
    console.log(body);
  });
   */
  let newfn = req.file.destination+req.file.filename+"."+req.file.mimetype.substr(req.file.mimetype.indexOf("/")+1,req.file.mimetype.length);
  console.log(newfn)
  fs.rename(req.file.path,newfn, function (err) {
    if (err) throw err;
    fs.stat(newfn, function (err, stats) {
      if (err) throw err;
      console.log('stats: ' + JSON.stringify(stats));


  var formData = {
    file: fs.createReadStream(newfn)
  };
  
  request.post({url:'http://127.0.0.1:5000/gen', formData: formData}, function(err, httpResponse, body) {
    if (err) {
      return console.error('upload failed:', err);
    }
    console.log('Upload successful!  Server responded with:', body);
  });
  res.status(200).send("ok");
  /*

  });

  */
  });
  });
});


app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);