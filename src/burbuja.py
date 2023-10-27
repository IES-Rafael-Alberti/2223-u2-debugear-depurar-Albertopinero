import time
def OrdenarNumerosBurbuja(a):
    num = len(a)
    CuentaAtras = 5
    print("Iniciando algoritmo burbuja..." )
    for j in range(CuentaAtras):
        print(CuentaAtras)
        time.sleep(1)
        CuentaAtras-=1

    for i in range(num-1):
        for x in range(num-1-i):
            if a[x] > a[x+1]:
                a[x], a[x+1] = a[x+1], a[x]
    return a

if __name__ == "__main__":
    a = [8, 3, 1, 19, 14]
    OrdenarNumerosBurbuja(a)
    print(a)