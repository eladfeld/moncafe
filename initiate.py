import sys
import os


if os.path.exists("moncafe.db"):
    os.remove("moncafe.db")
from PersistenceLayer.Repository import repo


def main(args):
    repo.init_tables()
    with open(args[1], 'r') as file:
        for line in file:
            if line[-1:] == "\n":
                line = line[:-1]
            tup = line.split(', ')
            repo.insert_to_database(tup)


if __name__ == "__main__":
    main(sys.argv)

