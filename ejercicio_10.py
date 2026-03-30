def sum(n):
    if n < 10:
        return 1
    return 1 + sum(n//10)

num=111111
print(sum(num))
    