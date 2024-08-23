import math

def converter(valor, taxa):
    imposto = 1.1
    calculo = int(valor * taxa * imposto * 100)
    return calculo / 100