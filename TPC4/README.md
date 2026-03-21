# TPC 4
## Gramáticas independentes de contexto (CFGs)

### Pergunta 1
Considere a seguinte gramática independente de contexto (CFG) com símbolo inicial S e terminais {a, b, c}.

`S → aSa | bSb | aa | bb`

Quais das seguintes palavras são geradas por esta CFG?
- [ ] `aba`
- [x] `abba`
- [ ] `aaabbb`
- [x] `baabbaab`

```
S => aSa => abba

S => bSb => baSab => baaSaab => baabbaab
```

---

### Pergunta 2
Considere a seguinte gramática independente de contexto (CFG) com símbolo inicial S e terminais {a, b, c}.

`S → aSa | bSb | a | b | ε`

Quais das seguintes palavras são geradas por esta CFG?
- [x] `aabbaa`
- [ ] `aaaabb`
- [x] `aabbbaa`
- [ ] `aabba`

```
S => aSa => aaSaa => aabSbaa => aabbaa

S => aSa => aaSaa => aabSbaa => aabbbaa
```

---

### Pergunta 3
Considere a seguinte gramática independente de contexto (CFG) com símbolo inicial S e terminais {a, b, c}.

`S → aSa | bSb | A`

`A → cAc | B`

`B → aB | ε`

Quais das seguintes palavras são geradas por esta CFG?

- [ ] `cbaabc`
- [x] `abaaaba`
- [ ] `ccc`
- [x] `cac`

```
S => aSa => abSba => abaSaba => abaAaba => abaBaba => abaaBaba => abaaaba

S => A => cAc => cBc => caBc => cac
```
