from editor import fileeditor


def main():
    print("TF2 Config Editor")
    print("Enter a command, or 'help' for help.")
    command = input("<<< ")

config = fileeditor.FileEditor()

if __name__ == "__main__":
    main()
