# TPC 1
## Expressões Regulares

### Conteúdo do Exercício
Considere o ficheiro de texto tpc.txt em anexo, e responda às seguintes questões. Para este exercício, considere que um token é qualquer sequência de caracteres delimitada por caracteres de espaçamento (espaço em branco ou mudança de linha).

### Pergunta 1
Quantos tokens têm pelo menos dois pontos seguidos?

Expressão Regular: `( |\n)\S*\.\.\S*( |\n)` ou `\s\S*\.\.\S*\s` (caso não seja no VSCode)

R: 205

### Pergunta 2
Quantos tokens começam e acabam num símbolo de adição e têm apenas (pelo menos um) símbolos alfa-numéricos entre eles?

Expressão Regular: `( |\n)\+[a-zA-Z0-9]+\+( |\n)` ou `\s\+[a-zA-Z0-9]+\+\s` (caso não seja no VSCode)

R: 20