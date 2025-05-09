This is the home assessment for 24x7

This is the main structures of the program
* routers -> stores all endpoint
* services -> logic function communicating from endpoint to repository
* repositories -> query transaction directly to database
* utils -> all utility scripts
  * logger -> integration of logger to the app
  * dependencies -> functions that will needed inside a router
* db/config.py -> configuration of the database (I am using Supabase PostgreSQL)
