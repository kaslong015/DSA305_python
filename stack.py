class Stack:
    def __init__(self,size):
        self.stack_list = []
        self.length = size 
    
    def add(self,value):
        
        """
         add value to the stack

        """
       
        if len(self.stack_list) == 10:
            return "stack is full "
        else:
            self.stack_list.append(value)


    def size(self):

        """
            get the size of the stack
        """
        return len(self.stack_list)


    def _pop(self,pos=-1):
        """
            remove and return the last element in the stack
        """
        #last element
        if len(self.stack_list) == 0:
            return "stack is empty"
        else:
            self.stack_list.pop(pos)
        # return self.stack_list[pos]


    def stack_max_size(self):
        """
        max size of data it can contain
        """
        return self.length


    def is_empty(self):
        """
        return is empty if the stack is zero
        """
        if len(self.stack_list) == 0:
            return "stack is empty"
        return len(self.stack_list)
       
         




