import sys
def count_steps_to_median(file1):
    data = []
    with open(file1) as f:
        for line in f:
            data.extend(map(float, line.split()))
    med = sorted(data)[len(data) // 2]
    res = 0
    for num in data:
        res += abs(num - med)
    if res <=20:
        print(int(res))
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу; ", res)

if len(sys.argv) != 2:
    print("<task4.py> <file> needed")
else:
    count_steps_to_median(sys.argv[1])