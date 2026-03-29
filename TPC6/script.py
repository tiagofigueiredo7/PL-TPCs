import ply.lex as lex

tokens = ("BOOL", "INT")

t_BOOL = r"T|F"
t_INT = r"\d+"

t_ignore = " \t\n"

def t_error(t):
    raise ValueError("Invalid symbol:", t.value[0])

lookahead = None

def next_token():
    tok = lexer.token()
    global lookahead
    if tok:
        lookahead = (tok.type, tok.value)
    else:
        lookahead = ("$", None)

lexer = lex.lex()

def recognize_Terminal(expected):
    tok_type, tok_value = lookahead
    if tok_type == expected:
        next_token()
        return tok_value
    else:
        raise ValueError("Expected token type:", expected, "but got:", tok_type)
    
def recognize_Tree():
    tok_type, tok_value = lookahead
    if tok_type == "BOOL":
        recognize_Terminal("BOOL")
        left_depth = recognize_Tree()
        right_depth = recognize_Tree()
        return 1 + max(left_depth, right_depth)
    elif tok_type == "INT":
        recognize_Terminal("INT")
        return 1
    else:
        raise ValueError("Expected token type: BOOL or INT, but got:", tok_type)
    
def parse(input_string):
    lexer.input(input_string)
    next_token()
    return recognize_Tree()

if __name__ == "__main__":
    import sys
    import os
    
    sys.setrecursionlimit(100000)
    
    file_path = os.path.join(os.path.dirname(__file__), "tpc6_9.lst")
    
    with open(file_path, "r") as f:
        content = f.read()
        
    depth = parse(content)
    print("Profundidade maxima: " + str(depth))
    