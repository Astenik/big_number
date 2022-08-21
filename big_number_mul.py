'''To use this functio you will use also the big_number_sum function that is
the another file in this repository, and use join functon that is exist
in my repos.'''
def big_number_mul(big1: str, big2: str):
       rem = 0
       res = []
       for i in range(len(big2) - 1, -1, -1):
           num = []
           for ii in range(len(big1) - 1, -1, -1):
                mul = int(big2[i]) * int(big1[ii]) + rem
                mul  %=  10
                rem = mul // 10 
                num.append(mul)
           res.append(num[::-1]) 
       new_res = []
       for num in res:
           str_number = join(f'{num}', '')
           new_res.append(str_number)
       _sum_ = 0
       for number in new_res:
              _sum_ += big_number_sum(f'{number}', f'{_sum_}')
       return _sum_
print(big_number_mul('1323', '89236'))
