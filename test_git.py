# TODO здесь писать код
def tpl_sort(*data):

    count = 0
    for i_tpl in data:
        if not(isinstance(i_tpl, int)):
            count += 1
    if count == 0:
        print(sorted(data))
    else:
        print(data)


print(tpl_sort(6, 3, -1, 8, 4, 10, -5))