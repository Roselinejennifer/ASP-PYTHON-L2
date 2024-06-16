my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"])
my_dict["email"] = "alice@example.com"
my_dict["age"] = 31
if "city" in my_dict:
    print("City is present")
for key in my_dict:
    print(key, my_dict[key])
del my_dict["city"]
   
