import os


class Numerizator():
    def __init__(self):
        self.current_location = os.path.dirname(os.path.abspath(__file__))
        self.counter = 0

    def main_menu(self):
        user_choice = (input("1. Show files\n2. Add numbers in front of current file names\n3. Add number behind current file names\n"
                             "4. Add number in front and change file names\n5. Add number behind and change file names\n6. Exit\nChoose your weapon: "))
        
        if user_choice == "1":
            self.show_files()
        elif user_choice == "2":
            self.add_num_front()
        elif user_choice == "3":
            self.add_num_back()
        elif user_choice == "4":
            self.custom_name_front()
        elif user_choice == "5":
            self.custom_name_back()
        elif user_choice == "6":
            exit()
        else:
            print("\nInvalid selection\n")
            self.main_menu()

    def show_files(self):
        num_of_files = len(os.listdir(self.current_location))

        if(num_of_files < 2):
            print("No files in this folder!")
        else:
            print("\nNumerizator found " + str(num_of_files) + " files:\n")
            for files in os.listdir(self.current_location):
                print(files)

    def add_num_front(self):
        for files in os.listdir(self.current_location):
            if "Numerizator" in files:
                continue

            self.counter += 1
            os.rename(self.current_location + "/" + files, self.current_location +
                      "/" + str("%02d" % self.counter) + ". " + files)
        print("<<< Mission Complete >>>")

    def add_num_back(self):
        for files in os.listdir(self.current_location):
            if "Numerizator" in files:
                continue

            self.counter += 1
            os.rename(self.current_location + "/" + files,
                      self.current_location + "/" + files + str("%02d" % self.counter))
        print("<<< Mission Complete >>>")

    def custom_name_front(self):
        new_file_name = input("Enter new file name: ")
        for files in os.listdir(self.current_location):
            if "Numerizator" in files:
                continue

            self.counter += 1
            os.rename(self.current_location + "/" + files, self.current_location +
                      "/" + str("%02d" % self.counter) + ". " + new_file_name)
        print("<<< Mission Complete >>>")

    def custom_name_back(self):
        new_file_name = input("Enter new file name: ")
        for files in os.listdir(self.current_location):
            if "Numerizator" in files:
                continue

            self.counter += 1
            os.rename(self.current_location + "/" + files, self.current_location +
                      "/" + new_file_name + str("%02d" % self.counter))
        print("<<< Mission Complete >>>")


if __name__ == "__main__":
    print(r""" 
 _   _                           _          _             
| \ | |                         (_)        | |            
|  \| |_   _ _ __ ___   ___ _ __ _ ______ _| |_ ___  _ __ 
| . ` | | | | '_ ` _ \ / _ \ '__| |_  / _` | __/ _ \| '__|
| |\  | |_| | | | | | |  __/ |  | |/ / (_| | || (_) | |   
\_| \_/\__,_|_| |_| |_|\___|_|  |_/___\__,_|\__\___/|_|
                                                          
                            made by Djordje Mancic 2020 (c)""")
    print("\nIMPORTANT: Place Numerizator in SAME folder with files you want to rename!\nNumerizator will rename ALL files in same folder\n")
    x = Numerizator().main_menu()
