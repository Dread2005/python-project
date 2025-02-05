#nesting

#nesting list in dictionary
dictionary = {
    "key":["value","value","Value"],
}

#nesting dictionary in dictionary
traavel_log = {"france":{"cities_visited": ["paris", "Little", "Dijon"],
                         "total visits": 16,}}

#nesting dictionaries in list
traavel_log = [
    {
    "country":"France",
    "cities_visited": ["paris", "Little", "Dijon"],
    "total visits": 16,
    },
    {
      "country":"France",
      "cities_visited": ["paris", "Little", "Dijon"],
      "total visits": 16
    }
]

