#DOCUMENTO INICIAL DE FUNCIONAMIENTO
import ejecutor as EJT
import motores as MTS
import raspardino_response as RDNR
import armado_mueble as ARM


class Main(object):
    sonido = MTS.Motores()
    switch = EJT.Ejecutor()
    arduino = RDNR.Raspardino()
    armado = ARM.Armado_mueble()


m = Main()
m.sonido.sonido_inicial()
m.switch.iniciar()
#m.armado.poste1_cerrar(True)
#m.armado.puerta1_abrir(True)