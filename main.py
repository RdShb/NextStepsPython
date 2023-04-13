import os
import Ex1
import Ex2
import Ex3
import Ex4
import Ex5
import Ejercicio9
import Ejercicio8
import Ejercicio7
import Ejercicio6
import Ejercicio11
import Ejercicio10


while True:
    os.system('cls') #limpia pantalla
    print('Bienvenidos')
    opcion = input('seleccione programa a ejecutar: ')
    if opcion == '1':
      Ex1.principal()
    elif opcion == '2':
      Ex2.principal()
    elif opcion == '3':
        Ex3.principal()
    elif opcion == '4':
      Ex4.principal()
    elif opcion == '5':
      Ex5.principal()
    elif opcion == '6':
      Ejercicio6.main()
    elif opcion == '7':
      Ejercicio7.main()
    elif opcion == '8':
      Ejercicio8.main()
    elif opcion == '9':
      Ejercicio9.main()
    elif opcion == '10':
      Ejercicio10.main()
    elif opcion == '11':
      Ejercicio11.main()
    elif opcion == "0":
      print('Un placer, hasta la proxima')
      break
    continuar = input('presione enter para continuar')
