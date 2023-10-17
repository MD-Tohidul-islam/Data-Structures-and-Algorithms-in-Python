"""Given two(singly) linked lists, determine if the two lists interest,
Return the intersecting node. Note that the intersection is defined  based on reference, not value.
that is , if the kth node jof the first linked list is the exact same node (by reference) as the jth node oth second linked
list, then they are intersecting
"""

from linked_list import LinkedList, Node

def intersection(lla, llb):
    if lla.tail is not llb.tail:
        return False
    lena = len(lla)
    lenb = len(llb)

    shorter = lla if lena < lenb else llb
    longer = llb if lena < lenb else lla

    diff = len(longer) - len(shorter)
    longernode = longer.head
    shorternode = shorter.head

    for i in range(diff):
        longernode = longernode.next

    while shorternode is not longernode:
        shorternode = shorternode.next
        longernode = longernode.next

    return longernode

# helper addition method
def addsamenode(lla, llb, value):
    tempnode = Node(value)
    lla.tail.next = tempnode
    lla.tail = tempnode
    llb.tail.next = tempnode
    llb.tail = tempnode

lla = LinkedList()
lla.generate(3,0,9)
llb = LinkedList()
llb.generate(4,0,10)

addsamenode(lla,llb,11)
addsamenode(lla,llb,14)
print(lla)
print(llb)
print(intersection(lla,llb))




