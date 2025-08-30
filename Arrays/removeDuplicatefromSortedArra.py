def removeDuplicates(nums) -> int:
            list1=[]
            for num in nums:
                if num  not in list1:
                   list1.append(num)
            
            return len(list1)



nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
