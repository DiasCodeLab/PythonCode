

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}


for key, valuer in users.copy().items():
    if valuer == 'inactive':
        del users[key]

print(users)



user_new = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for key,valuer in user_new.items():
    if valuer == 'inactive':
        print(key)

