with open("Input/Letters/starting_letter.txt", mode="r") as l:
    letter = l.read()
    with open("Input/Names/invited_names.txt", mode="r") as n:
        names = n.readlines()
        for name in names:
            change = letter.replace("[name]", name.strip())
            with open(f"Output/ReadyToSend/{name.strip()}.txt", mode="w") as k:
                k.write(change)


