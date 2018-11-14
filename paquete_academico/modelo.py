#Clase padre 
class Persona(object):
	def __init__(self):

		self.nombre = ""
		self.apellido = ""
		self.pais = Pais()
	pass

	def agregarNombre(self, m):
		self.nombre = m

	def obtenerNombre(self):
		return self.nombre

	def agregarApellido(self, m):
		self.apellido = m

	def obtenerApellido(self):
		return self.apellido

	def agregarPais(self, m):
		self.pais = m

	def obtenerPais(self):
		return self.pais

	
#Mi clase estudiante que hereda de la clase padre como lo es persona 
class Estudiante(Persona):
	def __init__(self):
		super(Estudiante, self).__init__()
		self.codigo = ""

	def agregarCodigo(self, c):
		self.codigo = c

	def obtenerCodigo(self):
		return self.codigo
#Con está función concateno taributs que necesito para mi reporte
	def presentarInformacion(self):
		cadena = "Informacion\nNombre Completo: %s-%s\nProcedencia: Pais: %s\nCapital: %s\n" % (self.obtenerNombre(), self.obtenerApellido(), self.pais.obtenerPais(), self.pais.obtenerCapital())
		return cadena

	pass

class EstudiantePresencial(Estudiante):
	def __init__(self):
		super(EstudiantePresencial, self).__init__()
		self.num_creditos = 0
		self.ciclo = ""

	def agregarNumCreditos(self, num_c):
		self.num_creditos = num_c

	def obtenerNumCreditos(self):
		return self.num_creditos

	def agregarCiclo(self, c):
		self.ciclo = c

	def obtenerCiclo(self):
		return self.ciclo

#Esta clase hereda los atributos de Estudiante que es su clase padre
class EstudianteDistancia(Estudiante): 
	def __init__(self):
		super(EstudianteDistancia, self).__init__()
		self.numMaterias = 0
		self.modulo = ""

	def agregarNumMaterias(self, m):
		self.numMaterias = m

	def obtenerNumMaterias(self):
		return self.numMaterias

	def agregarModulo(self, m):
		self.modulo = m

	def obtenerModulo(self):
		return self.modulo
#Retorno la cadena ya con los atributos que nesecito implementar en mi reporte
	def presentarInformacion(self):
		cadena ="%sCodigo: %s\nMódulo: %s\nNumero de materias: %d\n" % (super(EstudianteDistancia, self).presentarInformacion(), self.obtenerCodigo(), self.obtenerModulo(), self.obtenerNumMaterias())
		return cadena

	pass
#Creó la clase donde Pais donde guardo el nombre del pais y su capital
class Pais(object):

	def __init__(self):
		self.pais = ""
		self.capital = ""

	def agregarPais(self, m):
		self.pais = m

	def obtenerPais(self):
		return self.pais

	def agregarCapital(self, m):
		self.capital = m

	def obtenerCapital(self):
		return self.capital
	pass			
		