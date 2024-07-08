from node import Node
from stackfrontier import StackFrontier

class Maze:
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:            
            raise Exception("O labirinto só pode conter 1 ponto de partida.")
        if contents.count("B") != 1:
            raise Exception("O labirinto só pode conter 1 ponto de chegada.")
        contents = contents.splitlines()
        self.height = len(contents)-1
        self.width = max(len(line) for line in contents)-1
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if contents[i][j] == "A":
                    self.start = (i,j)
                    row.append(False)
                elif contents[i][j] == "B":
                    self.goal = (i,j)
                    row.append(False)
                elif contents[i][j] == " ":                    
                    row.append(False)
                else: 
                    row.append(True)
            self.walls.append(row)
        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("#", end="")
                elif (i,j) == self.start:
                    print("A", end="")
                elif (i,j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i,j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighboors(self, position):
        row, col = position
        candidates = [
            ("u", (row-1, col)),
            ("d", (row+1, col)),
            ("l", (row, col-1)),
            ("r", (row, col+1))
        ]
        result =[]
        for action, (r,c) in candidates:
            if (0 <= r < self.height) and (0 <= c < self.width) and (not self.walls[r][c]):
                result.append((action, (r,c)))
        return result
    
    def solve(self):
        self.num_explored = 0
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)
        self.explored = set()
        while True:
            if frontier.empty():
                raise Exception("Sem solução.")
            node = frontier.remove()
            self.num_explored += 1
            if (node.state == self.goal):
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            self.explored.add(node.state)
            for action, state in self.neighboors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)