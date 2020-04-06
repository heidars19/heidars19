
def update_file():
    filename = "./Wordbank.txt"
    BACKUP_FILE = filename + '.bak'

    with open(filename, 'r', encoding='utf-8') as file_original:
        with open(BACKUP_FILE, 'w+', encoding='utf-8') as file_bak:
            for line in file_original:
                file_bak.write(line.strip() + ",0,0,0,2000-01-01\n")


if __name__ == "__main__":
    # update_file()
    name = "heiðar"
    word = "Heiðar"
    if name.lower() == word.lower():
        print("Sama orð")
