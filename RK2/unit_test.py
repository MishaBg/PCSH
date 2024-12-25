import unittest

class TestCathFunctions(unittest.TestCase):

    def setUp(self):
        self.faculs = [
            Facul(1, 'РК'),
            Facul(2, 'РТ'),
            Facul(3, 'ИУ'),
        ]
        self.caths = [
            Cath(1, 'ИУ5', 25000, 3),
            Cath(2, 'ИУ6', 35000, 3),
            Cath(3, 'ИУ7', 45000, 3),
            Cath(4, 'РК6', 35000, 1),
            Cath(5, 'РТ5', 25000, 2),
        ]
        self.CathFaculs = [
            CathFacul(1, 1),
            CathFacul(2, 2),
            CathFacul(3, 3),
            CathFacul(3, 4),
            CathFacul(3, 5),
        ]

    def test_get_one_to_many(self):
        result = get_one_to_many(self.caths, self.faculs)
        expected = [
            ('ИУ5', 25000, 'ИУ'),
            ('ИУ6', 35000, 'ИУ'),
            ('ИУ7', 45000, 'ИУ'),
            ('РК6', 35000, 'РК'),
            ('РТ5', 25000, 'РТ'),
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_get_many_to_many(self):
        result = get_many_to_many(self.caths, self.faculs, self.CathFaculs)
        expected = [
            ('ИУ5', 25000, 'ИУ'),
            ('ИУ6', 35000, 'ИУ'),
            ('ИУ7', 45000, 'ИУ'),
            ('РК6', 35000, 'РК'),
            ('РТ5', 25000, 'РТ'),
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_count_caths_by_fio(self):
        one_to_many = [
            ('ИУ5', 25000, 'ИУ'),
            ('ИУ6', 35000, 'ИУ'),
            ('ИУ7', 45000, 'ИУ'),
            ('РК6', 35000, 'РК'),
            ('РТ5', 25000, 'РТ'),
        ]
        result = count_caths_by_fio(one_to_many)
        expected = [
            ['ИУ', 3],
            ['РК', 1],
            ['РТ', 1],
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_filter_caths_by_fio(self):
        many_to_many = [
            ('ИУ5', 25000, 'ИУ'),
            ('ИУ6', 35000, 'ИУ'),
            ('ИУ7', 45000, 'ИУ'),
            ('РК6', 35000, 'РК'),
            ('РТ5', 25000, 'РТ'),
        ]
        result = filter_caths_by_fio(many_to_many)
        expected = [
            ['ИУ5', 'ИУ'],
            ['ИУ6', 'ИУ'],
            ['ИУ7', 'ИУ'],
        ]
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == '__main__':
    unittest.main()
