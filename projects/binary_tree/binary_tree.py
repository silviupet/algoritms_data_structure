from node import Node


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('A node with that value already exists.')
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def find(self, value: int):
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise LookupError(f'A node with value {value} was not found.')

    def inorder(self):
        self._inorder_recursive(self.head)

    def _inorder_recursive(self, current_node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)
    # returneaza parintele nodului a carui valoare este atributul functiei
    def find_parent(self, value: int) -> Node:
        # daca nodul cautat este chiar head arunci returneaza parintele ca fiind tot head
        if self.head and self.head.value == value:
            return self.head

        current_node = self.head
        while current_node:
            # if current_node.left exists and .....   "\" means spliting the statement  in 2 lines
            # tot statmentul inseamna daca este parinte (daca nodul din dr sau nodul din stanga match inseamna ca
            # current mode este parintele nodului cautat
            if (current_node.left and current_node.left.value == value) or\
                    (current_node.right and current_node.right.value == value):
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left

    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, value: int):
        # gasim nodul care vrem sa-l stergem si gasim si parintele lui
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(value)
        # daca nodul care dorim sa-l stergem are si dreapta si stanga (are 2 copii) gasim
        # nodul rightmost(cel mai mare)  al ramurei stanga si parintele acestuia
        if to_delete.left and to_delete.right:
            rightmost = self.find_rightmost(to_delete.left)
            rightmost_parent = self.find_parent(rightmost.value)

            if rightmost_parent != to_delete:
                rightmost_parent.right = rightmost.left
                rightmost.left = to_delete.left
            rightmost.right = to_delete.right
            # to_delete_parent este parintele iar to_delete_parent.lefteste copilul din stanga
            # verificam daca este nodul din stanga
            if to_delete == to_delete_parent.left:
                # setam nodul cel mai din dreapta (rightmost) in locul nodului care doeim sa-l stergem
                to_delete_parent.left = rightmost
                # verificam daca este nodul din dreapta
            elif to_delete == to_delete_parent.right:
                # setam nodul cel mai din dreapta (rightmost)  in locul nodului care dorin sa fie sters
                to_delete_parent.right = rightmost
            else:
                # the head must became the rightmost node
                self.head = rightmost
        #        daca  are doar un copil
        elif to_delete.left or to_delete.right:
            # daca ce vrem sa stergem  este in stanga
            if to_delete == to_delete_parent.left:
    # setam copilul(to delete_right or to delete_left) in locul nodului  care vrem sa-l stergem(to_delete_parent.left)
    #  copilul poate sa fie fie la dreapta sau la stanga nodului pe care il vom sterge
                to_delete_parent.left = to_delete.right or to_delete.left
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = to_delete.right or to_delete.left
            else:
     # daca vrem sa stergem headul - setam noul head la copilul din dreapta sau cel din stanga (depinde unde avem un cocopil )
                self.head = to_delete.right or to_delete.left
        else:
            # daca nu are  children
            # to_delete_parent este parintele iar to_delete_parent.lefteste copilul din stanga
            if to_delete == to_delete_parent.left:
                # setam copilul din dreapta la None si pyton il va sterge
                to_delete_parent.left = None
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = None
            else:
                # situatia in care ce vrem sa stergem nu are nici un copil dar este si head (head fara copii)
                self.head = None

