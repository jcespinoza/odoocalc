var express = require('express');
var cors = require('cors');
var app = express();

app.use(cors());

// respond with "hello world" when a GET request is made to the homepage
app.get('/odoocalc/calculate', function (req, res) {
    res
        .status(200)
        .json({
            result:{
                success: true,
                errorMessage: 'Something went pretty bad, sorry',
                output: 1 + 9
            }
        });
});

// respond with "hello world" when a GET request is made to the homepage
app.post('/odoocalc/calculate', function (req, res) {
    res
        .status(200)
        .json({
            result:{
                success: true,
                errorMessage: 'Something went pretty bad, sorry',
                output: 2 + 9
            }
        });
});

app.listen(8069);