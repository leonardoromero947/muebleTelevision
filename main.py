#DOCUMENTO INICIAL DE FUNCIONAMIENTO
import switchs as SW
from gpiozero import Button


class Main:
    switch = SW.Switch()
    vida = True
    btn_accionador = Button(26)

    def iniciar(self):
        while self.vida:
            self.switch.pruebaSwitchs()
            self.vida = self.opcional()

    def opcional(self):
        continuar = raw_input("Continuar S/N")
        if continuar in ('s','S'):
            return True
        else:
            print("Adios")
            return False


m = Main()
m.iniciar()