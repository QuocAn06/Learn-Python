PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt", mode="r") as reader:
    content = reader.read()

with open("./Input/Names/invited_names.txt", mode="r") as reader:
    invited_names = reader.read().split("\n")

for name in invited_names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as writer:
        new_content = content.replace(PLACEHOLDER, f"{name}")
        writer.write(new_content)
