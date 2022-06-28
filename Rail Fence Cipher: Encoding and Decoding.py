def encode_rail_fence_cipher(string, n):
    lst = [[] for i in range(0, n)]
    count = 0
    tic=True
    for i in range(0, len(string)):
        lst[count].append(string[i])
        if count==n-1:
            tic=False
        if tic == True:
            count+=1
        else:
            count-=1
        if count==0:
            tic =True
    lst = [j for i in lst for j in i]
    result = ''.join(lst)
    return result

def decode_rail_fence_cipher(string, n):
    print(string, n)
    lst = [[] for i in range(0, n)]
    count = 0
    tic=True
    for i in range(0, len(string)):
        lst[count].append(string[i])
        if count==n-1:
            tic=False
        if tic == True:
            count+=1
        else:
            count-=1
        if count==0:
            tic =True
    count = 0
    for i in range(0, len(lst)):
        for k in range(0, len(lst[i])):
            lst[i][k] = string[count]
            count+=1
    lst_res=[]
    print(lst)
    count=0
    tic=True
    for zz in range(0, len(string)):
        lst_res.append(lst[count][0])
        lst[count].pop(0)
        if count==n-1:
            tic=False
        if tic == True:
            count+=1
        else:
            count-=1
        if count==0:
            tic =True
    result = ''.join(lst_res)
    return result
