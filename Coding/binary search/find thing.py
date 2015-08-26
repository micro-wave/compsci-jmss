l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# assuming ordered list/
'''
length = len(l)
print(length)
print(length//2)
'''
'''
l[0]
>> a

l[0:3] <-- creates new list -- splitting list.
>> [a,b,c]b
'''
'''
middle = length//2

print("first index", middle)
print("smaller than index", middle//2)
print("bigger than index", middle + middle//2)
'''

def find_thing (thing, haystack):
    found = False
    length = len(haystack)
    middle = length//2
    print(haystack)
    while found == False:
        if len(haystack) == 1:
            found = True
            return "not found :("
        
        elif thing > haystack[middle]:
            haystack = haystack[middle:]
            length = len(haystack)
            middle = length//2
            print(haystack)
            
        elif thing < haystack[middle]:
            haystack = haystack[0:middle]
            length = len(haystack)
            middle = length//2
            print(haystack)
            
        elif thing == haystack[middle]:
            found = True
            return "found!"

print(find_thing(int(input("number: ")), l))
        

       

