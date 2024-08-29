import pandas

data = pandas.read_csv('D:/UDEMY/Python/100DaysPythonWithAngelaYU/DAY26-NATO_Alphabet/Resources/nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only, letters in alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()