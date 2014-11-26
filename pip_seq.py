"""
Install packages in a specified order
"""
import sys
import pip


def main():
    args = []
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            args = [arg]
        else:
            args.append(arg)
            pip.main(['install'] + args)
            args = []


if __name__ == '__main__':
    main()
