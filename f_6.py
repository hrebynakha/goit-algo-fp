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
    calories, result = 0, []
    for _, values in items.items():
        values['ratio'] = values['calories'] / values['cost']
    items = sorted(items.items(), key=lambda x: x[1]['ratio'], reverse=True)
    iterator = iter(items)
    while money > 0:
        try:
            current = next(iterator)
        except StopIteration:
            break
        if current[1]['cost'] <= money:
            money = money - current[1]['cost']
            if money < 0:
                # we cannot buy it
                break
            result.append(current[0])
            calories += current[1]['calories']
    return calories, result


def dynamic_programming(items,  money):
    """Dynamic alroritm"""
    # empty table for save max calories for every money input
    max_calories = [0] * ( money + 1)
    selected_items = [[] for _ in range(money + 1)]

    # Cycle for every typr of item
    for name, item in items.items():
        cost = item['cost']
        calories = item['calories']
        # Update result in table
        for b in range(money, cost - 1, -1):
            #print( b, "max_calories", max_calories, selected_items[b])
            if max_calories[b] < max_calories[b - cost] + calories:
                max_calories[b] = max_calories[b - cost] + calories
                selected_items[b] = selected_items[b - cost] + [name]

    # max cal for this budget
    calories = max_calories[money]
    # Selected items
    chosen_items = selected_items[money]
    return calories, chosen_items


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

money = 75
print("Greede", greedy_algorithm(items, money))
print("Dynamic", dynamic_programming(items, money))
