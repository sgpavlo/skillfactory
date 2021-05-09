import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


def game_core(number, step=10):
    '''Последовательно увеличиваем predict на значение step=10. Если
    значение predict становится > загаданного number, то уменьшаем
    predict на единицу, пока predict не станет равен number. Функция
    принимает загаданное число и шаг, а возвращает число попыток
    '''
    count=0
    predict=0
    while number!=predict:
        count+=1
        if number>predict:
            predict+=step
        else:
            predict-=1
    return count


score_game(game_core)