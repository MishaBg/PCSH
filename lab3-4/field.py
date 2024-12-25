def field(goods, *args):
    assert len(args) > 0
    for i in goods:
        if len(args) == 1:
            value = i.get(args[0])
            if value is not None:
                yield value
        else:
            res_map = {key: i.get(key) for key in args if i.get(key) is not None}
            if res_map:
                yield res_map


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]
    print(list(field(goods, 'title')))
    print(*list(field(goods, 'title', 'price')))


if __name__ == '__main__':
    main()
