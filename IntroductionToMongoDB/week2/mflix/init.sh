#! /bin/bash

source ./env.sh

mongorestore --drop --uri "$MFLIX_DB_URI" data/dump