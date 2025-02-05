#black jack
import random

card = [1,2,3,4,5,6,7,8,9,10,11]
def cards(card):
    Card1 = random.choice(card)
    return Card1
      
Start_card = [cards(card=card),cards(card=card)]
user_cards = Start_card

comp_card = [cards(card=card),cards(card=card)]
comp_cards = comp_card

the_goal = 21

def user():
    from Bjart import logo
    print(logo)
    while_playing = True
    print(f"user cards:{user_cards}")
    print(f"comp card are: {comp_cards[1]}")
    
    total_comp = comp_cards[0]
    total_user = sum(user_cards[0:])


    while while_playing:
      user_cards.append(cards(card=card))
      User_input = input("If you would like a card type yes, if not type no : ")

      if User_input == "yes":
         total_user = sum(user_cards[0:])
         total_comp = sum(comp_cards[0:2]) 

         print(f"Your cards {user_cards}")
         print(total_user)

         print(f"comp card are: {comp_cards}")
         print(total_comp)

      if User_input == "no":
         total_user = sum(user_cards[0:])
         if total_comp > the_goal:
            print("User won")
            while_playing = False
         elif total_comp <= the_goal and total_comp > total_user:
            print("User lost")
            while_playing = False
         elif total_user > total_comp and total_user <= the_goal:
            print("User won")
            while_playing = False
         elif total_user > the_goal:
            print("User lost")
            while_playing = False
         elif total_user == total_comp and total_user <= the_goal:
            print("draw")
            while_playing = False
         
   
      
        
user()






        
        
        
      







    
    





