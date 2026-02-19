from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

# Autómato finito determinístico (DFA)
dfa = DFA(allow_partial = False,
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b', 'c'}, 
    transitions={ 
        'q0': { 'c': 'q0', 'a' : 'q2', 'b' : 'q2' },
        'q2': { 'c': 'q0', 'a' : 'q3', 'b' : 'q3' },
        'q3': { 'a': 'q3', 'b' : 'q2', 'c' : 'q2' },
        'q1': { 'a': 'q1', 'b' : 'q1', 'c' : 'q3' } 
    },
    initial_state='q0',
    final_states={'q0'} )

# METER A INPUT STRING  AQUI
print(dfa.accepts_input("aabbcc"))

# Autómato finito não-determinístico (NFA)
nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b', 'c'},
    transitions={
        'q0': { 'a': {'q1', 'q2'}, 'c' : {'q1'} },
        'q2': { 'b': {'q2'}, 'c' : {'q1'}, 'a' : {'q0','q1'} },
        'q1': { 'c': {'q2'}, 'b' : {'q1', 'q0'} } 
    },
    initial_state='q0',
    final_states={'q0'} )

# METER A INPUT STRING  AQUI
print(nfa.accepts_input("ababab"))