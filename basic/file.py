import os
currentPath = os.getcwd()
print(currentPath)

path = currentPath + "\\basic\\netflix.txt"


# with open(path) as file:
#   for line in file:
#     print(line)

def make_dictionary(filename):
    user_to_titles = {}
    with open(filename) as file:
        for line in file:

            user, title = line.strip().split(":")
            user_to_titles[user] = title

        return user_to_titles
 
print(make_dictionary(path))

