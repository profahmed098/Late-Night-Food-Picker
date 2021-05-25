import random

DS = []
rdm_num = 69
agn = "y"

while agn == "y":
    choice = input("Number of Choices(2-5): ")
    if choice == "2":
        lst_1 = input("First Choice: ")
        lst_2 = input("Second Choice: ")
        DS.append(lst_1)
        DS.append(lst_2)
        rdm_num = random.randrange(0, 1)
        print("Item that was picked: " + DS[rdm_num])
    elif choice == "3":
        lst_1 = input("First Choice: ")
        lst_2 = input("Second Choice: ")
        lst_3 = input("Third Choice: ")
        DS.append(lst_1)
        DS.append(lst_2)
        DS.append(lst_3)
        rdm_num = random.randrange(0, 2)
        print("Item that was picked: " + DS[rdm_num])
    elif choice == "4":
        lst_1 = input("First Choice: ")
        lst_2 = input("Second Choice: ")
        lst_3 = input("Third Choice: ")
        lst_4 = input("Fourth Choice: ")
        DS.append(lst_1)
        DS.append(lst_2)
        DS.append(lst_3)
        DS.append(lst_4)
        rdm_num = random.randrange(0, 3)
        print("Item that was picked: " + DS[rdm_num])
    elif choice == "5":
        lst_1 = input("First Choice: ")
        lst_2 = input("Second Choice: ")
        lst_3 = input("Third Choice: ")
        lst_4 = input("Fourth Choice: ")
        lst_5 = input("Fifth Choice: ")
        DS.append(lst_1)
        DS.append(lst_2)
        DS.append(lst_3)
        DS.append(lst_4)
        DS.append(lst_5)
        rdm_num = random.randrange(0, 4)
        print("Item that was picked: " + DS[rdm_num])
    else:
        print("Number out of range")
    agn = input("Want to try again(y/n): ")

print("Thank you for using this service (>-<)")
