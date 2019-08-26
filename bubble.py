class BubbleSort:
    def __init__(self):
        self.arr = [20,3,45,2,6,4,200,7,1]


    def bubble_sort(self):
        print("old array",self.arr)
        lent = len(self.arr) 
        for i in range(lent):
            # print(i)
            for k in range(1,lent-i):
                if self.arr[k] < self.arr[k -1]:
                    self.arr[k-1],self.arr[k] = self.arr[k],self.arr[k-1]
        print("new",self.arr)

# bb = BubbleSort()

# bb.bubble_sort()
