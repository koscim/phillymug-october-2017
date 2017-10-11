import pymongo
#
# client defaults to localhost and port 27017. eg MongoClient('localhost', 27017)
#
client  = pymongo.MongoClient()
blogDatabase = client[ "blog" ]
usersCollection = blogDatabase[ "users" ]
articlesCollection = blogDatabase[ "articles" ]
author = "mlynn"
article = { "title"  : "This is my first post",
            "body"   : "The is the longer body text for my blog post. We can add lots of text here.",
            "author" : author,
            "tags"   : [ "mlynn", "general", "Philly", "admin" ]
}
#
# Lets check if our author exists
#
if usersCollection.find_one( { "username" : author }) :
    result = articlesCollection.insert_one( article )
    print result
else:
    raise ValueError( "Author %s does not exist" % author )