from paquete_academico.modelo import *
#Creo el objeto pais,para gregar  el nombre del pais y la capital del pais
p = Pais()
p.agregarPais("Ecuador")
p.agregarCapital("Quito")
#Creo el objeto Est1 donde agrego cada uno de los atributos que necesito
est1 = EstudianteDistancia()
est1.agregarNombre("Jose")
est1.agregarApellido("Diaz")
est1.agregarCodigo("11012")
est1.agregarNumMaterias(5)
est1.agregarModulo("Noveno")
est1.agregarPais(p)
#Presento en pantalla
print(est1.presentarInformacion())