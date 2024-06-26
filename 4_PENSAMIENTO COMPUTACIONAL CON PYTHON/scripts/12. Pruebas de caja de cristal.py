import unittest


def mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):

    def test_es_mayor(self): # La palabra Test tiene que estar
        edad = 18
        result = mayor_edad(edad)

        self.assertEqual(result, True)

    def test_es_menor(self): # La palabra Test tiene que estar
        edad = 20
        result = mayor_edad(edad)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
