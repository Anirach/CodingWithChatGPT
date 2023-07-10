def count_animals(s):
    animals = ["dog", "cat", "bat", "cock", "cow", "pig",
               "fox", "ant", "bird", "lion", "wolf", "deer",
               "bear", "frog", "hen", "mole", "duck", "goat"]
    found_animals = []
    print('start s [%s]' %(s))
    for animal in animals:
        print(animal)
        while all(s.count(c) >= animal.count(c) for c in animal):
            s = list(s)  # convert string to list for character deletion
            for c in animal:
                s.remove(c)  # remove each character of the animal from string
            s = ''.join(s)  # convert list back to string
            print("[ %s ]" %(s))
            found_animals.append(animal)
    return len(found_animals), found_animals


print(count_animals("goatcode"))  # ➞ 2 ["dog", "cat"]
print(count_animals("cockdogwdufrbir"))  # ➞ 4 ["cow", "duck", "frog", "bird"]
print(count_animals("dogdogdogdogdog"))  # ➞ 5 ["dog","dog","dog","dog","dog"]
