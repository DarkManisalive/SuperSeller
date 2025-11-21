with open("UserNameForWeb.txt", "r") as Mainfile:
        list_of_names = Mainfile.readlines()
        Mainfile = [name.strip() for name in list_of_names]
print(list_of_names)