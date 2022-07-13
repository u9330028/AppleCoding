const express = require('express');
const { Pool } = require('pg');

const pg = new Pool({
    user: 'postgres',
    host: '127.0.0.1',
    database: 'palida',
    password: 'qlrgnlf',
    port: 5432
})

// const app = express.Router();
const app = express();
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }))

app.listen(3389, () => {
    console.log('listening 0n 8080');
})


app.get('/', (Req, Res) => {
    // Res.send("Port is 3389");
    Res.sendFile(__dirname + '/Html/index.html')
})

app.get('/write', (Req, Res) => {
    // Res.send("Port is 3389");
    Res.sendFile(__dirname + '/Html/write.html')
})

app.get('/pet', (Req, Res) => {
    console.log(Req);
    Res.send("this page is PET Shopping Mall.!!")
})

app.get('/beauty', (Req, Res) => {
    //console.log(`Req Name is ${Req.query.name}`);
    //Res.send("this page is beauty Shopping Mall.!!\n name :" + Req.query.name);
})

app.post('/add', (Req, Res) => {
    console.log(Req.body);
    console.log(Req.body.Email);
    console.log(Req.body.Pwd);
    console.log(Req.body.Check);
    postGreSql();
})

let postGreSql = () => {
    console.log('********');
    pg.connect();
    console.log('********');
    pg.query('SELECT * FROM kitchen_printer', (err, res) => {
        console.log(err, res);
        pg.end();
    })
}