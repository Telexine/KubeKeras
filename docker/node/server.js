'use strict';
var request = require('request');
const express = require('express');
var path = require('path'),
bodyParser = require('body-parser')
// Constants
const PORT = 8888;
const HOST = '0.0.0.0';


// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello world v3\n');
});

app.use(express.static('public'));
app.use(bodyParser.json());
 

app.post('/colorize', (req, res) => {
  let data = {
    api_key: "DD"
  };
  request.post("http://0.0.0.0:5000/gen"/*,{formData:data}*/, function optionalCallback(err, httpResponse, body) {
    if (err) {
      return console.error('analize failed:', err);
    }
    var result =  body;
    console.log(result)
    res.send(result)
  });
});


app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);