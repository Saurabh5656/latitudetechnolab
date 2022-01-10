def function(lst):
    l = len(lst)
    for i in range(0,l):
        if (lst[i]==0):
            lst.remove(lst[i])
            lst.append(0)
    print((lst))


num_list1 = [12,0,16,0,0,0,20,70]
num_list2 = [90,0,20,0,0,80,10,0]

function(num_list1)
function(num_list2)