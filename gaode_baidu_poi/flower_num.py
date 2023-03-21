def flower():
	for num in range(100, 1000):
		low = num % 10
		mid = num // 10 % 10
		high = num // 100
		if num == low ** 3 + mid ** 3 + high ** 3:
			print(num)

def chicken():
	for x in range(0,20):
		for y in range(0,33):
			z = 100 - x - y
			if x * 5 + y * 3 == 100:
				print("%d大吉%d中级%d小鸡" % (x , y , z))

# def fibonci():
# 	for x in range(1,100):
# 		a += b
# 		b = a
# 		if a < 101:
# 			print(a)

# fibonci()

def fib(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n+1):
        prev, curr = curr, prev + curr
        if prev < 200:
	        print(prev)
# fib(7)


def print_fibonacci(n):
    prev, curr = 0, 1
    for _ in range(n):
        print(curr)
        prev, curr = curr, prev + curr

print_fibonacci(10)

def fib2(n):
	prev = 0
	curr = 1
	for _ in range(n):
		print(curr) # print before
		prev, curr = curr, prev + curr
fib2(4)

