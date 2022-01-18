from Estudiante import Estudiante

alex = Estudiante()
#alex.imprimeInformacion()

alex.setNombre( "Alejandro" )
alex.setApellido( "Martinez" )
alex.setId( 12345 )

#alex.imprimeInformacion()

nombreAlex = alex.getNombre()

#print( nombreAlex )

maria = Estudiante( "Maria", "Gomez" )
#maria.imprimeInformacion()

Estudiante.programa = "Python"
#print( "Alex", alex.programa )
#print( "Maria", maria.programa )


#Estudiante.imprimeEstudiantes()

#alex.imprimeEstudiantes()

#alex.imrpimeID( 12345 )

#alex.imprimeInformacionDeAmbosEstudiantes( maria )

#maria.imprimeInformacionDeAmbosEstudiantes( alex )


alex.imprimeInformacion().setNombre( "Alex" ).imprimeInformacion()