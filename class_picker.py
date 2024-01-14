import random

available_classes = ['Warrior', 'Ranger', 'Sorceress', 'Berserker', 'Tamer', 'Musa', 'Maehwa',
              'Valkyrie', 'Kunoichi', 'Ninja', 'Wizard', 'Witch', 'Mystic', 'Striker', 'Lahn',
              'Archer', 'Dark Knight', 'Shai', 'Guardian', 'Hashashin', 'Nova', 'Sage', 'Corsair', 'Drakania', 'Woosa', 'Maegu',
              'Scholar']


awakeVSucc = ['Awakening', 'Succession']


print("Black Desert Online Classes - 2023")
for item in available_classes:
    print(item)
class_remove = input("\n\nWhich classes to exclude? (comma separated)\n").split(',')

for bdo_class in class_remove:
    # Making this not case sensitive for user input
    class_lower = bdo_class.strip().lower()
    available_classes = [value for value in available_classes if value.lower() != class_lower]
       
            
def The_Random_Matcher(available_classes,awakeVSucc):
    theClass = random.choice(available_classes)

    # Three classes in the game are neither Awakening or Succession, they're Ascension.
    if theClass not in ['Shai', 'Archer', 'Scholar']:
        theSpec = random.choice(awakeVSucc)
    else:
        theSpec = 'Ascension'

    print(f"\nRandomly Selected:\n \t• {theSpec} {theClass}")

def main(available_classes,awakeVSucc):
    # Initial Selector
    The_Random_Matcher(available_classes, awakeVSucc)
    defaultInput = ""
    # Trolling the indecisive people
    too_many_runs = int(0)
    # Main functional loop, re-select if not happy
    while defaultInput != 'n':
        defaultInput = input("\nWould you like to run again? (y/n): ")
        defaultInput.lower()
        if defaultInput == 'y':
            # Add too_many_runs to force break after 3 runs
            too_many_runs = too_many_runs + 1
            The_Random_Matcher(available_classes, awakeVSucc)
        # This person really needs to pick a class already
        if too_many_runs == 3:
            print("\n\nYOU NEED TO CHOOSE! STOP RIGHT THERE CRIMINAL!")
            break
    exit_code = input("\n\n<Enter> to exit the application.")

if __name__ == "__main__":
    main(available_classes,awakeVSucc)
