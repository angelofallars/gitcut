from sys import argv as sys_args
from os import system as exec_command


def interpret_command(args: list[str]) -> str:
    git_commit_args = []
    git_push_args = []
    shell_command = ""

    match args[0]:
        case "gm":
            git_commit_args += ["git commit"]
        case "gma":
            git_commit_args += ["git commit -a"]
        case "gmp":
            git_commit_args += ["git commit"]
            git_push_args += ["git push"]
        case "gmap":
            git_commit_args += ["git commit -a"]
            git_push_args += ["git push"]

    if len(args) >= 2:
        # Parse the git commit message
        git_commit_args += ["-m"]
        for i in range(1, len(args)):
            message_word = args[i]
            if i == 1:
                git_commit_args += [f'"{message_word.capitalize()}']
            elif i == len(args) - 1:
                git_commit_args += [f'{message_word}"']
            else:
                git_commit_args += [message_word]

    shell_command += " ".join(git_commit_args)

    if git_push_args:
        shell_command += " && "
        shell_command += " ".join(git_push_args)

    return shell_command


def main() -> int:
    exec_command(interpret_command(sys_args))
    return 0


if __name__ == "__main__":
    main()
