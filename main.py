print("\n\tWelcome to the Miles Per Hour Conversion App")

def usr_input():
    usr_name = input("\n\tEnter your username: ")
    usr_speed=float(input("\n\tHello {}!\n\tWhat is your speed in miles per hour: ".format(usr_name)))
    return usr_speed

def speed_conversion(usr_speed):
    usr_speed = usr_speed * 0.4474
    print("\tYour speed in meters per second is {}.".format(round(usr_speed,2)))

#MAIN PROGRAM
usr_data = usr_input()
speed_conversion(usr_data)