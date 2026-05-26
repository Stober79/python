contacts = {
    "Ola": "ola@onet.com",
    "Daniel": 30,
    "Ania": "ania@onet.com"
}
contacts["Rafał"] = "rafal@onet.com"
print(contacts["Ola"])
print(contacts["Daniel"])
print(len(contacts))
print(type(contacts))
print(contacts.keys())
print(contacts.values())
print(contacts.items())
for key in contacts:
    print(key, contacts[key])
for key, value in contacts.items():
    print(key, value)