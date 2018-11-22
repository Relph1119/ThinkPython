def check_fermat(a, b, c, n):
    if n>2 and a**n + b**n == c**n:
        print('天哪，费马弄错了！')
    else:
        print('不，那样不行！')

print('请输入a,b,c,n的值：')
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
n = int(input('n='))

check_fermat(a, b, c, n)
