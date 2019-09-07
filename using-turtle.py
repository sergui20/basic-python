import turtle

# window = turtle.Screen()
# david = turtle.Turtle()
# david.forward(50)
# david.left(90)
# david.forward(50)
# david.left(90)
# david.forward(50)
# david.left(90)
# david.forward(50)
# david.left(90)

# turtle.mainloop()

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    renderSquare(dave)

def renderSquare(dave):
    length = input("Ingrese la longitud de los lados del cuadrado: ")

    for i in range(4):
        dave.forward(length)
        dave.left(90)

    turtle.mainloop()    

# if __name__ == "__main__":
    # main()    
    
main()    