# line()
# Build the line() function that shows everyone their current place in the line. 
# If there is nobody in line, it should say "The line is currently empty.".
katz_deli = []
def line(l):
    if len(l) == 0:
        print('The line is currently empty.')
    else:
        message1= 'The line is currently: '
        message2= ''.join([f'{l.index(name)+1}. {name} ' for name in l])
        join = message1 + message2
        print(join)
def take_a_number(l, name):
    l.append(name)
    print(f'Welcome, {name}. You are number {l.index(name)+ 1} in line.')


def now_serving(l):
    print(f'Currently serving {l[0]}.')
    del l[0]
    if len(l) == 0:
        print("There is nobody waiting to be served!")

take_a_number(katz_deli, "Ada")
take_a_number(katz_deli, "Grace")
take_a_number(katz_deli, "Kent")
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)
take_a_number(katz_deli, "Matz")
line(katz_deli)
now_serving(katz_deli)

line(katz_deli)


# now_serving()
# Build the now_serving() function which should call out (print) the next person in line 
# and then remove them from the front. If there is nobody in line, it should call 
# out (print) that "There is nobody waiting to be served!".
