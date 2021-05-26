a = [10, 11, 0]
b = [0, 1, 0]
print(all(a), any(b))

name = 'Ninja'
count = 99

text1 = """Высоко - высоко в горах жил монах {0}, и было у монах 3 ворона... (с) , 15{1}""".format(name[2:5], count)
text2 = f"Высоко - высоко в горах жил монах {name[1:5]}, и было у монах 3 ворона... (с), 15{count}"
text3 = "Высоко - высоко в горах жил монах %s, и было у монах 3 ворона... (с), 15%s" % (name[2:5], count)
print(text1, text2, text3, sep='\n')


class Dog:
    pass


def foo():
    print('Hi')


print(callable(Dog))


g = 'gray'
def colors():
    y = 'yellow'
    g = 'green'
    def print_red():
        r = 'red'
        print(r, y, g)
    def print_blue():
        b = 'blue'
        print(b, y, g)

    print_red()
    print_blue()


colors()
