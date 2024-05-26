"""
Завдання 7: Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків,
обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів.
Для кожного кидка визначте суму чисел, які випали на обох кубиках.
Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції.
Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми,
виявлені за допомогою методу Монте-Карло.

"""
import random
import matplotlib.pyplot as plt


def toss_cube():
    """Toss cube"""
    return random.randint(1, 6)

def toss_cube_simulation(count, ):
    """Simulation 2 cube tossing"""
    result = []
    while count > 0:
        cube_1, cube_2 = toss_cube(), toss_cube()
        exp_result = {
            'cube_1' : cube_1,
            'cube_2' : cube_2,
            'sum' : cube_1 + cube_2
        }
        result.append(exp_result)
        count -= 1
    return result

def calc_result(simulation_result, toss_count):
    """Calculate count of cube sum and their probability"""
    counts = {}
    for toss_result in simulation_result:
        sum_value = toss_result['sum']
        if sum_value in counts:
            counts[sum_value] += 1
        else:
            counts[sum_value] = 1
    items, probability = [], []
    for item, count in counts.items():
        items.append(item)
        probability.append( (count / toss_count)  * 100)
    return {"sum": items, "probability" : probability}

if __name__ == "__main__":
    TOSS_CONF = {
        100: 'blue',
        1000: 'red',
        10000: 'green',
        100000: 'yellow'
    }
    fig, axs = plt.subplots(len(TOSS_CONF), 1, figsize=(10, 15))
    x_labels = range(1, 13)
    i = 0
    for toss_count, color in TOSS_CONF.items():
        simulation_result = toss_cube_simulation(toss_count)
        results = calc_result(simulation_result, toss_count)
        axs[i].bar(
                results["sum"],
                results["probability"],
                color=color,
                alpha=0.7
        )
        axs[i].set_title(f'Sum for {toss_count}')
        axs[i].set_ylabel('Probability')
        axs[i].set_xticks(x_labels)
        i += 1

    plt.tight_layout()
    plt.subplots_adjust(top=0.95)
    plt.show()
