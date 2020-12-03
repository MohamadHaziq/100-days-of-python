PLACEHOLDER = "[name]"

with open("./day_22-30/day_24/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./day_22-30/day_24/Input/Letters/starting_letter.docx") as letter:
    letter_contents = letter.read()
    for name in names:
        strip_name = name.rstrip()
        new_letter = letter_contents.replace(PLACEHOLDER, strip_name)
        with open(f"./day_22-30/day_24/Output/ReadyToSend/letter_to_{strip_name}.docx", "w") as completed_letter:
            completed_letter.write(new_letter)