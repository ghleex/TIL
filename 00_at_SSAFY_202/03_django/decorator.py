def hello(func):
    def wrapper():
        print('hi!')
        func()
        print('what?')
    return wrapper

@hello
def bye():
    print('bye')

bye()
