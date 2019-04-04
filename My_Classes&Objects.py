import datetime
# classes fundamental tool
# class are like templates for creating objects with relative data, and functions that do stuff with that data

class User: # this is how we create a class
    """ Testing for the doc string for responsible purposes """

    def __init__(self,full_name,birthday): # init method : a function inside a class, this method is called every time you create a new instance to the class
                                           # init = initialization, other languages is known as a constructor.
                                           # self = it's the first argument to this method,
                                           # self  it's a reference to the new object that it's being created

        self.name = full_name       # stored this values to fields in the object. # the field is "name" after self
        self.birthday = birthday    # birthday field it's different from birthday value. the field stores the value
        # extract the first and last names
        name_pieces = full_name.split(" ") # cut name in pieces whenever there's a space, the pieces will be stored in an array
        self.first_name = name_pieces[0] # the first string in the array
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4]) #yyyy mm dd
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) # date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days/365
        return int(age_in_years)


user = User("Carles Puyol", "19710315")
print(user.name)
print(user.birthday)
print(user.first_name)
print(user.last_name)
help(User)
print("user age:")
print(user.age())


#user1 = User() #ex: this is how create a user by calling the class, user1 is an "instance" of User, or an object of Class
#user1.first_name = "Dave"
#user1.last_name = "Bowman"  # first_name, and last_name are "fields" since they are attached to an object

#print(user1.first_name) # this is how we access the data user1."field"
#print(user1.last_name)

#user2 = User()
#user2.first_name = "Frank"
#user2.last_name = "Poole"

#print(user2.first_name)
#print(user2.last_name)

#user1.age = 37          # Attaching additional fields don't required to be all strings, you can have integers.
#user2.favorite_book = "2001 : A Space Odyssey"

# additional features of classes adding methods, using object initialization , including help text
