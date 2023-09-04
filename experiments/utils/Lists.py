from __future__ import annotations

class Node():
    def __init__(self, data = None):
        self.__data = data
        self.__next = None
        self.__prev = None
    
    def get_data(self) -> Node:
        return self.__data
    
    def set_data(self, value) -> None:
        self.__data = value
    
    def get_next(self) -> Node:
        return self.__next
    
    def set_next(self, value) -> None:
        self.__next = value
    
    def get_prev(self) -> Node:
        return self.__prev
    
    def set_prev(self, value) -> None:
        self.__prev = value
        
    def __str__(self):
        return f'Data: {self.__data}'

class DoublyLinkedList():
    def __init__(self):
        self.__count = 0
        self.__start = None
        self.__end = None
    
    def size(self):
        return self.__count
    
    def get_start(self):
        return self.__start
    
    def set_start(self, value):
        self.__start = value

    def get_end(self):
        return self.__end
    
    def set_end(self, value):
        self.__end = value
    
    def is_empty(self):
        if self.__start == None:
            return True
        return False
    
    def append(self, data = None):
        self.__count += 1
        new_node = Node(data)
        if self.is_empty():
            self.__start = new_node
            self.__end = new_node
        else:
            new_node.set_prev(self.__end)
            self.__end.set_next(new_node)
            self.__end = new_node
    
    def search(self, data) -> Node:
        i = self.__start
        while i != None:
            if data == i.get_data():
                break
            i = i.get_next()
        return i

    def remove(self, data):
        node_found = self.search(data)
        if node_found != None:
            if node_found.get_prev() != None:
                node_found.get_prev().set_next(node_found.get_next())
            else:
                self.__start = node_found.get_next()
            if node_found.get_next() != None:
                node_found.get_next().set_prev(node_found.get_prev())
            else:
                self.__end = node_found.get_prev()
        return node_found
    
    def pop(self):
        if not self.is_empty():
            deleted_node = self.__end
            if self.__end.get_prev() != None:
                self.__end.get_prev().set_next(None)
            else:
                self.__start = None
            self.__end = self.__end.get_prev()
        return deleted_node
    
    
    def to_array(self):
        result = [None] * self.__count
        i = 0
        temp = self.__start
        while(temp != None):
            result[i] = temp.get_data()
            temp = temp.get_next()
            i += 1
        return result
        
    def __repr__(self):
        string = ""
          
        if(self.is_empty()):
            string += "Doubly Linked List Empty"
            return string
          
        string += f"{self.__start.get_data()}"      
        temp = self.__start.get_next()
        while(temp != None):
            string += f" -> {temp.get_data()}"
            temp = temp.get_next()
        return string