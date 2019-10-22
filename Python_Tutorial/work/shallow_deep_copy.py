import copy

old_list = [[1,2,3],[4,5,6],7,8,9]
new_list = copy.deepcopy(old_list)

old_list[1][0]="DB"


print("Old_list:",str( old_list))
print("New_list:",str(new_list))