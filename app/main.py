import os


def move_file(command: str) -> None:
    commands_list = command.split()
    if len(commands_list) != 3 or commands_list[0] != "mv":
        return

    if commands_list[1] == commands_list[2]:
        return

    if commands_list[2][-1] == "/":
        commands_list[2] = os.path.join(
            commands_list[2],
            os.path.basename(commands_list[1])
        )

    folders = commands_list[2].split("/")
    new_path = ""
    for i in range(len(folders) - 1):
        new_path = os.path.join(new_path, folders[i])
        try:
            os.mkdir(new_path)
        except FileExistsError:
            pass

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
