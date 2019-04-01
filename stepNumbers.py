import queue

def isStepNum(num):
    str_num = str(num)

    for i in range(len(str_num)-1):
        if abs(int(str_num[i]) - int(str_num[i+1])) != 1:
            return False
    return True

def isStepnum2(num):
    prev = num % 10
    num = int(num/10)
    while(num != 0):
        curr = num % 10
        if abs(curr - prev) != 1:
            return False
        prev = curr
        num = int(num/10)
    return True

def bfs_approach(m, n, num):
    q = queue.Queue()
    q.put(num)
    res = []
    while not q.empty():

        stepnum = q.get()
        if m <= stepnum and stepnum <= n:
            res.append(stepnum)
        if num == 0 or stepnum > n:
            continue

        last_digit = stepnum % 10
        stepnum_l = stepnum * 10 + last_digit - 1
        stepnum_r = stepnum * 10 + last_digit + 1

        if last_digit == 0:
            q.put(stepnum_l)
        elif last_digit == 9:
            q.put(stepnum_r)
        else:
            q.put(stepnum_l)
            q.put(stepnum_r)

    return res







m = 10
n = 30

for i in range(10):
    print(bfs_approach(m, n, i))

