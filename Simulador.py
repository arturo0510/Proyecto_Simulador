import random
import os

opcion = 0
salir = 7
capital = 10000000.00
pproduccion = 10
acciones = 100
inver_pu = 0



global Area1,Area2,Area3,Area4,Area5,Area6,Area7,gastos
Area1 = list()
Area2 = list()
Area3 = list()
Area4 = list()
Area5 = list()
Area6 = list()
Area7 = list()
gastos = list()

class Empleado:
    nombre = ("")
    cargo = ("")
    sueldo = 0

print("\n\t\t\t\t\t\t\t\t\t\t\tBienvenido al simulador empresarial GTZ")
print("\n\t\t\t\t\t\t\t\tPodrás realizar multiples acciones para hacer crecer tu empresa")
print("\n\t\t\t\t\t\t\t\t\t\t\t\tDisfruta, aprende y diviertete")

while opcion != salir:
    # mostrar menu
    print("Balance General. ")
    capital = capital + ((pproduccion * capital) / 200)
    print("Capital mas produccion: ", capital)
    indice = len(gastos)
    i=0
    for i in range(indice):
        capital = capital - gastos[i]

    print("Capital menos gastos: ", capital)



    print("\n\t\t\t\t\t\t\t\t\t\t\t***MENU***")
    print("\t\t\t\t\t\t\t\t1. Venta de inmuebles")
    print("\t\t\t\t\t\t\t\t2. Inversiones propuestas")
    print("\t\t\t\t\t\t\t\t3. Inversion en publicidad")
    print("\t\t\t\t\t\t\t\t4. Contratatacion de empleados")
    print("\t\t\t\t\t\t\t\t5. Ver plantilla de empleados")
    print("\t\t\t\t\t\t\t\t7. Salir")

    opcion = int(input("\n\t\t\t\t\t\tDigite opcion"))

    os.system("cls")


    if opcion == 1: #opcion de menu 
        desci = []
        while desci != 2:

            print("\n\t\t\t\t\t\t\t\t\tVenta de inmuebles")
            zona = ["Norte", "Sur", "Oriente", "Centro"]
            precio = [1000000, 2000000, 1500000, 3000000]
            transito = ["Bajo", "Medio", "Medio", "Alto"]
            gastos_mensuales = [100000, 150000, 200000, 300000]
            produccion = [2, 4, 3, 6]


            print("\n\t\t\t\t\t\tCompra de inmuebles para ampliar la empresa")
            print("\n\t\t\tA continuacion se presentan los inmuebles disponibles:\n")

            for i in [1, 2, 3, 4]:
                print("\t\tInmueble ", i)
                print("\t\tLa ubicacion del inmueble es en la zona : ", zona[i - 1])
                print("\t\tPrecio del inmueble:", precio[i - 1])
                print("\t\tEl transito de personas por la zona es: ", transito[i - 1])
                print("\t\tLos gastos mensuales del inmueble seran de: ", gastos_mensuales[i - 1])
                print("\t\tEl aumento de produccion con la compra del nuevo inmueble es del: ", produccion[i - 1],
                      "porciento\n\n")

            op = int(input("Desea comprar un nuevo inmueble?  1) Si  2)  No"))

            if op == 1:
                op = int(input("Ingrese el numero de inmueble que desea comprar"))
                os.system("cls")
                if op > 0 and op <= 4:
                    if capital > 100000:
                        print("\n\t\t\t**Balance de compra**")
                        print("\t\t\nEl capital actual es: ",capital)
                        print("\t\t\nEl capital que se descontara de los activos es: ", precio[op - 1])
                        print("\t\t\nLos gastos mensuales seran de: ", gastos_mensuales[op - 1])
                        añadir = gastos_mensuales[i - 1]
                        gastos.append(añadir)
                        print("\t\t\nEl aumento de produccion con la compra del nuevo inmueble es del :", produccion[op - 1],"porciento")
                        capital = capital - precio[op - 1] - gastos_mensuales[op - 1]
                        pproduccion = pproduccion + produccion[op - 1]
                        print("\nEl capital final de la compra del inmueble menos los gastos del primer mes es de: ",capital)

                        print("\t\t\nEl porcentaje de produccion aumento a : ", pproduccion, "porciento")
                    else:
                        print("No cuentas con dinero suficiente.")
                else:
                    print("opcion incorrecta")
                    
            
            desci = int(input("¿Desea comprar otro inmueble? Presione 1, si desea salir presione 2"))

            os.system("cls")
        
        
    elif opcion == 2: #opcion de menu
        descic = []
        os.system("cls")
        while descic != 2:
            os.system("cls")
            print("\n\t\t\t\t\t\tInversion propuesta")

            print("\n\tEn esta seccion recibiras propuestas de diversos socios interesados en comprar acciones de tu empresa\n")
            deci = int(input("\n\tDesea generar una propuesta de inversion?: 1) SI 2) NO"))

            if deci == 1:
                print("\nLa propuesta es la siguiente: \n")
                random_dinero = (random.randint(1, 50))
                random_porcentaje = (random.randint(1, 20))
                print(f"\n\tEste socio desea invertir el {random_dinero} porciento del capital que tienes")
                print(f"Por el {random_porcentaje} porciento de tu empresa\n");
                decis = int(input("\n\tTe interesa esta propuesta? 1) SI 2) NO "))

                if decis == 1:
                    dinero_ganado = (random_dinero * capital) / 100
                    print("\n\t\t\t*** Balance de inversion ***")
                    print("\n\tEl capital actual es: ",capital)
                    print(f"\n\tEl capital que gano al realizar la inversion es: {dinero_ganado} ")
                    print(f"\n\tEl porcentaje de acciones de tu socio son de {random_porcentaje}")
                    acciones_dueno = acciones - random_porcentaje
                    print(f"\n\tEl porcentaje de tus acciones es de : {acciones_dueno}")
                    capital = capital + dinero_ganado
                    print("\n\tEl capital final es: ", capital)


            descic = int(input("¿Desea generar otra propuesta? Presione 1 si desea salir presione 2"""))

            os.system("cls")

        

    elif opcion == 3: #opcion de menu
        descici = []
        os.system("cls")
        while descici != 2:
            print("\n\t\t\t\t\t\tInversion en publicidad")
            print("\n\tEn esta seccion se puede invertir en publicidad")
            print("\n\tUsted decide la cantidad de dinero que desea invertir")
            print("\n\tCon el dinero que propone se hara una cotizacion con la cual puede aceptar o no")
            inver_pu = float(input("\n\tIngrese la cantidad de dinero que desea invertir en publicidad"))

            aumento_produccion = (inver_pu * 1) / 50000
            print(f"\n\t\t\tEl aumento de produccion sera de: {aumento_produccion} porciento")
            print("\n\t\t\tEl capital actual es: ",capital)

            descici = int(input("\n\tLe interesa invertir esa cantidad presione 1, si desea salir presione 2, si desea modificarla presione 3"))
            if descici == 1:
                os.system("cls")
                if capital > inver_pu:
                    capital = capital - inver_pu
                    pproduccion = pproduccion + aumento_produccion
                    print(f"\n\t\tEl capital final es de: {capital}")
                    print(f"\n\t\tEl porcentaje de produccion final es de : {pproduccion} porciento")
                    añadir = inver_pu
                    gastos.append(añadir)





        
    elif opcion == 4: #opcion de menu
        descicio = []
        sueldoa = 0
        os.system("cls")
        while descicio != 2:

            print("\n\t\t\t\t\t\tContratacion de empleados")
            print("\n\tEn esta seccion se podran contratar empleados para aumentar la produccion de la empresa")

            print("\n\tA continuacion se muestran las areas funcionales en las cuales se puede contratar empleados")
            print("1. Direccion   general")
            print("2. Auxiliar   administrativo")
            print("3. Administracion  y  recursos  humanos")
            print("4. Finanzas  y  contabilidad")
            print("5. Publiadad  y  mercadotecnia")
            print("6. Informatica")
            print("7. Produccion")
            opci = int(input("\n\tIngrese el numero del area en la que desea contratar personal"))
            if opci == 1:
                a = Empleado()
                a.nombre = input("\n\tIngrese nombre de empleado")
                a.cargo = input("\n\tIngrese el cargo que desempeñara")
                a.sueldo = int(input("\n\tIngrese sueldo del empleado"))
                sueldoa = a.sueldo
                capital = capital - sueldoa
                print("\n\tEl capital que se descontara es: ",sueldoa)
                print("\n\tCapital final: ",capital)
                añadir = sueldoa
                gastos.append(añadir)


                Area1.append(a)


            elif opci == 2:
                b = Empleado()
                b.nombre = input("\n\tIngrese nombre de empleado")
                b.cargo = input("\n\tIngrese el cargo que desempeñara")
                b.sueldo = int(input("\n\tIngrese sueldo del empleado"))

                sueldoa = b.sueldo
                capital = capital - sueldoa
                print("\n\tEl capital que se descontara es: ", sueldoa)
                print("\n\tCapital final: ", capital)
                añadir = sueldoa
                gastos.append(añadir)

                Area2.append(b)

            elif opci == 3:
                c = Empleado()
                c.nombre = input("\n\tIngrese nombre de empleado")
                c.cargo = input("\n\tIngrese el cargo que desempeñara")
                c.sueldo = int(input("\n\tIngrese sueldo del empleado"))

                sueldoa = c.sueldo
                capital = capital - sueldoa
                print("El capital que se descontara es: ", sueldoa)
                print("Capital final: ", capital)
                añadir = sueldoa
                gastos.append(añadir)

                Area3.append(c)

            elif opci == 4:
                d = Empleado()
                d.nombre = input("\n\tIngrese nombre de empleado")
                d.cargo = input("\n\tIngrese el cargo que desempeñara")
                d.sueldo = int(input("\n\tIngrese sueldo del empleado"))

                sueldoa = d.sueldo
                capital = capital - sueldoa
                print("\n\tEl capital que se descontara es: ", sueldoa)
                print("\n\tCapital final: ", capital)
                añadir = sueldoa
                gastos.append(añadir)

                Area4.append(d)

            elif opci == 5:
                e = Empleado()
                e.nombre = input("\n\tIngrese nombre de empleado")
                e.cargo = input("\n\tIngrese el cargo que desempeñara")
                e.sueldo = int(input("\n\tIngrese sueldo del empleado"))

                sueldoa = e.sueldo
                capital = capital - sueldoa
                print("\n\tEl capital que se descontara es: ", sueldoa)
                print("\n\tCapital final: ", capital)
                añadir = sueldoa
                gastos.append(añadir)

                Area5.append(e)

            elif opci == 6:
                f = Empleado()
                f.nombre = input("\n\tIngrese nombre de empleado")
                f.cargo = input("\n\tIngrese el cargo que desempeñara")
                f.sueldo = int(input("\n\tIngrese sueldo del empleado"))

                sueldoa = f.sueldo
                capital = capital - sueldoa
                print("\n\tEl capital que se descontara es: ", sueldoa)
                print("\n\tCapital final: ", capital)
                añadir = sueldoa
                gastos.append(añadir)

                Area6.append(f)

            elif opci == 7:
                g = Empleado()
                g.nombre = input("\n\tIngrese nombre de empleado")
                g.cargo = input("\n\tIngrese el cargo que desempeñara")
                g.sueldo = int(input("\n\tIngrese sueldo del empleado"))

                sueldoa = g.sueldo
                capital = capital - sueldoa
                print("\n\tEl capital que se descontara es: ", sueldoa)
                print("\n\tCapital final: ", capital)
                añadir = sueldoa
                gastos.append(añadir)

                Area7.append(g)

            else:
                print("Numero invalido")




            descicio = int(input("¿Desea contratar mas personal, presione 1, si desea salir presione 2"))
            os.system("cls")
        
       
    elif opcion == 5: #opcion de menu
        descicion = []
        os.system("cls")
        while descicion != 2:

            print("\n\t\ttEn esta seccion podra ver la plantilla de empleados que laboran en su empresa")
            print("\n\t1. Ver plantilla de empleados por area")
            print("\n\t2. Salir")
            descicion = int(input("Que opcion desea, presione el numero"))

            if descicion == 1:

                print("\n\tA continuacion se muestran las areas con empleados")
                print("\n\t1. Direccion   general")
                if len(Area1) == 0:
                    print("Sin empleados")
                else:
                    for a in Area1:
                        print("Nombre", a.nombre)
                        print("Cargo: ", a.cargo)
                        print("Sueldo\n", a.sueldo)

                print("\n\t2. Auxiliar   administrativo")
                if len(Area2) == 0:
                    print("Sin empleados")
                else:
                    for b in Area2:
                        print("Nombre", b.nombre)
                        print("Cargo: ", b.cargo)
                        print("Sueldo\n", b.sueldo)

                print("\n\t3. Administracion  y  recursos  humanos")
                if len(Area3) == 0:
                    print("Sin empleados")
                else:
                    for c in Area3:
                        print("Nombre", c.nombre)
                        print("Cargo: ", c.cargo)
                        print("Sueldo\n", c.sueldo)

                print("\n\t4. Finanzas  y  contabilidad")
                if len(Area4) == 0:
                    print("Sin empleados")
                else:
                    for d in Area4:
                        print("Nombre", d.nombre)
                        print("Cargo: ", d.cargo)
                        print("Sueldo\n", d.sueldo)

                print("\n\t5. Publiadad  y  mercadotecnia")
                if len(Area5) == 0:
                    print("Sin empleados")
                else:
                    for e in Area5:
                        print("Nombre", e.nombre)
                        print("Cargo: ", e.cargo)
                        print("Sueldo\n", e.sueldo)

                print("\n\t6. Informatica")
                if len(Area6) == 0:
                    print("Sin empleados")
                else:
                    for f in Area6:
                        print("Nombre", f.nombre)
                        print("Cargo: ", f.cargo)
                        print("Sueldo\n", f.sueldo)

                print("\n\t7. Produccion")
                if len(Area7) == 0:
                    print("Sin empleados")
                else:
                    for g in Area7:
                        print("Nombre", g.nombre)
                        print("Cargo: ", g.cargo)
                        print("Sueldo\n", g.sueldo)


            descicion = int(input("¿Desea volver? presione 1, si desea salir presione 2"))

            os.system("cls")
        


        
    elif opcion == 7: #opcion de menu 
        exit()
        

































































