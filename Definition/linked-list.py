class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print(self):
        head = self
        while head != None:
            print(head.value)
            head = head.next
            
