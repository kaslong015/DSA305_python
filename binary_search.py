class BinarySearch:
    def __init__(self):
        # self.collection = []
        pass


    def bubble_sort(self,arr):
        lent = len(arr) 
        for i in range(lent):
            # print(i)
            for k in range(1,lent-i):
                if arr[k] < arr[k -1]:
                    arr[k-1],arr[k] = arr[k],arr[k-1]
        return arr
        

    def binary_search(self,sorted_collection, item):

        # sorted_collection = [int(item) for item in sorted_collection.split(',')]
        # sorted_collection = bubble_sort(sorted_collection)   
        left = 0
        right = len(sorted_collection) - 1

        while left <= right:
            midpoint = (left + right) // 2
            current_item = sorted_collection[midpoint]
            if current_item == item:
                return midpoint
            else:
                if item < current_item:
                    right = midpoint - 1
                else:
                    left = midpoint + 1
        return None

# b1=BinarySearch()
# user_input = input('Enter numbers separated by comma:\n').strip()
# sorted_collection = [int(item) for item in user_input.split(',')]
# res=b1.bubble_sort(sorted_collection)

# print(b1.binary_search(res,10))