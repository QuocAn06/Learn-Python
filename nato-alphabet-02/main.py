import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def nato_alphabet():
    word = input("Enter the word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_alphabet()
    else:
        print(output_list)


nato_alphabet()
