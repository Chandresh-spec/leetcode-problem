# def two_sum(nums, target):
#     seen = {}
    
#     for i in range(len(nums)):
#         complement = target - nums[i]
        
#         if complement in seen:
#             return [seen[complement], i]
        
#         seen[nums[i]] = i
    
#     return []



# nums = [2,7,11,15]
# target = 9

# print(two_sum(nums,target))



# def remove_duplicates(nums):
#     k = 0
    
#     for i in range(1, len(nums)):
#         if nums[i] != nums[k]:
#             k += 1
#             nums[k],nums[i] = nums[i],nums[k]
            
    
#     return nums[:k+1]


# nums=[1,1,2,2,3]
# print(remove_duplicates(nums))



# def reverse_words(s):
#     words = s.split(" ")
#     result = []
    
#     for i in range(len(words)):
#         result.append(words[i])   
    
    
#     return " ".join(result[::-1])



# s="hello world python"
# print(reverse_words(s))



# def is_valid(s):
#     stack = []
    
#     for c in s:
#         if c in "({[":
#             stack.append(c)
#         else:
#             if not stack:
#                 return False
            
#             top = stack.pop()
            
#             if not (
#                (top == "(" and c == ")") or 
#                (top == "[" and c == "]") or 
#                (top == "{" and c == "}")):
#                 return False

    
#     return len(stack)==0


# s="([])"

# print(is_valid(s))




# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None


# def reverse(head):
#     prev = None
#     curr = head
    
#     while curr:
#         next_node=curr.next
#         curr.next = prev
#         prev = curr
#         curr = next_node
    
#     return prev




# def hasCycle(head):
#     slow = head
#     fast = head
    
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
        
#         if slow == fast:
#             return True
    
#     return False


# def insert(temp,stack):
#     if not stack or stack[-1]<=temp:
#         stack.append(temp)
#         return
    
#     ele=stack.pop()
#     insert(temp,stack)
#     stack.append(ele)


# def sort_stack(stack):
#     if stack:
#         temp=stack.pop()
#         sort_stack(stack)
#         insert(temp,stack)




# stack=[2,3,1,4]
# print(sort_stack(stack))
# print(stack)



def insert(stack,temp):
    if not stack:
        stack.append(temp)
        return
    
    ch=stack.pop()
    insert(stack,temp)
    stack.append(ch)



def reverse_stack(stack):
    if stack:
        temp=stack.pop()
        reverse_stack(stack)
        insert(stack,temp)

    



stack = [10, 20, -5, 7, 15]
print(reverse_stack(stack))
print(stack)