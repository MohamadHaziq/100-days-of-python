import pandas as pd 

data = pd.read_csv('./day_22-30/day_26/nato_phonetic_alphabet.csv')

nato_conversion = {row.letter:row.code for (idx,row) in data.iterrows()}

def generate_phonetic():
    word_to_convert = input("What would you like to convert ?: ").upper()
    try:
        codeword = [nato_conversion[letter] for letter in word_to_convert]
    except KeyError:
        print ("Please, only letters")
        generate_phonetic()
    else:
        print (codeword)

generate_phonetic()