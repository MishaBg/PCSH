def print_result(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        res = func(*args, **kwargs)
        if isinstance(res, list):
            print(*res, sep='\n')
        elif isinstance(res, dict):
            # for key in res:
            #     print(f'{key} = {res[key]}')

            # для 7 задачи
            for key in res:
                print(f'{key}, зарплата {res[key]} руб.')
        else:
            print(res)
        return res
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


def main():
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()
