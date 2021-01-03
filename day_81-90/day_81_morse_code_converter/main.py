import json

with open('./day_81-90/day_81_morse_code_converter/morsecode.json') as f:
    morse_code_values = json.loads(f.read())

converter_on = True

print ("Welcome To The Morse Code Converter")

while converter_on:
    string_to_convert = input("Please enter string to convert:\n")
    if string_to_convert == "off":
        converter_on = False
    else:
        morse_code = []
        for char in string_to_convert.lower():
            converted_char = morse_code_values[char]
            morse_code.append(converted_char)
        print ((" ").join(morse_code))