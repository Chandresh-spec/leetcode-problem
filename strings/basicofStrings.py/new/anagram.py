#  if len(s)!=len(t):
#             return False
        
#         hashmap={}
#         for item in s:
#             hashmap[item]=hashmap.get(item,0)+1
        
#         for item in t:
#             if item in hashmap:
#                 hashmap[item]=hashmap.get(item,0)-1
            
        
#         for value,count in hashmap.items():
#             if count>=1:
#                 return False
            
        
#         return True