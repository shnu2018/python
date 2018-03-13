
all_animals = []
zoos = [["shanghai", {"animals": ["monkey", "dog", "tigger"]}, ("2017-10-10", "2017-10-15")], 
        ["wuhan", {"animals": ["lion", "dog", "fish"]}, ("2017-08-10", "2017-9-15")],
        ["jiangxi", {"animals": ["fish", "cat", "tigger"]}, ("2017-09-10", "2017-09-11")],
        ["shandong", {"animals": ["horse", "monkey", "tigger"]}, ("2017-11-10", "2017-11-25")]]
zoos.sort(key=lambda x: x[2][0], reverse=True)
for zoo in zoos:
    for animal in zoo[1]["animals"]:
        all_animals.append(animal)
animal_nums = [{animal: all_animals.count(animal)} for animal in set(all_animals)]
print(animal_nums)