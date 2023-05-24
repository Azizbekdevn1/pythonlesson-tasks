import unittest
from upperchar import Upperchar


class test_Upperchar(unittest.TestCase):
    def test_upperchar(self):
        auditable = Upperchar(
            ["easy", "diffucult", "normal", "wrap", "column", "table"]
        )
        self.assertEqual(
            auditable, ["Easy", "diffucult", "Normal", "Wrap", "Column", "Table"]
        )

    def test_uppercharother(self):
        auditable = Upperchar(["edj", "dif", "norm", "wrap", "colum", "tabl"])
        self.assertEqual(auditable, ["edj", "Dif", "Norm", "Wrap", "Colum", "Tabl"])


unittest.main()
