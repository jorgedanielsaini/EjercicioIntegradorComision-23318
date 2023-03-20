# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
from abc import ABC, abstractclassmethod

class Persona():
    def __init__(self, nombre, edad, dni):
        try:
            if type(nombre) == str and  nombre.isalpha():
                self.__nombre = nombre
            else:
                raise ValueError("Error: el atributo 'nombre' solo puede ser un string del tipo alpha")
            
            if type(edad) == int and edad > 0:
                self.__edad = edad
            elif type(edad) == int and edad < 0:
                raise ValueError("Error: el atributo 'edad' no puede ser negativo")
            elif type(edad) == float or type(edad)== str:
                raise ValueError("Error: el atributo 'edad' solo puede ser un número entero")
            
            if type(dni) == int and dni > 0 and len(str(dni)) > 6 and len(str(dni)) < 9:
                self.__dni = dni
            else:
                raise ValueError("Error: DNI no valido. Ingrese solo números sin puntos (Ejemplo: 32255685)")            
        except ValueError as e:
            print(e)                       

    #GETTERS
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def dni(self):
        return self.__dni

    #SETTERS
    @nombre.setter
    def nombre(self,nombre):
        if nombre.isalpha():
            self.__nombre = nombre
        else:
            print("El parametro 'nombre' no puede contener números")

    #METODOS
    def mostrar(self):
        print(f"Nombre: {self.__nombre}\nEdad:{self.__edad}\nDNI: {self.__dni}")

    def es_mayor_de_edad(self):
        if self.__edad >= 18: 
            return True
        else:
            return False


#7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos

class Cuenta(Persona):
    def __init__(self, nombre, edad, dni, cantidad=0):
        super().__init__(nombre, edad, dni) 
        try:
            if type(cantidad) in (float, int):
                self.__cantidad = cantidad
            else:
                raise ValueError("El atributo 'cantidad' debe ser un número")
        except ValueError as e:
            print(e)

    #GETTERS
    @property
    def titular(self):
        return super().mostrar()
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    #SETTERS #No funciona
    #@titular.setter
    #def titular(self, nombre, edad, dni):
    #    super().__init__(nombre, edad, dni)
    
    #METODOS
    def mostrar(self):
        print(f"{super().mostrar()} \nCantidad: {self.__cantidad}")

    def ingresarCantidad(self, numero):
        try:
            if type(numero) in (int, float): 
                if(numero > 0):    
                    self.__cantidad += numero
            else:
                raise ValueError("ERROR: Metodo '.ingresarCantidad()' debe recibir un número como parametro")
        except ValueError as e:
            print(e)

    def retirarCantidad(self, numero):
        try:
            if type(numero) in (int, float): 
                if(numero > 0):    
                    self.__cantidad -= numero
            else:
                raise ValueError("ERROR: Metodo '.retirarCantidad()' debe recibir un número como parametro")
        except ValueError as e:
            print(e)

cuenta1 = Cuenta("daniel",22,32255575)
cuenta1.mostrar()
cuenta1.ingresarCantidad(3)
cuenta1.mostrar()
#cuenta1.ingresarCantidad(-13)
#cuenta1.mostrar()
#uenta1.retirarCantidad(10)
#cuenta1.mostrar()

#8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase: 
#  Un constructor. 
#  Los setters y getters para el nuevo atributo. 
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class Cuenta_joven(Cuenta):
    def __init__(self, nombre, edad, dni, bonificacion, cantidad=0):
        super().__init__(nombre, edad, dni, cantidad)
        self.__bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        pass

    def retirarCantidad(self, numero):
        return super().retirarCantidad(numero)
    
    def mostrar(self):
        return f"Cuenta Joven. Bonificación: {self.__bonificacion}"