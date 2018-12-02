def is_triangle(a, b, c):
    if a>b+c or b>a+c or c>a+b:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    print('请输入三角形的三条边长度：')
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    is_triangle(a, b, c)
