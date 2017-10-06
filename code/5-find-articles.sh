#!/bin/sh
mongo <<EOD
db.users.findOne()

EOD


