# def findunion(nums1,nums2):
    # st=set()
    # for num in nums1:
        # st.add(num)
    # 
    # for num in nums2:
        # st.add(num)
# 
    # arr=list(st)
    # arr.sort()
    # return arr



def findunion(nums1,nums2):
    i=0
    j=0
    lst=[]
    while i<= len(nums1)-1 or j<= len(nums2)-1 :
        if nums1[i] < nums2[j]:
            if nums1[i] not in lst:
                lst.append(nums1[i])
            i+=1
        else:
            if nums2[j] not in lst:
                lst.append(nums2[j])
            j+=1
    return lst

nums1=[3, 4, 6, 7, 9, 9]
nums2= [1, 5, 7, 8, 8]
print(findunion(nums1,nums2))