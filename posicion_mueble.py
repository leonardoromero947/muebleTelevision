import switchs as SW

class Posicion_Mueble(object):

    sts = SW.Switch()
    activar_log = False
    activar_log_request = False
    def log_activo(self, seleccion):
        self.sts.activar_log = False
        self.activar_log_request = seleccion
        self.id_posicion = 0

    def puerta1_abierta(self):
        # 1A Falso
        # 1B Verdadero
        # 1D Falso
        # 2D Verdadero
        if((self.sts.status_1A() is False) and (self.sts.status_1B() is True) and (self.sts.status_1D() is False)
        and (self.sts.status_2D() is True)):
            if self.activar_log:
                print ("Puerta 1 :::: ABIERTA")
            return True
        else:
            return False

    def puerta1_cerrada(self):
        # 1A Falso
        # 1B Verdadero
        # 1D Verdadero
        # 2D Falso
        if((self.sts.status_1A() is False) and (self.sts.status_1B() is True) and (self.sts.status_1D() is True)
        and (self.sts.status_2D() is False)):
            if self.activar_log:
                print ("Puerta 1 :::: CERRADA")
            return True
        else:
            return False

    def puerta1_guardada(self):
        # 1A Verdadero
        # 1B Falso
        # 1D Falso
        # 2D Verdadero
        if((self.sts.status_1A() is True) and (self.sts.status_1B() is False) and (self.sts.status_1D() is False)
        and (self.sts.status_2D() is True)):
            if self.activar_log:
                print ("Puerta 1 :::: GUARDADA")
            return True
        else:
            return False

    def puerta2_abierta(self):
        # 1E Falso
        # 1F Verdadero
        # 1H Falso
        # 2H Verdadero
        if((self.sts.status_1E() is False) and (self.sts.status_1F() is True) and (self.sts.status_1H() is False)
        and (self.sts.status_2H() is True)):
            if self.activar_log:
                print ("Puerta 2  :::: ABIERTA")
            return True
        else:
            return False

    def puerta2_cerrada(self):
        # 1E Falso
        # 1F Verdadero
        # 1H Verdadero
        # 2H Falso
        if((self.sts.status_1E() is False) and (self.sts.status_1F() is True) and (self.sts.status_1H() is True)
        and (self.sts.status_2H() is False)):
            if self.activar_log:
                print ("Puerta 2  :::: CERRADA")
            return True
        else:
            return False

    def puerta2_guardada(self):
        # 1E Verdadero
        # 1F Falso
        # 1H Falso
        # 2H Verdadero
        if((self.sts.status_1E() is True) and (self.sts.status_1F() is False) and (self.sts.status_1H() is False)
        and (self.sts.status_2H() is True)):
            if self.activar_log:
                print ("Puerta 2  :::: GUARDADA")
            return True
        else:
            return False

    def poste1_abierta(self):
        # 1C Verdadero
        # 2A Falso
        if ((self.sts.status_1C() is True) and (self.sts.status_2A() is False)):
            if self.activar_log:
                print ("Poste 1 :::: ABIERTA")
            return True
        else:
            return False

    def poste1_cerrada(self):
        # 1C Falso
        # 2A Verdadero
        if ((self.sts.status_1C() is False) and (self.sts.status_2A() is True)):
            if self.activar_log:
                print ("Poste 1 :::: CERRADA")
            return True
        else:
            return False

    def poste2_abierta(self):
        # 1G Verdadero
        # 2E Falso
        if((self.sts.status_1G() is True) and (self.sts.status_2E() is False)):
            if self.activar_log:
                print ("Poste 2 :::: ABIERTA")
            return True
        else:
            return False

    def poste2_cerrada(self):
        # 1G Falso
        # 2E Verdadero
        if((self.sts.status_1G() is False) and (self.sts.status_2E() is True)):
            if self.activar_log:
                print ("Poste 2 :::: CERRADA")
            return True
        else:
            return False

    def diagrama(self):
        print (" _ _ _ _ ")
        print ("|P|D|D|P| ")
        print ("|O|O|O|O| ")
        print ("|L|O|O|L| ")
        print ("|E|R|R|E| ")
        print ("|1|1|2|2| ")

    def posicion_partes_mueble(self):
        self.puerta1_abierta()
        self.puerta1_cerrada()
        self.puerta1_guardada()
        self.puerta2_abierta()
        self.puerta2_cerrada()
        self.puerta2_guardada()
        self.poste1_abierta()
        self.poste1_cerrada()
        self.poste2_abierta()
        self.poste2_cerrada()

    def log_switch_activar(self):
        self.sts.activar_log = self.activar_log_request
        self.sts.pruebaSwitchs()
        self.sts.activar_log = False
        self.activar_log = self.activar_log_request
        self.posicion_partes_mueble()
        self.activar_log = False

    def opcion_correcta(self,numero):
        print ("MUEBLE "+`numero`)
        self.log_switch_activar()
        self.id_posicion = numero
        self.diagrama()

    def consultar_status_mueble(self):
        # 01 MUEBLE ::: _ _ _ _
        # 02 MUEBLE ::: | _ _ _
        # 03 MUEBLE ::: | _ _ |
        # 04 MUEBLE ::: | | _ |
        # 05 MUEBLE ::: | | | |
        # 06 MUEBLE ::: | * | |
        # 07 MUEBLE ::: | * * |
        # 08 MUEBLE ::: _ * * |
        # 09 MUEBLE ::: _ * * _
        # 10 MUEBLE ::: | * * _
        # 11 MUEBLE ::: | | * |
        # 12 MUEBLE ::: | _ | |
        # 13 MUEBLE ::: _ _ _ |
        # 00 MUEBLE ::: ? ? ? ?
        if((self.poste1_cerrada() is True) and (self.puerta1_cerrada() is True) and
        (self.puerta2_cerrada() is True) and (self.poste2_cerrada() is True)):
            self.opcion_correcta(1)
            print (" _ _ _ _")
        if((self.poste1_abierta() is True) and (self.puerta1_cerrada() is True) and
        (self.puerta2_cerrada() is True) and (self.poste2_cerrada() is True)):
            self.opcion_correcta(2)
            print (" | _ _ _")
        if ((self.poste1_abierta() is True) and (self.puerta1_cerrada() is True) and
        (self.puerta2_cerrada() is True) and (self.poste2_abierta() is True)):
            self.opcion_correcta(3)
            print (" | _ _ |")
        if ((self.poste1_abierta() is True) and (self.puerta1_abierta() is True) and
        (self.puerta2_cerrada() is True) and (self.poste2_abierta() is True)):
            self.opcion_correcta(4)
            print (" | | _ |")
        if ((self.poste1_abierta() is True) and (self.puerta1_abierta() is True) and
        (self.puerta2_abierta() is True) and (self.poste2_abierta() is True)):
            self.opcion_correcta(5)
            print (" | | | |")
        if ((self.poste1_abierta() is True) and (self.puerta1_guardada() is True) and
        (self.puerta2_abierta() is True) and (self.poste2_abierta() is True)):
            self.opcion_correcta(6)
            print (" | * | |")
        if ((self.poste1_abierta() is True) and (self.puerta1_guardada() is True) and
        (self.puerta2_guardada() is True) and (self.poste2_abierta() is True)):
            self.opcion_correcta(7)
            print (" | * * |")
        if ((self.poste1_cerrada() is True) and (self.puerta1_guardada() is True) and
        (self.puerta2_guardada() is True) and (self.poste2_abierta() is True)):
            self.opcion_correcta(8)
            print (" _ * * |")
        if ((self.poste1_cerrada() is True) and (self.puerta1_guardada() is True) and
        (self.puerta2_guardada() is True) and (self.poste2_cerrada() is True)):
            self.opcion_correcta(9)
            print (" _ * * _")
        if ((self.poste1_abierta() is True) and (self.puerta1_guardada() is True) and
        (self.puerta2_guardada() is True) and (self.poste2_cerrada() is True)):
            self.opcion_correcta(10)
            print (" | * * _")
        if ((self.poste1_abierta() is True) and (self.puerta1_guardada() is True) and
        (self.puerta2_guardada() is True) and (self.poste2_cerrada() is True)):
            self.opcion_correcta(11)
            print (" | | * |")
        if ((self.poste1_abierta() is True) and (self.puerta1_cerrada() is True) and
        (self.puerta2_abierta() is True) and (self.poste2_abierta() is True)):
            self.opcion_correcta(12)
            print (" | _ | |")
        if ((self.poste1_cerrada() is True) and (self.puerta1_cerrada() is True) and
        (self.puerta2_cerrada() is True) and (self.poste2_abierta() is True)):
            self.opcion_correcta(13)
            print (" _ _ _ |")
        if(self.id_posicion == 0):
            self.opcion_correcta(0)
            print (" ? ? ? ?")
        return self.id_posicion

    def instructivo_digital(self):
        print("*****DIAGRAMA DIGITAL****")
        print("*****NOMENCLATURA****")
        print(" _   ---->  CERRADO")
        print(" |   ---->  ABIERTO ")
        print(" *   ---->  GUARDADO ")
        print(" ?   ---->  INVALIDO ")
        print("POSTE == POLE")
        print("PUERTA == DOOR")

    def ejemplo_diagrama(self):
        print("*****EJEMPLO A POSTES ABIERTOS PUERTAS CERRADAS****")
        print (" _ _ _ _ ")
        print ("|P|D|D|P| ")
        print ("|O|O|O|O| ")
        print ("|L|O|O|L| ")
        print ("|E|R|R|E| ")
        print ("|1|1|2|2| ")
        print(" | _ _ |")
        print("*****EJEMPLO B MUEBLE ABIERTO****")
        print (" _ _ _ _ ")
        print ("|P|D|D|P| ")
        print ("|O|O|O|O| ")
        print ("|L|O|O|L| ")
        print ("|E|R|R|E| ")
        print ("|1|1|2|2| ")
        print(" _ * * _")

    def mueble_cerrado(self):
        if((self.puerta1_cerrada() is True) and (self.puerta2_cerrada() is True) and
        (self.poste1_cerrada() is True) and (self.poste2_cerrada() is True)):
            print ("Mueble :::: CERRADO")
            return True
        else:
            return False

    def mueble_(self):
        if((self.puerta1_cerrada() is True) and (self.puerta2_cerrada() is True) and
        (self.poste1_cerrada() is True) and (self.poste2_cerrada() is True)):
            print ("Mueble :::: CERRADO")
            return True
        else:
            return False