def cumulative(lists):
    #cu_list = []
    length =  len(lists)
    cu_list = [sum(lists[0 +1 ]) for x in range (0,length)]
    return cu_list

lists = [10,20,30,40,50]
print(cumulative(lists))