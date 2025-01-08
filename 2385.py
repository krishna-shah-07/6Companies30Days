# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = {}

        def build_graph(node, parent=None):
            if node:
                if node.val not in graph:
                    graph[node.val] = set()
                if parent:
                    graph[node.val].add(parent.val)
                    graph[parent.val].add(node.val)
                build_graph(node.left, node)
                build_graph(node.right, node)

        build_graph(root)

        # BFS to find the distance between each node and the start node
        queue = deque([(start, 0)])
        visited = set([start])
        max_distance = 0

        while queue:
            current_node, distance = queue.popleft()
            max_distance = max(max_distance, distance)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
                    visited.add(neighbor)

        return max_distance
