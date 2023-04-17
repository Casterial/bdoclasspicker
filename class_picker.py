import random

allClasses = ['Warrior', 'Ranger', 'Sorceress', 'Berserker', 'Tamer', 'Musa', 'Maehwa',
              'Valkyrie', 'Kunoichi', 'Ninja', 'Wizard', 'Witch', 'Mystic', 'Striker', 'Lahn',
              'Archer', 'Dark Knight', 'Shai', 'Guardian', 'Hashashin', 'Nova', 'Sage', 'Corsair', 'Drakania', 'Woosa', 'Maegu']


awakeVSucc = ['Awakening', 'Succession']


print('Class List: {}'.format(allClasses))
print('\n\nPlease follow the prompt, remember its case sensitive...\n')
resp = ''
while resp != 'exit':
    resp = input("Any class you wish to not randomly pick? exit to exit:\t")
    if resp != 'exit':
        try:
            allClasses.remove(resp)
        except ValueError:
            print("\n\nYou may have mispelled that, please try again...\n")
            
print("Lets choose your class for the season....\n")
def The_Random_Matcher(allClasses,awakeVSucc):
    theClass = random.choice(allClasses)

    # Logic because some classes are unique
    if theClass not in ['Shai', 'Archer']:
        theSpec = random.choice(awakeVSucc)
    else:
        theSpec = 'Awakening'
    # Not Released Yet
    if theClass in ['Maegu', 'Woosa']:
        theSpec = 'Sucession'
        
    print("Class: {}, Playstyle: {}".format(theClass, theSpec))

def main(allClasses,awakeVSucc):
    # Initial Selector
    The_Random_Matcher(allClasses, awakeVSucc)
    defaultInput = ""
    # Trolling the indecisive people
    too_many_runs = int(0)
    # Main functional loop, re-select if not happy
    while defaultInput != 'n':
        defaultInput = input("Would you like to run again? (y/n):\t")
        defaultInput.lower()
        if defaultInput == 'y':
            # Add too_many_runs to force break after 3 runs
            too_many_runs = too_many_runs + 1
            The_Random_Matcher(allClasses, awakeVSucc)
        # This person really needs to pick a class already
        if too_many_runs == 3:
            print("\n\nYOU NEED TO CHOOSE! STOP RIGHT THERE CRIMINAL!")
            break
    exit_code = input("\n\n<Enter> to exit the application.")

if __name__ == "__main__":
    main(allClasses,awakeVSucc)
