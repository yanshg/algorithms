'''
This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.

'''

OPPOSITES_CARDINALS = {"N": "S", "S": "N", "E": "W", "W": "E"}


class Node:
    def __init__(self, val: str) -> None:
        self.val = val
        self.neighbours = {"N": set(), "E": set(), "S": set(), "W": set()}

    def __repr__(self) -> str:
        return f"{self.val}"

    def __eq__(self, other) -> bool:
        if type(other) == Node:
            return self.val == other.val
        elif type(other) == str:
            return self.val == other
        return False

    def __hash__(self) -> int:
        return hash(self.val)

class Map:
    def __init__(self) -> None:
        self.nodes = {}

    def add_rule(self, rule: str) -> None:
        n1, direction, n2 = rule.split()

        if n1 not in self.nodes:
            self.nodes[n1] = Node(n1)
        if n2 not in self.nodes:
            self.nodes[n2] = Node(n2)

        node1 = self.nodes[n1]
        node2 = self.nodes[n2]

        # updating the neighbours
        for char in direction:
            if (node1 in node2.neighbours[char]) or (
                node2 in node1.neighbours[OPPOSITES_CARDINALS[char]]):
                raise RuntimeError
            for node in node1.neighbours[char]:
                self.add_rule(f"{node} {char} {node2}")

        # adding the rule to the calling node
        for char in direction:
            node2.neighbours[char].add(node1)
            node1.neighbours[OPPOSITES_CARDINALS[char]].add(node2)

class Solution(object):
    def __init__(self):
        self.opposites = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}

    def is_valid(self, rules):
        nodes = {}
        for rule in rules:
            val1, directions, val2 = tuple(rule.split())
            node1 = nodes.setdefault(val1, Node(val1))
            node2 = nodes.setdefault(val2, Node(val2))
            if not self._add_rule(node1, directions, node2):
                return False
        return True

    def _add_rule(self, node1, directions, node2):
        # recursive
        for direction in directions:
            if node1 in node2.neighbours[self.opposites[direction]] or node2 in node1.neighbours[direction]:
                return False
            # check node1's transfer dependency
            for node in node1.neighbours[direction]:
                self._add_rule(node, direction, node2)
                
        for direction in directions:
            node2.neighbours[direction].add(node1)
            node1.neighbours[self.opposites[direction]].add(node2)
        return True
    

if __name__ == "__main__":

    rules = [ "A N B", "B NE C", "C N A" ]

    m = Map()
    for rule in rules:
        try:
            m.add_rule(rule)
            print("Rule Applied")
        except RuntimeError:
            print("Invalid Rule!")