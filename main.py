####################################
#								   #
# ALGORITHMS AND DATA STRUCTURES   #
#								   #
####################################



from termcolor import colored
from queue_ import Queue
from linear import Array
from stack import Stack
from bubble import BubbleSort
from linked_list import LinkedList
from binary_search import BinarySearch
from bubble import BubbleSort
from selection import SelectionSort
from binary_tree import BinaryTree

# all objects of the classes
larr = Array()
stk = Stack(10)
quez = Queue()
llist = LinkedList()
binary = BinarySearch()
bubble = BubbleSort()
selection = SelectionSort()
bitree = BinaryTree()

def main_menu():
    print("\v")
    text = colored(' ALGORITHMS AND DATA STRUCTURES ','magenta','on_cyan',['blink'])
    print("\t\t\t\t",text)
    print("\v")

    AL = {
        1:"Array",2:"stacks",3:"Queue",4:"Linked list",5:"Binary trees",
        6:"binary Search",7:"BubbleSort",8:"insertion sort",9:"selection sort"}
    for k,v in AL.items():
        print("{} {}".format(k,v))
    print("")
main_menu()


def arr_display():
    print("1 : insert\n2 : delete\n0 : main menu\n")


def stack_display():
    print("1 : add\n2 : remove\n0 : main menu\n")

def queue_display():
    print("1 : add\n2 : remove\n0 : main menu\n")

def _Linklist_display():
    print("1 : append\n2 : between\n3 : prepend\n4 : delete\n0 : main menu\n")
# _Linklist_display()

def control():
    command = int(input("-> "))

    if command == 1:
        while True:
            arr_display()
            sha = int(input("-> "))
            if sha == 1:

                a = int(input("enter index: "))
                b = int(input("enter Item: "))
                larr.insert_value(a,b)

            elif sha == 2:

                a = int(input("enter index to delete: "))
                larr.delete(a)
            else:
                main_menu()
                break
        control()

    elif command == 2:
        while True:
            stack_display()
            sha = int(input("->"))
            if sha == 1:
                a = int(input("enter item :"))
                stk.add(a)
                print(stk.stack_list[::-1])
            elif sha == 2:
                stk._pop()
                print(stk.stack_list[::-1])
            else:
                main_menu()
                break
        control()

    elif command == 3:
        while True:
            queue_display()
            sha = int(input("->"))
            if sha == 1:
                a = int(input("enter item :"))
                quez.dequeue(a)
                print(quez.que[:])
            elif sha == 2:
                quez.enqueue()
                print(quez.que[:])
            else:
                main_menu()
                break
        control()


    elif command == 4:
        while True:
            _Linklist_display()
            sha = int(input("->"))
            if sha == 1:
                a = int(input("enter item :"))
                llist.append(a)
                llist.print_list()
            elif sha == 2:
                a = int(input("enter item :"))
                
                llist.insert_after_node(llist.head.next,a)
                llist.print_list()
            elif sha == 3:
                a = int(input("enter item :"))
                llist.prepend(a)
                llist.print_list()
            elif sha == 4:
                a = int(input("enter item :"))
                llist.delete_node(a)
                llist.print_list()            
            else:
                main_menu()
                break
    elif command == 5:
        while True:
            bitree.build_tree()
            a = int(input("enter 0 to go back to main menu"))
            if a == 0:
                main_menu()
                break
        control()
    elif command == 6:
        while True:                       
            user_input = input('Enter numbers separated by comma:\n').strip()
            sorted_collection = [int(item) for item in user_input.split(',')]
            cin = int(input("enter Item to find: "))
            res=binary.bubble_sort(sorted_collection)
            print(binary.binary_search(res,cin))
            a = int(input("enter 0 to get to main :"))
            if a == 0:
                main_menu()
                break    
        control()
    elif command == 7:
        # while True:
        bubble.bubble_sort()           
        main_menu()                
        control()
    elif command == 8:
        main_menu()
        control()
    elif command == 9:
        user_input = input('Enter numbers separated by a comma:\n').strip()
        unsorted = [int(item) for item in user_input.split(',')]
        print(selection.selection_sort(unsorted))
        main_menu()
        control()
    else:
        exit()
#     unsorted = [int(item) for item in user_input.split(',')]
#     print(selection_sort(unsorted))


control()


