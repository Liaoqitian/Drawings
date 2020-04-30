var = input('')
♥
lst = []
for y in range(12, -12, -1):
    sublst = []
    res = ''
    for x in range(-35, 35):
        formula = math.pow((math.pow((x * 0.05), 2) + math.pow((y * 0.1), 2) - 1), 3) - math.pow((x * 0.05), 2) * math.pow((y * 0.1), 3)
        if formula <= 0:
            res += var[0]
        else:
            res += ' '
    sublst.append(res)
    lst += sublst

print('\n'.join(lst))