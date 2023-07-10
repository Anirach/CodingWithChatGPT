def count_animals(s):
    animals = ["dog", "cat", "bat", "cock", "cow", "pig",
               "fox", "ant", "bird", "lion", "wolf", "deer",
               "bear", "frog", "hen", "mole", "duck", "goat"]
    found_animals = []
    for animal in animals:
        while animal in s:
            found_animals.append(animal)
            s = s.replace(animal, '', 1)  # replace first occurrence of animal in string
    return len(found_animals), found_animals


print(count_animals("goatcode"))  # ➞ 2 ["dog", "cat"]
print(count_animals("cockdogwdufrbir"))  # ➞ 4 ["cow", "duck", "frog", "bird"]
print(count_animals("dogdogdogdogdog"))  # ➞ 5 ["dog","dog","dog","dog","dog"]
