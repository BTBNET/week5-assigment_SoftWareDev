# Python Program for Floyd Warshall Algorithm

# Number of vertices in the graph
V = 4

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = 99999

# Solves all pairs shortest path
# via Floyd Warshall Algorithm

# Calculate the shortest distance between i and j using nodes 0 to k


# Python Program for Floyd Warshall Algorithm
INF = 99999


def floydWarshall(graph):
    """ dist[][] will be the output
    matrix that will finally
            have the shortest distances
            between every pair of vertices """
    """ initializing the solution matrix
	same as input graph matrix
	OR we can say that the initial
	values of shortest distances
	are based on shortest paths considering no
	intermediate vertices """

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))


def floydWarshall(graph, n):  # n=no. of vertex
    dist = graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
