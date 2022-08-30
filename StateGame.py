import random
x = 0
def statefunc(statenum):
    print(" ")
    statenum = random.choice(list)
    print(statenum)
    list.remove(statenum)
    input()
list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
print("50 State List Game, Press enter for next state.\n")
input("Press eneter to begin")
while len(list) != 0:
    x += 1
    statefunc(x)
    
print("All States Complete")

##I made this over 2 years ago in my bedroom at my dad's house, and the version before this didn't use a loop, i just typed out statefunc() with ascending numbers lol.
##I tried to use a for loop but i don't use python anymore so im clueless and gave up after one failure
##not sure what i thought this was useful for but i suppose it exists 
