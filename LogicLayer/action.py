import sys
from LogicLayer import printdb
from PersistenceLayer.Repository import repo


def main(args):
    with open(args[1], 'r') as file:
        for line in file:
            if line[-2:] == "\n":
                line = line[:-1]
            tup = line.split(', ')
            repo.apply_action(tup)
    printdb.main()


if __name__ == "__main__":
    main(sys.argv)
