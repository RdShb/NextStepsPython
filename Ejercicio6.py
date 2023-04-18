##El codigo suma todos los numeros anteriores a n, sin sumar el propio n
def main():
    n = int(input("Ingrese un numero: "))
    total = 0
    for i in range(n):
        total = total + i
    print(total)
if __name__=="__main__":
   main()