import unittest
import main


def program_command(initial_command: str) -> str:
    transformed_command = main.interpret_command(initial_command.split())
    return transformed_command


class TestGitCommands(unittest.TestCase):

    def check_validity(self, before: str, after: str) -> None:
        self.assertEqual(program_command(before), after)

    def test_gm_blank(self):
        before = "gm"
        after = "git commit"
        self.check_validity(before, after)

    def test_gma_blank(self):
        before = "gma"
        after = "git commit -a"
        self.check_validity(before, after)

    def test_gm_message(self):
        before = "gm add new features"
        after = 'git commit -m "Add new features"'
        self.check_validity(before, after)

    def test_gma_message(self):
        before = "gma add stuff"
        after = 'git commit -a -m "Add stuff"'
        self.check_validity(before, after)

    def test_gm_one_message(self):
        before = "gm upskill"
        after = 'git commit -m "Upskill"'
        self.check_validity(before, after)

    def test_gma_one_message(self):
        before = "gma download"
        after = 'git commit -a -m "Download"'
        self.check_validity(before, after)

    def test_gm_gitpush(self):
        before = "gm update the mainframe ,,"
        after = 'git commit -m "Update the mainframe" && git push'
        self.check_validity(before, after)

    def test_gma_gitpush(self):
        before = "gma update the mainframe ,,"
        after = 'git commit -a -m "Update the mainframe" && git push'
        self.check_validity(before, after)

    def test_gm_gitpush_args(self):
        before = "gm remove old code ,, origin dev"
        after = 'git commit -m "Remove old code" && git push origin dev'
        self.check_validity(before, after)

    def test_gma_gitpush_args(self):
        before = "gma remove old code ,, origin dev"
        after = 'git commit -a -m "Remove old code" && git push origin dev'
        self.check_validity(before, after)

    def test_gma_gitpush_force(self):
        before = "gma force rebase time ,, -f"
        after = 'git commit -a -m "Force rebase time" && git push -f'
        self.check_validity(before, after)

    def test_gm_gitpush_normal(self):
        before = "gm add the index.js file ,,"
        after = 'git commit -m "Add the index.js file" && git push'
        self.check_validity(before, after)

    def test_gma_gitpush_normal2(self):
        before = "gma update stuff for release 2 ,, origin main"
        after = 'git commit -a -m "Update stuff for release 2" && \
git push origin main'
        self.check_validity(before, after)

    def test_gm_blank_gitpush(self):
        before = "gm ,,"
        after = "git commit && git push"
        self.check_validity(before, after)

    def test_gma_blank_gitpush(self):
        before = "gma ,,"
        after = "git commit -a && git push"
        self.check_validity(before, after)

    def test_invalid_command(self):
        before = "gmessi got stuff"
        after = 'echo "undefined command gmessi"'
        self.check_validity(before, after)


if __name__ == "__main__":
    unittest.main()
