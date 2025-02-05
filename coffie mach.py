coff_flavours = ["flavour1", "flavour2", "flavour3"]
choice1 = coff_flavours[0]
choice2 = coff_flavours[1]
choice3 = coff_flavours[2]
coins = 0
change = 0
add_coin = int(input("add a coin: "))
coins += add_coin
if add_coin > 1:
    change = add_coin - 1
    coins = 1
if coins == 1:
    ur_choice = input("enter here: ").lower()
    if ur_choice == "c1":
        print(choice1)
    elif ur_choice == "c2":
        print(choice2)
    elif ur_choice == "c3":
        print(choice3)

if change > 0:
    print(f"ur change: {change}")


