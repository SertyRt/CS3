if __name__ == '__main__':

    list1 = list(range(1, 21))
    listSquare = [x**2 for x in list1]
    listEven = [x for x in list1 if x % 2 == 0]


    print(listSquare + listEven + list1)