'''
Created on 17 Sep 2017
@author: mlynn
'''
import pymongo
#
# client defaults to localhost and port 27017. eg MongoClient('localhost', 27017)
client  = pymongo.MongoClient()
blogDatabase = client[ "blog" ]
usersCollection = blogDatabase[ "users" ]

usersCollection.insert_one( { "username" : "mlynn", 
                              "password" : "no peeking", 
                              "lang" : "EN" })
user = usersCollection.find_one()
print( user )
