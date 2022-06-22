with open("Input/Names/invited_names.txt") as names:
    reading_names = names.readlines()

with open("Input/Letters/template.txt") as invite_template:
    reading_invite_template = invite_template.readlines()
    for name in reading_names:
        reading_invite_template[0] = "Dear"+" " +name+","
        name_change = name.lower()
        with open(f"Output/ReadyToSend/invite_for_{name_change}.txt","w") as invite_send_to_all:
            for line in reading_invite_template:
                invite_send_to_all.write(line)
