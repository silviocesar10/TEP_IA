<Instalar Extensão *Markdown All in One*>

### Fábrica de Chapas Polidas de Mármores e Granitos

Em Cachoeiro de Itapemirim, existem pedreiras onde mármore e granito brilham sob a luz do sol escaldante. Há uma fábrica especial, a "HotRock", que produz chapas polidas de mármore e granito.

**Detalhes da Produção:**
1. Uma chapa de mármore leva 3 horas para ser polida e rende um lucro de R$150.
2. Uma chapa de granito leva 2 horas para ser polida e rende um lucro de R$130.

**Restrições:**
1. A máquina de polimento só pode operar por no máximo 40 horas por semana.
2. Devido a acordos, a fábrica deve produzir pelo menos 5 chapas de mármore por semana.

**Objetivo:** 
A fábrica quer determinar quantas chapas de mármore e granito deve produzir para maximizar o lucro semanal, considerando as restrições de horas de operação e a exigência mínima de chapas de mármore.

### Formulação do Problema de Programação Linear:

**Variáveis de Decisão:**
- \(x<sub>1</sub>\): número de chapas de mármore produzidas por semana.
- \(x<sub>2</sub>\): número de chapas de granito produzidas por semana.

**Função Objetivo (Maximizar o lucro):**
\[Z = 150x<sub>1</sub> + 130x<sub>2</sub>\]

**Restrições:**
1. Tempo de polimento: \(3x<sub>1</sub> + 2x<sub>2</sub> $\le$ 40\)
2. Produção mínima de mármore: \(x<sub>1</sub> $\ge$ 5\)