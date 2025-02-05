#dictinarie
#{key:value}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    
}
#use key to get the value
#print(programming_dictionary["Bug"])

#adding new item to dictionary
programming_dictionary["loop"] = "action of doing something repetedly",


#empty dictionary
empty_dictionary = {}
empty_dictionary#[] #to add to the empty dictionary

# to wipe a full dictionary 
#programming_dictionary = {}

#edit item in dictionary
#programming_dictionary["bug"] = "moth in comp" #whatever you asign
#print(programming_dictionary)

#looping in a dictionary
for key in programming_dictionary:
    #gives the key
    print(key)
    #gives the value
    print(programming_dictionary[key])






#lesson for today:
    

#country = input() # Add country name
#visits = int(input()) # Number of visits
#list_of_cities = eval(input()) # create list from formatted string
#
#travel_log = [
#  {
#    "country": "France",
#    "visits": 12,
#    "cities": ["Paris", "Lille", "Dijon"]
#  },
#  {
#    "country": "Germany",
#    "visits": 5,
#    "cities": ["Berlin", "Hamburg", "Stuttgart"]
#  },
#]
## Do NOT change the code above 👆
#
#def add_new_country(countryy,visitss,list_of_citiess):
#  new_country = {}
#  new_country["country"] = countryy
#  new_country["visits"] = visitss
#  new_country["cities"] = list_of_citiess
#  travel_log.append(new_country)
## TODO: Write the function that will allow new countries
## to be added to the travel_log. 
#
#
## Do not change the code below 👇
#add_new_country(country, visits, list_of_cities)
#print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
#print(f"My favourite city was {travel_log[2]['cities'][0]}.")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#