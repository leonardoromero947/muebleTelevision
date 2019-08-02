import xml.etree.ElementTree as ET
import ast

class Extra(object):

    instructivo = False
    ejemplo = False
    log = False
    visor = False
    cerrado = False
    abierto= False
    pruebas = False
    proceso = 0
    seguro = False

    def leer_documento(self):
        documento = open('propiedades.txt')
        propiedades = documento.readlines()
        documento.close()
        print(type(propiedades[0]))
        print(len(propiedades))
        print(propiedades[0])

    def sobreescribir_documento(self):
        pass

    def leer_xml(self):
        tree = ET.parse('propiedades.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            self.instructivo = child.find('instructivo').text
            self.ejemplo = ast.literal_eval(child.find('ejemplo').text)
            self.log = ast.literal_eval(child.find('log').text)
            self.proceso = int(child.find('proceso').text)
            self.cerrado = ast.literal_eval(child.find('cerrado').text)
            self.pruebas = ast.literal_eval(child.find('pruebas').text)
            self.abierto = ast.literal_eval(child.find('abierto').text)
            self.seguro = ast.literal_eval(child.find('abierto').text)

    def leer_proceso_xml(self):
        tree = ET.parse('propiedades.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            self.proceso = child.find('proceso').text
            self.cerrado = ast.literal_eval(child.find('cerrado').text)
            self.abierto = ast.literal_eval(child.find('abierto').text)

    def verificar_variables(self):
        print (":::instructivo:::")
        print (self.instructivo)
        print (":::ejemplo:::")
        print (self.ejemplo)
        print (":::log:::")
        print (self.log)
        print (":::cerrado:::")
        print (self.cerrado)
        print (":::abierto:::")
        print (self.abierto)
        print (":::pruebas:::")
        print (self.pruebas)
        print (":::proceso:::")
        print (self.proceso)


    def insertar_proceso_xml(self,numero_proceso):
        tree = ET.parse('propiedades.xml')
        root = tree.getroot()
        for proceso in root.iter('proceso'):
            new_proceso = int(numero_proceso)
            proceso.text = str(new_proceso)
            proceso.set('update','yes')
        tree.write('propiedades.xml')

    def insertar_estados_finales_xml(self, numero):
        if numero == 1:
            self.insert_abierto(True)
            self.insert_cerrado(False)
        if numero == 2:
            self.insert_abierto(False)
            self.insert_cerrado(True)
        if numero == 3:
            self.insert_abierto(False)
            self.insert_cerrado(False)

    def insert_abierto(self, estado):
        tree = ET.parse('propiedades.xml')
        root = tree.getroot()
        for abierto in root.iter('abierto'):
            new_abierto = estado
            abierto.text = str(new_abierto)
            abierto.set('update', 'yes')
        tree.write('propiedades.xml')

    def insert_cerrado(self,estado):
        tree = ET.parse('propiedades.xml')
        root = tree.getroot()
        for cerrado in root.iter('cerrado'):
            new_cerrado = estado
            cerrado.text = str(new_cerrado)
            cerrado.set('update', 'yes')
        tree.write('propiedades.xml')

    def seguro(self):
        estado = self.devolver_status_seguro()
        tree = ET.parse('propiedades.xml')
        root = tree.getroot()
        if estado is True:
            print("SEGURO DESACTIVADO")
            new_cerrado = 'False'
        else:
            print("SEGURO ACTIVADO")
            new_cerrado = 'True'
        for cerrado in root.iter('seguro'):
            cerrado.text = str(new_cerrado)
            cerrado.set('update', 'yes')
        tree.write('propiedades.xml')

    def devolver_status_seguro(self):
        tree = ET.parse('propiedades.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return ast.literal_eval(child.find('seguro').text)