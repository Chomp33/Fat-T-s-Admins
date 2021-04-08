# This program will print the names of Fat Tony admins
# Allow a user to add a new admin
# Print message making the user aware that the added admin already exists
# Allow a user to remove Fat Tony admins

# List of current Fat Tony admins

fat_tony_admins = ['Greg', 'SebS', 'Sebastian', 'Jack', 'Jesse']

# Print a list of Fat Tony admins

print("The Fat Tony's admins are: ")
for items in fat_tony_admins:
    print(items)

# Allow user to add an admin to Fat Tony's admin list

print('Please enter a name to add an individual to the Fat Tony admin list: ')

name = input()

fat_tony_admins += (name,)

print(items)

# Will inform user that the name he entered is already an admin

def is_admin(name):

    if name in fat_tony_admins:
        print(name + ' is already an admin.')
    else:
        print("The Fat Tony's admins are: ")
        for names in fat_tony_admins:
            print(names)

# Will allow user to delete a fat tony admin
