class Order:
    def __init__(self, id, cust_details, order_details) -> None:
        self.id = id
        self.cust_details = cust_details
        self.order_details = order_details

class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class OrderList:
    def __init__(self, head) -> None:
        self.head = head
        self.tail = None

    def append(self, order):
        self.tail.next = order
        self.tail = self.tail.next

    def display(self):
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next
    
    def reverse_helper(self, curr, prev):
        if curr.next == None:
            return curr
        next = curr.next
        curr.next = prev
        previous = curr
        self.reverse(curr.next, previous)

    def reverse(self):
        self.reverse_helper(self.head, None)

