#decorators used to increase a functanality of a excicting function
def start_end_print(func):          #decorator function takes the function need to be changed as argument
    def wrapper():                  #wrapper will take the all functanality together and will return
        print("Starts")             #things we can add before the function
        func()                      #function need to be changed
        print("Ends")               #things we can add after the function
    return wrapper                  #returning the wrapper

@start_end_print                                #linking decorator to the function
def print_name():                               #function needed to be changed
    print("Mayura")

#print_name = start_end_print(print_name)        #assinging the decorator to function(we dont need this line if we add @stsrt_end_print above the function)

print_name()
