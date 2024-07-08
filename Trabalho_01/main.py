import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node, _ in self.frontier)


    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Fronteira vazia.")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def add(self, node, priority):
        self.frontier.append((node, priority))

    def remove(self):
        if self.empty():
            raise Exception("Fronteira vazia.")
        else:
            # Encontre o índice do nó com a menor prioridade
            min_index = 0
            for i in range(len(self.frontier)):
                if self.frontier[i][1] < self.frontier[min_index][1]:
                    min_index = i
            node, _ = self.frontier.pop(min_index)
            return node


class Maze():

    def manhattan_distance(self, state1, state2):
        x1, y1 = state1
        x2, y2 = state2
        return abs(x1 - x2) + abs(y1 - y2)


    def __init__(self, filename):

        # lê o arquivo e define a altura e a largura do labirinto
        with open(filename) as f:
            contents = f.read()

        # valida o ponto de partida e o ponto de chegada
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # determina a altura e a largura do labirinto
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # mantém listas de células que representam paredes
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        self.solution = None


    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("#", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()


    def neighbors(self, state):
        # computa as possíveis ações de movimento a partir de um estado
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        # filtra somente as ações viáveis
        result = []        
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result


    def solve(self):
        #"""Encontra uma solução para o labirinto, caso exista."""
        # memória para a quantidade de estados explorados
        self.num_explored = 0

        # inicializa a fronteira com o estado inicial e sua prioridade (f)
        start = Node(state=self.start, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start, priority=0)  # Adiciona a prioridade 0 para o estado inicial

        # inicializa um conjunto vazio de estados explorados
        self.explored = set()

        # inicializa um dicionário para rastrear o custo g de cada estado
        g_costs = {self.start: 0}

        # executa enquanto não explorar todos os estados
        while True:
            # se a fronteira está vazia, então não há caminho viável
            if frontier.empty():
                raise Exception("Sem solução.")

            # pega o nó da fronteira com o menor valor de f = g + h
            node = frontier.remove()
            self.num_explored += 1

            # se o nó é o objetivo, então temos uma solução
            if node.state == self.goal:
                # computa o caminho da solução percorrendo os nós pais
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

            # marca um nó como explorado
            self.explored.add(node.state)

            # adiciona os vizinhos (ações possíveis) à fronteira
            for action, state in self.neighbors(node.state):
                if state not in self.explored and not frontier.contains_state(state):
                    g = g_costs[node.state] + 1
                    h = self.manhattan_distance(state, self.goal)
                    f = g + h
                    child = Node(state=state, parent=node, action=action)
                    g_costs[state] = g
                    frontier.add(child, priority=f)
                elif state in frontier.frontier and g_costs[state] > g_costs[node.state] + 1:
                    # Atualiza a prioridade e o pai se encontrarmos um caminho melhor
                    g = g_costs[node.state] + 1
                    h = self.manhattan_distance(state, self.goal)
                    f = g + h
                    child = Node(state=state, parent=node, action=action)
                    g_costs[state] = g
                    frontier.add(child, priority=f)



    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2

        # cria um canvas de pintura em branco
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        # desenha as células, de acordo com seu tipo
        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (30, 30, 30)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(filename)


if len(sys.argv) != 2:
    sys.exit(f"Uso: python {sys.argv[0]} maze.txt")

m = Maze(sys.argv[1])
print("#####################")
print("Labirinto")
print("#####################")
m.print()
print("Resolvendo...")
m.solve()
print("Estados explorados:", m.num_explored)
print("Solução:")
m.print()
m.output_image("maze.png", show_explored=True)