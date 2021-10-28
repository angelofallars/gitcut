#!/bin/python3
from sys import argv as sys_args
from os import system as exec_command


def interpret_command(args: list[str]) -> str:
    git_commit_args = []
    git_message_words = []
    git_message_in_quotes = ""
    git_push_args = []
    shell_command = ""

    # Check the first command
    match args[0].split("/")[-1]:
        case "gm":
            git_commit_args += ["git commit"]
        case "gma":
            git_commit_args += ["git commit -a"]
        case _:
            return f'echo "undefined command {args[0]}"'

    # Process the commit message and git push arguments
    if len(args) >= 2:
        commit_message_start = 1
        commit_message_end = len(args)

        # Check for ,, (the git push indicator)
        if ",," in args:
            commit_message_end = args.index(",,")
            git_push_args += ["git push"]
            # Add the git push arguments (ex: origin main, -f)
            git_push_args += [i for i in args[commit_message_end + 1:]]

        # Parse the git commit message
        if (commit_message_end > commit_message_start):
            git_commit_args += ["-m"]

            for i in range(commit_message_start, commit_message_end):
                message_word = args[i]

                # Capitalize the first word
                if i == commit_message_start:
                    message_word = message_word.capitalize()

                # Handle double quotes " in git commit message
                message_word = message_word.replace('"', '\\"')

                git_message_words += [message_word]

    shell_command += " ".join(git_commit_args)

    if git_message_words:
        git_message_in_quotes = f'"{" ".join(git_message_words)}"'
        shell_command = f"{shell_command} {git_message_in_quotes}"

    if git_push_args:
        shell_command += " && "
        shell_command += " ".join(git_push_args)

    return shell_command


def main() -> int:
    usage = "usage: (gm | gma) (commit message) (,,) (remote) (remote branch)"

    # Make this program callable if invoked directly with `python main.py`
    if sys_args[0] == "main.py":
        sys_args.remove("main.py")

    if sys_args == []:
        print(usage)
        return 1

    exec_command(interpret_command(sys_args))
    return 0


if __name__ == "__main__":
    main()
