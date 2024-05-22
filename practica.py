# lista de usuarios

users_list = [
{"name": "Sergio", "age": 27, "phone": "615489326"},
{"name": "Diego", "age": 30, "phone": "698510236"},
{"name": "Xenn", "age": 22, "phone": "694501365"},
]

name = input("Name: ")
age = int(input("Age: "))
phone = input("Phone: ")

users_list.append({"name": name, "age": age, "phone": phone})


# Print the header
print(" / ".join(users_list[0].keys()))


for user in users_list:
    print(f"{user['name']} / {user['phone']} / {user['age']}")