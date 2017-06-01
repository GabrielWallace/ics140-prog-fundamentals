celsius = 0
while celsius <= 20:
    fahrenheit = (9 / 5) * celsius + 32
    print('{0:2d}'.format(celsius))
    celsius = celsius + 1
    print('{0:2d}{1:3f}'.format(celsius, fahrenheit))
