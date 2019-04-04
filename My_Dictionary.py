# we can stored all of this data inside 1 object. such as:
        # the user_id =209
        # message = "D5 E5 C5 C4 G4"
        # language = " Enlgish"
        # datetime = "22929292929"
        #location = (44.590, -104.7155)


# this is how you create a dictionary
post = {"user_id" : 209, "message":"D5 E5 C5 C4 G4", "language":"English", "datetime":"20230215t124231z", "location":(44.590533, -104.715556)}

# we created a dictionary called post with 5 pieces of data
# if we thinking dictionary as a map, we have 5 inputs, and 5 outputs
# in python inputs are called keys, and outputs are called values

print(type(post)) # we can see that post is type "dict"
print(post)

# this time we will create a new dictionary with the dict constructor
post2 = dict (message="SS Cotopaxi", language = "English")
print(post2)

# this is how we add additional data into our dictionary
post2["user_id"] = 209
post2["datetime"] = "19771116t093001z"

print(post2)

# this is how we access data in a dictionary  . p.s: spaces inside the dict count
print(post["message"])

# ways that we can check if a key is in the dictionary
#1st way
if "location" in post2:
    print(post2["location"])
else:
    print("Location key doesn't exist on dictionary")

#2nd way
    try:
        print(post2["location"])
    except KeyError:
        print("Location key doesn't exist on dictionary")

# another way to check if key is on dictionary + error check
print(dir(post2)) # we see a list of methods available to us

print(help(post2.get)) # to see what a method does, use the help method

# now that we now what get does, lets use it

loc =post2.get("location", None) # the None is what we tell get to return if the key its not there
print(loc)

# A common task that a dict does is to iterate over all the key values on the dictionary

# we can to this if we loop over all key , then get the values for each key.

for key in post.keys():
    value = post[key]
    print(key, "=",value)

# another way to see over all values in the dictionary, this time by using the items method which gives the key + the value for each iteration
for key, value in post.items():
    print(key,"=",value)

# to remove data from a dict ,if we want we can check by using dir, and looking through all methods
print (dir(post)) # we can see that pop, and popitem methods allow us to remove 1 item, clear in the other hand removes all data.
