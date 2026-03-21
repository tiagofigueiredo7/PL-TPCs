# TPC 5
## Gramáticas LL(1)

### Pergunta 1
O que pode concluir sobre a condição LL(1) relativamente à gramática abaixo?

`S → A B`

`A → 'd' | ε`

`B → 'd' B | 'f'`

- [ ]Não tem conflitos
- [ ]Tem conflitos FIRST/FIRST
- [x]Tem conflitos FIRST/FOLLOW

```
Calcular FIRST e FOLLOW:

FIRST(A) = { 'd', ε }
FIRST(B) = { 'd', 'f' }
FIRST(S) = FIRST(A B) = { 'd' } ∪ (como A pode ser ε) FIRST(B) = { 'd', 'f' }

FOLLOW(S) = { $ }
FOLLOW(A) = FIRST(B) = { 'd', 'f' }
FOLLOW(B) = FOLLOW(S) = { $ }

Verificar conflitos em A → 'd' | ε:
A tem duas produções onde uma deriva ε, por isso aplica-se a condição FIRST/FOLLOW.
É necessário verificar se FIRST('d') ∩ FOLLOW(A) = ∅:
FIRST('d') = { 'd' } e FOLLOW(A) = { 'd', 'f' }
{ 'd' } ∩ { 'd', 'f' } = { 'd' } ≠ ∅ → Conflito FIRST/FOLLOW!
```

### Pergunta 2
O que pode concluir sobre a condição LL(1) relativamente à gramática abaixo?

`S → A | B`

`A → 'a' A | C`

`B → 'a' B | D`

`C → 'x'`

`D → 'y'`

- [ ]Não tem conflitos
- [x]Tem conflitos FIRST/FIRST
- [ ]Tem conflitos FIRST/FOLLOW

```
Calcular FIRST:

FIRST(C) = { 'x' }
FIRST(D) = { 'y' }
FIRST(A) = { 'a', 'x' }
FIRST(B) = { 'a', 'y' }
FIRST(S) = FIRST(A) ∪ FIRST(B) = { 'a', 'x', 'y' }

Verificar conflitos em S → A | B:
FIRST(A) ∩ FIRST(B) = { 'a', 'x' } ∩ { 'a', 'y' } = { 'a' } ≠ ∅ → Conflito FIRST/FIRST!
Ao ver 'a', o parser não consegue decidir se expande S → A ou S → B.

Verificar conflitos em A → 'a' A | C:
FIRST('a' A) ∩ FIRST(C) = { 'a' } ∩ { 'x' } = ∅ → sem conflito.

Verificar conflitos em B → 'a' B | D:
FIRST('a' B) ∩ FIRST(D) = { 'a' } ∩ { 'y' } = ∅ → sem conflito.
```
