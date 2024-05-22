alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#STEP-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
'''
def encrypt(text, shift):
    cipher_text = ''
    for i in text:
        a = alphabet.index(i)
        a += shift
        cipher_text += alphabet[a]
    print(f"The encoded text is {cipher_text}")
            
def decrypt(text=text, shift=shift):
    plain_text = ''
    for i in text:
        d = alphabet.index(i)
        d -= shift
        plain_text += alphabet[d]
    print(f"The decoded text is {plain_text}")

if direction == "encode":
    encrypt(text=text, shift=shift)
elif direction == "decode":
    decrypt(text=text, shift=shift)
'''
def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for l in text:
        p = alphabet.index(l)
        new_p = p + shift
        end_text += alphabet[new_p]
    print(f"The {direction} text is {end_text}")


#STEP-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text=text, shift=shift, direction=direction)
            
    
    
    
    