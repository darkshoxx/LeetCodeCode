from typing import List

# even slower
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = []
        unsafe_nodes = []
        for index in range(len(graph)):
            if index not in unsafe_nodes + safe_nodes:
                # either returns all safe or a loop of unsafes
                safe, history = self.traverse(graph, [], index, index)
                if safe:
                    for node in history:
                        if node not in safe_nodes:
                            safe_nodes.append(node) 
                else:
                    unsafe_nodes += history
        return sorted(safe_nodes)

    def traverse(self, graph, memory, origin, current):
        memory.append(current)
        targets = graph[current]
        for target in targets:
            if target in memory:
                return (False, memory)
        if targets == []:
            return (True, memory)
        all_safe = True
        combined_memory = []
        for target in targets:
            truth, new_memory = self.traverse(graph, memory[:], origin, target)
            all_safe = all_safe and truth
            if not all_safe:
                return (False, new_memory)
            else: combined_memory += new_memory
        return (True, combined_memory)
            




# too slow, sadge
class Solution1:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = []
        nodes_added = True
        length = len(graph)
        rep_graph = [None]*length
        while nodes_added:
            nodes_added = False
            for i in range(length):
                if rep_graph[i] is None:
                    # if graph[i] == []:
                    #     safe_nodes.append(i)
                    #     nodes_added = True
                    #     rep_graph[i] = 0
                    all_safe = True
                    for target in graph[i]:
                        if target not in safe_nodes:
                            all_safe = False
                    if all_safe:
                        safe_nodes.append(i)
                        nodes_added = True
                        rep_graph[i] = 0
        return sorted(safe_nodes)



if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.eventualSafeNodes
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)