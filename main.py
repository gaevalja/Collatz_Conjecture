import matplotlib.pyplot as plt

def repeat(result, start_num):
    cnt = 0
    current_num = start_num
    while(True):
        if current_num == 1:
            print('finally done!', cnt)
            break
        elif current_num % 2 == 0:
            current_num /= 2
            cnt += 1
            result.append(current_num)
        else:
            current_num = current_num + current_num + current_num + 1
            cnt += 1
            result.append(current_num)
    return cnt, result

# environmental variables
start_num = int(input('start number : '))
result = list()
cnt, result = repeat(result, start_num)



max =max(result)
print('max :', max)

plt.plot(result)
plt.show()