import xml.etree.ElementTree as ET
import ast

class TiempoTranscurrido(object):

    extra = 0.0
    permiso = True
    siempre_grabar = True

    def set_transcurrido_tiempo_abrirposte1(self,data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('abrirposte1'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_abrirposte1() < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_abrirposte1(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('abrirposte1').text))+ self.extra

    def set_transcurrido_tiempo_cerrarposte1(self,data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('cerrarposte1'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_cerrarposte1 < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_cerrarposte1(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('cerrarposte1').text))+ self.extra

    def set_transcurrido_tiempo_abrirposte2(self, data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('abrirposte2'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_abrirposte2 < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_abrirposte2(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('abrirposte2').text)) + self.extra

    def set_transcurrido_tiempo_cerrarposte2(self, data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('cerrarposte2'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_cerrarposte2 < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_cerrarposte2(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('cerrarposte2').text)) + self.extra

    def set_transcurrido_tiempo_abrirpuerta1(self, data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('abrirpuerta1'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_abrirpuerta1 < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_abrirpuerta1(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('abrirpuerta1').text)) + self.extra

    def set_transcurrido_tiempo_cerrarpuerta1(self, data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('cerrarpuerta1'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_cerrarpuerta1 < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_cerrarpuerta1(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('cerrarpuerta1').text)) + self.extra

    def set_transcurrido_tiempo_abrirpuerta2(self, data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('abrirpuerta2'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_abrirpuerta2 < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_abrirpuerta2(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('abrirpuerta2').text)) + self.extra

    def set_transcurrido_tiempo_cerrarpuerta2(self, data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('cerrarpuerta2'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_cerrarpuerta2 < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_cerrarpuerta2(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('cerrarpuerta2').text)) + self.extra

    def set_transcurrido_tiempo_guardarpuerta1(self, data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('guardarpuerta1'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_guardarpuerta1 < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_guardarpuerta1(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('guardarpuerta1').text)) + self.extra

    def set_transcurrido_tiempo_desplegarpuerta1(self, data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('desplegarpuerta1'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_desplegarpuerta1 < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_desplegarpuerta1(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('desplegarpuerta1').text)) + self.extra

    def set_transcurrido_tiempo_guardarpuerta2(self, data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('guardarpuerta2'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_guardarpuerta2 < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_guardarpuerta2(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('guardarpuerta2').text)) + self.extra

    def set_transcurrido_tiempo_desplegarpuerta2(self, data):
        if self.permiso:
            tree = ET.parse('tiempo_ejecutado.xml')
            root = tree.getroot()
            for datos in root.iter('desplegarpuerta2'):
                datos.text = str(data)
                datos.set('update', 'yes')
            if self.get_transcurrido_tiempo_desplegarpuerta2 < data or self.siempre_grabar:
                tree.write('tiempo_ejecutado.xml')

    def get_transcurrido_tiempo_desplegarpuerta2(self):
        tree = ET.parse('tiempo_ejecutado.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            return float(ast.literal_eval(child.find('desplegarpuerta2').text)) + self.extra

