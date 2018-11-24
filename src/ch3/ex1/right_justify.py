def right_justify(s):
    length = 70 - len(s)
    print(length * ' ' + s)

if __name__ == '__main__':
    right_justify('monty')