import random
from flask import render_template
with open("UserNameForWeb.txt", "r") as Mainfile:
    list_of_names = Mainfile.readlines()
    Mainfile = [name.strip() for name in list_of_names]
def main():
    YourUserName=""
    for i in range(16):
        YourUserName += chr(random.randint(65, 90))  # Generate a random uppercase letter
        if i >= 5:
            YourUserName += chr(random.randint(48, 57))  # Generate a random digit
    if YourUserName in list_of_names:
        main()
    else:
        with open("UserNameForWeb.txt", "a") as Mainfile:
            Mainfile.write(YourUserName + '\n')
    return YourUserName
if __name__ == '__main__':
    main()