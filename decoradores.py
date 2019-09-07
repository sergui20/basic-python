def protected(func):
    def handler(password):
        if password == 'platzi':
            return func()
        else:
            print('Contrasena incorrecta')  

    return handler          

@protected
def protected_func():
    print("Contrasena correcta")

if __name__ == "__main__":
    password = input("Ingresa tu contrasena: ")  

    # Algo mucho mas sencillo es usar decoradores

    # wrapper =  protected(protected_func)
    # wrapper(password)

    protected_func(password)  