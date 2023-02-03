from build import write_to_file, print_statistics, guess_questions

if __name__ == '__main__':
    user_name = input('Введите ваше имя ')

    user = {'name': user_name, 'points': 0}

    guess_questions('FILE/words.txt', user)
    write_to_file('FILE/history.txt', user)
    print(print_statistics('FILE/history.txt'))
