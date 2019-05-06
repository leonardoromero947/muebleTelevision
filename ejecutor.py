import switchs as SW


class Ejecutor(object):
    switch = SW.Switch()
    vida = True

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