def check(list1):
    change_inx_list = []
    prev = list1[0]
    change_inx_list.append(0)
    for i in range(len(list1)):
        if prev == list1[i]:
            continue
        else: # change happened
            # change_inx_list.append((i-1 + i)/2)
            change_inx_list.append(i)
            prev = list1[i]
    # change_inx_list.append((i + i+1)/2)
    change_inx_list.append(len(list1)+1)
    print(change_inx_list)
    prev = change_inx_list[0]
    change2 = []
    for i in range(1, len(change_inx_list)):
        change2.append(change_inx_list[i]-prev)
        prev = change_inx_list[i]
    print(change2)
    change3 = []
    for i in range(1, len(change2)):
        change3.append(min(change2[i], change2[i-1]))
    print(change3)
    change4 = []
    for i in range(1, len(change3)):
        if change3[i]
    print("-----------------")
    return 0

def read(list1):
    # no, list1 = inp.split("\n")
    list1 = [int(e) for e in list1.split(" ")] 
    return list1

t1 = """
2 2 2 1 1 2 2
"""

t2 = """
1 2 1 2 2 1 1
"""

check(read(t1))
check(read(t2))
