# super-exponential
def power_tower(n, depth):
    if depth == 1:
        return n
    return n ** power_tower(n, depth - 1)


result = power_tower(2, 4)
print("power_tower(2, 4):", result)
