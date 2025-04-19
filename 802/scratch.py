# reversal of
[[1,2],[2,3],[5],[0],[5],[],[]]
def reverse(graph):
    length = len(graph)
    rev_list = []*length
    for i in range(len(graph)):
        targets = graph[i]
        for j in targets:
            rev_list[j].append[i]
[[3],[0],[0,1],[1],[],[2,4],[]]