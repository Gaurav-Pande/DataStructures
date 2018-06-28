# Author: Gaurav Pande
def ransom_note(magazine, ransom):
    from collections import Counter
    result = True
    dict_magazine = {}
    dict_ransom = {}
    # Create a dictionary/hash table for each params
    # Note if you count an element in a list or a string using count method than it is slow
    # Instead use Counter methos which is fast by a factor of 2
    
    #for elem in magazine:
    #    dict_magazine[elem] = magazine.count(elem)
    #for elem in ransom:
    #    dict_ransom[elem] = ransom.count(elem)
    
    
    dict_magazine =  Counter(magazine)
    dict_ransom = Counter(ransom)
    
    
    # Now we parse each dictionary and matches the key,value
    for k,v in dict_ransom.items():
        if k not in dict_magazine:
            result = False
            break
        else:
            if dict_magazine[k] >= dict_ransom[k]:
                continue
            else:
                result = False
                break
            result = True
    return result
            
            
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
