# 1. Tuples

pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")

biryani = ("Chicken Biryani", "Indian", 45, "Hard")

print("Pasta:", pasta)

print("Name:", pasta[0])

print("Difficulty:", pasta[-1])
#nested tupple
recipe=(pasta,biryani)
print("biriyani recipe time",recipe[1][2])
for details in pasta:
    print(details)
pasta_ingredients={"tomato","chilli","garlic"} 
biriyani_ingredients={"rice","chicken","garlic"}
pasta_ingredients.add("cheese")
pasta_ingredients.discard("garlic")
all_ingredients=pasta_ingredients.union(biriyani_ingredients)
common=pasta_ingredients.intersection(biriyani_ingredients)
print("all ingredients:", all_ingredients)
print("common:", common)
