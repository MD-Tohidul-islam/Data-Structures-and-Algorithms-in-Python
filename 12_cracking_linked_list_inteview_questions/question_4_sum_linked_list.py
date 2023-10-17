"""you have two numbers represented by a linked list, where each node contains a single digit.
the digits are stored in reverse order , such that the 1;s digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list"""


from linked_list import LinkedList

def sumlist(lla , llb):
    n1 = lla.head
    n2 = llb.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1 :
            result += n1.value
            n1 = n1.next


        if n2:
            result +=n2.value
            n2 = n2.next

        ll.add(int(result % 10))
        carry = result//10

    return ll

lla = LinkedList()
lla.add(7)
lla.add(1)
lla.add(6)


llb = LinkedList()
llb.add(5)
llb.add(9)
llb.add(2)

print(lla)
print(llb)
print(sumlist(lla,llb))
