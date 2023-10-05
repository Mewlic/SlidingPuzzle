import heapq
from Node import Node


class PuzzleSolver:
    def __init__(self, strategy, size=3):
        """
        :param strategy: 启发函数的定义，分为：
                        1：”不在位“的将牌数
                        2：将牌“不在位”的距离和
                        3：不使用启发函数（退化为广度优先）
        :param size: 数字华容道的大小，size*size，默认为3
        """
        self.strategy = strategy
        self.size = size

    def heuristic(self, state, goal_state):
        """
        :param state: 当前节点的状态
        :param goal_state: 当前节点的状态
        :return: 估计代价h值
        """

        distance = 0
        if self.strategy == 1:
            return sum(1 for i, j in zip(state, goal_state) if i != j)

        elif self.strategy == 2:
            for i in range(len(state)):
                if state[i] == 0:
                    continue
                current_row = i // self.size
                current_col = i % self.size
                goal_index = goal_state.index(state[i])
                goal_row = goal_index // self.size
                goal_col = goal_index % self.size
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
            return distance

        elif self.strategy == 3:
            return 0

    def solve_puzzle(self, start_state, goal_state):
        """
        :param start_state: 起始节点的状态
        :param goal_state: 目标节点的状态
        :return: 最小代价路径
        """
        open_list = []
        closed_set = set()

        start_node = Node(start_state, 0, self.heuristic(start_state, goal_state), None)
        heapq.heappush(open_list, start_node)

        while open_list:
            current_node = heapq.heappop(open_list)
            current_state = current_node.state

            if current_state == goal_state:
                path = []
                while current_node:
                    path.append(current_node.state)
                    current_node = current_node.parent
                path.reverse()
                return path

            closed_set.add(tuple(current_state))

            neighbors = self.get_neighbors(current_state)

            for neighbor_state in neighbors:
                neighbor_g = current_node.g + 1
                neighbor_h = self.heuristic(neighbor_state, goal_state)

                neighbor_node = Node(neighbor_state, neighbor_g, neighbor_h, current_node)

                if tuple(neighbor_state) in closed_set:
                    continue

                existing_index = None
                for i, node in enumerate(open_list):
                    if node.state == neighbor_state:
                        existing_index = i
                        break

                if existing_index is not None and neighbor_g < open_list[existing_index].g:
                    del open_list[existing_index]

                heapq.heappush(open_list, neighbor_node)

        return None

    def get_neighbors(self, state):
        """
        :param state: 当前节点的状态
        :return: 当前节点的邻居节点
        """
        neighbors = []
        zero_index = state.index(0)

        if zero_index > self.size - 1:
            neighbor = state[:]
            neighbor[zero_index], neighbor[zero_index - self.size] = neighbor[zero_index - self.size], neighbor[zero_index]
            neighbors.append(neighbor)

        if zero_index < self.size * self.size - self.size:
            neighbor = state[:]
            neighbor[zero_index], neighbor[zero_index + self.size] = neighbor[zero_index + self.size], neighbor[zero_index]
            neighbors.append(neighbor)

        if zero_index % self.size != 0:
            neighbor = state[:]
            neighbor[zero_index], neighbor[zero_index - 1] = neighbor[zero_index - 1], neighbor[zero_index]
            neighbors.append(neighbor)

        if zero_index % self.size != self.size - 1:
            neighbor = state[:]
            neighbor[zero_index], neighbor[zero_index + 1] = neighbor[zero_index + 1], neighbor[zero_index]
            neighbors.append(neighbor)

        return neighbors
