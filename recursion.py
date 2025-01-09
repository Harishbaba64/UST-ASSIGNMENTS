def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

base = 2
exponent = 3
print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")


def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
