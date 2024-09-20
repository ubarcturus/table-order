//Instanziate sqlite3 Module
const sqlite3 = require('sqlite3');

// Creating/Connecting To A Database
const db = new sqlite3.Database('./db.sqlite');


//SQL QUERYS

//CREATE IF NOT EXIST TABLE/S

/* NEW
CREATE TABLE IF NOT EXISTS desks (
	'desk' INTEGER PRIMARY KEY AUTOINCREMENT,
	'active' boolean TRUE,
    'ordernummer' int
	);

CREATE TABLE IF NOT EXISTS product (
	'desk' int PRIMARY KEY,
	'name' int NOT NULL,
	'quantity' char NOT NULL,
	FOREIGN KEY (desk) REFERENCES desks(desk)
	);
    */


	//orderid dynamically

    var order_list = [[]]
    //loop trough items in order_list
    var order = [1, "Apple", 3] //DESK PRODUCT QUANITY
    //ORDER
        //CHECK IF A ORDER PERSISTS (active)
        if (db.get("SELECT active from desks WHERE active = 1 AND desk = "+order[0]+");")){
            db.run("INSERT INTO product (desk, name, quantity) VALUES ("+order[0]+","+order[1]+","+order[2]+");") //append product to order
        }
        else {
            db.serialize(() =>{    //IF FALSE MAKE A NEW ONE
                db.run("INSERT INTO desks (active, desk) VALUES (1,"+order[0]+");"),
                db.run("INSERT INTO product (desk, name, quantity) VALUES ("+order[0]+","+order[1]+","+order[2]+");") //append product to order
         });
        };

    //ORDER RESIVED done 
        //change active to False
