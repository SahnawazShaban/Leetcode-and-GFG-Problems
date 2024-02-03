print("Recursion")

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# 0 1 1 2 3 5
n = 5
print(fibonacci(n))

# Time Complexity: O(2^n)
# Space Complexity: O(n)

# In detail:
'''
Time Complexity:
The time complexity of the recursive Fibonacci function is exponential, 
specifically O(2^n). This is because, for each call, the function makes 
two recursive calls (fibonacci(n-1) and fibonacci(n-2)), leading to an 
exponential growth in the number of function calls.

Space Complexity:
The space complexity of the recursive Fibonacci function is O(n) due to 
the depth of the recursion stack. In the worst case, the recursion stack 
could grow to a depth of n, where n is the input to the Fibonacci function.
'''

# -------------------------------------------------

# Memoization Method: Top-down approach
print("Memoization Method")

def fibonacci(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibonacci(n - 1, dp) + fibonacci(n - 2, dp)

    return dp[n]


n = 5
dp = [-1] * (n + 1)
print(fibonacci(n, dp))

# Time Complexity: O(n)
# Space Complexity: O(n)[recursion stack space] + O(n)[array] = O(n)

# In detail:
'''
Time Complexity:
The time complexity of this optimized Fibonacci function is O(n). This is because 
each Fibonacci number is calculated only once, and the results are stored in the 
memoization table. Therefore, there are n calculations in total.

Space Complexity:
The space complexity is O(n) as well. This is due to the memoization table (dp) 
that is used to store the results of intermediate Fibonacci numbers. The size of 
the memoization table is proportional to the input value n.
'''

# -----------------------------------

# Tabulation Method: Bottom-up approach
print("Tabulation Method")

def fibonacci(n):
    if n <= 1:
        return n

    dp = [-1] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n])


n = 5
fibonacci(n)

# Time Complexity: O(n) [running a simple iterative loop]
# Space Complexity: O(n+1) [external size of array]

# In detail
'''
Time Complexity:
The time complexity of this tabulation-based implementation is O(n). The loop iterates 
from 2 to n, and at each iteration, a constant amount of work is done to update the dp 
array. Therefore, the overall time complexity is linear with respect to the input size n.

Space Complexity:
The space complexity is O(n). The dp array of size n + 1 is used to store the intermediate 
results of the Fibonacci sequence. As n grows, the space required for the array also grows 
linearly.
'''

'''
1. Space Efficiency:
Tabulation: The tabulation approach typically uses less memory since it only stores the 
necessary intermediate results in an array (dp array in this case). It avoids the 
overhead of recursive function calls and only keeps the values needed to compute the 
final result.

Memoization: Memoization uses a recursive call stack and a memoization table to store 
intermediate results. In some cases, this can lead to a higher memory overhead due to 
the recursive function calls.

2. No Recursion Overhead:
Tabulation: The tabulation approach uses a loop to iteratively fill in the DP array. 
It doesn't involve recursive calls, avoiding the overhead associated with function calls.

Memoization: The memoization approach involves recursive function calls, which can 
result in a deeper call stack and potentially higher overhead.

3. Better for Bottom-Up Approaches:
Tabulation: Tabulation is a bottom-up approach where you solve the smaller subproblems 
first and build up to the larger problem. This is more natural with tabulation and fits 
well with iterative solutions.

Memoization: Memoization is a top-down approach where you start with the original 
problem and break it down into smaller subproblems. While it's effective, it may 
not be as intuitive for certain problems, and it relies heavily on the call stack.

4. Readability and Simplicity:
Tabulation: Tabulation often leads to more straightforward and readable code, 
especially for problems that naturally fit into a bottom-up approach.

Memoization: While memoization can be elegant, it sometimes involves additional 
complexities related to recursive calls and maintaining a memoization table.
'''

# -----------------------------------

# Space Optimization
print("Space Optimization")

# dp[i-1] as prev
# dp[i-2] as prev2

# step1: prev2 *(0)     prev *(1)      cur *(1)
# step2:                prev2 *(1)     prev *(1)      cur *(2)
# step3:                               prev2 *(1)     prev *(2)      cur *(3) ....... so on

def fibonacci(n):
    prev2 = 0
    prev = 1

    for i in range(2, n+1):
        cur = prev2 + prev
        prev2 = prev
        prev = cur

    print(prev)


print(fibonacci(5))

# Time Complexity: O(n) [iterative loop]
# Space Complexity: O(1) [not using any extra space]


# In detail
'''
Time Complexity:
The time complexity of this implementation is O(n). The loop iterates from 2 to n, 
performing a constant amount of work in each iteration. The number of iterations 
directly depends on the input size n.

Space Complexity:
The space complexity is O(1) or constant space. This is because only three variables 
(prev2, prev, and cur) are used to store intermediate values, and the amount of memory 
required does not grow with the input size.
'''

'''
1. Space Efficiency:
Tabulation: The tabulation approach typically uses less memory since it only stores 
the necessary intermediate results in an array (dp array in this case). It avoids 
the overhead of recursive function calls and only keeps the values needed to compute 
the final result.

Memoization: Memoization uses a recursive call stack and a memoization table to store 
intermediate results. In some cases, this can lead to a higher memory overhead due to 
the recursive function calls.

2. No Recursion Overhead:
Tabulation: The tabulation approach uses a loop to iteratively fill in the DP array. 
It doesn't involve recursive calls, avoiding the overhead associated with function calls.

Memoization: The memoization approach involves recursive function calls, which can 
result in a deeper call stack and potentially higher overhead.

3. Better for Bottom-Up Approaches:
Tabulation: Tabulation is a bottom-up approach where you solve the smaller subproblems 
first and build up to the larger problem. This is more natural with tabulation and fits 
well with iterative solutions.

Memoization: Memoization is a top-down approach where you start with the original 
problem and break it down into smaller subproblems. While it's effective, it may not 
be as intuitive for certain problems, and it relies heavily on the call stack.

4. Readability and Simplicity:
Tabulation: Tabulation often leads to more straightforward and readable code, especially 
for problems that naturally fit into a bottom-up approach.

Memoization: While memoization can be elegant, it sometimes involves additional 
complexities related to recursive calls and maintaining a memoization table.
'''

# **************************************************************

# Implementations for printing the Fibonacci series using different approaches: 
# recursion, memoization, tabulation, and space optimization.

# 1. Recursion:

def fibonacci_recursion(n):
    if n <= 1:
        return n
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def print_fibonacci_recursion(limit):
    for i in range(limit):
        print(fibonacci_recursion(i), end=' ')

# Example usage for recursion
print_fibonacci_recursion(10)

# -----------------------------

# 2. Memoization:

def fibonacci_memoization(n, memo):
    if n <= 1:
        return n
    if memo[n] == -1:
        memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]

def print_fibonacci_memoization(limit):
    memo = [-1] * (limit + 1)
    for i in range(limit):
        print(fibonacci_memoization(i, memo), end=' ')

# Example usage for memoization
print_fibonacci_memoization(10)

# ---------------------------------

# 3. Tabulation:

def fibonacci_tabulation(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp

def print_fibonacci_tabulation(limit):
    result = fibonacci_tabulation(limit)
    for num in result:
        print(num, end=' ')

# Example usage for tabulation
print_fibonacci_tabulation(10)

# ---------------------------------

# 4. Space Optimization:

def print_fibonacci_space_optimization(limit):
    prev2, prev = 0, 1

    while prev <= limit:
        print(prev, end=' ')
        cur = prev2 + prev
        prev2 = prev
        prev = cur

# Example usage for space optimization
print_fibonacci_space_optimization(50)
