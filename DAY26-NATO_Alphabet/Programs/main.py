import pandas

data = pandas.read_csv('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY26-NATO_Alphabet/Resources/nato_phonetic_alphabet.csv')

# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
