
## Exemplos Conhecidos de Filtros de Convolução 3x3

Filtros de convolução 3x3 são amplamente utilizados em processamento de imagens e redes neurais convolucionais (CNNs) para diversas operações, como detecção de bordas, desfoque e realce. Aqui estão alguns exemplos conhecidos de filtros de convolução 3x3:

01. **Filtro de Borda Sobel (Sobel Edge Detection Filter) - Horizontal**:
   ```
   -1  0  1
   -2  0  2
   -1  0  1
   ```
   Este filtro é usado para destacar as bordas horizontais em uma imagem.

02. **Filtro de Borda Sobel - Vertical**:
   ```
   -1 -2 -1
    0  0  0
    1  2  1
   ```
   Semelhante ao filtro Sobel horizontal, mas focado em detectar bordas verticais.

03. **Filtro de Borda Prewitt - Horizontal**:
   ```
   -1  0  1
   -1  0  1
   -1  0  1
   ```
   Um filtro de detecção de borda que é semelhante ao Sobel, mas usa pesos iguais para os pixels.

04. **Filtro de Borda Prewitt - Vertical**:
   ```
   -1 -1 -1
    0  0  0
    1  1  1
   ```
   Usado para detectar bordas verticais, com pesos iguais para os pixels.

05. **Filtro de Nitidez (Sharpen Filter)**:
   ```
    0 -1  0
   -1  5 -1
    0 -1  0
   ```
   Este filtro ajuda a tornar a imagem mais nítida, realçando as transições de intensidade.

06. **Filtro de Desfoque de Caixa (Box Blur Filter)**:
   ```
   1/9  1/9  1/9
   1/9  1/9  1/9
   1/9  1/9  1/9
   ```
   Um filtro de suavização simples que aplica um desfoque uniforme à imagem.

07. **Filtro de Desfoque Gaussiano (Gaussian Blur Filter)**:
   ```
   1  2  1
   2  4  2
   1  2  1
   ```
   Este filtro aplica um desfoque Gaussiano, que é útil para reduzir o ruído da imagem. Geralmente, os valores são normalizados (divididos pela soma de todos os valores no kernel).

08. **Filtro de Detecção de Borda Laplaciano (Laplacian Edge Detector)**:
   ```
   0 -1  0
   -1  4 -1
   0 -1  0
   ```
   Um filtro que detecta bordas em todas as direções, enfatizando regiões de rápida mudança de intensidade.

09. **Filtro de Borda de Scharr**:
   ```
   -3  0  3
   -10 0 10
   -3  0  3
   ```
   e
   ```
    -3 -10 -3
     0   0  0
     3  10  3
   ```

10. **Filtro de Realce de Bordas**:
   ```
    0 -1  0
   -1  5 -1
    0 -1  0
   ```

11. **Filtro de Desfoque de Movimento (Motion Blur)**:
   ```
   1/9 1/9 1/9
   1/9 1/9 1/9
   1/9 1/9 1/9
   ```

12. **Filtro de Suavização (Smoothing Filter)**:
   ```
   1/25 1/25 1/25 1/25 1/25
   1/25 1/25 1/25 1/25 1/25
   1/25 1/25 1/25 1/25 1/25
   1/25 1/25 1/25 1/25 1/25
   1/25 1/25 1/25 1/25 1/25
   ```

13. **Filtro de Média Ponderada**:
   ```
   1 2 1
   2 4 2
   1 2 1
   ```

14. **Filtro de Aresta Laplaciana**:
   ```
   -1 -1 -1
   -1  8 -1
   -1 -1 -1
   ```

15. **Filtro High Boost**:
   ```
   -1 -1 -1
   -1  a -1
   -1 -1 -1
   ```
   Onde `a` é um fator de realce.