from unittest import TestCase
import src.calculadora_de_cambio as calc

class TestesDaCalculadoraDeCambio(TestCase):

    def teste_valor_0_resultado_0(self):
        valor = 0
        taxa = 3.37
        resultado_esperado = 0

        resultado_obtido = calc.converter(valor, taxa)

        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_valor_1_resultado_3_70(self):
        valor = 1
        taxa = 3.37
        resultado_esperado = 3.70

        resultado_obtido = calc.converter(valor, taxa)

        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_valor_2_3_resultado_8_52(self):
        valor = 2.3
        taxa = 3.37
        resultado_esperado = 8.52

        resultado_obtido = calc.converter(valor, taxa)

        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_valor_2_3_resultado_37_07(self):
        valor = 10
        taxa = 3.37
        resultado_esperado = 37.07

        resultado_obtido = calc.converter(valor, taxa)

        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_valor_0_1_resultado_0_37(self):
        valor = 0.1
        taxa = 3.37
        resultado_esperado = 0.37

        resultado_obtido = calc.converter(valor, taxa)

        self.assertEqual(resultado_obtido, resultado_esperado)