# Health management system
# First we have to make three files for that
# Her our three users are Deep, Harry, Poojan
# First we have to ask what you wanna do lock or retrieve
# We have to make total 6 files
# 3 files for exercise amd 3 for diet
# exercise files are deep_ex, harry_ex, poojan_ex
# diet files are deep_diet, harry_diet, poojan_diet

while True:
    print("What you want to do lock or retrieve : ")
    inp = input().capitalize()
    if inp == "Lock":
        print("For whom you want to lock the data")
        print(" Press 1 for deep")
        print(" Press 2 for harry")
        print(" Press 3 for poojan")
        inp2 = int(input())
        if inp2 == 1:
            print("What you want to lock in deep's log")
            print("Press 1 for diet")
            print("Press 2 for exercise")
            inp2_1 = int(input())
            if inp2_1 == 1:
                f = open("deep_diet.txt", "a")
                a = input("Enter which diet you follow : ")


                def getdate():
                    import datetime
                    return datetime.datetime.now()


                f.write(str([str(getdate())]) + " : " + a + "\n")
                f.close()
            elif inp2_1 == 2:
                f = open("deep_ex.txt", "a")
                a = input("Enter which exercise you do : ")


                def getdate():
                    import datetime
                    return datetime.datetime.now()


                f.write(str([str(getdate())]) + " : " + a + "\n")
                f.close()
            else:
                print("Please select valid option")

        elif inp2 == 2:
            print("What you want to lock in harry's log")
            print("Press 1 for diet")
            print("Press 2 for exercise")
            inp2_2 = int(input())
            if inp2_2 == 1:
                f = open("harry_diet.txt", "a")
                a = input("Enter which diet you follow : ")


                def getdate():
                    import datetime
                    return datetime.datetime.now()


                f.write(str([str(getdate())]) + " : " + a + "\n")
                f.close()
            elif inp2_2 == 2:
                f = open("harry_ex.txt", "a")
                a = input("Enter which exercise you do : ")


                def getdate():
                    import datetime
                    return datetime.datetime.now()


                f.write(str([str(getdate())]) + " : " + a + "\n")
                f.close()
            else:
                print("Please select valid option")

        elif inp2 == 3:
            print("What you want to lock in poojan's log")
            print("Press 1 for diet")
            print("Press 2 for exercise")
            inp2_3 = int(input())
            if inp2_3 == 1:
                f = open("poojan_diet.txt", "a")
                a = input("Enter which diet you follow : ")


                def getdate():
                    import datetime
                    return datetime.datetime.now()


                f.write(str([str(getdate())]) + " : " + a + "\n")
                f.close()
            elif inp2_3 == 2:
                f = open("poojan_ex.txt", "a")
                a = input("Enter which exercise you do : ")


                def getdate():
                    import datetime
                    return datetime.datetime.now()


                f.write(str([str(getdate())]) + " : " + a + "\n")
                f.close()
            else:
                print("Please select valid option")

        else:
            print("Please provide valid option")

    elif inp == "Retrieve":
        print("For whom you want to retrieve the data")
        print("press 1 for deep")
        print("press 2 for harry")
        print("press 3 for poojan")
        inp3 = int(input())

        if inp3 == 1:
            print("What you want to retrieve from deep's data")
            print("Press 1 for diet")
            print("Press 2 for exercise")
            inp3_1 = int(input())
            if inp3_1 == 1:
                f = open("deep_diet.txt", "rt")
                for i in f:
                    print(i)
                f.close()
            elif inp3_1 == 2:
                f = open("deep_ex.txt", "rt")
                for i in f:
                    print(i)
                f.close()
            else:
                print("Please select valid option")

        elif inp3 == 2:
            print("What you want to retrieve from harry's data")
            print("Press 1 for diet")
            print("Press 2 for exercise")
            inp3_2 = int(input())
            if inp3_2 == 1:
                f = open("harry_diet.txt", "rt")
                for i in f:
                    print(i)
                f.close()
            elif inp3_2 == 2:
                f = open("harry_ex.txt", "rt")
                for i in f:
                    print(i)
                f.close()
            else:
                print("Please select valid option")

        elif inp3 == 3:
            print("What you want to retrieve poojan's data")
            print("Press 1 for diet")
            print("Press 2 for exercise")
            inp3_3 = int(input())
            if inp3_3 == 1:
                f = open("poojan_diet.txt", "rt")
                for i in f:
                    print(i)
                f.close()
            elif inp3_3 == 2:
                f = open("poojan_ex.txt", "rt")
                for i in f:
                    print(i)
                f.close()
            else:
                print("Please select valid option")

        else:
            print("Please select valid option")

    else:
        print("Please write valid option")
        print("Do you want to continue this : (Press Y for yes and N for no) ")
        ch = input()
        if ch == 'y':
            continue
        else:
            print("Okay see you next time...")

    print("Do you want to continue this : (Press Y for yes and N for no) ")
    ch = input()
    if ch == 'y':
        continue
    else:
        print("Okay see you next time...")
        break
