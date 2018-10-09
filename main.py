def fact(n):
    if n == 0:
        return 1
    p = 1
    for i in range(1, n+1):
        p *= i
    return p

def calc_binom(n, k):
    return int(fact(n)/(fact(k)*fact(n-k)))

lines = 10

pascal_triangle = []
for i in range(lines):
    nums = []
    for j in range(i+1):
        nums.append(calc_binom(i, i-j))
    pascal_triangle.append(nums)

print(pascal_triangle)

longest_line = sum([len(str(x))+1 for x in pascal_triangle[-1]])+1

print("|{:^10d}|".format(12))