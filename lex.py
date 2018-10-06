# -----------------------------------------------------------------------------
# nansus.py
#
#  Nando and Jesus’ Programming Language
# -----------------------------------------------------------------------------
# Build the lexer
import ply.lex as lex

tokens = ( "ID", "PLUS", "MINUS", "MULTIPLY", "DIVIDE",
        "CSTI","CSTF", "PRGM", "MAIN", "END", "FUNCTION",
        "EOS","LEFTP", "RIGHTP", "LEFTB", "RIGHTB", "WHILE",
        "FOR","IF", "ELSE", "ELSEIF", "PRINT", "AND",
        "OR", "JEDO","CIRCLE", "SQUARE", "RECTANGLE", "FORWARD",
        "BACK", "TURNRIGHT", "TURNLEFT", "COLOR", "ARCH", "LINE",
        "THICKNESS","SEPARATOR", "POINT", "EQUALS", "TYPEINT",
        "TYPEFLOAT", "TYPECHAR", "STRING", "NOTYPE", "GREATER",
        "GREATEREQUAL","LESS", "LESSEQUAL", "EQUAL", "NOTEQUAL", "EMPTY")

# Tokens
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE =  r'/'
t_CSTI = r'\d+'
t_CSTF = r'\d*\.\d+'
t_PRGM = r'program'
t_MAIN = r'main'
t_END = r'end'
t_FUNCTION = r'function'
t_WHILE = r'while'
t_FOR = r'for'
t_IF = r'if'
t_ELSE = r'else'
t_ELSEIF = r'elseif'
t_PRINT = r'print'
t_EOS = r'\;'
t_LEFTP = r'\('
t_RIGHTP = r'\)'
t_LEFTB = r'\['
t_RIGHTB = r'\]'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_JEDO = r'jedo'
t_CIRCLE = r'circle'
t_SQUARE = r'square'
t_RECTANGLE = r'rectangle'
t_FORWARD = r'forward'
t_BACK = r'back'
t_TURNRIGHT = r'turnRight'
t_TURNLEFT = r'turnLeft'
t_COLOR = r'color'
t_ARCH = r'arch'
t_LINE = r'line'
t_THICKNESS = r'thickness'
t_SEPARATOR = r'\,'
t_POINT = r'\.'
t_EQUALS = r'\='
t_TYPEFLOAT = r'float'
t_TYPECHAR = r'char'
t_STRING = r'\”.*\”'
t_NOTYPE = r'void'
t_GREATER = r'\>'
t_GREATEREQUAL = r'\>\='
t_LESS = r'\<'
t_LESSEQUAL = r'\<\='
t_EQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
t_TYPEINT = r'int'
T_EMPTY = r'empty'

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
