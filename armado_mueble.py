from gpiozero import Button,LED,Buzzer
import switchs as SW
import time
import raspardino_response as RDNR

class Armado_mueble(object):

    armado_mueble_switch = SW.Switch()
    arduino = RDNR.Raspardino()
    H1L = LED(15)
    H1R = LED(18)
    H2L = LED(23)
    H2R = LED(25)
    H3L = LED(8)
    H3R = LED(7)
    H4L = LED(12)
    H4R = LED(16)
    H5L = LED(20)
    H5R = LED(21)
    H6L = LED(17)
    H6R = LED(4)
    H1L_tiempo_definido = 600
    H1R_tiempo_definido = 600
    H2L_tiempo_definido = 600
    H2R_tiempo_definido = 600
    H3L_tiempo_definido = 600
    H3R_tiempo_definido = 600
    H4L_tiempo_definido = 600
    H4R_tiempo_definido = 600
    H5L_tiempo_definido = 600
    H5R_tiempo_definido = 600
    H6L_tiempo_definido = 600
    H6R_tiempo_definido = 600
    delay_puerta_apertura_A = 0.5
    delay_puerta_cierre_A = 1
    delay_puerta_apertura_B = 0.5
    delay_puerta_cierre_B = 1
    delay_poste_apertura_A = 1.2
    delay_poste_cierre_A = 0.5
    delay_poste_apertura_B = 1.2
    delay_poste_cierre_B = 0.5

    def get_tiempos_xml(self):
        pass

    def cronometro(self,inicio_tiempo):
        tiempo_final = time.time()
        return (tiempo_final - inicio_tiempo)

    def puerta1_abrir(self):
        tiempo = time.time()
        tiempo_adicional = 0
        contador = 0
        while True:
            if(self.armado_mueble_switch.status_1D()):
                self.arduino.espruino_cmd('y').strip()

                if(contador == 0):
                    self.H3R.on()
                    time.sleep(3.5)
                    self.H3R.off()
                    time.sleep(2)
                    contador = 1
                else:
                    self.H3R.on()
            if(self.armado_mueble_switch.status_2D()):
                time.sleep(self.delay_puerta_apertura_A)
                self.arduino.espruino_cmd('w').strip()
                self.H3R.off()
                print("PUERTA 1 ABIERTA")
                return True
                break
            if(self.armado_mueble_switch.status_seguro()):
                self.H3R.off()
                print("SEGURO ACTIVO PAUSA ABRIENDO PUERTA 1")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H3R.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if(self.cronometro(tiempo) > (self.H3R_tiempo_definido + tiempo_adicional)):
                self.H3R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta1_cerrar(self):
        tiempo = time.time()
        tiempo_adicional = 0
        while True:
            if (self.armado_mueble_switch.status_2D()):
                self.H3L.on()
            if (self.armado_mueble_switch.status_1D()):
                time.sleep(self.delay_puerta_cierre_A)
                self.H3L.off()
                print("PUERTA 1 CERRADA")
                return True
                break
            if (self.armado_mueble_switch.status_seguro()):
                self.H3L.off()
                print("SEGURO ACTIVO PAUSA CERRANDO PUERTA 1")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H3L.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if (self.cronometro(tiempo) > (self.H3L_tiempo_definido + tiempo_adicional)):
                self.H3L.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta1_guardar(self):
        tiempo = time.time()
        tiempo_adicional = 0
        while True:
            if (self.armado_mueble_switch.status_1B()):
                self.H2R.on()
            if (self.armado_mueble_switch.status_1A()):
                self.H2R.off()
                print("PUERTA 1 GUARDAR")
                return True
                break
            if (self.armado_mueble_switch.status_seguro()):
                self.H2R.off()
                print("SEGURO ACTIVO PAUSA GUARDAR PUERTA 1")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H2R.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if (self.cronometro(tiempo) > (self.H2R_tiempo_definido + tiempo_adicional)):
                self.H2R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta1_desplegar(self):
        tiempo = time.time()
        tiempo_adicional = 0
        while True:
            if (self.armado_mueble_switch.status_1A()):
                self.H2L.on()
            if (self.armado_mueble_switch.status_1B()):
                self.H2L.off()
                print("PUERTA 1 DESPLEGAR")
                return True
                break
            if (self.armado_mueble_switch.status_seguro()):
                self.H2L.off()
                print("SEGURO ACTIVO PAUSA DESPLEGAR PUERTA 1")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H2L.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if (self.cronometro(tiempo) > (self.H2L_tiempo_definido + tiempo_adicional)):
                self.H2L.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta2_abrir(self):
        tiempo = time.time()
        tiempo_adicional = 0
        contador = 0
        while True:
            if (self.armado_mueble_switch.status_1H()):
                self.arduino.espruino_cmd('z').strip()
                if(contador == 0):
                    self.H6R.on()
                    time.sleep(3.5)
                    self.H6R.off()
                    time.sleep(2)
                    contador = 1
                else:
                    self.H6R.on()
            if (self.armado_mueble_switch.status_2H()):
                time.sleep(self.delay_puerta_apertura_B)
                self.arduino.espruino_cmd('x').strip()
                self.H6R.off()
                print("PUERTA 2 ABIERTA")
                return True
                break
            if (self.armado_mueble_switch.status_seguro()):
                self.H6R.off()
                print("SEGURO ACTIVO PAUSA ABRIENDO PUERTA 2")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H6R.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if (self.cronometro(tiempo) > (self.H6R_tiempo_definido + tiempo_adicional)):
                self.H6R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta2_cerrar(self):
        tiempo = time.time()
        tiempo_adicional = 0
        while True:
            if (self.armado_mueble_switch.status_2H()):
                self.H6L.on()
            if (self.armado_mueble_switch.status_1H()):
                time.sleep(self.delay_puerta_cierre_B)
                self.H6L.off()
                print("PUERTA 2 CERRAR")
                return True
                break
            if (self.armado_mueble_switch.status_seguro()):
                self.H6L.off()
                print("SEGURO ACTIVO PAUSA CERRAR PUERTA 2")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H6L.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if (self.cronometro(tiempo) > (self.H6L_tiempo_definido + tiempo_adicional)):
                self.H6L.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta2_guardar(self):
        tiempo = time.time()
        tiempo_adicional = 0
        while True:
            if (self.armado_mueble_switch.status_1F()):
                self.H5R.on()
            if (self.armado_mueble_switch.status_1E()):
                self.H5R.off()
                print("PUERTA 2 GUARDAR")
                return True
                break
            if (self.armado_mueble_switch.status_seguro()):
                self.H5R.off()
                print("SEGURO ACTIVO PAUSA GUARDAR PUERTA 2")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H5R.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if (self.cronometro(tiempo) > (self.H5R_tiempo_definido + tiempo_adicional)):
                self.H5R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta2_desplegar(self):
        tiempo = time.time()
        tiempo_adicional = 0
        while True:
            if (self.armado_mueble_switch.status_1E()):
                self.H5L.on()
            if (self.armado_mueble_switch.status_1F()):
                self.H5L.off()
                print("PUERTA 2 DESPLEGAR")
                return True
                break
            if (self.armado_mueble_switch.status_seguro()):
                self.H5L.off()
                print("SEGURO ACTIVO PAUSA DESPLEGAR PUERTA 2")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H5L.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if (self.cronometro(tiempo) > (self.H5L_tiempo_definido + tiempo_adicional)):
                self.H5L.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def poste1_abrir(self):
        tiempo = time.time()
        tiempo_adicional = 0
        while True:
            if (self.armado_mueble_switch.status_2A()):
                self.H1L.on()
            if (self.armado_mueble_switch.status_1C()):
                time.sleep(self.delay_poste_apertura_A)
                self.H1L.off()
                print("POSTE 1 ABRIR")
                return True
                break
            if (self.armado_mueble_switch.status_seguro()):
                self.H1L.off()
                print("SEGURO ACTIVO PAUSA ABRIR POSTE 1")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H1L.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if (self.cronometro(tiempo) > (self.H1L_tiempo_definido + tiempo_adicional)):
                self.H1L.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def poste1_cerrar(self):
        tiempo = time.time()
        tiempo_adicional = 0
        while True:
            if (self.armado_mueble_switch.status_1C()):
                self.H1R.on()
            if (self.armado_mueble_switch.status_2A()):
                time.sleep(self.delay_poste_cierre_A)
                self.H1R.off()
                print("POSTE 1 CERRAR")
                return True
                break
            if (self.armado_mueble_switch.status_seguro()):
                self.H1R.off()
                print("SEGURO ACTIVO PAUSA CERRAR POSTE 1")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H1R.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if (self.cronometro(tiempo) > (self.H1R_tiempo_definido + tiempo_adicional)):
                self.H1R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def poste2_abrir(self):
        tiempo = time.time()
        tiempo_adicional = 0
        while True:
            if (self.armado_mueble_switch.status_2E()):
                self.H4L.on()
            if (self.armado_mueble_switch.status_1G()):
                time.sleep(self.delay_puerta_apertura_B)
                self.H4L.off()
                print("POSTE 2 ABRIR")
                return True
                break
            if (self.armado_mueble_switch.status_seguro()):
                self.H4L.off()
                print("SEGURO ACTIVO PAUSA ABRIR POSTE 2")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H4L.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if (self.cronometro(tiempo) > (self.H4L_tiempo_definido + tiempo_adicional)):
                self.H4L.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def poste2_cerrar(self):
        tiempo = time.time()
        tiempo_adicional = 0
        while True:
            if (self.armado_mueble_switch.status_1G()):
                self.H4R.on()
            if (self.armado_mueble_switch.status_2E()):
                time.sleep(self.delay_puerta_cierre_B)
                self.H4R.off()
                print("POSTE 2 CERRAR")
                return True
                break
            if (self.armado_mueble_switch.status_seguro()):
                self.H4R.off()
                print("SEGURO ACTIVO PAUSA CERRAR POSTE 2")
                tiempo_pausa = time.time()
                while True:
                    if self.armado_mueble_switch.status_seguro() is False:
                        time.sleep(2)
                        self.H4R.on()
                        tiempo_adicional = self.cronometro(tiempo_pausa)
                        break
            if (self.cronometro(tiempo) > (self.H4R_tiempo_definido + tiempo_adicional)):
                self.H4R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def apagar_motores(self):
        self.H1L.off()
        self.H1R.off()
        self.H2L.off()
        self.H2R.off()
        self.H3L.off()
        self.H3R.off()
        self.H4L.off()
        self.H4R.off()
        self.H5L.off()
        self.H5R.off()
        self.H6L.off()
        self.H6R.off()