from collections import Counter
def can_construct(animal_counter, string_counter):
    for c in animal_counter:
        if animal_counter[c] > string_counter[c]:
            return False
    return True

def count_animals(s):
    animals = ["dog", "cat", "bat", "cock", "cow", "pig",
               "fox", "ant", "bird", "lion", "wolf", "deer",
               "bear", "frog", "hen", "mole", "duck", "goat"]

    s_counter = Counter(s)
    found_animals = []
    
    for animal in animals:
        animal_counter = Counter(animal)
        while can_construct(animal_counter, s_counter):
            s_counter.subtract(animal_counter)
            found_animals.append(animal)
            
    return len(found_animals), found_animals

print(count_animals("goatcode"))  # ➞ 2 ["dog", "cat"]
print(count_animals("cockdogwdufrbir"))  # ➞ 4 ["cow", "duck", "frog", "bird"]
print(count_animals("dogdogdogdogdog"))  # ➞ 5 ["dog","dog","dog","dog","dog"]