import unittest

def contar_vocales(palabra):
    vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    resultado = {}
    for letra in palabra:
        if letra in vocales:
            if letra in resultado.keys():
                resultado[letra] += 1
            else:
                resultado[letra] = 1
    return resultado

class TestContarVocales(unittest.TestCase):
    def test_sin_vocales(self):
        palabra = "tryhgf"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {})

    def test_con_vocal_o(self):
        palabra = "sol"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 1})

    def test_con_vocal_doble_o(self):
        palabra = "solo"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 2})

    def test_con_dos_vocales(self):
        palabra = "sola"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 1, "a": 1})

    def test_con_todas_las_vocales(self):
        palabra = "solamente quiero que gane Boca"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado,{"a": 3, "e": 5, "i": 1, "o": 3, "u": 2})

    def test_con_vocales_en_mayuscula(self):
        palabra = "SOlAmente quIerO"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado,{'O': 2, 'A': 1, 'e': 3, 'u': 1, 'I': 1})

    def test_con_cadena_vacia(self):
        palabra = ""
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {})

    def test_con_numeros_y_caracteres_especiales(self):
        palabra = "H0l4 mUnd0!"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {'U': 1})

unittest.main()
