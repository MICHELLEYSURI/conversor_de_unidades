"""1) Módulo temperatura.py: Este módulo debe contener funciones para convertir entre diferentes unidades de temperatura, como Celsius, Fahrenheit y Kelvin.(0.5 puntos) """
"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
"""3) Crear el primer versionamiento con git de los dos módulos creados de temperatura y masa (usar git add y git commit ). (0.5 puntos) """
"""4) Crear una nueva rama llamada “desarrollo” y en esta nueva rama agregar los módulos tiempo.py y convertidor.py (recuerda usar git branch ). (0.5 puntos) """
"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
"""6) Módulo convertidor.py: Este módulo importa los módulos de masa, temperatura y tiempo. Actúa como el punto de entrada del programa. Debe permitir a los usuarios seleccionar la categoría de conversión deseada (temperatura, masa o tiempo), ingresar el valor a convertir y las unidades de origen y destino, y obtener el resultado de la conversión.(2 puntos) """
"""7) Versionar esta rama “desarrollo” con git add y git commit para luego fusionar con la rama master (para fusionar, usar: git merge). (1 punto) """
""" Desde la rama main o master subir al nuevo repositorio de github llamado conversor_de_unidades. (1 punto) """

""" Recuerda que cada uno de los módulos, deben incluir el bloque if __name__ == "__main__" para sus pruebas en cada módulo. """

import temperatura
import masa
import tiempo
def main():
    while True:
        # Muestra el menú principal
        print("Menú Principal:")
        print("[1] Convertir de Celsius a Fahrenheit")
        print("[2] Convertir de Celsius a kelvin")
        print("[3] Convertir de Fahrenheit a Celsius")
        print("[4] Convertir de fahrenheit a kelvin")
        print("[5] Convertir de Kelvin a Celsius")
        print("[6] Convertir de Kelvin a fahrenheit")
        print("[7] Convertir de Kilogramos a Gramos")
        print("[8] Convertir de Kilogramos a Toneladas")
        print("[9] Convertir de Gramos a Kilogramos")
        print("[10] Convertir de Gramos a Toneladas")
        print("[11] Convertir de toneladas a kilogramos")
        print("[12] Convertir de Toneladas a gramos")
        print("[13] Convertir de Segundos a Minutos")
        print("[14] Convertir de Segundos a Horas")
        print("[15] Convertir de Minutos a Segundos")
        print("[16] Convertir de Minutos a Horas")
        print("[17] Convertir de Horas a Segundos")
        print("[18] Convertir de Horas a Minutos")
        
    
    
        
        print("[0] Salir")
        
         # Solicita al usuario que ingrese una opción
        valorInicial=int(input("ingrese valor inicial"))
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                resultado = temperatura.celsius_a_fahrenheit(valorInicial)
                print("el resultado es:", resultado)
            elif opcion == 2:
                resultado = temperatura.celsius_a_kelvin(valorInicial)
                print("el resultado es:", resultado)

            elif opcion == 3:
                resultado = temperatura.fahrenheit_a_celsius(valorInicial)
                print("el resultado es:", resultado)
                
            elif opcion == 4:
                resultado = temperatura.fahrenheit_a_kelvin(valorInicial)
                print("el resultado es:", resultado)
                
            elif opcion == 5:
                resultado = temperatura.kelvin_a_celsius(valorInicial)
                print("el resultado es:", resultado)
                
            elif opcion == 6:
                resultado = temperatura.kelvin_a_fahrenheit(valorInicial)
                print("el resultado es:", resultado)
               
            elif opcion == 7:
                resultado = masa.Kilogramos_a_Gramos(valorInicial)
                print("el resultado es:", resultado)

            elif opcion == 8:
                resultado = masa.Kilogramos_a_Toneladas(valorInicial)
                print("el resultado es:", resultado)

            elif opcion == 9:
                resultado = masa.Gramos_a_Kilogramos(valorInicial)
                print("el resultado es:", resultado)

            elif opcion == 10:
                resultado = masa.Gramos_a_Toneladas(valorInicial)
                print("el resultado es:", resultado)

            elif opcion == 11:
                resultado = masa.Toneladas_a_Kilogramos(valorInicial)
                print("el resultado es:", resultado)
                
            elif opcion == 12:
                resultado = masa.Toneladas_a_Gramos(valorInicial)
                print("el resultado es:", resultado)

            elif opcion == 13:
                resultado = tiempo.Segundos_a_Minutos(valorInicial)
                print("el resultado es:", resultado)
            
            elif opcion == 14:
                resultado = tiempo.Segundos_a_Horas(valorInicial)
                print("el resultado es:", resultado)
            
            elif opcion == 15:
                resultado = tiempo.Minutos_a_Segundos(valorInicial)
                print("el resultado es:", resultado)
            
            elif opcion == 16:
                resultado = tiempo.Minutos_a_Horas(valorInicial)
                print("el resultado es:", resultado)
            
            elif opcion == 17:
                resultado = tiempo.Horas_a_Segundos(valorInicial)
                print("el resultado es:", resultado)
            
            elif opcion == 18:
                resultado = tiempo.Horas_a_Minutos(valorInicial)
                print("el resultado es:", resultado)

            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

if __name__ == "__main__":
    main()

    #https://github.com/MICHELLEYSURI/conversor_de_unidades.git