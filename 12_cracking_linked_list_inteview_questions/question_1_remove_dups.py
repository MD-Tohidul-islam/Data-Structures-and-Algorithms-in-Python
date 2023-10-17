# Question 1 - Remove dups: write a code to remove duplicates from an unsorted linked list

from  linked_list import LinkedList
def removeDups(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll

def removeDups1(ll):
    if ll.head is None:
        return
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return ll.head



customLl = LinkedList()
customLl.generate(10,0,99)
# print(customLl)
# removeDups(customLl)
print(customLl)
removeDups1(customLl)
print(customLl)


