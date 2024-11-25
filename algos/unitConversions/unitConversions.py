"""
from https://www.youtube.com/watch?v=V8DGdPkBBxg

m = 3.28 ft
ft = 12 in
hr = 60 min
min = 60 sec
expample queries:
2 m = ? in _>> answer 78.22
13 in = ? m >> ansewr 0.330
13 in = ? hr >> not convertible
"""

class Solution:
    def feetToM(self, feet):
        """
        1m       xm
        3.28ft  inputft
        """
        return (feet) / 3.28

    
    def metersToF(self, meters):
        return (meters * 3.28)
    
    def feetToIn(self, feet):
        return feet * 12
    
    def inToFeet(self, inches):
        return inches / 12

    def hoursToMin(self, hours):
        return hours * 60
    
    def minToHours(self, min):
        return min / 60
    
    # dict that maps strings (units) to class representing node in graph
    # nodes store (float, node)

class Edge: 
    def __init__(self, multiplier, node):
        self.multiplier = multiplier
        self.node = node

class Node:
    def __init__(self, unit):
        self.unit = unit
        self.edges = []

    def add_edge(self, multiplier, other_node):
        edge = Edge(multiplier, other_node)
        self.edges.append(edge)

def parse_facts(facts):
    name_to_node = {}
    for (left_unit, multiplier, right_unit) in facts:
        if left_unit not in name_to_node:
            left_node = Node(left_unit)
            name_to_node[left_unit] = left_node
        if right_unit not in name_to_node:
            right_node = Node(right_unit)
            name_to_node[right_unit] = right_node
        name_to_node[left_unit].add_edge(multiplier, right_unit)
        name_to_node[right_unit].add_edge(1. / multiplier, left_unit)
    return name_to_node

from collections import deque

def answer_query(query, facts):
    """
    starting_amount = 2
    from_unit = 'm'
    to_unit = 'in'
    """
    starting_amount, from_unit, to_unit = query
    if from_unit not in facts:
        return None
    if to_unit not in facts:
        return None
    from_node = facts[from_unit]
    to_node = facts[to_unit]

    visited = set()
    visited.add(from_unit)
    to_visit = deque()
    to_visit.append((from_node, starting_amount))
    visited.add(from_node)    

    while not to_visit:
        current_node, current_amount = to_visit.pop()
        if current_node == to_node: return current_amount

        for edge in current_unit.edges:
            if edge.node not in visited:
                visited.add(edge.node)
                with_latest_multipler = current_amount * edge.multiplier
                to_visit.push((edge.node, with_latest_multipler))
    
    return None
    

    # given node, we want to enqueue tuple (current_amount, unit_to_check)
