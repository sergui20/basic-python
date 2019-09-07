def main():
    print("Calculadora de pesos mexicanos a pesos colombianos")
    amount = float(input("Ingresa la cantidad de pesos colombianos que deseas calcular: "))
    result = calculator(amount)

    print("${} pesos mexicanos son ${} pesos colombianos".format(amount, result))

def calculator(amount):
    mex_to_col_rate = 145.97
    return mex_to_col_rate * amount

if __name__ == '__main__':
    main()