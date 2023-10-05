class Node:
    def __init__(self, state, g, h, parent):
        """
        :param state: 当前节点的状态，空位用0表示
        :param g: 从起始节点到当前节点的实际代价
        :param h: 从当前节点到目标节点的估价代价
        :param parent: 父节点，用于输出路径
        """
        self.state = state
        self.g = g
        self.h = h
        self.parent = parent

    def __lt__(self, other):
        return self.g + self.h < other.g + other.h
