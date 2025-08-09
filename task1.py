import sys
def find_path(n1, m1, n2, m2):
    current1 = (1 + m1 - 2) % n1 + 1
    current2 = (1 + m2 - 2) % n2 + 1
    res1, res2 = [1], [1]
    while True:         
        if current1 != 1:
            res1.append(current1)
            current1 = (current1 + m1 - 2) % n1 + 1  
        if current2 != 1:
            res2.append(current2)
            current2 = (current2 + m2 - 2) % n2 + 1
        if current1 == 1 and current2 == 1:
            break
    return res1, res2  

if len(sys.argv) != 5:
    print("task1.py n1 m1 n2 m2")
    sys.exit(1)
n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])
result1, result2 = find_path(n1, m1, n2, m2)
print(''.join(map(str, result1)) + ''.join(map(str, result2)))