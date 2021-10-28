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

    def test_gmp_blank(self):
        before = "gmp"
        after = "git commit && git push"
        self.check_validity(before, after)

    def test_gmap_blank(self):
        before = "gmap"
        after = "git commit -a && git push"
        self.check_validity(before, after)

    def test_gm_message(self):
        before = "gm add new features"
        after = 'git commit -m "Add new features"'
        self.check_validity(before, after)

    def test_gm_one_message(self):
        before = "gm upskill"
        after = 'git commit -m "Upskill"'
        self.check_validity(before, after)

    def test_gma_message(self):
        before = "gma add stuff"
        after = 'git commit -a -m "Add stuff"'
        self.check_validity(before, after)

    def test_gma_one_message(self):
        before = "gma download"
        after = 'git commit -a -m "Download"'
        self.check_validity(before, after)

    def test_gmp_message(self):
        before = "gmp change some things"
        after = 'git commit -m "Change some things" && git push'
        self.check_validity(before, after)

    def test_gmap_message(self):
        before = "gmap update the variables"
        after = 'git commit -a -m "Update the variables" && git push'
        self.check_validity(before, after)

    def test_gmp_branch_blank(self):
        before = "gmp ,, origin main"
        after = "git commit && git push origin main"
        self.check_validity(before, after)

    def test_gmap_branch_blank(self):
        before = "gmap ,, origin main"
        after = "git commit -a && git push origin main"
        self.check_validity(before, after)

    def test_gmp_branch_message(self):
        before = "gmp get some stuff going ,, origin main"
        after = 'git commit -m "Get some stuff going" && git push origin main'
        self.check_validity(before, after)

    def test_gmap_branch_message(self):
        before = "gmap get some stuff going ,, origin main"
        after = 'git commit -a -m "Get some stuff going" && git push origin main'
        self.check_validity(before, after)

    def test_gm_with_two_commas(self):
        before = "gm update the mainframe ,,"
        after = 'git commit -m "Update the mainframe ,,"'
        self.check_validity(before, after)


if __name__ == "__main__":
    unittest.main()
