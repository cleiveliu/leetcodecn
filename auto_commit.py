"""
auto commit git and push to master with a git path and a optional commit message.
usage:
put this file in your git project dir and run it or \
    script.py [-p|-pathname] filename [-m|-message] message
"""

import sys
import os


class Args:
    def __init__(
        self, pathname=os.path.dirname(__file__), commit_message="auto commit"
    ):
        self.pathname = pathname
        self.commit_message = commit_message

    def __repr__(self):
        return "Args(pathname={}, commit_message={})".format(
            self.pathname, self.commit_message
        )


def _exit():
    print(__doc__)
    sys.exit(1)


def perse_args():
    args = sys.argv[1:]
    args = list(map(lambda x: x.lower(), args))

    theArgs = Args()
    index = 0
    if index < len(args):
        if args[index] in ("-p", "-pathname"):
            if index + 1 < len(args):
                theArgs.pathname = args[index + 1]
                index += 2
            else:
                _exit()
        if index < len(args):
            if args[index] in ("-m", "-message", "--m"):
                if index + 1 < len(args):
                    theArgs.commit_massage = args[index + 1]
                    index += 2
                else:
                    _exit()
            else:
                _exit()
        if index < len(args):
            _exit()

    return theArgs


def execute(args: Args):
    os.chdir(args.pathname)
    os.system("git add .")
    os.system('git commit -m "{}"'.format(args.commit_massage))
    os.system("git push")


if __name__ == "__main__":
    args = perse_args()
    print(f"args:\n{args}")
    execute(args)
