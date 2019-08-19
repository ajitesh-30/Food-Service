# Food-Service
A Food Service API

## Requirements

      Django==2.1.2
      Python=3.x

## API Endpoints

### Customer

Get all foods 

      GET /api/v1/food/
      
Get an individual food item

      GET /api/v1/food/<food_item>
      
Add one of more food item to cart

      POST /api/v1/cart/ -d 
      {
        user : user instance,
        item : food_item instance,
        quantity : quantity of food item
      }


View Cart

      GET /api/v1/cart/<user_id>
 
Checkout
      
      GET /api/v1/cart/checkout/<user_id>
      
Order Details

      GET /api/v1/cart/order/<user_id>
      

### Food Delivery Service

Get all pending orders

      GET /api/v1/pending

Mark pending orders as delivered/shipped

      POST /api/v1/cart/pending -d
      {
          cart_id : Id of cart to be marked as shipped
      }
      
  
