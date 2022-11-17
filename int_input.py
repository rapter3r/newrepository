def int_input(message):
    while True:
        try:
            resault = float(input(message))
            print('Вы ввели коректно.')
        except:
            print('Вы ввели некоректно, попробуйте ввести ещё раз.')
        else:
            return resault
a = int_input('a=')
b = int_input('b=')