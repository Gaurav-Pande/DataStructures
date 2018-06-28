# Author: Gaurav Pande
# [Strings: Making Anagrams](https://www.hackerrank.com/challenges/ctci-making-anagrams/problem)

def number_needed(a, b):
    res = 0
    freq_dict_a = {}
    freq_dict_b = {}
    for elem in b:
        freq_dict_b[elem] = b.count(elem)
        
    
    for elem in a:
        freq_dict_a[elem] = a.count(elem)
        
        
                    
    if len(a) > len(b):
        for k,v in freq_dict_b.items():
            if k in freq_dict_a:
                if v >= freq_dict_a[k]:
                    res = res + freq_dict_a[k]
                else:
                    res = res + v
            else:
                continue
                
    else:
        for k,v in freq_dict_a.items():
            if k in freq_dict_b:
                if v >= freq_dict_b[k]:
                    res = res + freq_dict_b[k]
                else:
                    res = res + v
            else:
                continue
    
            
                    
    return abs(len(a) + len(b) - 2*res)
        
        

a = input().strip()
b = input().strip()

print(number_needed(a, b))
