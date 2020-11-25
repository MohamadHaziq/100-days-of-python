import art

print (art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(ciper_direction, input_text, shift_amount):
        output_text =""
        if ciper_direction == "decode":
            shift_amount *= -1
        for char in input_text:
            if char in alphabet:
                position = alphabet.index(char)     
                new_position = position + shift_amount        
                output_text +=  alphabet[(new_position % 26)]
            else:
                output_text += char

        print (f"The {ciper_direction}d text is {output_text}")

    caesar(ciper_direction = direction, input_text = text, shift_amount = shift)

    restart = input("Type 'yes' if you want to go again or 'no' to end the program")
    if restart == 'no':
        should_continue = False
        print ("Thank you and Goodbye !")
