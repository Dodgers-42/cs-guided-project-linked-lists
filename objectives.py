class LinkedListNode:
    def __init__(self, val):
        self.value = val
        self.next = None # Always stores another LinkedListNode



def insert_at_head(linked_list, new_value):
    #create a new linked list noed
    new_node = LinkedListNode(new_value)
    new_node.next = linked_list

    return new_node
def insert_at_tail(linked_list, new_value):
    new_node = LinkedListNode(new_value)
    tail.next = new_node
    return new_node

def print_list(start_node):
    curr_node = start_node
    while curr_node is not None:
        #print the node value
        print(curr_node.value)
        # move on to the next node
        curr_node = curr_node.next

# def print_list_recursive(curr_node):
#     if curr_node:
#         print(curr_node.value)
#         print_list_recursive(curr_node.next)

# Init code for my linked list
head = LinkedListNode(6) # This is the haed of our "Linked list"
tail = head

head = insert_at_head(head,5)
head = insert_at_head(head,4)
head = insert_at_head(head,3)
head = insert_at_head(head,2)

tail = insert_at_tail(tail, 7)

print(head.next.value)
print(tail.value)