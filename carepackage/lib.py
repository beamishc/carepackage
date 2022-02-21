def try_me():
    string1 = "I know what you're thinking."
    string2 = '"Did he fire six shots or only five?"'
    string3 = 'Well, to tell you the truth, in all this excitement I kind of lost track myself.'
    string4 = "But being as this is a .44 Magnum, the most powerful handgun in the world, and would blow your head clean off, you've got to ask yourself one question:"
    string5 = '"Do I feel lucky?"'
    print(string1)
    print(string2)
    print(string3)
    print(string4)
    print(string5)
    query = input("Well, do ya, punk?\n> ")
    if query == str(6) or query.lower() == 'six':
        return "Looks like it's your lucky day."
    else:
        return "BLAM! Looks like your luck just ran out."
