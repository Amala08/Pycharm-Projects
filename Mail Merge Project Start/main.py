with open("./input/Names/invited_names.txt") as names:
    name = names.readlines()
    for i in name:
        with open("./Input/Letters/template.txt") as template:
            content_list = template.readlines()
            content_list[0] = f"Dear {i.strip()},\n"
            with open(f"./Output/ReadyToSend/invite_for_{i.lower().strip()}.txt", "w") as invite:
                invite_string = "".join(content_list)
                invite.write(invite_string)

