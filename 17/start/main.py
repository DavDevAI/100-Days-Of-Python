class User:

    def __init__(self,user_id,username): #THIS IS OUR CONSTRUCTOR, ALSO USED FOR THE INSTANCE METHOD CONTEXT AS SEEN IN UNIV PYTHON
        #WHENEVER THE CLASS IS CALLED OR INITIALIZED OR INVOKED TRIGGERS AUTOMATICALLY THE ACTION SET HERE, GENERALLY IS ALWAYS VARIABLE SET UP
        #print ("initializing this object")
        self.id = user_id
        self.username = username
        #WHENEVER I SET THE CONSTRUCTOR WITH PARAMETERS I ALWAYS NEED TO INITIALIZE THE CLASS WITH THOSE PARAMETERS
        #MOST OF THE TIME IS EMPTY AS THE INITIALIZATION AS WELL BECAUSE ITS THE CONSTRUCTOR

        #AS HAPPENS HERE: setting a default value
        self.followers = 0
        self.following = 0

    def follow(self, user): # AS ALSO SEEN IN UNIV PYTHON PUT SELF WHEN THERE ARE PARAMETERS WITHIN THE CLASS IS LIKE A POINTER, ALSO AS
        #REFERENCE THAT WE ARE TALKING ABOUT FUNCTIONS AND METHODS RELATED TO THE INSTANCE
        user.followers += 1
        self.following += 1


user_1 = User("001","Angela")
user_2 = User("002","John")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)