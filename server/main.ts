import {require} from "../node_modules/requires/"


//Instanziate sqlite3 Module
const sqlite3 = require('sqlite3');
const http = require('node:http');
const fs = require('fs');

// Node.js init
const hostname = '127.0.0.1';
const port = 3000;

fs.readFile('../index.html', function (err, html) {
    if (err) {
        throw err; 
    }  

const server = http.createServer((req, res) => {
    res.writeHeader(200, {"Content-Type": "text/html"});  
    res.write(html);  
    res.end();
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
}); 
// Creating/Connecting To A Database
const db = new sqlite3.Database('./db.sqlite');


//SQL QUERYS

//CREATE IF NOT EXIST TABLE/S

/* NEW
CREATE TABLE IF NOT EXISTS desks (
	'desk' INTEGER PRIMARY KEY AUTOINCREMENT,
	'active' boolean TRUE,
    'ordernumber' int
	);

CREATE TABLE IF NOT EXISTS product (
	'name' int NOT NULL,
	'quantity' char NOT NULL,
	FOREIGN KEY (ordnenumber) REFERENCES desks(desk)
	);
    */


	//orderid dynamically

var order_list = [] ////DESK, ORDER_ACITVE,[PRODUCT, QUANTITY]
var order_active = 0
//loop trough items in order_list
for (var order in order_list[3])
{
    //ORDER
    //CHECK IF A ORDER PERSISTS (active)
    if (db.get("SELECT active from desks WHERE active = 1 AND desk = "+order_active+");")){
        db.run("INSERT INTO product (desk, name, quantity) VALUES ("+order_active+","+order[1]+","+order[2]+");") //append product to order
    }
    else {
        db.serialize(() =>{    //IF FALSE MAKE A NEW ONE
            db.run("INSERT INTO desks (active, desk) VALUES (1,"+order_active+");"),
            db.run("INSERT INTO product (desk, name, quantity) VALUES ("+order_active+","+order[1]+","+order[2]+");") //append product to order
        });
    };
}
//ORDER RESIVED done 
//change active to False and remove products needs a failsave
