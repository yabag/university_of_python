garden = [input().split() for i in range(int(input()))]
total_of_flowers = [int(i[1]) for i in garden]

def divisors_of_number(n):
    list_divisors = [i for i in range(2, n) if n % i == 0]
    return list_divisors


