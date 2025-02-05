class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


#Passing arguments associated with the function
def is_authenticated_decorate(function):
    def wrapper(*args):
        #to define the "user.is_logged_in" attribute, you must add *args and **kwargs(unlimited positional arguments= args, unlimited key word arguments= **kwargs)
        #use the "*args" and replace user with *args and the position "user" in "def create_blog_post": e.g. *args[0] (position is zero because evrythin in python starts from 0)
        #if user.is_logged_in == True:
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorate
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


user_name_input = input("Enter_new_username: ")
new_user = User(user_name_input)
#to be recognised as logged in, change User.is_logged_in as True
new_user.is_logged_in = True
create_blog_post(new_user)
