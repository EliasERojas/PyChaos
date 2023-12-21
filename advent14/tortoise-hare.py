class Node : 
    def __init__(self, value : int):
        self.value : int = value
        self.next : 'Node | None' = None

class LinkedList : 
    def __init__(self):
        self.head : Node | None = None

    def add(self, value) :
        new_node = Node(value)
        if self.head == None :
            self.head = new_node
            return

        pivot = self.head
        while pivot.next != None :
            pivot = pivot.next
        pivot.next = new_node

    def nodes_list (self) -> list[Node] :
        values = []
        pivot = self.head
        while pivot != None : 
            values.append(pivot)
            pivot = pivot.next
        return values

    def empty(self) -> bool : 
        return self.head == None

    def loop(self) -> bool :
        if not self.head : 
            return False
        
        tortoise = self.head
        hare = self.head.next

        while tortoise != hare :
            if not (tortoise and hare and hare.next and hare.next.next) :
                return False
            tortoise = tortoise.next
            hare = hare.next.next
        return True


list = LinkedList()
for i in range(0,5) :
    list.add(i)

last_node = list.nodes_list().pop()
last_node.next = list.head.next.next
if list.loop() : 
    print("chimangos")
