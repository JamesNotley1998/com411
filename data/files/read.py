#Chars function
def display_chars(file_path, num_chars):
    with open(file_path) as file:
        data = file.read(num_chars)
        print(data)

#Display function
def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)

#Display Text function
def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)

#run function
def run():
    display_chars("txt\library.txt", 5)
    display_line("txt\library.txt")
    display_text("txt\library.txt")

if __name__ == "__main__":
    run()