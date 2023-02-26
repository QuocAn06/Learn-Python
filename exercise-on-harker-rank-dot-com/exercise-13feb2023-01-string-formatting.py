def print_formatted(number):
    # count the number of characters of the hexadecimal sequence
    width = len("{0:b}".format(number))

    # print the sequence of numbers according to the requirements of the topic
    for i in range(1, number + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)