my_dict = {"Vera": 2001, "Darina": 2002, "Irina": 2003}
print(my_dict)
print(my_dict ["Vera"])
my_dict.update ({"Mara" : 2006,
                 "Corvus": 2000})
my_dict.pop("Vera")
print(my_dict)

my_set = {1, 2, 1, 1, 2, 3, 5, 4, 4, 5, "Corvus", "cake", "Corvus"}
print(my_set)
my_set.update({"Hello", "cat"})
print(my_set)
my_set.discard(5)
print(my_set)