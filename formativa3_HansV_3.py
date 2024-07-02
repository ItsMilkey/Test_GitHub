import csv
import os
import time
def limpieza():
    cls="cls"
    os.system(cls)
    time.sleep(0.5)
# Diccionario para almacenar cargos y posteriormente añadir al .txt
sueldos_por_cargo = {
    "CEO": [],
    "Desarrollador": [],
    "Analista de datos": []
}

# Datos a registrar del trabajador, será opción 1 en el menú
def datos():
    nombre=input("Nombre y apellido del trabajador: ")
    while True:
        limpieza()
        print("Seleccione un cargo\n1. CEO\n2. Desarrollador\n3. Analista de datos\n")
        try:
            seleccion_cargo=int(input("Cargo del trabajador: "))
            if seleccion_cargo==1:
                cargo = 'CEO'
                break
            elif seleccion_cargo==2:
                cargo = 'Desarrollador'
                break
            elif seleccion_cargo == 3:
                cargo = 'Analista de datos'
                break
            else:
                limpieza()
                print("Cargo no existe, seleccione uno existente.")
        except ValueError:
            print("Seleccione usando dígitos.")
    try:
        sueldo_bruto=int(input("Sueldo bruto: "))
    except ValueError:
        print("Solo valores númericos permitidos.")
        return None
    des_salud = (sueldo_bruto * 0.93)
    des_afp = (sueldo_bruto * 0.90)
    liquido = sueldo_bruto - (des_salud+des_afp)
    return nombre, cargo, sueldo_bruto, des_salud, des_afp, liquido

def archivo_registro_csv(nombre, cargo, sueldo_bruto,des_salud,des_afp,liquido, archivo_csv= 'Planilla.csv'):
    with open(archivo_csv, 'a', newline='') as archivo:
        campos=['Nombre','Cargo','Sueldo Bruto','Desc. Salud','Desc. AFP','Sueldo Líquido']
        escritor_csv=csv.DictWriter(archivo,fieldnames=campos)
        if archivo.tell() == 0:
            escritor_csv.writeheader()
        escritor_csv.writerow({
            'Nombre': nombre,
            'Cargo': cargo,
            'Sueldo Bruto': sueldo_bruto,
            'Desc. Salud':des_salud,
            'Desc. AFP':des_afp,
            'Sueldo Líquido':liquido
        })
    sueldos_por_cargo[cargo].append(sueldo_bruto)
    guardar_sueldos_cargos()

def mostrar_contenido_csv(archivo_csv='Planilla.csv'):
    if os.path.exists(archivo_csv):
        with open(archivo_csv, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                print(fila)
    else:
        print("El archivo Planilla.csv no existe.")

def guardar_sueldos_cargos(archivo_txt='sueldos_cargos.txt'):
    with open(archivo_txt, 'w') as archivo:
        for cargo, sueldos in sueldos_por_cargo.items():
            archivo.write(f"{cargo}:\n")
            for sueldo in sueldos:
                archivo.write(f"  - {sueldo}\n")
            archivo.write("\n")

def mostrar_sueldos_cargos(archivo_txt='sueldos_cargos.txt'):
    if os.path.exists(archivo_txt):
        with open(archivo_txt, 'r') as archivo:
            contenido = archivo.read()
            print("Sueldos por cargo:")
            print(contenido)
    else:
        print("El archivo sueldos_cargos.txt no existe.")

def mostrar_sueldos_por_cargo(archivo_txt='sueldos_cargos.txt'):
    if os.path.exists(archivo_txt):
        while True:
            try:
                cargo= int(input("Ingrese el cargo para mostrar los sueldos:\n1. CEO\n2. Desarrollador\n3. Analista de datos\n4.Salir\n "))
                if cargo == 1:
                    limpieza()
                    leer_txt('CEO')
                    break
                elif cargo == 2:
                    limpieza()
                    leer_txt('Desarrollador')
                    break
                elif cargo == 3:
                    limpieza()
                    leer_txt('Analista de datos')
                    break
                elif cargo == 4:
                    break
                else:
                    limpieza()
                    print("Seleccione una de las opciones disponibles.")
            except ValueError:
                limpieza()
                print("Solo dígitos.")

def leer_txt(cargo,archivo_txt='sueldos_cargos.txt'):
    with open(archivo_txt, 'r')as f:
        lineas = f.readlines()
        for i in range(len(lineas)):
            if lineas[i].strip().startswith(cargo):
                print(f"Sueldos para el cargo {cargo}:")
                j = i+1
                while j < len(lineas) and lineas[j].strip().startswith('-'):
                    print(lineas[j].strip())
                    j += 1
                break
            else:
                print("El archivo .txt no existe.")

def principal():
    resultado = datos()
    if resultado:
        nombre, cargo, sueldo_bruto, des_salud, des_afp, liquido = resultado
        limpieza()
        print(f"Nombre del trabajador: {nombre}")
        print(f"Cargo: {cargo}")
        print(f"Sueldo Bruto: {sueldo_bruto}\nDesc. Salud: {des_salud}\nDesc. AFP: {des_afp}\nSueldo líquido: {liquido}")
        archivo_registro_csv(nombre, cargo, sueldo_bruto, des_salud, des_afp, liquido)
        limpieza()
        print(f"Se ha registrado correctamente al trabajador {nombre}")  
    
while True:
    print("1. Registrar trabajador\n2. Listar todos los trabajadores\n3. Imprimir planilla de sueldos\n4. Salir del programa")
    try:
        opc = int(input("Seleccione la opción que desee: "))
        if opc == 1:
            limpieza()
            principal()
        elif opc == 2:
            limpieza()
            mostrar_contenido_csv()
        elif opc == 3:
            try:
                limpieza()
                opc2=int(input("1. Mostrar planilla de sueldos\n2. Mostrar planilla de sueldos por cargo específico\n"))
                if opc2 == 1:
                    limpieza()
                    mostrar_sueldos_cargos()
                elif opc2 == 2:
                    limpieza()
                    mostrar_sueldos_por_cargo()
                else:
                    limpieza()
                    print("Inválido, ingrese una opción correcta.")
            except ValueError:
                print("Ingrese solo dígitos.")
        elif opc == 4:
            "Saliendo del programa"
            limpieza()
            break
        else:
            print("Me vuelvo loco")
    except ValueError:
        print("Opción inválida, ingrese una opción correcta. ")
