from Estudiante import Estudiante

alex = Estudiante()
alex.imprimeInformacion()

alex.setNombre( "Alejandro" )
alex.setApellido( "Martinez" )
alex.setId( 12345 )

alex.imprimeInformacion()

nombreAlex = alex.getNombre()

print( nombreAlex )

maria = Estudiante( "Maria", "Gomez" )
maria.imprimeInformacion()

alex.imprimeDos()

