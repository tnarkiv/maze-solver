"""Main module of the program"""
from window import Window


def main():
    """Main function"""
    win = Window(800, 600)
    win.wait_for_close()

main()
