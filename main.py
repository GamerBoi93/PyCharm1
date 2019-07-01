def main():
    print("Hello World")

if __name__ == "__main__":
        main()

        name = input("What is your name?")
        print("Hello %s" %name)

        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,]

        Number = int(input("Enter A Number"))


        count = 0
        for x in test_list:
            if x > Number:
                count = count + 1

        print("The numbers greater than your input is " + str(count))



        Number2 = int(input("Enter A Number"))
        if Number2 % 2 == 0:
            print("Even")
        else:
            print("Odd")