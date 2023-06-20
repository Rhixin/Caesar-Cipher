import art
print(art.logo)
flow = "y"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift, choice):
    plain_mess = ""
    
    if choice == "decode":
        shift *= -1
        
    for i in message:
        if i in alphabet:
            index = alphabet.index(i) 
            plain_mess += alphabet[(index + shift) % 26]
        else:
           plain_mess += i
    
    print(f"The {choice}d message: {plain_mess}")
    

while(flow == "y"):
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    
    shift = int(input("Type the shift number:\n"))
    
    caesar(message, shift, choice)
        
    flow = input("Do you want to process again? y/n\n")
   

        
    
    