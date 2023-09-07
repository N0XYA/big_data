def auth():
    n = ("")
    n = input(n)

    if 1 <= int(n) <= 1000000:
        k = 1
        names = []
        output = []
        for i in range(int(n)):
            string = ""
            string = input(string)
            if string in names:
                string = string + str(k)
                names.append(string)
                output.append(string)
                k += 1
            else:
                names.append(string)
                output.append("OK")

    for name in output:
        print(name)

    return


def main():
    auth()
    return 0


if __name__ == "__main__":
    main()