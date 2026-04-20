from array import array

if __name__ == '__main__':
    array_int = array('i', [1,2,3,4])
    try:
        array_int.append('test')
    except TypeError:
        print('Nie można dodać napisu do arraya')