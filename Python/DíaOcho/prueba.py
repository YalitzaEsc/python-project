import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "Mi gata se llama Kitty"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "MI GATA SE LLAMA KITTY")


if __name__ == '__main__':
    unittest.main()

