hopping_list = ["milk",
                         "pasta",
                                          "spam",
                                                           "bread",
                                                                            "rice"
                                                                                             ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(another_list)

# There is only one list but 2 names for the list using the '=' symbol

a = b = c = d = e = f = another_list
print(a)

print("Adding cream")
b.append("cream")
print(c)
print(d)
