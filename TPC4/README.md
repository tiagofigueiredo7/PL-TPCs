# TPC 4
## Gramáticas independentes de contexto (CFGs)

### Pergunta 1
Considere a seguinte gramática independente de contexto (CFG) com símbolo inicial S e terminais {a, b, c}.

`S → aSa | bSb | aa | bb`

Quais das seguintes palavras são geradas por esta CFG?
1. `aba`
2. `abba`
3. `aaabbb`
4. `baabbaab`

R:

---

### Pergunta 2
Considere a seguinte gramática independente de contexto (CFG) com símbolo inicial S e terminais {a, b, c}.

`S → aSa | bSb | a | b | ε`

Quais das seguintes palavras são geradas por esta CFG?
- [ ] `aabbaa`
- [ ] `aaaabb`
- [ ] `aabbbaa`
- [ ] `aabba`

R:

---

### Pergunta 3
Considere a seguinte gramática independente de contexto (CFG) com símbolo inicial S e terminais {a, b, c}.

`S → aSa | bSb | A`
`A → cAc | B`
`B → aB | ε`

Quais das seguintes palavras são geradas por esta CFG?

1. `cbaabc`
2. `abaaaba`
3. `ccc`
4. `cac`

R:

$$
f(x) = \begin{cases}
1 & \text{se } x \text{ é gerada pela CFG} \\
0 & \text{caso contrário}
\end{cases}
$$