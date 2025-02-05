# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
Placeholder = "[name]"
with open("./Input/Names/invited_names.txt") as names:
    lis = names.readlines()
    print(lis)


with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()
    for the_name in lis:
        str_name = the_name.strip()
        new_letter = content.replace(Placeholder, str_name)
        with open(f"./Output/ReadyToSend/letter_for_{str_name}.txt", "w") as letters:
            letters.write(new_letter)



#with open("\Tshifhiwa\Downloads\python stuffs\day_24_files_directories_paths\Mail Merge Project Start\Input\Letters") as mail:


