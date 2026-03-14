from editor import change_line

def process_command(command):

    if "run npm start" in command:
        run_npm_start()

    elif "git status" in command:
        git_status()

    elif "git add all" in command:
        git_add_all()

    elif "git push" in command:
        git_push()

    elif "open vscode" in command:
        open_vscode()

    elif "change line" in command:

        # example: change line 10
        words = command.split()

        line_number = int(words[2])

        text = input("Enter new code: ")

        change_line("app.js", line_number, text)