n = int(input())
res = 0
iterat = 2
while n > 1:
    if n % iterat == 0:
        res += iterat
        while n % iterat == 0:
            n /= iterat
    iterat += 1
print(res)
