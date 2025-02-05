##########################Scope#################################

enemies = 1

#def increase_enemies():
#  enemies = 2
#  print(f"enemies inside function: {enemies}")
#
#increase_enemies()
#print(f"enemies outside function: {enemies}")

##################### local scopes ######################

#def drink_potion():
#  potion_str = 2        # this will only happen if the function(drink_potion) is called
#  print(potion_str)
#
#drink_potion()

################# global_scope ###########################

#player_health = 10      #this can be printed both inside a function and outside a function, it can be accessed by everything
#def drink_potion():
#    potion_strength = 2
#    print(player_health)
#drink_potion()
#print(player_health)

############## editing using a global scope ###############

#enemies = 1
#def increase_enemies():
#  global enemies#>>>>>>>>>>>>>>>>>>>>> the global function is what lets us edit a global scope in a local scope
#  enemies += 1                          #(try not to edit any global functions)
#  print(f"enemies inside function: {enemies}")
#
#increase_enemies()
#print(f"enemies outside function: {enemies}")

####################### better way to edit ###########################
#enemies = 1
#def increase_enemies():                         
#  print(f"enemies inside function: {enemies}")
#  return enemies + 1#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>try using a return function insted
#
#enemies = increase_enemies()#assign the global variable to the "return" in the function
#print(f"enemies outside function: {enemies}")

################################### global constants #############################
PI = 3.14159 #>>>>>>>>>>>>>>>>>>>>>>>>>> try using all caps for global constance

