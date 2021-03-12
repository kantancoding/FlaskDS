class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class ValueItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i)) % self.table_size
        return hash_value

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(ValueItem(key, value), None)
        else:
            # head at hashed_key index
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            # when the next node is None, we are at
            # the end of the linked list
            node.next_node = Node(ValueItem(key, value), None)

    def del_key_val(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            if (
                self.hash_table[hashed_key].data.key == key
                and self.hash_table[hashed_key].next_node == None
            ):
                self.hash_table[hashed_key] = None
                return True
            node = self.hash_table[hashed_key]
            if node.data.key == key:
                self.hash_table[hashed_key] = node.next_node
                return True
            if node.next_node:
                while node.next_node:
                    if node.next_node.data.key == key:
                        node.next_node = node.next_node.next_node
                        return True
                    node = node.next_node
            return False
        return False

    def get_value_for_key(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.data.value
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node
            # for last node (because next node will be None)
            if key == node.data.key:
                return node.data.value
        return None

    def print_table(self):
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )
                        node = node.next_node
                    llist_string += (
                        str(node.data.key) + " : " + str(node.data.value) + " --> None"
                    )
                    print(f"    [{i}] {llist_string}")
                else:
                    print(f"    [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{i}] {val}")
        print("}")


hash_table = HashTable(20)
hash_table.add_key_value("strawberry", {"strawberries": "value"})
# hash_table.print_table()
hash_table.add_key_value("cow", {"cows": "value"})
hash_table.add_key_value("stigma", {"stigmas": "value"})
hash_table.add_key_value("fluent", {"fluents": "value"})
hash_table.add_key_value("very", {"veries": "value"})
hash_table.add_key_value("nice", {"nices": "value"})
hash_table.add_key_value("nice", {"nices": "value"})
hash_table.add_key_value("nice", {"nices": "value"})
# hash_table.print_table()
print(hash_table.get_value_for_key("nice"))
hash_table.del_key_val("cow")
hash_table.del_key_val("stigma")
hash_table.del_key_val("strawberry")
hash_table.print_table()
