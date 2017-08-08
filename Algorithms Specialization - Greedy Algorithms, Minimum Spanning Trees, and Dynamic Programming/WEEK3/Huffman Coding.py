from queue import PriorityQueue

class HuffmanNode:
    def __init__(self, left, right):
        self.left_child = left
        self.right_child = right


def huffman_coding(freqs):
    pq = PriorityQueue()
    for value in freqs:
        pq.put(value)

    while pq.qsize() > 1:
        l, r = pq.get(), pq.get()
        node = HuffmanNode(l, r)
        pq.put((l[0]+r[0], node))
    return pq.get()


def walk_tree(node, prefix="", code={}):
    if isinstance(node[1], HuffmanNode):
        walk_tree(node[1].left_child, prefix + "0", code)
        walk_tree(node[1].right_child, prefix + "1", code)
    else:
        code[node[1]] = prefix

    return code




freq = [ (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
    (12.702, 'e'), (2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
    (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
    (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'),
    (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'),
    (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
    (1.974, 'y'), (0.074, 'z')]

root_node = huffman_coding(freq)
code = walk_tree(root_node)
for i in sorted(freq, reverse=True):
    print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])