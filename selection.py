class SelectionSort:
    def __init__(self):
        pass

    def selection_sort(self,collection): 
        #get the len 
        length = len(collection)
        #from values in range of len - 1 to access index
        for i in range(length - 1):
            #assume that the 1st index is the least
            least = i
            # print("i={} and least{}".format(i,least))
            for k in range(i + 1, length):
                if collection[k] < collection[least]:
                    least = k
            collection[least], collection[i] = (
                collection[i], collection[least]
            )
        return collection