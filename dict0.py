#So dict works on the key and value pair

kids = {"Dog" : "Puppy",
        "Cat" : "Kitten",
        "Cow" : "Calf"

}

print(kids)

for keys, values in kids.items():
    print(f"{keys} : {values}")

for keys in kids.keys():
    print(keys)

for values in kids.values():
    print(values)


print(kids.get("Cat"))

#How to use dictionary as conitional for if else:

if kids.get("Horse"):
    print("Kid exists")
else:
    print("Kid doesn't exist")

kids.update({"Fish":"School"})
kids.update({"Cat" : "Meow"})

print(kids)

kids.pop("Cow")
kids.popitem()
print(kids)