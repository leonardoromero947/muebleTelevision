from gpiozero import LED,Buzzer
from time import sleep
import switchs as SW
import posicion_mueble as POMU
import armado_mueble as ARMU
import memoria as MEM

class Motores(object):

    ### MOTORES
    memoria = MEM.Extra()
    pruebas = False
    motores_posicion_mueble = POMU.Posicion_Mueble()
    switch_motores = SW.Switch()
    armar = ARMU.Armado_mueble()
    mueble_cerrado = False
    mueble_abierto = False
    mueble_pruebas = False
    mueble_proceso = 0
    log_activo = False


    testigo = LED(14)
    buzzer = Buzzer(24)

    def ejecucion_inicial(self):
        if(self.switch_motores.status_accionador() or self.switch_motores.status_accionador_control()):
            if(self.switch_motores.status_seguro()):
                print ("SEGURO ACTIVO IMPOSIBLE EJECUTAR MOVIMIENTO")
                self.buzzer.on()
                sleep(1)
                self.buzzer.off()
                sleep(1)
                self.buzzer.on()
                sleep(1)
                self.buzzer.off()
                return False
            else:
                return True
        else:
            return False

    def valida_status_mueble(self):
        self.motores_posicion_mueble.log_activo(self.log_activo)
        self.memoria.leer_xml()
        if(self.memoria.proceso == 1):
            print("MUEBLE INICIALMENTE CERRADO")
            self.mueble_cerrado_proceso_abrir()
        if(self.memoria.proceso == 6 or self.memoria.proceso == 7):
            print("MUEBLE INICIALMENTE ABIERTO")
            self.mueble_abierto_proceso_cerrar()
        if(self.memoria.proceso != 6 and self.memoria.proceso != 1 and self.memoria.proceso != 7):
            print("MUEBLE REGRESANDO DE UN ESTADO INCOMPLETO")
            if(self.memoria.abierto is True):
                print("MUEBLE SEGUIR APERTURA")
                self.mueble_cerrado_proceso_abrir()
            else:
                if(self.memoria.cerrado is True):
                    print("MUEBLE SEGUIR CIERRE")
                    self.mueble_abierto_proceso_cerrar()
                else:
                    self.mueble_cerrado_proceso_abrir()


    def mueble_cerrado_proceso_abrir(self):
        while True:
            print("Modo a = ABRIR LADO A")
            print("Modo b = ABRIR LADO B")
            print("Modo c = ABRIR AMBOS LADOS")
            continuar = raw_input("ABRIR MUEBLE MODO a, b o c")
            print("Seleccionaste: "+continuar)
            if continuar in ('a', 'A'):
                self.abrir_solo_puerta_a()
                break;
            else:
                if continuar in ('b', 'B'):
                    self.abrir_solo_puerta_b()
                    break;
                else:
                    if continuar in ('c', 'C'):
                        self.abrir_mueble_completo()
                        break;
                    else:
                        print("OPCION INVALIDA " + continuar)

    def mueble_abierto_proceso_cerrar(self):
        while True:
            print("Modo a = CEERAR LADO A")
            print("Modo b = CERRAR LADO B")
            print("Modo c = CERRAR AMBOS LADOS")
            continuar = raw_input("CERRAR MUEBLE MODO a, b o c")
            print("Seleccionaste: "+continuar)
            if continuar in ('a', 'A'):
                self.cerrar_solo_puerta_a()
                break;
            else:
                if continuar in ('b', 'B'):
                    self.cerrar_solo_puerta_b()
                    break;
                else:
                    if continuar in ('c', 'C'):
                        self.cerrar_mueble_completo()
                        break;
                    else:
                        print("OPCION INVALIDA " + continuar)

    def abrir_solo_puerta_a(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("A")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(3)
            self.error_fatal()
        if (status_mueble == 1):
            self.memoria.insertar_estados_finales_xml(1)
            self.armar.poste1_abrir()
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 3):
            self.armar.puerta1_abrir()
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 4):
            self.armar.puerta1_guardar()
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 6):
            status_mueble = self.valida_continuar("A")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE ABIERTO LADO A")

    def abrir_solo_puerta_b(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("B")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(3)
            self.error_fatal()
        if (status_mueble == 1):
            self.memoria.insertar_estados_finales_xml(1)
            status_mueble = self.valida_continuar("B")
            self.armar.poste2_abrir()
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 3):
            self.armar.puerta2_abrir()
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 5):
            self.armar.puerta2_guardar()
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 7):
            status_mueble = self.valida_continuar("B")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE ABIERTO LADO B")

    def abrir_mueble_completo(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("C")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(1)
            self.error_fatal()
        if (status_mueble == 1):
            self.memoria.insertar_estados_finales_xml(1)
            self.armar.poste1_abrir()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 2):
            self.armar.poste2_abrir()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 3):
            self.armar.puerta1_abrir()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 4):
            self.armar.puerta2_abrir()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 5):
            self.armar.puerta1_guardar()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 6):
            self.armar.puerta2_guardar()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 7):
            status_mueble = self.valida_continuar("C")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE COMPLETAMENTE ABIERTO")

    def cerrar_solo_puerta_a(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("A")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(3)
            self.error_fatal()
        if (status_mueble == 6):
            self.memoria.insertar_estados_finales_xml(2)
            self.armar.puerta1_desplegar()
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 4):
            self.armar.puerta1_cerrar()
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 3):
            self.armar.poste1_cerrar()
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 1):
            status_mueble = self.valida_continuar("A")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE CERRADO LADO A")

    def cerrar_solo_puerta_b(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("B")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(3)
            self.error_fatal()
        if (status_mueble == 7):
            self.memoria.insertar_estados_finales_xml(2)
            self.armar.puerta2_desplegar()
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 5):
            self.armar.puerta2_cerrar()
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 3):
            self.armar.poste2_cerrar()
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 1):
            status_mueble = self.valida_continuar("B")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE CERRADO LADO B")

    def cerrar_mueble_completo(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("C")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(3)
            self.error_fatal()
        if (status_mueble == 7):
            self.memoria.insertar_estados_finales_xml(2)
            self.armar.puerta2_desplegar()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 6):
            self.armar.puerta1_desplegar()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 5):
            self.armar.puerta2_cerrar()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 4):
            self.armar.puerta1_cerrar()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 3):
            self.armar.poste2_cerrar()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 2):
            self.armar.poste1_cerrar()
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 1):
            status_mueble = self.valida_continuar("C")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE COMPLETAMENTECERRADO")

    def valida_continuar(self,tipo):
        numero_status = 0
        if self.pruebas:
            validacion = True
            while validacion:
                numero_status = self.motores_posicion_mueble.consultar_status_mueble(tipo)
                continuar = raw_input("La posicion del diagrama es correcta s/n?")
                if continuar in ('s', 'S'):
                    self.memoria.insertar_proceso_xml(numero_status)
                    break
                else:
                    validacion = True
            return numero_status
        else:
            numero_status = self.motores_posicion_mueble.consultar_status_mueble(tipo)
            self.memoria.insertar_proceso_xml(numero_status)
            return numero_status

    def error_fatal(self):
        print("PELIGRO POSICION INVALIDA")
        self.buzzer.on()
        sleep(1)
        self.buzzer.off()
        self.buzzer.on()
        sleep(1)
        self.buzzer.off()