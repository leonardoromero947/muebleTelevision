from gpiozero import Button

class Switch(object):

    #ATRIBUTOS
    activar_log = False
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
    btn_2H = Button(25)
    btn_2E = Button(23)


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

    # self.led_testigo.on()

    def status_1A(self):
        if self.btn_1A.is_active:
            if self.activar_log:
                print("1A Liberado")
            return False
        else:
            if self.activar_log:
                print("1A Presionado")
            return True

    def status_1B(self):
        if self.btn_1B.is_active:
            if self.activar_log:
                print("1B Liberado ")
            return False
        else:
            if self.activar_log:
                print("1B Presionado")
            return True

    def status_1C(self):
        if self.btn_1C.is_active:
            if self.activar_log:
                print("1C Liberado ")
            return False
        else:
            if self.activar_log:
                print("1C Presionado")
            return True

    def status_1D(self):
        if self.btn_1D.is_active:
            if self.activar_log:
                print("1D Liberado ")
            return False
        else:
            if self.activar_log:
                print("1D Presionado")
            return True

    def status_1E(self):
        if self.btn_1E.is_active:
            if self.activar_log:
                print("1E Liberado ")
            return False
        else:
            if self.activar_log:
                print("1E Presionado")
            return True

    def status_1F(self):
        if self.btn_1F.is_active:
            if self.activar_log:
                print("1F Liberado ")
            return False
        else:
            if self.activar_log:
                print("1F Presionado")
            return True

    def status_1G(self):
        if self.btn_1G.is_active:
            if self.activar_log:
                print("1G Liberado ")
            return False
        else:
            if self.activar_log:
                print("1G Presionado")
            return True

    def status_1H(self):
        if self.btn_1H.is_active:
            if self.activar_log:
                print("1H Liberado ")
            return False
        else:
            if self.activar_log:
                print("1H Presionado")
            return True

    def status_2A(self):
        if self.btn_2A.is_active:
            if self.activar_log:
                print("2A Liberado ")
            return False
        else:
            if self.activar_log:
                print("2A Presionado")
            return True

    def status_2D(self):
        if self.btn_2D.is_active:
            if self.activar_log:
                print("2D Liberado ")
            return False
        else:
            if self.activar_log:
                print("2D Presionado")
            return True

    def status_2E(self):
        if self.btn_2E.is_active:
            if self.activar_log:
                print("2E Liberado ")
            return False

        else:
            if self.activar_log:
                print("2E Presionado")
            return True

    def status_2H(self):
        if self.btn_2H.is_active:
            if self.activar_log:
                print("2H Liberado ")
            return False
        else:
            if self.activar_log:
                print("2H Presionado")
            return True

    def status_seguro(self):
        if self.btn_seguro.is_active:
            if self.activar_log:
                print("SEGURO Liberado ")
            return False
        else:
            if self.activar_log:
                print("SEGURO Presionado")
            return True

    def status_accionador(self):
        if self.btn_accionador.is_active:
            if self.activar_log:
                print("Inicio Liberado ")
            return False
        else:
            if self.activar_log:
                print("Inicio Presionado")
            return  True

    def say_hello(self):
         print("Hello")

    def say_goodbye(self):
         print("Goodbye")

    def cerrarPines(self):
        self.btn_1A.close()
    # def prueba(self):
    #     self.btn_1A.when_activated = say_hello
    #     self.btn_1A.when_deactivated = say_goodbye