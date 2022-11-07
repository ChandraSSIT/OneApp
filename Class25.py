# API Testing
#  API (Application Program Interface)
# The API is the middle ware between database and UI(user interface)
# The main job of API is to send or receive data from database
# Manual test of API => Post man (this is a tool)
# we can check in browser also
# webservices , Rest API
# webservices => it gives response only xml format
# Rest API => it supports Json,XML
# what are the things we need to consider to call API
   # Methods( get,post,put,patch,delete)
   # URL (uniform resource locator)
   # Headers
   # Body
   # we will see result in response

   # Get => will use when we want to fetch the existing records , here we can not pass body, we can pass
   # header information
   # how will pass the data with get api => query parameter or path parameter
#    query parameter => we will use the ?page=2 ,
# path parameter => we will pass the value with url by appending with slash(/)

# HTTP Status codes
# 100
# 200 => Success Response =>
# 300
# 400  => Client Error =>
# 500  => Server Error =>

# To test anything , we need to follow some scenarios
# Positive scenarios
# Negative
# boundary scenarios => Minimum and maximum
