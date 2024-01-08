def option_rock():
    print("The orc is stunned, but regains control. He begins running towards you again.")
    print("A. Run")
    print("B. Throw another rock")
    print("C. Run towards a nearby cave")
    choice = input().lower()
    if choice == "a":
        option_run()
    elif choice == "b":
        print("The rock flew well over the orcs head. You missed. You died!")
    elif choice == "c":
        option_cave()

def option_cave():
    print("Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?")
    choice1 = input().lower()
    print("What do you do next?")
    print("A. Hide in silence")
    print("B. Fight")
    print("C. Run")
    choice2 = input().lower()
    if choice2 == "a":
        print("I think orcs can see very well in the dark, right? You died!")
    
    
    elif choice2 == "c":
        print("The orc turns around and sees you running.")
        option_run()
    elif choice1 == "y":
        print("As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!")
    elif choice1 == "n":
        print("You're defenseless. You died!")
def option_run():
    print("You run as quickly as possible.")
    print("A. Hide behind boulder")
    print("B. Trapped, so you fight")
    print("C. Run towards an abandoned town")
    choice = input().lower()
    if choice == "a":
        print("You're easily spotted. You died!")
    elif choice == "b":
        print("You're no match for an orc. You died!")
    elif choice == "c":
        option_town()

def option_town():
    print("You notice a purple flower near your foot. Do you pick it up? Y/N")
    choice = input().lower()
    if choice == "y":
        print("You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!")
    elif choice == "n":
        print("Maybe you should have picked up the flower. You died!")

print("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.")
print("A. Grab a nearby rock and throw it at the orc")
print("B. Lie down and wait to be mauled")
print("C. Run")
choice = input().lower()
if choice == 'a':
    option_rock()
elif choice == 'b':
    print("Welp, that was quick. You died!")
elif choice == 'c':
    option_run()
