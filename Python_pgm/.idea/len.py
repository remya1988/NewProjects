username = input("Username : ")
password = input("Password : ")

data = [
    ["rem","rem123"],
    ["raj","raj123"],
    ["dev","dev123"]
]
if [username,password] in data:
    print("Your access granted.....")
else:
    print("U are rejected")