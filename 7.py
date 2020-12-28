from typing import Any, Dict, List


def edge(node: str, weight: int) -> Dict[str, Any]:
    return { 
        'node': node, 
        'weight': weight 
    }


def adjacency_list(input_file: str) -> Dict[str, List[str]]:
    G = {}
    for line in open(input_file, 'r').readlines():
        lhs, rhs = line.split('contain')
        node = lhs.replace('bags', '').strip()
        adjacency_list = []
        for adjacent_node_with_weight in rhs.replace('bags', '').replace('bag', '').replace('.', '').split(','):
            adjacent_node = " ".join(adjacent_node_with_weight.strip().split(' ')[1:])
            if not adjacent_node == 'other': # no other, first part was stripped
                weight = int(adjacent_node_with_weight.strip().split(' ')[0].strip())
                adjacency_list.append(edge(adjacent_node, weight))
        G[node] = adjacency_list
    return G


def predecessors_of(node: str, G: Dict[str, List[str]]) -> List[str]:
    Q = []
    S = []
    Q.append(node)
    while len(Q) != 0:
        node = Q.pop()
        for key in G.keys():
            for edge in G[key]:
                if edge['node'] == node:
                    Q.append(key)
                    if key not in S:
                        S.append(key)
    return S


def weight_of(node: str, G: Dict[str, List[str]]) -> int:
    sum = 0
    for edge in G[node]:
        sum += edge['weight'] * (1 + weight_of(edge['node'], G))
    return sum


G = adjacency_list('7.in')

print(len(predecessors_of('shiny gold', G)))
print(weight_of('shiny gold', G))