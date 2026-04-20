from array import array

if __name__ == '__main__':
    array1 = array('i', [1,2,3,4,5])
    array1.append(6)
    array1.extend([7])

    print(f"Długość array1: {len(array1)}")
    print(f"Itemsize array1: {array1.itemsize}")
    list1 = array1.tolist()