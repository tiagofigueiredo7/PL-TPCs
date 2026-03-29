# TPC 6
## Parser recursivo descendente

### Pergunta 1
Considere a gramática abaixo para representar árvores binárias com valores nos nós e nas folhas. Escreva um parser recursivo descendente para calcular a profundidade máxima da árvore dada em anexo. Considere que as folhas têm profundidade 1.

```
Tree → BOOL Tree Tree

    | INT
```
R: 32

## Testar
Para testar o parser, basta executar o comando abaixo no terminal:

```
python3 script.py
```