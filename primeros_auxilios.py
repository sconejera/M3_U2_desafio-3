# inicio de bucle infinito
while True: 
    responde_estimulos = input("¿Responde a estímulos? (s/n): ")
    if responde_estimulos == 's':
        print("Valorar la necesidad de llevar al hospital más cercano")
        print("Fin")
        
    else:
        print("Abrir la vía aérea")
        respira = input("¿Respira? (s/n): ")
        if respira == 's':
            print("Permitirle posición de suficiente ventilación")
            print("Fin")            
        else:
            print("Administrar 5 Ventilaciones y llamar a Ambulancia")
            signos_de_vida = input("¿Signos de Vida? (s/n): ")
            
            #inicio bucle signos de vida
            while signos_de_vida == 'n':
                print("Administrar Compresiones Torácicas hasta que llegue ambulancia")
                llego_ambulancia = input("¿Llegó la Ambulancia? (s/n): ")
                if llego_ambulancia == 's':
                    print("Fin")
                    break                  
                else:
                    signos_de_vida = input("¿Signos de Vida? (s/n): ")
            if signos_de_vida == 's':
                print("Reevaluar a la espera de la Ambulancia")
                llego_ambulancia = input("¿Llegó la Ambulancia? (s/n): ")
                if llego_ambulancia == 's':
                    print("Fin")
    
    # termino de bucle infinito
    break
