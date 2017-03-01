import math

import math

def answer(n):
    # check inputs
    if n < 0 or n > 10000 or type(n) != int:
        print ("Raise exception")
        return
        
    # edge case
    prime_str_map = {
        0 : '23571',
        1 : '35711'
    }
    result = prime_str_map.get(n, '')
    if result:
        return result
        
    # run algorithm
    current_num = 4
    #prime_count = 2
    prime_idx_count = 1
    while len(result) < 5:
        # skip multiples of 2 and 3
        if current_num % 2 != 0 and current_num % 3 != 0:
            sqrt = math.sqrt(current_num)
            tmp = 4
            # check all numbers between 4 and sqrt(N)
            while tmp <= sqrt and (current_num % tmp) != 0:
                tmp += 1
            if tmp > sqrt:
                # prime found
                num_str = str(current_num)
                prev_idx_count = prime_idx_count
                prime_idx_count += len(num_str)

                if prime_idx_count >= n:
                    #start = min(0, len(num_str)-1-(prime_idx_count-n))
                    start = max(n - prev_idx_count - 1, 0)
                    result += num_str[start:]
                #prime_count += 1
                # n starts from 0
                #if prime_count >= (n+1):
                #    result += str(current_num)
        current_num += 1
    return result[:5]

if __name__=='__main__':
    # 2357111317192329
    print('{} == {}'.format(answer(3), 71113))
    print('{} == {}'.format(answer(4), 11131))
    print('{} == {}'.format(answer(7), 31719))
