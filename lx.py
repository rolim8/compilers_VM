import ply.lex as lex

keywords = {'if', 'while', 'func', 'return'}

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',

    'ID',
    'ATTRIB',
    'SEMICOLON',
    'COMMA',
    'RETURN',

    'IF',
    'WHILE',
    'FUNC',

    'LPAREN',
    'RPAREN',
    'LBR',
    'RBR',
    'LT',
    'RT',
    'LTE',
    'RTE',
    'DOUBLEEQUALS',
    'NE',
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_ATTRIB = r'='
t_SEMICOLON = r';'
t_COMMA = r','

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBR = r'{'
t_RBR = r'}'
t_LT = r'<'
t_RT = r'>'
t_LTE = r'<='          # NEW
t_RTE = r'>='          # NEW
t_DOUBLEEQUALS = r'==' # NEW
t_NE = r'!='           # NEW

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_]\w*'
    if t.value in keywords:
        t.type = t.value.upper()
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
