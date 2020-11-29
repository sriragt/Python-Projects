Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def Pythagorean(*number_range):
        import math
        try:
                if type(number_range[0]) != int or type(number_range[1]) != int:
                        print('Please input integer values.')
                        return
        except IndexError:
                pass
        if len(number_range) == 2:
                first = number_range[0]
                number = number_range[1]
                region = 'between ' + str(first) + ' and ' + str(number)
        elif len(number_range) == 1:
                first = number_range[0]
                number = number_range[0]
                region = 'equal to ' + str(first)
        elif len(number_range) >= 3:
                print('Please input one or two integers.')
                return
        order = []
        for i in range(1, number + 1):
                for j in range(1, number + 1):
                        x = i*i + j*j
                        y = int(math.sqrt(x))
                        if y*y == x and y <= number and y >= first:
                                if i <= j:
                                        order.append(int(y))
        order.sort()
        for i in range(1, number + 1):
                for j in range(1, number + 1):
                        x = i*i + j*j
                        y = int(math.sqrt(x))
                        if y*y == x and y <= number and y >= first:
                                if i <= j:
                                        for b, c in enumerate(order):
                                                if c == y:
                                                        order[b] = str(i) + ', ' + str(j) + ', ' + str(y)
                                                        break
        if len(order) == 1:
                print("There is " + str(len(order)) + " Pythagorean triple " + region + '.')
        else:
                print("There are " + str(len(order)) + " Pythagorean triples " + region + '.')
        for a in order:
                print(a)
        
                
def Primitive(*number_range):
        import math
        def coprime(p, q):
                while q != 0:
                        p, q = q, p%q
                return p == 1
        if type(number_range[0]) != int or type(number_range[1]) != int:
                print('Please input integer values.')
                return
        if len(number_range) == 2:
                first = number_range[0]
                number = number_range[1]
                region = 'between ' + str(first) + ' and ' + str(number)
        elif len(number_range) == 1:
                first = number_range[0]
                number = number_range[0]
                region = 'equal to ' + str(first)
        elif len(number_range) >= 3:
                print('Please input one or two integers.')
                return
        order = []
        for i in range(1, number + 1):
                for j in range(1, number + 1):
                        x = i*i + j*j
                        y = int(math.sqrt(x))
                        if y*y == x and y <= number and y >= first:
                                if i <= j:
                                        if coprime(i, j):
                                                order.append(int(y))
        order.sort()
        for i in range(1, number + 1):
                for j in range(1, number + 1):
                        x = i*i + j*j
                        y = int(math.sqrt(x))
                        if y*y == x and y <= number and y >= first:
                                if i <= j:
                                        if coprime(i, j):
                                                for b, c in enumerate(order):
                                                        if c == y:
                                                                order[b] = str(i) + ', ' + str(j) + ', ' + str(y)
                                                                break
        if len(order) == 1:
                print("There is " + str(len(order)) + " primitive Pythagorean triple " + region + '.')
        else:
                print("There are " + str(len(order)) + " primitive Pythagorean triples " + region + '.')
        for a in order:
                print(a)
