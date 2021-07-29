const pool= require('../utils/database');
const Cart = require('../models/cart');
module.exports = class Orders{

    constructor(user_id){
        
        this.user_id = user_id;
        
    }
    wait(){
        setTimeout(function(){ 
            console.log("waiting");
        }, 1000);
    }
    buy_cart(){
        //var quantity = pool.query('Select quantity from orders where user_id=1 and item_id=$1',[this.item_id]);
        var prom = Cart.get_creds();
        var req_cred = pool.query('SELECT sum(cart.quantity*products.price) from cart inner join products on products.id=cart.item_id;');
        var ret = 1;
        prom.then(async function(creds){
                const cred = creds['rows'][0]['credit'];
                console.log("hereeee");
                req_cred.then(async function(req){
                req = req['rows'][0]['sum'];
                if(cred>=req){
                    console.log("okayyyyyyy",cred, req, cred-req);
                    
                    
                   console.log("done0-1");
                    await pool.query("update orders set quantity=cart.quantity+orders.quantity from cart where orders.user_id=1 and orders.item_id = cart.item_id;\
                         ");
                   console.log("done00");
                    await pool.query("insert into orders \
        select * from cart t1 where t1.user_id=1 and not exists (select 1 from orders t2 where t2.item_id=t1.item_id)");
                    console.log("done10");
                    await pool.query('UPDATE cart set quantity=0');
                    await pool.query('Update users set credit=$2 where user_id=$1;',[1, cred-req]);
                    //return new Promise({"val":1});
                }
                
                }).catch(err => console.log("buy errrir",err));
                //return new Promise({"val":0});

            }).catch(err => console.log("buy errrir",err));
            //return Promise.resolve(prom);


            
        return Promise.resolve(req_cred);
        
       
        
    }
    
    static view_orders(){
        return pool.query('SELECT orders.quantity,products.title,products.image,products.price FROM orders inner join products on orders.item_id=products.id \
            where orders.user_id = 1;');
    }

};