import shelve
books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled_egg": ["egg", "milk", "butter"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]},
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}
print(books["recipes"])
# print([books["recipes"]["scrambled_egg"]])

# print(books["maintenance"]["loose"])
books.close()
