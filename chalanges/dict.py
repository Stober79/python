dict = {
    "website": "example.com",
    "dbType": "mysql",
    "dbUser": "admin",
    "dbPassword": "12345"
}
print(len(dict))
print(dict["dbType"])
for key , value in dict.items():
    print(key, value)