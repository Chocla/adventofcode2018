from string import ascii_lowercase
import networkx as nx

text = open('input.txt','r').read().splitlines()
deps = []
orders = ""
G = nx.DiGraph()
for o in text:
    a = o.split('tep ')
    deps.append((a[1][0],a[2][0]))
G.add_edges_from(deps)
size = len(G.nodes())
nodeOrder = ""
while  G.order() > 0:
    tmp = ""
    for n in G.nodes():
        if len(G.pred[n]) == 0:
            tmp += str(n)
    tmp = ''.join(sorted(tmp))
    nodeOrder += tmp[0]
    G.remove_node(tmp[0])
print nodeOrder