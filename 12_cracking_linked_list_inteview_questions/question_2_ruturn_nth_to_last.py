# implement and algorithm to find the nth to last element of a singly linked list
from linked_list import LinkedList
def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 =pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1
custtomll = LinkedList()
custtomll.generate(10,0,99)
print(custtomll)
print(nthToLast(custtomll,3))
