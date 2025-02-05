alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesor(PLAIN_TEXT,SHIFT_NUM,CYPHER_DIRECTION):
    end_text = ""
    if CYPHER_DIRECTION == "decode":
            SHIFT_NUM *= -1
    for n in PLAIN_TEXT:
        if n in alphabet:
            position = alphabet.index(n)
            new_position = position + SHIFT_NUM
            end_text += alphabet[new_position]
        else:
             end_text += n
    print(f"the {CYPHER_DIRECTION} text is: {end_text}")  

go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    Shift = shift % 26

    from logo2 import logo
    print(logo)

    caesor(PLAIN_TEXT = text,SHIFT_NUM = Shift, CYPHER_DIRECTION = direction)


    restart = input("Would you like to restart? ")
    if restart == "no":
        go_again = False











#
#
#
#
#def encrypt(PLANE_TEXT,SHIFT_NUM):
#    cipher_text = ""
#    for n in PLANE_TEXT:
#        position = alphabet.index(n)
#        new_position = position + SHIFT_NUM
#        new_letter = alphabet[new_position]
#        cipher_text += new_letter
#    
#        print(f"the encoded text is:{cipher_text}")
#
#
#def decrypt(PLANE_TEXT,SHIFT_NUM):
#    plain_text = ""
#    for n in PLANE_TEXT: 
#        position = alphabet.index(n)
#        new_position = position - SHIFT_NUM
#        new_letter = alphabet[new_position]
#        plain_text += new_letter
#        
#        print(f"the decoded text is:{plain_text}")
    




  
 

    
    

    
