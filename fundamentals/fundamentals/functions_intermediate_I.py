x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
hero_names = [
    {'first_name': 'Steve', 'last_name': 'Rogers'},
    {'first_name': 'Sam', 'last_name': 'Wilson'},
    {'first_name': 'Bucky', 'last_name': 'Barnes'},
    {'first_name': 'Peter', 'last_name': 'Parker'}
]

# 1.
# Change the value 10 to 15
# - Referencing the indexes of the number in question allows the ability to change the value.

x[1][0] = 15

print(x)


# Change the last_name of the first student from 'Jordan' to 'Bryant'
# - By referencing the index of the first list and then the 'last_name' value, we can change it.

students[0]['last_name'] = 'Bryant'

print(students[0]['last_name'])


# In the sports_directory, change 'Messi' to 'Andres'
# - By referencing the indexes of the tuple and the nested list, the specific value can be changed.

sports_directory['soccer'][0] = 'Andres'

print(sports_directory['soccer'][0])


# Change the value 20 in z to 30
# - I referenced the index of the list and the number was changed by referencing the value name 'y'.

z[0]['y'] = 30

print(z)


# 2.
# Create a function iterateDictionary(hero_names) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value
# - I used an F-String to print the 'i'(keys) and their corresponding values.

def iterateDictionary(hero_names):
    for i in range(0, len(hero_names)):
        print(
            f"first_name: {hero_names[i]['first_name']}, last_name: {hero_names[i]['last_name']}")


iterateDictionary(hero_names)


# 3.
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary
# - I used a for-loop to run through the dictionaries by their specified 'key name' and print the corresponding value.

def iterateDictionary2(key_name, hero_names):
    for i in range(0, len(hero_names)):
        print(hero_names[i][key_name])


# - by establishing the 'key_name' in specific, the loop knows what to look for
iterateDictionary2('first_name', hero_names)
iterateDictionary2('last_name', hero_names)


# 4.
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list
# - I combined the use of printing by the key name and indexed value with running through the range of the dictionaries and printing the associated values.
heroes = {
    'names': ['Steve Rogers', 'Sam Wilson', 'Bucky Barnes', 'Peter Parker'],
    'identities': ['Captain America', 'Falcon', 'Winter Soldier', 'Spider-Man']
}


def printInfo(heroes):
    for key in heroes:
        print(key, "-", len(heroes[key]))
        for i in range(0, len(heroes[key])):
            print(heroes[key][i])


printInfo(heroes)
