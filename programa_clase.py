import csv
def obtener_fichero_calificaciones():
    lista = []
    with open(r"C:\Users\cetecom\Downloads\calificaciones.csv", "r", newline="") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";") 
        pos = 0
        for linea in lector_csv: #Recorre la lista linea por linea y la ingresa en variable linea
            if pos != 0:         #No lee la primera linea 
               for i in range(2,len(linea)): #recorre desde la posicion 2 y va llamando el [i]
                    if linea[i] == '': #Si encuentra un espacio en blanco le agrega el valor '0,0"
                        linea[i] = '0,0'

               Apellidos = linea[0]
               nombre    = linea[1]
               Asistencia = float(linea[2].replace('%','')) #reemplaza caracteres para poder pasar a numero
               Parcial1 = float(linea[3].replace(',','.'))  #Python usa punto para separar los decimales, excel usa coma, acá se reemplaza la coma para que python pueda ejecutar
               Parcial2 = float(linea[4].replace(',','.'))
               Ordinario1 = float(linea[5].replace(',','.'))
               Ordinario2 = float(linea[6].replace(',','.'))
               Practicas = float(linea[7].replace(',','.'))
               OrdinarioPracticas = float(linea[8].replace(',','.'))
               lista.append({
                   'Apellidos':Apellidos,
                   'nombre':nombre,
                   'Asistencia': Asistencia,
                   'Parcial1': Parcial1,
                   'Parcial2': Parcial2,
                   'Ordinario1': Ordinario1,
                   'Ordinario2': Ordinario2,
                   'Practicas': Practicas,
                   'OrdinarioPracticas': OrdinarioPracticas,
                })    
            else:
                pos = 1  
    print('es lista: ',lista) 
    input()     
    return lista


def añadir_nota_final(calificaciones):
        lista =[]
        for alumno in calificaciones:

            if alumno['Ordinario1']>0: #Si el alumno se ha presentado al examen de repesca del primer parcial tomamos esa nota como la nota del primer parcial
                parcial1 = alumno['Ordinario1']
            else:
                parcial1 = alumno['Parcial1']
            if alumno['Ordinario2']>0: #Si el alumno se ha presentado al examen de repesca del segundo parcial tomamos esa nota como la nota del segundo parcial
                parcial2 = alumno['Ordinario2']
            else:
                parcial2 = alumno['Parcial2']
            if alumno['OrdinarioPracticas']>0: #Si el alumno se ha presentado al examen de repesca de prácticas tomamos esa nota como la nota de prácticas
                practicas = alumno['OrdinarioPracticas']
            else:
                practicas = alumno['OrdinarioPracticas']
            alumno_Final1 = parcial1
            alumno_Final2= parcial2
            alumno_FinalPracticas = practicas
            alumno_NotaFinal = parcial1 * 0.3 + parcial2 * 0.3 + practicas * 0.4
            alumno_Apellidos =alumno['Apellidos']
            alumno_nombre =alumno['nombre']
            alumno_asistencia =alumno['Asistencia']

            lista.append({
                   'Apellidos':alumno_Apellidos,
                   'nombre':alumno_nombre,
                   'Asistencia': alumno_asistencia ,
                   'Parcial1': alumno_Final1,
                   'Parcial2': alumno_Final2,
                   'Practicas': alumno_FinalPracticas,
                   'NotaFinal': alumno_NotaFinal
                })    
        
            return alumno



calificacion = obtener_fichero_calificaciones()
calificacion2=añadir_nota_final(calificacion)
print(calificacion2)