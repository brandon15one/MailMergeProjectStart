# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
def listToString(s):
    str1 = " "

    return str1.join(s)


with open("Input/Letters/starting_letter.txt", mode="r") as l:
    letter = l.readlines()
    join = listToString(letter)
    with open("Input/Names/invited_names.txt", mode="r") as n:
        names = n.readlines()
        for name in names:
            change = join.replace("[name]", name.strip())
            with open(f"Output/ReadyToSend/{name.strip()}.txt", mode="w") as k:
                k.write(change)


