# User
game_status = 1
username = (input("username: "))
username = username.capitalize()
gender2 = 0
gender = (input("male or female: "))
if gender == "male":
    gender = "his"
    gender2 = "he"
else:
    gender = "her"
    gender2 = "she"

# Intro
print ()
beginning = ("Greetings, " + username + " and welcome to the Land Down Under!")
print (beginning)
start = ("Our heroes journey starts here, " + username + " with " + gender + " first choice being a simple one.")
print (start)
print ()

while game_status > 0:

# Humble beginnings
    start11 = input ("Wake up/Sleep ")
    start11 = start11.capitalize()
    if start11 == ("Wake up"):
        print ()
        print ("And so, your journey, begins. ")
    elif start11 == ("Sleep"):
        print ("Yeah no, you're getting up. NOW ")
    else:
        print ("What? Anyway, GET UP! ")
        
# The stranger
    stranger1 = ('Whilst our "hero" is doing ' + gender + ' thing, a hooded stranger in a black robe comes knocking on ' + gender + ' door. ')
    stranger2 = ("The stranger asks our hero, if " + gender2 + " knows where the local library might be. ")
    stranger3 = ("Since our hero is freshly born, " + gender2 + " pardons the stranger and tells him off. ")
    stranger4 = ("Whilst our hero is closing the door, the stranger puts his foot inbetween the door and tells out hero that it's important. ")
    print (stranger1)
    print (stranger2)
    print (stranger3)
    print (stranger4)
    print ()

# First choice
    choice1 = input("Our hero is put in a sticky situation, will " + gender2 + " [let the stranger speak] or will he [shut the door], violently.? ")
    if choice1 == "shut the door":
        print ("Whilst our hero was attempting to shut the door, " + gender2 + " broke the stranger's foot, making a black hol.")
        game_status = 0
    elif choice1 == ("let the stranger speak"):
        print ()
        print ("The stranger told that the weight of the world lies on his shoulders and the location of the library is more important than anything else.")
    else:
        print ("you complete brainlet.")
        game_status = 0
    
# The Library
    library1 = ("Our brave hero brings the stranger sad news for not knowing the libraries location even though " + gender2 + " has lived " + gender + " entire live here.")
    library2 = ("The stranger sighs and turns the other way.")
    print (library1)
    choice2 = input("Our most brave hero has a choice to [go with the stranger], or close the door and [continue on with the day] ")
    if choice2 == ("go with the stranger"):
        print ("Before the stranger has turned the corner, our hero shouts to wait up and runs after the stranger.")
        print ("our hero vows to go with the stranger to help him find the library and help him with his quest")
    elif choice2 == ("continue on with the day"):
        print ("You fool. This was supposed to be the start of your amazing adventure, but no, you just let it slip and now you feel depressed. ")
        game_status = 0
    else:
        print ("can you speak?")
        game_status = 0

# The road to hell
    road1 = ("As our hero was walking with the stranger on the busy streets of [REDACTED], " + gender2 + " asks the stranger what his name is")
    road2 = ("The stranger tell out hero that his name is [REDACTED] ")
    
else:
    print ()
    print ("Game Over")