import math
import os
import random


class Space:
    def __init__(self, altura, largura, qtde_casas, qtde_hospitais):
        """Cria um novo espaço de estados com dada dimensão e quantidade de hospitais."""
        self.altura = altura
        self.largura = largura
        self.qtde_hospitais = qtde_hospitais
        self.casas = set()
        self.hospitais = set()
        self.solucao_encontrada = set()

        # Para i de 0 até o número de casas
        for i in range(qtde_casas):
            # Adiciona uma casa em um dos espaços disponíveis
            self.adicionar_casa(random.choice(list(self.espacos_vazios())))

        self.inicializar_hospitais()

    def adicionar_casa(self, casa):
        """Adiciona uma casa a um local determinado do espaço de estados."""
        self.casas.add(casa)

    def adicionar_hospital(self, hospital):
        """Adiciona um hospital a um local determinado do espaço de estados."""
        self.hospitais.add(hospital)

    def inicializar_hospitais(self):
        # Zera os hospitais
        self.hospitais = set()
        # Para i de 0 até o número de hospitais
        for i in range(self.qtde_hospitais):
            # Adiciona um hospital em um dos espaços disponíveis
            self.adicionar_hospital(random.choice(list(self.espacos_vazios())))

    def espacos_vazios(self):
        """Retorna todas as células que não são casa e nem hospital."""

        # Inicializa a lista de candidatos com um conjunto de todas as células
        candidatas = set(
            (linha, coluna)
            for linha in range(self.altura)
            for coluna in range(self.largura)
        )

        # Remove todas as células correspondentes a casas e a hospitais
        for casa in self.casas:
            candidatas.remove(casa)
        for hospital in self.hospitais:
            candidatas.remove(hospital)
        return candidatas

    def obter_custo(self, hospitals):
        """Computa a soma das distâncias de Manhatan das casas para o hospital mais próximo."""
        custo = 0
        # Para cada casa, calcula a distância para todos os hospitais e pega a menor
        for casa in self.casas:
            custo += min(
                # Distância de manhattan entre a casa e cada um dos hospitais
                abs(casa[0] - hospital[0]) + abs(casa[1] - hospital[1])
                for hospital in hospitals
            )
        return custo

    def obter_vizinhos(self, linha, coluna):
        """Retorna os vizinhos válidos que não são casa e nem hospital."""
        candidatos = [
            (linha - 1, coluna), #cima
            (linha + 1, coluna), #baixo
            (linha, coluna - 1), #esquerda
            (linha, coluna + 1), #direita
        ]
        vizinhos_validos = []
        for l, c in candidatos:
            # Se não é uma casa ou hospital, pula
            if (l, c) in self.casas or (l, c) in self.solucao_encontrada:
                continue
            # Se está dentro das dimensões do espaço de estados, adiciona
            if 0 <= l < self.altura and 0 <= c < self.largura:
                vizinhos_validos.append((l, c))
        return vizinhos_validos

    def hill_climb(self, max_iteracoes=None, prefixo_imagem=None, gerar_log=False):
        """Executa o hill-climbing para encontrar uma solução."""
        # Inicializa o contador de iterações
        contador = 0
        # Inicializa a solução encontrada como uma cópia do estado inicial
        self.solucao_encontrada = self.hospitais.copy()
        # Executa até que o número máximo de iterações seja atingido
        # ou até que não sejam encontradas soluções candidatas melhores
        # com base no movimento dos hospitais pora sua vizinhança
        while max_iteracoes is None or contador < max_iteracoes:
            # Inicializa a lista de vizinhos melhores como uma lista vazia
            melhores_solucoes = []
            # Inicializa o melhor custo encontrado até o momento com o custo da solução inicial
            custo_melhor_solucao = self.obter_custo(self.solucao_encontrada)

            # Percorre cada um dos hospitais da melhor solução encontrada até o momento verifica
            # se sua movimentação para cada um dos vizinhos acarreta em uma solução melhor que a atual
            for hospital in self.solucao_encontrada:
                # Incrementa o contador de iterações
                contador += 1
                # Percorre todos os vizinhos possíveis do hospital atual
                # O asterisco é para desempacotar a tupla "hospital"
                # em dois argumentos: linha e coluna
                for vizinho in self.obter_vizinhos(*hospital):
                    # Gera uma cópia da lista de hospitais que representa a solução atual
                    solucao_candidata = self.solucao_encontrada.copy()
                    # Remove o hospital atual da solução candidata
                    solucao_candidata.remove(hospital)
                    # Adiciona um hospital a um dos espaços vizinhos possíveis
                    # do hospital atual, depois de remover o hospital original
                    solucao_candidata.add(vizinho)

                    # Computa o custo da nova configuração de hospitais
                    custo_solucao_candidata = self.obter_custo(solucao_candidata)
                    # Se o custo for menor que o melhor custo até agora
                    if custo_solucao_candidata < custo_melhor_solucao:
                        # O melhor custo encontrado até agora é atualizado
                        custo_melhor_solucao = custo_solucao_candidata
                        # A solução candidata é salva. A variável a seguir armazena
                        # uma lista em que cada elemento é uma lista de hospitais, pois pode haver
                        # mais de uma solução candidata, ou seja, configurações de hospitais com mesmo custo
                        melhores_solucoes = [solucao_candidata]
                    # Se o cussolut gnal ao melhor custo encontrado até agora
                    elif custo_melhor_solucao == custo_solucao_candidata:
                        # Adiciona a nova configuração de hospitais à lista
                        melhores_solucoes.append(solucao_candidata)

                # Se nessa iteração encontrou solução candidata melhor que a solução já encontrada,
                # atualiza a melhor solução computada até o momento e vai para a próxima iteração
                # do while, onde vai buscar soluções candidatas entre os vizinhos da nova melhor solução
                if custo_melhor_solucao < self.obter_custo(self.solucao_encontrada):
                    self.solucao_encontrada = random.choice(melhores_solucoes)
                    # Gera um log com o custo da melhor solução encontrada até o momento
                    if gerar_log:
                        print(
                            f"Encontrada uma melhor solução ao custo de {custo_melhor_solucao}."
                        )
                # Se não há nenhuma solução candidata melhor que a solução já encontrada, a busca local termina
                else:
                    return self.solucao_encontrada

                # Gera a imagem da solução atual
                if prefixo_imagem:
                    self.gerar_imagem(f"{prefixo_imagem}{str(contador).zfill(3)}.png")

    def random_restart(self, qtd_iteracoes, prefixo_imagem=None, gerar_log=False):
        """Repete varias """
        custo_melhor_solucao = float("inf")
        for i in range(qtd_iteracoes):
            self.inicializar_hospitais()
            hospitais = self.hill_climb()
            custo = self.obter_custo(hospitais)
            if custo < custo_melhor_solucao:
                custo_melhor_solucao = custo
                if gerar_log:
                    print(f"Encontrada uma melhor solução ao custo de {custo}")
                if prefixo_imagem:
                    self.gerar_imagem(f"{prefixo_imagem}{str(i+1).zfill(3)}.png")
        return self.solucao_encontrada        

    def gerar_imagem(self, nome_arquivo):
        """Gera uma imagem com todas as casas e hospitais."""
        from PIL import Image, ImageDraw, ImageFont

        cell_size = 100
        cell_border = 2
        cost_size = 40
        padding = 10

        # Cria um novo canvas em branco
        img = Image.new(
            "RGBA",
            (
                self.largura * cell_size,
                self.altura * cell_size + cost_size + padding * 2,
            ),
            "white",
        )
        house = Image.open("assets/images/House.png").resize((cell_size, cell_size))
        hospital = Image.open("assets/images/Hospital.png").resize(
            (cell_size, cell_size)
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 30)
        draw = ImageDraw.Draw(img)

        for i in range(self.altura):
            for j in range(self.largura):
                # Desenha a célula
                rect = [
                    (j * cell_size + cell_border, i * cell_size + cell_border),
                    (
                        (j + 1) * cell_size - cell_border,
                        (i + 1) * cell_size - cell_border,
                    ),
                ]
                draw.rectangle(rect, fill="black")

                if (i, j) in self.casas:
                    img.paste(house, rect[0], house)
                if (i, j) in self.solucao_encontrada:
                    img.paste(hospital, rect[0], hospital)

        # Adiciona o custo
        draw.rectangle(
            (
                0,
                self.altura * cell_size,
                self.largura * cell_size,
                self.altura * cell_size + cost_size + padding * 2,
            ),
            "black",
        )
        draw.text(
            (padding, self.altura * cell_size + padding),
            f"Custo: {self.obter_custo(self.solucao_encontrada)}",
            fill="white",
            font=font,
        )

        img.save(f"resultados/{nome_arquivo}")

    def simulated_annealing(self, temperatura_inicial=100, taxa_resfriamento=0.95, prefixo_imagem=None, gerar_log=False):
        contador = 0
        self.solucao_encontrada = self.hospitais.copy()
        custo_melhor_solucao = self.obter_custo(self.solucao_encontrada)
        while temperatura_inicial > 0.01:
            contador += 1
            solucao_candidata = list(self.solucao_encontrada)
            hospital_aleatorio = random.choice(solucao_candidata)
            vizinhos = self.obter_vizinhos(*hospital_aleatorio)
            vizinho_aleatorio = random.choice(vizinhos)
            solucao_candidata.remove(hospital_aleatorio)
            solucao_candidata.append(vizinho_aleatorio)
            custo_solucao_candidata = self.obter_custo(solucao_candidata)
            if custo_solucao_candidata < custo_melhor_solucao:
                self.solucao_encontrada, custo_melhor_solucao = (solucao_candidata, custo_solucao_candidata)
                if gerar_log:
                    print(f"Encontrada uma melhor solução ao custo de {custo_melhor_solucao}")
                if prefixo_imagem:
                    self.gerar_imagem(f"{prefixo_imagem}{str(contador+1).zfill(3)}.png")
            else:
                deltaE = custo_melhor_solucao - custo_solucao_candidata
                probabilidade = math.exp(deltaE/temperatura_inicial)
                if random.uniform(0,1) < probabilidade:
                    self.solucao_encontrada, custo_melhor_solucao = (solucao_candidata, custo_solucao_candidata)
                if gerar_log:
                    print(f"Encontrada uma melhor solução ao custo de {custo_melhor_solucao}")
                if prefixo_imagem:
                    self.gerar_imagem(f"{prefixo_imagem}{str(contador+1).zfill(3)}.png")
            temperatura_inicial *= taxa_resfriamento
        return self.solucao_encontrada



# Apagar todos os arquivos da pasta raiz que comecem com img_
for arquivo in os.listdir("./resultados"):
    if arquivo.startswith("img_"):
        os.remove(f"./resultados/{arquivo}")

# Cria um novo espaço 10x20 com 3 hospitais e adiciona 15 casas aleatoriamente
s = Space(altura=20, largura=20, qtde_casas=14, qtde_hospitais=4)

custo_solucao_inicial = s.obter_custo(s.hospitais)
print(f"Custo da solução inicial: {custo_solucao_inicial}")

# Usa busca local para determinar a localização dos hospitais
print("\nUsando busca local...")
hospitais = s.hill_climb(prefixo_imagem="img_hill_climb_", gerar_log=True)

#Usa o random restart hiil climb para determinar a localização dos hospitais
print("\nUsando random restart hill climb...")
hospitais = s.random_restart(
    qtd_iteracoes=100, prefixo_imagem="img_random_restart_", gerar_log=True
)

#Usa o random simulated annealing para determinar a localização dos hospitais
print("\nUsando random restart hill climb...")
hospitais = s.simulated_annealing(prefixo_imagem="img_sim_anneal_",gerar_log=True)