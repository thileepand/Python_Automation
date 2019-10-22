def remove_duplication(x):
    return list(dict.fromkeys(x))
my_list = remove_duplication([1,2,3,4,5,6,4,3])
print(my_list)

# def Remove(duplicate):
#     final_list = []
#     for num in duplicate:
#         if num not in final_list:
#             final_list.append(num)
#             return final_list
#
# duplicate = [1,2,3,4,5,6,7,5,45,43,3,1]
# print(Remove(duplicate))