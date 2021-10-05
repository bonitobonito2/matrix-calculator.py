print("____________________________________________")
print("program calculates matrix multiplication.\nEnter the coordinates of first matrix.")
print("program only knows how to multiplicative 3x3 matrix")
first_cords = input("ENTER: ")
counter = 0
counter1 = 1
first_values = []
idk = 0

if first_cords == "3x3":
    for i in range(9):
        print(counter1, "th number")
        while True:
            try:
                num = int(input(":::"))
                break
            except ValueError:
                print("Enter number!")
        first_values.append(num)
        counter += 1
        counter1 += 1
        if counter == 9:

            a = []
            b = []
            c = []
            for i in range(10):

                if idk < 3:
                    a.append(first_values[idk])

                elif idk < 6:
                    b.append(first_values[idk])

                elif idk < 9:
                    c.append(first_values[idk])
                idk += 1

print("", a, "\n", b, "\n", c, "\n")
counter2 = 0
counter3 = 1
second_values = []
idk1 = 0
if first_cords == "3x3":
    print("now u have to choose next matrix cords from this types: 1. 3x3.PROGRAM ONLY KNOWS 3x3 matrix")
    second_cords = input("Enter:::")
    if second_cords == "3x3":
        for i in range(9):
            print(counter3, "th number")
            while True:
                try:
                    num1 = int(input(":::"))
                    break
                except ValueError:
                    print("Enter Number: ")

            second_values.append(num1)
            counter2 += 1
            counter3 += 1
            if counter2 == 9:

                a1 = []
                b1 = []
                c1 = []
                for i in range(10):

                    if idk1 < 3:
                        a1.append(second_values[idk1])

                    elif idk1 < 6:
                        b1.append(second_values[idk1])

                    elif idk1 < 9:
                        c1.append(second_values[idk1])
                    idk1 += 1

print("FIRST MATRIX\n", a, "\n", b, "\n", c, "\n")
print("SECOND MATRIX\n", a1, "\n", b1, "\n", c1, "\n")


def calculate():
    result = []
    numbers_for1 = 0
    numbers_for2 = 0
    numbers_for3 = 0

    for i in range(3):
        result.append((a[0] * a1[numbers_for1]) + (a[1] * b1[numbers_for1]) + (a[2] * c1[numbers_for1]))
        numbers_for1 += 1
    for i in range(3):
        result.append((b[0] * a1[numbers_for2]) + (b[1] * b1[numbers_for2]) + (b[2] * c1[numbers_for2]))
        numbers_for2 += 1
    for i in range(3):
        result.append((c[0] * a1[numbers_for3]) + (c[1] * b1[numbers_for3]) + (c[2] * c1[numbers_for3]))
        numbers_for3 += 1

    print("multiplication RESULT!\n", result[0], result[1], result[2], "\n", result[3], result[4], result[5], "\n", result[6],
          result[7], result[8])

    result1 = []
    mon = 0
    mon1 = 0
    mon2 = 0
    for i in range(3):
        result1.append(a[mon] + a1[mon])
        mon += 1
    for i in range(3):
        result1.append(b[mon1] + b1[mon1])
        mon1 += 1
    for i in range(3):
        result1.append(b[mon2] + b1[mon2])
        mon2 += 1
    print("\naddition RESULT!\n", result1[0], result1[1], result1[2], "\n", result1[3], result1[4], result1[5], "\n",
          result1[6],
          result1[7], result1[8])

calculate()