import pandas
NATO_dictionary = pandas.read_csv("./nato_phonetic_alphabet.csv")

user_message = input("Enter your Message: ")
user_message = user_message.upper()
list_letter = [letter for letter in user_message]

phonetic_code_words = []
for letter in list_letter:
    for (index, row) in NATO_dictionary.iterrows():
        if row.letter == letter:
            phonetic_code_words.append(row.code)

print(phonetic_code_words)
# for (index, row) in NATO_dictionary.iterrows():
#     print(row.letter)
