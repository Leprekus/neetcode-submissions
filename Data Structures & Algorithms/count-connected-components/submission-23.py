class UF:
    
    def union(self, node1, node2):
        r1 = self.find(node1)
        r2 = self.find(node2)
        if r1 == r2:
            return
        if r1.size < r2.size:
            r1.parent = r2
            r2.size += r1.size
        else:
            r2.parent = r1
            r1.size += r2.size

    def find(self, node):
        if node.parent != node:
            node.parent = self.find(node.parent)
        return node.parent
        
    def add(self, element):
        node = Node(element)
        return node
    
class Node:

    def __init__(self, element):
        self.element = element
        self.parent = self
        self.size = 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
            if len(edges) == 0: return n
            uf = UF()
            nodes = [None] * (n+1)
            k = n
            for u, v in edges:
                if nodes[u] == None:
                    nodes[u] = uf.add(u)
                if nodes[v] == None:
                    nodes[v] = uf.add(v)

            for (u, v) in edges:            
                if uf.find(nodes[v]) != uf.find(nodes[u]):
                    uf.union(nodes[u], nodes[v])
                    k -= 1
            
            return k 
