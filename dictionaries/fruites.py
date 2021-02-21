fruit={"orange": " a sweet , orange,citrus fruit",
       "apple":"good for making cider",
       "lemon":"a sour,yellow citrus fruit",
       "grape":"a small,sweet fruit growing in bunches",
       "lime":"a sour , green citrus fruit",
     }

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"]= "an odd shaped apple"
# print(fruit)
# fruit["pear"]= "great with tequila"
# print(fruit)
# del fruit["lemon"]
# print(fruit)
# fruit.clear()
# print(fruit)

# while True:
#     dict_key=input("please enter a fruit: ")
#     if dict_key=="quite":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a {}".format(dict_key))

# for snack in fruit:
#     print(fruit[snack])
#
# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("-" * 40)

print(fruit)
print(fruit.items())
f_tupple=tuple(fruit.items())
print(f_tupple)