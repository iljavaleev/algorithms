if __name__ == '__main__':
    counter = 0
    register = [0] * 10
    ram = [0] * 1000
    with open('input.txt') as f:
        n = next(f)
        next(f)
        while n > 0:
            c = [int(x) for x in f.readline().strip('\n')]
            if c == '':
                n -= 1
            if c[0] == 1:
                counter += 1
                break
            if c[0] == 2:
                register[c[1]] = c[2]
            elif c[0] == 3:
                register[c[1]] += c[2]
            elif c[0] == 4:
                register[c[1]] *= c[2]
            elif c[0] == 5:
                register[c[1]] = register[c[2]]
            elif c[0] == 6:
                register[c[1]] += register[c[2]]
            elif c[0] == 7:
                register[c[1]] *= register[c[2]]
            elif c[0] == 8:
                register[c[1]] = ram[register[c[2]]]
            elif c[0] == 9:
                ram[register[c[2]]] = register[c[1]]
            else:
                ...
            counter += 1
            register[c[1]] %= 1000
