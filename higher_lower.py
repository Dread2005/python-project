import random
from game_data import data
from higher_lower_art import logo
from higher_lower_art import vs
print(logo)
start = True
def game():
    points = 0
    playing = True
    while playing:
        data_length = len(data)
        person1 = random.choice(range(data_length))
        person2 = random.choice(range(data_length))
        person_data1 = data[person1]
        print_data1 = person_data1["name"],\
                person_data1["description"],\
                person_data1["country"]

        person_data2 = data[person2]
        print_data2 = person_data2["name"],\
                person_data2["description"],\
                person_data2["country"]

        print (print_data1)
        print(vs)
        print (print_data2)

        choice = input("WHat is Your choice: ")
        if choice == "t" and person_data1["follower_count"] > person_data2["follower_count"]:
            print("yes")
            points += 1
            print("")
        elif choice == "t" and person_data1["follower_count"] < person_data2["follower_count"]:
            print("no")
            print(f"these are your points: {points}")
            playing = False
        elif choice == "b" and person_data1["follower_count"] > person_data2["follower_count"]:
            print("yes")
            points += 1
            print("")
        elif choice == "b" and person_data1["follower_count"] < person_data2["follower_count"]:
            print("no")
            print(f"these are your points{points}")
            playing = False

game()
while start:
    start_again = input("Would yo like to start again? ")
    if start_again == "yes":
        game()
    else:
        start = False

    



