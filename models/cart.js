const pool= require('../utils/database');
module.exports = class Cart{

    constructor(item_id, user_id){
        this.item_id = item_id;
        this.user_id = user_id;
    }
    //const wait=ms=>new Promise(resolve => setTimeout(resolve, ms)); 
    add_to_cart(){
        const user_id = this.user_id;
        const item_id = this.item_id;
        var prom = pool.query('Select quantity from products where id=$1;',[this.item_id]);
        var ret = 1;
        prom.then(async function(avail_quant){
            var avail = avail_quant['rows'][0]['quantity'];
            console.log(avail,"avail",avail>0);
            if(avail>0){
                var prom = Promise.resolve(pool.query('Select quantity from cart where user_id=1 and item_id=$1;',[item_id]));
                console.log("imma inside");
                prom.then(function(quantity){
                pool.query('UPDATE products set quantity=$1 where id=$2;', [avail-1, item_id]); 
                    try
                    {
                    var qty = quantity['rows'][0]['quantity'];
                    
                    pool.query('UPDATE cart set quantity=$1 where item_id=$2 and user_id=$3;', [qty+1, item_id,user_id]);
                   
                    }
                    catch(err){
                        pool.query('INSERT into cart(user_id,item_id,quantity) VALUES ($1, $2, $3);', [user_id, item_id,1]);
                        
                        //console.log(err);
                    }
                }).catch(err => console.log(err));
                //return new Promise(()=>{var val=1});
            }  
            
        }).catch(err => console.log(err));
        return Promise.resolve(prom);
        
    }
    static get_cart_items(){
        //console.log("inside");
        return pool.query('SELECT cart.quantity,products.title,products.image,products.price FROM cart inner join products on cart.item_id=products.id;');

    }
    static get_creds(){
        return pool.query('SELECT credit from users where user_id=$1;',[1]);
        var prom = Promise.resolve(pool.query('SELECT credit from users where user_id=$1;',[1]));
        prom.then(function(creds){
            //console.log("creds",creds, creds['rows'][0]['credit']);
            return creds;
        }).catch(err => console.log(err));
    }

};