# write your code here
def copy_file(command: str, filename: str, copy_name: str) -> None:
    if command == "cd" and filename != copy_name:
        with open(filename, "r") as file_in, open(copy_name, "w") as file_out:
            original_text = file_in.read()
            file_out.write(original_text)
