while True:
    try:
        num = int(input("digite um numero inteiro: "))
        resultado = 10 / num
        print(f"resultado da divisao: {resultado}")
        break
    except ZeroDivisionError:
        print("erro: nao é possivel dividir por zero.")
    except ValueError:
        print("erro: digite um numero inteiro valido")