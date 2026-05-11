import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def umn_matr(M1, M2):
    A = np.array(M1)
    B = np.array(M2)
    return (A @ B > 0).astype(int)

def sum_matr(M1, M2):
    A = np.array(M1)
    B = np.array(M2)
    return (A + B > 0).astype(int)

def peresec(M1, M2):
    A = np.array(M1)
    B = np.array(M2)
    return (A * B).astype(int)

def ris_hasse(matr):
    n = len(matr)
    G = nx.DiGraph()
    
    for i in range(n):
        for j in range(n):
            if matr[i][j] == 1:
                pokr = True
                for k in range(n):
                    if matr[i][k] == 1 and matr[k][j] == 1:
                        if k != i and k != j:
                            pokr = False
                if pokr:
                    G.add_edge(i+1, j+1)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700,
            node_color="lightgreen", arrows=True,
            font_weight="bold")
    plt.title("Diagramma Hasse")
    plt.show()

versh = [1, 2, 3]

otn1 = [(1,1), (2,2), (3,3), (1,2), (2,3)]
otn2 = [(3,2), (1,3), (2,1), (2,2)]

n = 3
M1 = np.zeros((n, n))
M2 = np.zeros((n, n))

for t in otn1:
    M1[t[0]-1][t[1]-1] = 1

for t in otn2:
    M2[t[0]-1][t[1]-1] = 1

print("Matrica G1", M1)
print("Matrica G2", M2)

M3 = umn_matr(M1, M2)
print("Kompoziciya", M3)

M4 = sum_matr(M1, M2)
print("Ob\"edinenie", M4)

M5 = peresec(M1, M2)
print("Peresechenie", M5)

G1 = nx.DiGraph(np.matrix(M1))
G2 = nx.DiGraph(np.matrix(M2))
G3 = nx.DiGraph(np.matrix(M3))
G4 = nx.DiGraph(np.matrix(M4))
G5 = nx.DiGraph(np.matrix(M5))

pos1 = nx.spring_layout(G1, scale=100000, center=[0, 0])
pos2 = nx.circular_layout(G2, scale=80000, center=[30, 40])
pos4 = nx.spiral_layout(G4, scale=40000, center=[35, 4])

nx.draw(G1, pos=pos1, with_labels=True, node_size=200, arrows=True, 
        node_color="blue", font_size=10, font_weight="bold")
nx.draw(G2, pos=pos2, with_labels=True, node_size=200, arrows=True, 
        node_color="lightblue", font_size=10, font_weight="bold")
nx.draw(G4, pos=pos4, with_labels=True, node_size=200, arrows=True, 
        node_color="orange", font_size=10, font_weight="bold")
plt.show()

data = np.array([
    [0,1,1,1,0,0,0,0],
    [0,0,0,0,1,1,0,0],
    [0,0,0,0,1,0,1,0],
    [0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0]
])

ris_hasse(data)
