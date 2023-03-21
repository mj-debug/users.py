user_0 = {
    'username':'efermi',
    'first_name':'enrico',
    'last_name':'fermi',
}
user_1 = {
    'username' : 'albetega',
    'first_name' : 'albert',
    'last_name' : 'ortega',
}

user_2 = {
    'username' : 'fivoss',
    'first_name' : 'finn',
    'last_name' : 'voss',
}

people = [user_0, user_1, user_2]

for person in people:
    print(f"Your username is {person['username']} and your full name is {person['first_name'].title()} {person['last_name'].title()}.")
