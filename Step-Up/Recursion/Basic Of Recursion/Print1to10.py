def print_numbers_recursive(N):
    if N > 0:
        print_numbers_recursive(N - 1)
        print(N, end=' ')

N = 10
print_numbers_recursive(N)