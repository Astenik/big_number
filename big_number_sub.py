def big_number_sub(big1: str, big2: str):
        q1 = len(big1) % 3
        q2 = len(big2) % 3
        lst1 = []
        lst2 = []
        lst1.append(big1[:q1])
        lst2.append(big2[:q2])
        i = q1
        while i < len(big1):
           count = 3
           num = []
           while (count > 0) and (i < len(big1)):
              num.append(int(big1[i]))
              count -= 1
              i += 1
           lst1.append(num)
        ii = q2
        while ii < len(big2):
           count = 3
           num = []
           while (count > 0) and (ii < len(big2)):
              num.append(int(big2[ii]))
              count -= 1 
              ii += 1
           lst2.append(num)
        if len(lst1) >= len(lst2):
            res = []
            for j in range(len(lst2) - 1, -1, -1):
                  for jj in range(len(lst2[j]) - 1, -1, -1):
                    if int(lst1[j][jj]) >= int(lst2[j][jj]):
                         sub = int(lst1[j][jj]) - int(lst2[j][jj])
                    else:
                        if jj != 0:
                             lst1[j][jj - 1] = int(lst1[j][jj - 1]) - 1 
                        else:
                            lst1[j - 1][-1] = int(lst1[j - 1][-1]) - 1
                        lst1[j][jj] = int(lst1[j][jj]) + 10
                        sub = int(lst1[j][jj]) - int(lst2[j][jj])
                    res.append(sub)
            if len(lst1) != len(lst2):
                 length = len(lst1) - len(lst2)
                 for k in range(length, -1, -1):
                      for kk in range(len(lst1[k]) -1, -1, -1):
                           res.append(lst1[k][kk])
            sign = '+'
        else:
            res = []
            for j in range(len(lst1) - 1, -1, -1):
                  for jj in range(len(lst1[j]) - 1, -1, -1):
                    if int(lst2[j][jj]) >= int(lst1[j][jj]):
                         sub = int(lst2[j][jj]) - int(lst1[j][jj])
                    else:
                        if jj != 0:
                             lst2[j][jj - 1] = int(lst2[j][jj - 1]) - 1 
                        else:
                            lst2[j - 1][-1] = int(lst2[j - 1][-1]) - 1
                        lst2[j][jj] = int(lst2[j][jj]) + 10
                        sub = int(lst2[j][jj]) - int(lst2[j][jj])
                    res.append(sub)
            sign = '-'
        ij = 0
        new_res = []
        while ij < len(res):
           count = 3
           num = []
           while (count > 0) and (ij < len(res)):
                num.append(res[ij])
                ij += 1
                count -= 1
           num = num[::-1]
           new_res.append(num)
        res = new_res[::-1]
        return res if sign == '+' else - res
num1 = 2**33
num2 = 2**30 
print(big_number_sub(f'{num1}', f'{num2}'))
