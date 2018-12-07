from check_equiv import check_equiv
import os
import sys


def main(argv):
    if len(argv) != 3:
        print('Usage: {0} <file1> <file2>'.format(os.path.basename(__file__)))
        return -1

    with open(argv[1], 'r') as f1:
        query1 = f1.read()
    with open(argv[2], 'r') as f2:
        query2 = f2.read()

    print(
        'First query:\n\n{0}\n\n----------------------------\n\nSecond query:\n\n{1}\n\n----------------------------\n'.format(query1, query2))

    try:
        queries_are_equiv, msg = check_equiv(query1, query2)
        print(
            'Queries are equivalent' if queries_are_equiv else 'Queries are not equivalent\nMessage: {0}'.format(msg))
    except Exception as e:
        print('Error: {0}'.format(e))
        return -2
    return 0


if __name__ == '__main__':
    main(sys.argv)
