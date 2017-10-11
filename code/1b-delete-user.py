'''
Created on 08 Oct 2017
@author: mlynn
'''
import pymongo
#
# client defaults to localhost and port 27017. eg MongoClient('localhost', 27017)
#
client  = pymongo.MongoClient()
blogDatabase = client[ "blog" ]
usersCollection = blogDatabase[ "users" ]
result = usersCollection.delete_many({'username': 'mlynn'})
print( result )