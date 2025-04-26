 #sum
#function to sum all elements in a list

def sum_list(elements):
    totalsum = 0
    for num in elements:
        totalsum +=num
    return totalsum

#example sum
list_1=[12,34,54,23,67]
result = sum_list(list_1)
print("Sum:",result)