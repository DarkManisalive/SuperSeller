import random
with open("UserNameForWeb.txt", "r") as Mainfile:
    list_of_names = Mainfile.readlines()
    Mainfile = [name.strip() for name in list_of_names]
def main():
    Name=""
    for i in range(16):
        Name += chr(random.randint(65, 90))  # Generate a random uppercase letter
        if i >= 5:
            Name += chr(random.randint(48, 57))  # Generate a random digit
    if Name in list_of_names:
        main()
    else:
        with open("UserNameForWeb.txt", "a") as Mainfile:
            Mainfile.write(Name + "\n")

if __name__ == '__main__':
    main()
