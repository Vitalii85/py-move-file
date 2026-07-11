import os


def move_file(command: str) -> None:
    commands_list = command.split(" ")
    if len(commands_list) != 3 or commands_list[0] != "mv":
        return

    if commands_list[1] == commands_list[2]:
        return

    if commands_list[2][-1] == "/":
        commands_list[2] += commands_list[1].split("/")[-1]

    if "/" in commands_list[2]:
        folders = commands_list[2].split("/")
        os.makedirs("/".join(folders[:-1]), exist_ok=True)

    try:
        with (
            open(commands_list[1], "r") as file_in,
            open(commands_list[2], "w") as file_out
        ):
            file_out.write(file_in.read())
    except OSError:
        return
    else:
        os.remove(commands_list[1])
