import math

def out_attribute(compass):
    attr = compass[0].copy()

    for i in range(1, len(compass)):
        for j in range(0, len(compass[i])):
            attr[j] += compass[i][j]

    return attr

def entropy_calculator(var):
    total = 0
    temp = sum(var)
    for x in var:
        if x > 0:
            total += (x/temp)*(-math.log(x/temp, 2))
    return total


def conditional_entropy(compass):

    total_sum = 0
    total_prob = 0

    for val in compass:
        total_prob += sum(val)

    for val in compass:
        prob = sum(val)/total_prob
        total_sum += prob * entropy_calculator(val)

    return total_sum



def conditional_entropy_specific(compass, i):
    return entropy_calculator(compass[i])


def information_gain(compass):
    return entropy_calculator(out_attribute(compass)) - conditional_entropy(compass)


m = 2
n = 2

m = int(input("m: (numar de valori ale etichetei)"))
n = int(input("n: (numar de valori posibile ale atributului)"))
compass = list(list())


for i in range(n):
    line = list()
    for j in range(m):
        line.append(int(input()))
    compass.append(line)

print("Entropia atributului de iesire:")
print(entropy_calculator(out_attribute(compass)))

print()

print("Entropiile conditionale specifice fiecarui descendent:")
for val in compass:
    print(conditional_entropy_specific(compass, compass.index(val)))

print()

print("Entropia conditionata medie")
print(conditional_entropy(compass))

print()

print("Castigul de informatie")
print(information_gain(compass))
