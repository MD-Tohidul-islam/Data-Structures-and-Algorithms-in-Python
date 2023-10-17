"""write code to partition a linked list around a value x,
 such that all nodes less than x come before all nodes greater than or equal to x
 """
from linked_list import LinkedList

def partion(ll,x):
    curnode = ll.head
    ll.tail = ll.head

    while curnode:
        nextnode = curnode.next
        curnode.next = None
        if curnode.value < x:
            curnode.next = ll.head
            ll.head = curnode
        else:
            ll.tail.next = curnode
            ll.tail = curnode
        curnode = nextnode
    if ll.tail.next is not None:
        ll.tail.next = None

customll = LinkedList()
customll.generate(10,0,99)
print(customll)
partion(customll,50)
print(customll)
