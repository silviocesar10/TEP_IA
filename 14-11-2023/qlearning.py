import pygame
import sys
import numpy as np
import random

N = 10 #tamanho do tabuleiro
START = (0,0)
GOAL = (9,9)
OBSTACLES = [(2,2), (2,3), (2,4), (5,6), (6,6), (7,6)]

# Cores 
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
 
# Tamanho do tabuleiro e das células 
CELL_SIZE = 100 
BOARD_SIZE = N * CELL_SIZE 
 
# settings -> pylint args -> "pylint.args": ["--extension-pkg-whitelist=pygame"] 
# Inicializar Pygame 
pygame.init() 
 
# Configurar a janela 
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE)) 
pygame.display.set_caption("Q-Learning Robot Navigation") 
 
 
# Função para desenhar texto 
def draw_text(surface, text, color, rect, font, aa=False, bkg=None): 
    textobj = font.render(text, aa, color, bkg) 
    textrect = textobj.get_rect() 
    textrect.center = rect.center 
    surface.blit(textobj, textrect) 
 
 
# Função para desenhar o tabuleiro 
def draw_board(current_state, Q, i): 
    font = pygame.font.Font(None, 24)  # Define a fonte para o texto 
    pygame.display.set_caption(f"Q-Learning Robot Navigation: Episode {i}") 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
 
    screen.fill(WHITE) 
 
    for i in range(N): 
        for j in range(N): 
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE) 
            if (i, j) == current_state: 
                pygame.draw.rect(screen, BLUE, rect) 
            elif (i, j) == START: 
                pygame.draw.rect(screen, GREEN, rect) 
            elif (i, j) == GOAL: 
                pygame.draw.rect(screen, RED, rect) 
            elif (i, j) in OBSTACLES: 
                pygame.draw.rect(screen, BLACK, rect) 
            else: 
                pygame.draw.rect(screen, WHITE, rect) 
            pygame.draw.rect(screen, BLACK, rect, 1)  # Desenha a borda 
 
            # Desenhar os valores de Q para cada ação 
            if (i, j) not in [GOAL] + OBSTACLES: 
                actions = ["U", "D", "L", "R"] 
                for a in range(4): 
                    q_value = round(Q[i, j, a], 2) 
                    text_pos = ( 
                        j * CELL_SIZE + 4, 
                        i * CELL_SIZE + (a * CELL_SIZE / 4) + 2, 
                    ) 
                    draw_text( 
                        screen, 
                        f"{actions[a]}={q_value}", 
                        BLACK, 
                        pygame.Rect(*text_pos, CELL_SIZE / 2, CELL_SIZE / 4), 
                        font, 
                    ) 
 
    pygame.display.flip()


board = np.zeros((N, N))
for obs in OBSTACLES:
    board[obs] = -1 # representa obstaculos
board[START] = 1 #ponto de partida
board[GOAL] = 2 # ponto de chegada

Q = np.zeros((N, N, 4)) # acoes possiveis

#parametros do q-learning

alpha = 0.1 #taxa de aprendizado
gamma = 0.9 # fator de desconto
epsilon = 0.1 # probabilidade de exploração

#funcao para escolher proxima acao
def chose_action(state):
    if random.uniform(0,1) < epsilon:
        return random.choice([0,1,2,3]) #exploracao
    else:
        return np.argmax(Q[state]) # explotacao

#funcao para atualizar a tabele de recompensas q
def update_q(state, action, reward, next_state):
    predict = Q[state][action]
    target = reward + gamma * np.max(Q[next_state])
    Q[state][action] += alpha * (target * predict)

#funcao para obter a recompensa
def get_reward(state):
    if state == GOAL:
        return 100 # recompensa quando alcanca objetivo
    elif state in OBSTACLES:
        return -100 # penalidade quando encontra obstaculo
    else:
        return -1 #pequena penalidade para cada movimento

#verifica se atingiu um estado terminal
def is_terminal_state(state):
    return state == GOAL or state in OBSTACLES

#acoes
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

#funcao para aplicar uma acao e obter um novo estado
def take_action(state,action):
    i,j = state
    if action == UP:
        i = max(i-1,0)
    elif action == DOWN:
        i = min(i+1, N-1)
    elif action == LEFT:
        j = max(j-1,0)
    elif action == RIGHT:
        j = min(j+1, N-1)
    if(i,j) in OBSTACLES:
        return state #permanece no estado atual se o novo for um obstaculo
    return (i,j)


num_epsodes = 1000
max_steps_per_epsode = 100
for episode in range(num_epsodes):
    state = START
    for step in range(max_steps_per_epsode):
        action = chose_action(state)
        new_state = take_action(state,action)
        reward = get_reward(new_state)
        update_q(state, action, reward, new_state)
        state = new_state
        draw_board(state, Q, episode)
        pygame.time.delay(10)
        if is_terminal_state(state):
            break
