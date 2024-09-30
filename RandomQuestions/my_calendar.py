class Tree:
    vals = None
    left = None
    right = None
    
    def __init__(self, start, end):
        self.vals = (start, end)
        return

    def insert(self, book):
        cur = self
        # print("inserting book")
        while True:
            if cur.vals[1] <= book[0]:
                if cur.left:
                    cur = cur.left
                    continue
                elif cur.left == None:
                    cur.left = Tree(book[0], book[1])
                    return True
            elif cur.vals[0] >= book[1]:
                if cur.right:
                    cur = cur.right
                    continue
                elif cur.right == None:
                    cur.right = Tree(book[0], book[1])
                    return True
            
            return False


class MyCalendar:
    root = None
    def __init__(self):
        return
    def book(self, start: int, end: int) -> bool:
        if self.root == None:
            self.root = Tree(start, end)
            return True
        else:
            ret = self.root.insert((start,end))
            return ret


sol = MyCalendar()

print(sol.book(10, 20))
print(sol.book(15, 25))
print(sol.book(20, 30))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)