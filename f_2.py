"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію
для створення фрактала “дерево Піфагора”. 
Програма має візуалізувати фрактал “дерево Піфагора”, 
і користувач повинен мати можливість вказати рівень рекурсії.

"""

"""Home work 3_2"""
import turtle

def pifagor_tree():
    pass
def draw_tree():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(300 / 2, 0)
    t.pendown()
    t.left(90)
    t.forward(300)
    for _ in range(3):
        t.left(-120)

    window.mainloop()

draw_tree()