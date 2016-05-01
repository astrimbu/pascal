''' Define a function that returns n lines of Pascal's Triangle '''

def pascal(n):
    if n == 0: return [1]
    if n == 1: return [1,1]
    prev_line = pascal(n-1)
    cur_line = []
    for i in range(n+1):
        if i == 0: cur_line.append(1) 
        elif i == n: cur_line.append(1)
        else:
            cur_num = prev_line[i-1] + prev_line[i]
            cur_line.append(cur_num)
    return cur_line 

if __name__ == '__main__':
    for i in range(15):
        print pascal(i)
