def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

if __name__ == '__main__':
    recurse(3, 0)