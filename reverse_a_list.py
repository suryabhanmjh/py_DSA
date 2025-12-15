# 1 - arrange list in assending order
# 2 - arrange list in dessending order
# 3 - Move zero end of the list
# 4 - Anagram check
# ex:- st1 = madam   st2= adam   not anagram
# ex:- st1 = madam   st2= adamm  anagram


# find max value element in the list 
li = [3,19,7,4,8,10,34]
second_largest=0
largest = li[0]
for i in li:
    if i>largest:
        second_largest = largest
        largest=i
    if i>second_largest and i<largest:
        second_largest=i
print(second_largest) 