PLACEHOLDER = '[name]'

with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY24-Mail_Merger/Programs/Input/Names/invited_names.txt') as name_file:
    names = name_file.readlines()

with open('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY24-Mail_Merger/Programs/Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f'D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY24-Mail_Merger/Programs/Output/ReadyToSend/letter_for_{stripped_name}', mode='w') as complete_letter:
            complete_letter.write(new_letter)
