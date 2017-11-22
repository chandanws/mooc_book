#!/bin/bash

export FLASK_APP=mflix/mflix.py
export FLASK_DEBUG=false
export MFLIX_DB_URI="mongodb://analytics:analytics-password@mflix-shard-00-00-mz7dv.mongodb.net:27017, mflix-shard-00-01-mz7dv.mongodb.net:27017, mflix-shard-00-02-mz7dv.mongodb.net:27017/mflix?ssl=true&replicaSet=mflix-shard-0&authSource=admin" # Replace it with your MongoDB Connection URI