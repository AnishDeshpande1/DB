const Prod = require('../models/prod');
const Cart = require('../models/cart');
const Order = require('../models/orders');

exports.get_products = (req,res,next) => {
	
    const product_arr = Prod.get_all();
    Promise.resolve(0);
	
	Prod.get_all().then((product_arr)=>{
		console.log(product_arr['rows']);
		res.render('includes/prods', {
        pageTitle: 'Add Product',
        path: '/prods',
        editing: false,
        prod_arr: product_arr['rows'] });
	}).catch(err => console.log(err));
       
};

exports.add_to_cart = (req,res,next) => {

	const item_id = req.body.product_id;
	const user_id = 1;
	const quantity = 1;

	const cart_item =  new Cart(item_id,1);
	//console.log(cart_item);
	cart_item.add_to_cart().then(function(val){
		console.log("Value",val['rows'][0]['quantity']>0);
		if(val['rows'][0]['quantity']>0)
		setTimeout(function(){ res.redirect('/cart'); }, 1000);
	});
	

};

exports.view_cart = (req,res,next) => {
	//setTimeout(function(){
	var prom = Promise.resolve(Cart.get_creds());
	prom.then(function(creds){
//}
	//	,1000);
	//console.log("credit",creds['rows'][0]['credit'], creds);
	Cart.get_cart_items()
	.then(function(concat_array){
		console.log("okayy");
		//console.log(concat_array, concat_array[1]);
		//console.log(concat_array);
		try{
			res.render('includes/cart', {
	        pageTitle: 'Cart',
	        path: '/cart',
	        editing: false,
	        cart_arr:  concat_array['rows'], 
	    	credits: creds['rows'][0]['credit'] });
			
		}catch(err) {
			console.log(err);
		}
	
	}).catch(err => console.log(err));
	}).catch(err => console.log(err));
};

exports.buy_cart = (req,res,next) => {

	
	const user_id = 1;
	

	const order =  new Order(1);
	var prom = Promise.resolve(Cart.get_creds());
	prom.then(function(creds){
		order.buy_cart().then(function(val){
			console.log("Value",creds['rows'][0]['credit']>val['rows'][0]['sum']);
			if(creds['rows'][0]['credit']>val['rows'][0]['sum'])
			setTimeout(function(){ res.redirect('/orders'); }, 1000);
	    }).catch(err => console.log(err));
	}).catch(err => console.log(err));

};



exports.view_orders = (req,res,next) => {

	Order.view_orders()
	.then(function(concat_array){
		//console.log(concat_array);
		////WAIT FOR APPROPRIATE TIME BEFORE QUERY EXECUTES
		try{
			res.render('includes/orders', {
	        pageTitle: 'Order',
	        path: '/orders',
	        editing: false,
	        orders:  concat_array['rows'], 
	    	});
			
		}catch(err) {
			console.log(err);
		}
	
	}).catch(err => console.log(err));
	
};
