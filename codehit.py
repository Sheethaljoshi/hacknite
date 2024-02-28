import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple script with argument parsing")
    
    parser.add_argument("-f", "--file", help="File Name", required=True)

    args = parser.parse_args()

    file_path = args.file

    print("File path:", file_path)


if __name__ == "__main__":
    main()
