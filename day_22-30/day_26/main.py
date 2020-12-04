import pandas as pd 

data = pd.read_csv('./day_22-30/day_26/nato_phonetic_alphabet.csv')

nato_conversion = {row.letter:row.code for (idx,row) in data.iterrows()}

word_to_convert = input("What would you like to convert ?: ").upper()

codeword = [nato_conversion[letter] for letter in word_to_convert]
print (codeword)