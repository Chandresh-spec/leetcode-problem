class SortingAlog:
    def __init__(self,arr):
        self.arr=arr
    


    def bubble_sort(self):
        n=len(self.arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j],self.arr[j+1]=self.arr[j+1],self.arr[j]


        return self.arr


    def selection_sort(self):
        n=len(self.arr)
        for i in range(n):
            mini=i
            for j in range(i+1,n):
                if self.arr[mini] > self.arr[j]:
                    mini=j

            self.arr[mini],self.arr[i]=self.arr[i],self.arr[mini]

        return self.arr


    def insertion_sort(self):
        n=len(self.arr)

        for i in range(1,n):
            current=i
            j=i-1

            while j >= 0 and self.arr[current] < self.arr[j]:
                self.arr[j],self.arr[current]=self.arr[current],self.arr[j]
                j-=1
                current-=1



        return self.arr





algo=SortingAlog([1,1,2,5,2])
print(algo.bubble_sort())


selection_algo=SortingAlog([])
print(selection_algo.selection_sort())


insertion_algo=SortingAlog([1])
print(insertion_algo.insertion_sort())