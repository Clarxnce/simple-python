#Edge List
#each array states a connection
graph = [[0,2], [2,3], [2,1], [1,3]]

#Adjacent List
#index is the node, value is the nodes neighbours
#the index of the array is the value of the actual graph node
graph2 = [[2], [2,3], [0,1,3], [1,2]]

#Adjacent Matrix
#0s and 1s indicating if node x has a connection to node y
graph3 = [
    [0,0,1,0],
    [0,0,1,1],
    [1,1,0,1],
    [0,1,1,0]
]