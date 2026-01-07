"""
This file holds the practice on Custom Exception
"""
import sys

class PlatformException(Exception):
    """
    Exception for Platform dependency issues
    """

def check_linux_version():
    if "linux" not in sys.platform:
        raise PlatformException("Error: Not a Linux environment")
    print("Inside the Linux env")


def upgrade_version():
    try:
        check_linux_version()
    except PlatformException as e:
        print(f"Encountered platform error {e}: Halting upgrade")
    finally:
        print("Exiting upgrade")


if __name__=="__main__":
    upgrade_version()
