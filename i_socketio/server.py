#!/usr/bin/env python3


import os
import time
import signal


# Main program
def main(args=None, test=False):
    assert os.name == "posix", "This code makes Unix-specific assumptions"
    # if we hup, restart by making a new Supervisor()
    first = True
    print("server.....")


if __name__ == "__main__": # pragma: no cover
    main()