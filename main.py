import random
from operator import truediv
from turtledemo.penrose import start


def string_generator(n):
    global length_n_string
    if n == 0:
        if len(length_n_string) == 1:
            print(length_n_string)
        else:
            print(length_n_string.replace('ε', ''))
        return
    else:
        ok = 0
        for s in non_terminals:
            if s in length_n_string:
                ok = 1

        if ok == 0:
            if len(length_n_string) == 1:
                print(length_n_string)
            else:
                print(length_n_string.replace('ε', ''))
            return

        poz = 0
        for char in length_n_string:
            if char in non_terminals:
                chosen_production_rule = random.choice(production_rules[char])
                length_n_string = length_n_string[:poz] + chosen_production_rule + length_n_string[poz+1:]
                break
            poz += 1

        string_generator(n-1)

def derivation(target_string):
    global start_string
    if start_string.replace('S', '') == target_string:
        print(' -> ',start_string.replace('S', 'ε'), end='')
        print (' = ', target_string)
    else:
        poz = 0
        for char in start_string:
            if char in non_terminals:
                start_string = start_string[:poz] + production_rules[char][0] + start_string[poz+1:]
                break
            poz += 1
        print(' -> ', start_string, end = '')

        derivation(target_string)

def tester(target_string):
    cnt_a = 0
    ok = 0
    cnt_b = 0
    for char in target_string:
        if char not in terminals:
            return False
    for char in target_string:
        if char == 'a' and ok == 0:
            cnt_a += 1
        else:
            ok = 1
        if char == 'a' and ok == 1:
            return False
        if char == 'b':
            cnt_b += 1
    if cnt_a == cnt_b:
        return True
    return False





if __name__ == '__main__':

    #Define a CFG
    non_terminals = ['S']
    terminals = ['a', 'b', 'ε']
    start_symbol = 'S'
    production_rules = {'S':['aSb', 'ε']}

    #String generator

    for i in range(10):
        length_n_string = "S"
        string_generator(10)

    #Derivation
    print("Target string: ")
    target_string = input()
    start_string = "S"
    print(start_string, end = '')
    derivation(target_string)

    #Membership Tester

    print("Target string: ")
    target_string = input()
    print(tester(target_string))











