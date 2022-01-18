class Estudiante:
    programa = "Web development 3-full-stack"
    listaEstudiantes = []
    # Constructor  
    def __init__( self, nombre = "N/A", apellido = "N/A", id = -1):
        # Atributos
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.calificaciones = []
        
        Estudiante.listaEstudiantes.append( self )
    
    def imprimeInformacion( self ):
        print( self.nombre + " " + self.apellido + " " + str( self.id ) )
        return self

    def setNombre( self, nuevoNombre ):
        self.nombre = nuevoNombre
        return self
    
    def setApellido( self, nuevoApellido ):
        self.apellido = nuevoApellido

    def setId( self, nuevoId ):
        self.id = nuevoId

    def getNombre( self ):
        return self.nombre
    
    def getApellido( self ):
        return self.apellido
    
    def getId( self ):
        return self.id
    
    def imprimeDos( self ):
        self.imprimeInformacion()
        print( "Mas datos aquí" )

    def promedio( self ):
        suma = 0
        for x in self.calificaciones:
            suma += x
        calificacionFinal = suma / len( self.calificaciones )
        return calificacionFinal

    @classmethod
    def imprimeEstudiantes( cls ):
        for estudiante in cls.listaEstudiantes:
            estudiante.imprimeInformacion()

    @staticmethod
    def imrpimeID( identificador ):
        print( identificador )

    def imprimeInformacionDeAmbosEstudiantes( self, estudiante2 ):
        self.imprimeInformacion()
        estudiante2.imprimeInformacion()