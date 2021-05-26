

def decator(func):
    def inner(*args, **kwargs):
        print("==========de=======================")
        func(*args, **kwargs)
        print("==========de=======================")

    return inner

def table(func):
    def inner(*args, **kwargs):
        print("=========table==================")
        func(*args, **kwargs)
        print("=========table========================")

    return inner
print("""Использование декораторов""")
@decator
@table # say = table(decator(say))
def say(x, y, z):
    print('hi', x, y, z)


say("vas", 'vas', 10)



print("""Использование замыканий""")

d = decator(say)
d("vas", 'vas', 10)





print("""замыкания""")

def main1():
    name = 'Ivan'
    def inner1():
        print("ЗАМЫКАНИЕ №1===================", name)
    return inner1

a = main1()
a()


def main1(name):
    def inner1():
        print("ЗАМЫКАНИЕ №2===================", name)
    return inner1

b = main1('Toshiba')
b()

print("ЗАМЫКАНИЕ №3===================")
def main1(val1):
    def inner1(val2):
        return val1+val2
    return inner1

b = main1(10)
print(b(5))
print(b(7))


print("ЗАМЫКАНИЕ №4===================")
#

def main2():
    count = 0 #
    def inner():
        nonlocal count #переменная count будет ссылаться на область видимости main2()
        count += 1
        print(count)
        return count # для присвоения глобальному полю видимости
    return inner


inc = main2()
inc()
inc()
inc()
inc()
inc()
inc()
print(inc())


print("ЗАМЫКАНИЕ №5===================")





