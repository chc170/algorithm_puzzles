def answer(n, b):
    
    bag = {}
    k = len(n)
    
    count = 0
    curr = n
    
    while curr not in bag:
        bag[curr] = count
        count += 1
        
        x = sorted(curr, reverse=True)
        y = sorted(curr)
        
        x_val = to_val(x, b, k)
        y_val = to_val(y, b, k)
        
        z_val = x_val - y_val
        z = to_str(z_val, b, k)
        
        curr = z
    return count - bag[curr]
        
def to_val(s, b, k):
    """
    """
    print('In: {}, {}'.format(s, b))
    val = 0
    d = 1
    for i in range(k-1, -1, -1):
        val += d * int(s[i])
        d *= b
    print('Out: {}'.format(val))
    return val
    
def to_str(val, b, k):
    """
    """
    print('To str In: {}, {}'.format(val, b))
    output = ''
    for _ in range(k):
        d = val % b
        val = val // b
        output = str(d) + output
    print('Out: {}'.format(output))
    return output


if __name__=='__main__':
    print(answer('1211', 10))
    print(answer('210022', 3))