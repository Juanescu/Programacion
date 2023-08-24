
fecha = input("Ingrese la fecha actual en formato 'día, DD/MM:'")
dia_semana, fecha = fecha.split(', ')
dia, mes = fecha.split('/')

if not (1 <= int(dia) <= 31 and 1 <= int(mes) <= 12):
    raise ValueError("Fecha inválida")

dia_semana = dia_semana.lower()
niveles_con_examenes = ['lunes', 'martes', 'miércoles']

if dia_semana in niveles_con_examenes:
    alumnos_aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
    alumnos_totales = int(input("Ingrese la cantidad total de alumnos: "))
    porcentaje_aprobados = (alumnos_aprobados / alumnos_totales) * 100
    print(f"Porcentaje de aprobados: {porcentaje_aprobados:.2f}%")

elif dia_semana == 'jueves':
    asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
    if asistencia > 50:
        print("Asistió la mayoría")
    else:
        print("No asistió la mayoría")

elif dia_semana == 'viernes' and (mes == '1' or mes == '7') and dia == '1':
    print("Comienzo de nuevo ciclo")
    alumnos_nuevo_ciclo = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
    arancel_por_alumno = float(input("Ingrese el arancel en $ por cada alumno: "))
    ingreso_total = alumnos_nuevo_ciclo * arancel_por_alumno
    print(f"Ingreso total en $: {ingreso_total:.2f}")

else:
    print("No se requiere acción adicional para este día.")
