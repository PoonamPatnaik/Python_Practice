# n = 5
# for i in range(1,5):
#     print("* " *i)
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)


# n = 5
# for i in range(1, n + 1):
#     print("* " *n)
#     n -= 1

# n = 5
# for i in range (1, n+1):
#     print(" " *(n-i) + "* " *i)

n = 4
num = 1
for i in range (1, n+1):
    for j in range (1, i+1):
        print(num, end=" ")
        num += 1
    print()
