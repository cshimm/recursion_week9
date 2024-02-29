import unittest

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
        self.tail = head

    def append(self, order):
        self.tail.next = order
        self.tail = self.tail.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.value.id)
            curr = curr.next
    
    def reverse_helper(self, curr, prev):
        if curr == None:
            self.head = prev
            return
        next = curr.next
        curr.next = prev
        previous = curr
        self.reverse_helper(next, previous)

    def reverse(self):
        self.reverse_helper(self.head, None)
        return self

class TestReverseLinkedListRecursion(unittest.TestCase):
    def test_append(self):
        order_list = OrderList(ListNode(Order(1,1,1)))
        for i in range(2, 5):
            order = Order(i, str(i), str(i))
            order_list.append(ListNode(order))
        # order_list.display()
    
    def test_reverse(self):
        order_list = OrderList(ListNode(Order(1,1,1)))
        for i in range(2, 5):
            order = Order(i, str(i), str(i))
            order_list.append(ListNode(order))
        order_list.reverse()
        order_list.display()
        
if '__main__' == __name__:
    unittest.main()