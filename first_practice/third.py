def file_sys():
    n = ""
    n = input(n)
    names = {}
    ans = []
    for i in range(int(n)):
        file_name = ""
        file_name = input(file_name)
        file_name = file_name.split()
        names[file_name[0]] = file_name[1:]

    m = ""
    m = input(m)
    for i in range(int(m)):
        line = ""
        line = input(line)
        command = line.split()[0]
        file_name = line.split()[1]
        match command:
            case "read":
                command = "r"
            case "write":
                command = "w"
            case "execute":
                command = "x"
            case _:
                print("wrong command!")
                return
        if command in names[file_name]:
            ans.append("OK")
        else:
            ans.append("Access denied")
    for a in ans:
        print(a)
    return


def main():
    file_sys()
    return 0


if __name__ == "__main__":
    main()