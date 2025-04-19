# Approach 1

from typing import List

# Still not completed
class Solution1:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        term_nodes = []
        in_graph = [[] for _ in graph]
        for index in range(len(graph)):
            if graph[index] == []:
                term_nodes.append(index)
            else:
                for entry in graph[index]:
                    in_graph[entry].append(index)
        safe_nodes = term_nodes[:]
        for node in term_nodes:
            safe_nodes += self.traverse(in_graph, node)
        return safe_nodes

    def traverse(self, in_graph, node):
        if in_graph[node] == []:
            return [node]
        return_list = []
        for target in in_graph[node]:
            return_list.append(self.traverse(in_graph, target))
        return return_list




if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.eventualSafeNodes
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)