from gpiozero import Button,LED,Buzzer
import switchs as SW
import time
import raspardino_response as RDNR
import memoriaTiempo as MT
import tiempoTranscurrido as TT

class Armado_mueble(object):
    #Hola Mundo
    armado_mueble_switch = SW.Switch()
    arduino = RDNR.Raspardino()
    tiempo_memoria = MT.MemoriaTiempo()
    previo_tiempo = TT.TiempoTranscurrido()
    H1L = LED(15)
    H1R = LED(18)
    H2L = LED(23)
    H2R = LED(25)
    #H3L = LED(8)
    H3R = LED(7)
    H4L = LED(12)
    H4R = LED(16)
    H5L = LED(20)
    H5R = LED(21)
    #H6L = LED(17)
    H6R = LED(4)
    delay_puerta_apertura_A = 1
    delay_puerta_cierre_A = 1
    delay_puerta_apertura_B = 1
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

    def validar_ejecucion_previa(self,data):
        if(data > 0):
            return True
        else:
            return False

    def ttt(self,data,data_prev,validation):
        if validation:
            tiempo = self.cronometro(data)
            tiempo = tiempo + data_prev
            return tiempo
        else:
            return self.cronometro(data)

    def puerta1_abrir(self,data):
        ta = 1.6
        tp = 3
        tiempo = time.time()
        inicio_tiempo = time.time()
        previo = self.validar_ejecucion_previa(self.previo_tiempo.get_transcurrido_tiempo_abrirpuerta1())
        time.sleep(1.5)
        while True:
            if(self.armado_mueble_switch.status_1D() or data is True):
                self.arduino.espruino_cmd('y').strip()
                time.sleep(1)
                while self.armado_mueble_switch.status_2D() is False :
                    self.H3R.on()
                    if self.armado_mueble_switch.status_2D() is False:
                        time.sleep(ta)
                        if ((ta - .4) > .1):
                            ta = ta - .4
                        else:
                            ta = ta + .1
                    self.H3R.off()
                    if self.armado_mueble_switch.status_2D() is False:
                        time.sleep(tp)
                        tp = tp + .2
                    self.H3R.on()
                    self.previo_tiempo.set_transcurrido_tiempo_abrirpuerta1(self.cronometro(tiempo))
            if (self.armado_mueble_switch.status_2D()):
                time.sleep(1)
                self.H3R.off()
                self.arduino.espruino_cmd('w').strip()
                tiempo_final = time.time()
                print("PUERTA 1 ABIERTA")
                #self.previo_tiempo.set_transcurrido_tiempo_abrirpuerta1(0.0)
                self.tiempo_memoria.set_tiempo_abrirpuerta1(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_abrirpuerta1())
                return True
                break
            if(self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_abrirpuerta1()):
                self.H3R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta1_cerrar(self,data):
        ta = 1.2
        tp = 1.5
        tiempo = time.time()
        inicio_tiempo = time.time()
        time.sleep(1.5)
        while True:
            if (self.armado_mueble_switch.status_2D() or data is True):
                self.arduino.espruino_cmd('w').strip()
                while self.armado_mueble_switch.status_1D() is False:
                    self.arduino.espruino_cmd('b').strip()
                    if self.armado_mueble_switch.status_1D() is False:
                        time.sleep(ta)
                    self.arduino.espruino_cmd('c').strip()
                    if((ta-.4)>.1):
                        ta = ta - .4
                    else:
                        ta = ta + .1
                    if self.armado_mueble_switch.status_1D() is False:
                        time.sleep(tp)
                        tp = tp + .2
                    self.arduino.espruino_cmd('b').strip()
            if (self.armado_mueble_switch.status_1D()):
                self.arduino.espruino_cmd('c').strip()
                tiempo_final = time.time()
                print("PUERTA 1 CERRADA")
                self.tiempo_memoria.set_tiempo_abrirpuerta1(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_cerrarpuerta1())
                return True
                break
            if (self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_cerrarpuerta1()):
                self.arduino.espruino_cmd('c').strip()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta1_guardar(self,data):
        tiempo = time.time()
        inicio_tiempo = time.time()
        time.sleep(1.5)
        while True:
            if (self.armado_mueble_switch.status_1B() or data is True):
                self.H2R.on()
            if (self.armado_mueble_switch.status_1A()):
                self.H2R.off()
                tiempo_final = time.time()
                print("PUERTA 1 GUARDAR")
                self.tiempo_memoria.set_tiempo_guardarpuerta1(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_guardarpuerta1())
                return True
                break
            if (self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_guardarpuerta1()):
                self.H2R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta1_desplegar(self,data):
        tiempo = time.time()
        inicio_tiempo = time.time()
        time.sleep(1.5)
        while True:
            if (self.armado_mueble_switch.status_1A() or data is True):
                self.H2L.on()
            if (self.armado_mueble_switch.status_1B()):
                self.H2L.off()
                tiempo_final = time.time()
                print("PUERTA 1 DESPLEGAR")
                self.tiempo_memoria.set_tiempo_desplegarpuerta1(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_desplegarpuerta1())
                return True
                break
            if (self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_desplegarpuerta1()):
                self.H2L.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta2_abrir(self,data):
        tiempo = time.time()
        ta = 3
        tp = 1.5
        inicio_tiempo = time.time()
        time.sleep(1.5)
        while True:
            if (self.armado_mueble_switch.status_1H() or data is True):
                self.arduino.espruino_cmd('z').strip()
                time.sleep(1)
                while self.armado_mueble_switch.status_2H() is False:
                    self.H6R.on()
                    if self.armado_mueble_switch.status_2H() is False:
                        time.sleep(ta)
                        if ((ta - .4) > .1):
                            ta = ta - .4
                        else:
                            ta = ta + .1
                    self.H6R.off()
                    if self.armado_mueble_switch.status_2H() is False:
                        time.sleep(tp)
                        tp = tp + .2
                    self.H6R.on()
            if(self.armado_mueble_switch.status_2H()):
                self.H6R.off()
                self.arduino.espruino_cmd('x').strip()
                tiempo_final = time.time()
                print("PUERTA 2 ABIERTA")
                self.tiempo_memoria.set_tiempo_abrirpuerta2(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_abrirpuerta2())
                return True
                break
            if (self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_abrirpuerta2() ):
                self.H6R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta2_cerrar(self,data):
        tiempo = time.time()
        inicio_tiempo = time.time()
        time.sleep(1.5)
        while True:
            if (self.armado_mueble_switch.status_2H() or data is True):
                self.arduino.espruino_cmd('x').strip()
                while self.armado_mueble_switch.status_1H() is False:
                    self.arduino.espruino_cmd('f').strip()
                    if self.armado_mueble_switch.status_1H() is False:
                        time.sleep(1.8)
                    self.arduino.espruino_cmd('g').strip()
                    if self.armado_mueble_switch.status_1H() is False:
                        time.sleep(0.8)
                    self.arduino.espruino_cmd('f').strip()
            if (self.armado_mueble_switch.status_1H()):
                time.sleep(1)
                self.arduino.espruino_cmd('g').strip()
                tiempo_final = time.time()
                print("PUERTA 2 CERRAR")
                self.tiempo_memoria.set_tiempo_cerrarpuerta2(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_cerrarpuerta2())
                return True
                break
            if (self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_cerrarpuerta2() ):
                self.arduino.espruino_cmd('g').strip()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta2_guardar(self,data):
        tiempo = time.time()
        inicio_tiempo = time.time()
        time.sleep(1.5)
        while True:
            if (self.armado_mueble_switch.status_1F() or data is True):
                self.H5R.on()
            if (self.armado_mueble_switch.status_1E()):
                self.H5R.off()
                tiempo_final = time.time()
                print("PUERTA 2 GUARDAR")
                self.tiempo_memoria.set_tiempo_guardarpuerta2(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_guardarpuerta2())
                return True
                break
            if (self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_guardarpuerta2()):
                self.H5R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def puerta2_desplegar(self,data):
        tiempo = time.time()
        inicio_tiempo = time.time()
        time.sleep(1.5)
        while True:
            if (self.armado_mueble_switch.status_1E() or data is True):
                self.H5L.on()
            if (self.armado_mueble_switch.status_1F()):
                self.H5L.off()
                tiempo_final = time.time()
                print("PUERTA 2 DESPLEGAR")
                self.tiempo_memoria.set_tiempo_desplegarpuerta2(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_desplegarpuerta2())
                return True
                break
            if (self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_desplegarpuerta2()):
                self.H5L.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def poste1_abrir(self,data):
        tiempo = time.time()
        inicio_tiempo = time.time()
        time.sleep(1.5)
        while True:
            if (self.armado_mueble_switch.status_2A() or data is True):
                self.H1L.on()
            if (self.armado_mueble_switch.status_1C()):
                time.sleep(self.delay_poste_apertura_A)
                self.H1L.off()
                tiempo_final = time.time()
                print("POSTE 1 ABRIR")
                self.tiempo_memoria.set_tiempo_abrirposte1(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_abrirposte1())
                return True
                break
            if (self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_abrirposte1() ):
                self.H1L.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def poste1_cerrar(self,data):
        tiempo = time.time()
        inicio_tiempo = time.time()
        time.sleep(1.5)
        while True:
            if (self.armado_mueble_switch.status_1C() or data is True):
                self.H1R.on()
            if (self.armado_mueble_switch.status_2A()):
                time.sleep(self.delay_poste_cierre_A)
                self.H1R.off()
                tiempo_final = time.time()
                print("POSTE 1 CERRAR")
                self.tiempo_memoria.set_tiempo_cerrarposte1(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_cerrarposte1())
                return True
                break
            if (self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_cerrarposte1() ):
                self.H1R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def poste2_abrir(self,data):
        tiempo = time.time()
        inicio_tiempo = time.time()
        time.sleep(1.5)
        while True:
            if (self.armado_mueble_switch.status_2E() or data is True):
                self.H4L.on()
            if (self.armado_mueble_switch.status_1G()):
                time.sleep(self.delay_puerta_apertura_B)
                self.H4L.off()
                tiempo_final = time.time()
                print("POSTE 2 ABRIR")
                self.tiempo_memoria.set_tiempo_abrirposte2(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_abrirposte2())
                return True
                break
            if (self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_abrirposte2() ):
                self.H4L.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def poste2_cerrar(self,data):
        tiempo = time.time()
        inicio_tiempo = time.time()
        time.sleep(1.5)
        while True:
            if (self.armado_mueble_switch.status_1G() or data is True):
                self.H4R.on()
            if (self.armado_mueble_switch.status_2E()):
                time.sleep(self.delay_puerta_cierre_B)
                self.H4R.off()
                tiempo_final = time.time()
                print("POSTE 2 CERRAR")
                self.tiempo_memoria.set_tiempo_cerrarposte2(round(tiempo_final - inicio_tiempo, 2))
                print(self.tiempo_memoria.get_tiempo_cerrarposte2())
                return True
                break
            if (self.cronometro(tiempo) > self.tiempo_memoria.get_tiempo_cerrarposte2() ):
                self.H4R.off()
                print("TIEMPO ESPERA AGOTADO")
                return False
                break

    def apagar_motores(self):
        self.H1L.off()
        self.H1R.off()
        self.H2L.off()
        self.H2R.off()
        #h3L
        self.arduino.espruino_cmd('w').strip()
        self.H3R.off()
        self.H4L.off()
        self.H4R.off()
        self.H5L.off()
        self.H5R.off()
        #h6l
        self.arduino.espruino_cmd('g').strip()
        self.H6R.off()