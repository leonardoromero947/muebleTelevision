from gpiozero import Button
from time import sleep

class Switch(object):

    #ATRIBUTOS
    btn_seguro = Button(19)
    btn_accionador = Button(26)
    btn_1A = Button(27)
    btn_1B = Button(22)
    btn_1C = Button(10)
    btn_1D = Button(9)
    btn_1E = Button(11)
    btn_1F = Button(5)
    btn_1G = Button(6)
    btn_1H = Button(13)
    btn_2A = Button(15)
    btn_2D = Button(18)
    btn_2E = Button(25)
    btn_2H = Button(23)

    def pruebaSwitchs(self):
        self.status_1A()
        self.status_1B()
        self.status_1C()
        self.status_1D()
        self.status_1E()
        self.status_1F()
        self.status_1G()
        self.status_1H()
        self.status_2A()
        self.status_2D()
        self.status_2E()
        self.status_2H()
        self.status_seguro()
        self.status_accionador()

    def status_1A(self):
        if self.btn_1A.is_active:
            print("1A Presionado")
            sleep(2)
        else:
            print("1A Liberado")
            sleep(2)

    def status_1B(self):
        if self.btn_1B.is_active:
            print("1B Presionado")
            sleep(2)
        else:
            print("1B Liberado")
            sleep(2)

    def status_1C(self):
        if self.btn_1C.is_active:
            print("1C Presionado")
            sleep(2)
        else:
            print("1C Liberado")
            sleep(2)

    def status_1D(self):
        if self.btn_1D.is_active:
            print("1D Presionado")
            sleep(2)
        else:
            print("1D Liberado")
            sleep(2)

    def status_1E(self):
        if self.btn_1E.is_active:
            print("1E Presionado")
            sleep(2)
        else:
            print("1E Liberado")
            sleep(2)

    def status_1F(self):
        if self.btn_1F.is_active:
            print("1F Presionado")
            sleep(2)
        else:
            print("1F Liberado")
            sleep(2)

    def status_1G(self):
        if self.btn_1G.is_active:
            print("1G Presionado")
            sleep(2)
        else:
            print("1G Liberado")
            sleep(2)

    def status_1H(self):
        if self.btn_1H.is_active:
            print("1H Presionado")
            sleep(2)
        else:
            print("1H Liberado")
            sleep(2)

    def status_2A(self):
        if self.btn_2A.is_active:
            print("2A Presionado")
            sleep(2)
        else:
            print("2A Liberado")
            sleep(2)

    def status_2D(self):
        if self.btn_2D.is_active:
            print("2D Presionado")
            sleep(2)
        else:
            print("2D Liberado")
            sleep(2)

    def status_2E(self):
        if self.btn_2E.is_active:
            print("2E Presionado")
            sleep(2)
        else:
            print("2E Liberado")
            sleep(2)

    def status_2H(self):
        if self.btn_2H.is_active:
            print("2H Presionado")
            sleep(2)
        else:
            print("2H Liberado")
            sleep(2)

    def status_seguro(self):
        if self.btn_seguro.is_active:
            print("SEGURO Presionado")
            sleep(2)
        else:
            print("SEGURO Liberado")
            sleep(2)

    def status_accionador(self):
        if self.btn_accionador.is_active:
            print("Inicio Presionado")
            sleep(2)
        else:
            print("Inicio Liberado")
            sleep(2)

    def say_hello(self):
         print("Hello")

    def say_goodbye(self):
         print("Goodbye")

    def cerrarPines(self):
        self.btn_1A.close()
    # def prueba(self):
    #     self.btn_1A.when_activated = say_hello
    #     self.btn_1A.when_deactivated = say_goodbye