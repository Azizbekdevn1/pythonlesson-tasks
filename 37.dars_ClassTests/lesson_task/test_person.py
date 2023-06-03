# Sana:25.05.2023 year
# Mavzu:Classni testlash
# Muallif:Murodov Azizbek

import unittest
from person import Shaxs


class testPerson(unittest.TestCase):
    """Shaxs classini tekshirishuchun test"""

    def setUp(self):
        ism = "Azizbek"
        self.familiya = "Murodov"
        self.passport = "AC2296088"
        self.tyil = 2003
        self.gender = "erkak"
        self.person1 = Shaxs(ism, self.familiya, self.passport, self.tyil)
        self.person2 = Shaxs(ism, self.familiya, self.passport, self.tyil, self.gender)

    def test_create(self):
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(self.person1.passport)
        self.assertIsNotNone(self.person1.familiya)
        self.assertIsNotNone(self.person1.ism)
        # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiramiz
        self.assertIsNone(self.person1.gender)
        # Qiymat tengligini assertEquals metodi bilan tekshiramiz
        self.assertEqual(20, self.person1.get_age(2023))
        # avto2 narhini tekshiramiz
        self.assertEqual(self.gender, self.person2.gender)

    def test_get_info(self):
        person1_info = "Azizbek Murodov. Passport:AC2296088, 2003-yilda tug'ilgan"
        self.assertEqual(self.person1.get_info(), person1_info)


unittest.main()
