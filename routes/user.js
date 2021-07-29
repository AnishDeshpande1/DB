
const path = require('path');
const express = require('express');

const userCon = require('../controllers/user');

const router = express.Router();

router.get('/prods',userCon.get_products);
//router.post('/prods',userCon.add_to_cart);
router.get('/cart',userCon.view_cart);
router.post('/cart',userCon.add_to_cart);
router.post('/orders',userCon.buy_cart);
router.get('/orders',userCon.view_orders);

module.exports = router;