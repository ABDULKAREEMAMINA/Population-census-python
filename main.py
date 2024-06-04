# insert function
def addPerson():
    print()
    print("          ADD RECORD")
    print("----------------------------------")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    sex = input("Enter Sex [M/F]: ")
    with open("census.txt", "a") as file:
        file.write("{}, {}, {}\n".format(name.upper(), age, sex.upper()))
        print()

def displayCensus():
    print()
    print("----------------------------------")
    print("          ALL RECORDS")
    print("----------------------------------")
    print("FULLNAME | AGE | GENDER")
    print("----------------------------------")
    with open("census.txt", "r") as file:
        for lines in file:
            records = lines.strip().split(",")
            if records[2].upper() == ' M':
                sex = "MALE"
            else:
                sex = "FEMALE"
            print("{} | {} | {}".format(records[0], records[1], sex))
    print()

def searchPerson():
    print()
    print("----------------------------------")
    print("          SEARCH RECORD")
    print("----------------------------------")
    name = input("Enter Name: ")
    print("----------------------------------")
    print("         Searched Result".upper())
    print("----------------------------------")
    with open("census.txt", "r") as file:
        for lines in file:
            records = lines.strip().split(",")
            if name.upper() == records[0]:
                if records[2].upper() == ' M':
                    sex = "MALE"
                else:
                    sex = "FEMALE"
                print("{} | {} | {}".format(records[0], records[1], sex))

    print()

def totalCensus():
    print()
    print("----------------------------------")
    print("          TOTAL RECORDS")
    print("----------------------------------")
    sum = 0
    with open("census.txt", "r") as file:
        for lines in file:
            sum = sum + 1
    print("Total Records = {}". format(sum))
    print()

if __name__ == "__main__":
    print("       Census Taking System")
    print("----------------------------------")
    while True:
        print("----------------------------------")
        print("          MAIN MENU")
        print("----------------------------------")
        print("1 - Add Person")
        print("2 - Display Census")
        print("3 - Search Person")
        print("4 - Total Census")
        option = int(input("Enter Option: "))
        if option == 1:
            addPerson()
        elif option == 2:
            displayCensus()
        elif option == 3:
            searchPerson()
        elif option == 4:
            totalCensus()
        else:
            print("Invalid Option Entered!")
