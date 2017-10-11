#
# Lets add a new type of article with a posting date and a section
#
import pymongo
import datetime

client  = pymongo.MongoClient()
blogDatabase = client[ "blog" ]
usersCollection = blogDatabase[ "users" ]
articlesCollection = blogDatabase[ "articles" ]

author = "mlynn"
title  = "This is a post on MongoDB"
 
newPost = { "title"    : title,
            "body"     : "MongoDB is the worlds most popular NoSQL database. It is a document database",
            "author"   : author,
            "tags"     : [ "mike", "mongodb", "Philly" ],
            "section"  : "technology",
            "postDate" : datetime.datetime.now(),
}

#
# Lets check if our author exists
#

if usersCollection.find_one( { "username" : author }) :
    articlesCollection.insert_one( newPost )

