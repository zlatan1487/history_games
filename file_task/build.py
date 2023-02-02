
def guess_questions(words, user):
    """
    Функция, в которой программа выбирает первое слово из списка,
    перемешивает буквы и предлагает пользователю его отгадать.
    """
    with open(words, encoding='utf-8') as words:
        for word in words:
            word_ = word[::-1].strip()

            answer = input(f'Угадайте слово:{word_} ')

            if word.strip() == answer.lower():
                user['points'] += 10
                points = user['points']
                print(f'Верно, это {word.strip()}. Вы получаете {points} очков.')
                print()
            else:
                print(f'Неверно, это {word.strip()}.')
                print()


def write_to_file(history, user):
    """
    Функция окрывает и записывает в файл 'history.txt'
    имя игрока, а так же количество набранных им баллов
    """
    with open(history, 'a', encoding='utf-8') as file_history:
        name = user['name']
        point = user['points']

        file_history.writelines(f'{name} {point}\n')


def print_statistics(history):
    """
    Функция возвращает количество сыгранных игр и максимальный рекорд
    """
    games_count = 0
    arr_point = []
    with open(history, encoding='utf-8') as data:
        for item in data:
            name, point = item.strip().split(' ')
            games_count += 1
            arr_point.append(int(point))

    return f'Всего игр сыграно: {games_count}\n' f'Максимальный рекорд: {max(arr_point)}'
