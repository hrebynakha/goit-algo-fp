"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію
для створення фрактала “дерево Піфагора”. 
Програма має візуалізувати фрактал “дерево Піфагора”, 
і користувач повинен мати можливість вказати рівень рекурсії.

"""
import turtle

def pifagor_tree(t, branch_length, angle, level, recursion_level=1):
    """Pifagot tree draw function"""
    if level == 0:
        return
    # малюємо гілку та визначаємо нову довжину гілки
    t.forward(branch_length)
    new_length = branch_length * (2**0.5 / 2)
    # задаємо поворт на відповідний кут
    t.left(angle)
    # запускаємо рекурсію для побудови гілки дерева
    pifagor_tree(t, new_length, angle, level-1, recursion_level+1)
    # повертаємось назад
    t.right(2 * angle)
    pifagor_tree(t, new_length, angle, level-1, recursion_level+1)

    # йдемо на початковий стан
    t.left(angle)
    t.backward(branch_length)


def draw_tree(levels):
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.color("green")
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(90) # Повертаємо стрілку на 90 градусів, щоб дерево росло вгору
    init_leng = 100
    init_angle = 45
    pifagor_tree(t, init_leng, init_angle , level=levels)
    window.mainloop()

if __name__ == '__main__':
    levels = int(input("Input tree level:"))
    draw_tree(levels)
