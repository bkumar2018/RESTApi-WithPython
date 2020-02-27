import json

#Convert String json to Dictionary python object.
# x = '{ "name":"Birender", "age":30, "city":"Pune" }'  # This is a json format String
# print(type(x))
# y = json.loads(x)
# print(type(y)) # converted to dict
# print(type(y["name"]))
# print(y["name"])
# print(y["age"])
# print(y["city"])



#Convert Dict python object to  String json.
# x = { "name":"Birender", "age":30, "city":"Pune" }      # This is a python dictionary object
# print(type(x))
# #y = json.dumps(x)
# y = json.dumps(x, indent=2)
# print(type(y)) # converted to dict
# print(y)


#Convert Python objects into JSON strings, and print the values:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))