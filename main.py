import random

name_file = "santa names with exceptions.txt"

with open (name_file) as f:
    data = list(filter(None,f.readlines()))
    
raw_names = [x.strip() for x in data] # strips spaces,newline etc
raw_names = list(filter(None,raw_names))# removing empty elements from list
raw_names.pop(0) # removing the "Names" element in the list

# extract names and restrictions
restricted = {}
names = []
for name in raw_names:
    if '(' in name:
        main_name, restrictions = name.lstrip().split('(')
        restrictions = restrictions.rstrip(')').split(',')
        restricted[main_name] = restrictions
        names.append(main_name)
    else:
        names.append(name)

# function to assign Secret Santas
def assign_santas(names, restricted):
    # copy the list of names and shuffle it
    shuffled = names[:]
    random.shuffle(shuffled)

    # create a dictionary to hold the assignments
    assignments = {}

    # assign secret santas
    i = 0
    while i < len(names):
        santa = names[i]
        recipient = shuffled[i]
        # check if the santa is restricted from giving to the recipient or if the santa and recipient are the same
        if santa == recipient or (santa in restricted and recipient in restricted[santa]):
            # if so, shuffle the recipient list again and start over
            random.shuffle(shuffled)
            i = 0
            assignments = {}
            continue

        # if not, assign the santa to the recipient
        assignments[santa] = recipient
        i += 1

    return assignments

# print out the assignments
assignments = assign_santas(names, restricted)
count = 1
for santa, recipient in assignments.items():
    print(f"{count}.Notifying {santa} that they are assigned to get a gift for {recipient}")
    count += 1


