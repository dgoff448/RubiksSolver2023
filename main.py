import argparse
import pprint
from typing import Optional
from typing import Sequence
import os

import createCells
import Cube

# Argparse Tutorial (https://www.youtube.com/watch?v=-Sgw-6a1HjU)
def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()



    # Positional 
    parser.add_argument('-t', '--test', action='store_true')
    parser.add_argument('filename', help='Rubiks Cube configuration file')
    args = parser.parse_args(argv)
    # pprint.pprint(vars(args))

    if args.test:
        os.system("python C:\\Users\\sc864\\OneDrive\\Desktop\\RubiksSolver2023\\tests.py")
    else:
        cube = Cube.Cube(createCells.createCells(vars(args)['filename']))     # cube contains list of Cell Objects


    return 0




if __name__ == "__main__":
    main()