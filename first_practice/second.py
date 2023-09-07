def auth():
    n = ("")
    n = input(n)

    if 1 <= int(n) <= 1000000:
        names = {}
        output = []
        for i in range(int(n)):
            string = ""
            string = input(string)
            if string in names:
                names[string] += 1
                string = string + str(names[string])
                names[string] = 0
                output.append(string)
            else:
                names[string] = 0
                output.append("OK")

    for name in output:
        print(name)

    return


def main():
    auth()
    return 0


if __name__ == "__main__":
    main()