pet_name = input("What will you name your pet rock?")
max_value = int(10)
fullness = int(5)
happiness = int(5)
cleanliness = int(5)
age = int(0)

while fullness > 0 and happiness > 0 and cleanliness > 0:

    age += 1

    if fullness > max_value:
        fullness = max_value

    if happiness > max_value:
        happiness = max_value
    
    if cleanliness > max_value:
        cleanliness = max_value

    print(f"---Your pet rock, {pet_name}---\nFullness: {fullness}/10\nHappiness: {happiness}/10\nCleanliness: {cleanliness}/10")
    next_move = input(f"1:Feed {pet_name} \n2:Play with {pet_name}\n3:Clean {pet_name}")
    if next_move == "1":
        fullness += 2
        happiness -= 1
        cleanliness -= 1
    if next_move == "2":
        happiness += 2
        fullness -= 1
        cleanliness -= 2
    if next_move == "3":
        cleanliness += 2
        happiness -= 2
        fullness -= 1

if fullness <= 0:
    print(f"{pet_name} died from starvation :(")
if happiness <= 0:
    print(f"{pet_name} died from boredom :(") 
if cleanliness <= 0:
    print(f"{pet_name} died from stinkiness :(")
print(f"{pet_name} lived for {age} years.")