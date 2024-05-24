"""
Завдання 6: Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — 
жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі 
з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність.
Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник 
з вартістю та калорійністю.



Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, 
максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming,
яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.
"""

def greedy_algorithm(items, money):
    """Return greed items"""
    result = []
    for _, values in items.items():
        values['ratio'] = values['calories'] / values['cost']
    items = sorted(items.items(), key=lambda x: x[1]['ratio'], reverse=True)
    iterator = iter(items)
    current = next(iterator)
    while money > 0:
        if current[1]['cost'] <= money:
            money = money - current[1]['cost']
            if money < 0:
                # we cannot buy it
                break
            result.append(current[0])
        else:
            try:
                current = next(iterator)
            except StopIteration:
                break

    return result, money


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print(greedy_algorithm(items, 49))