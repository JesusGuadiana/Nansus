# -----------------------------------------------------------------------------
#  Juan Fernando and Jesus’ Programming Language Lexer
#  Last edit: 14/11/2018
# -----------------------------------------------------------------------------

# Build the lexer
from functions.printToOutputFile import *
import ply.lex as lex
import os
import sys

# Reserved Words
reservedWords = {
'program'   :   'PRGM',
'main'      :   'MAIN',
'end'       :   'END',
'function'  :   'FUNCTION',
'while'     :   'WHILE',
'for'       :   'FOR',
'if'        :   'IF',
'else'      :   'ELSE',
'elseif'    :   'ELSEIF',
'print'     :   'PRINT',
'jedo'      :   'JEDO',
'circle'    :   'CIRCLE',
'square'    :   'SQUARE',
'rectangle' :   'RECTANGLE',
'forward'   :   'FORWARD',
'back'      :   'BACK',
'turnRight' :   'TURNRIGHT',
'turnLeft'  :   'TURNLEFT',
'color'     :   'COLOR',
'arch'      :   'ARCH',
'line'      :   'LINE',
'thickness' :   'THICKNESS',
'int'       :   'TYPEINT',
'float'     :   'TYPEFLOAT',
'char'      :   'TYPECHAR',
'void'      :   'NOTYPE'
}

#Token Definition
tokens = ['ID', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
        'CSTI','CSTF','EOS','LEFTP', 'RIGHTP', 'LEFTB', 
        'RIGHTB', 'LEFTBRACE', 'RIGHTBRACE', 'AND', 'OR',
        'SEPARATOR', 'POINT', 'EQUALS', 'GREATER', 'GREATEREQUAL',
        'LESS', 'LESSEQUAL', 'EQUAL', 'NOTEQUAL', 'INCREMENT']

#Add the reserved words to the token definition
tokens += reservedWords.values()

# Tokens RegEx for accepted values
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE =  r'/'
t_CSTI = r'\d+'
t_CSTF = r'\d*\.\d+'
t_EOS = r'\;'
t_LEFTP = r'\('
t_RIGHTP = r'\)'
t_LEFTB = r'\['
t_RIGHTB = r'\]'
t_LEFTBRACE = r'\{'
t_RIGHTBRACE = r'\}'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_SEPARATOR = r'\,'
t_POINT = r'\.'
t_EQUALS = r'\='
t_GREATER = r'\>'
t_GREATEREQUAL = r'\>\='
t_LESS = r'\<'
t_LESSEQUAL = r'\<\='
t_EQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
t_INCREMENT = r'\+\+'

#Only complex syntaxis token
def t_ID(t):
    r"[a-zA-Z][a-zA-Z0-9]*"
    t.type = reservedWords.get(t.value, 'ID')
    return t

# Ignored characters (tabs, blanks, new line)
t_ignore = " \t\n"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

#Executes Lexer
lexer = lex.lex()

#Resets compilerOutput.txt
file = open('compilerOutput.txt', 'w')
print_to_output_file("TOKENS GENERATED:\n")
file.close()

#Reads from test file
file = open('test.txt','r')
lexer.input(file.read())

#Cycles through token list
while True:
    tokenList = lexer.token()
    if not tokenList:
        break
    print_to_output_file(tokenList)