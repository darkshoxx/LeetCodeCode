# Approach 1

from typing import List


class Solution1:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        term_nodes = []
        in_graph = [[]]*len(graph)
        for index in range(len(graph)):
            if graph[index] == []:
                term_nodes.append(index)
            else:
                for entry in graph[index]:
                    in_graph[entry] = graph[index]
        

        print(graph)
        print(in_graph)
        print(term_nodes)
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.eventualSafeNodes
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]

    print(checks)