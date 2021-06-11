import ply.ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['ID', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EXP', 'ASSIGN', 'EQUALS', 'NE', 'GT',
          'LT', 'GE', 'LE', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON',
          'INT', 'FLOAT', 'STRING', 'BOOL', 'IF', 'ELSE', 'ELIF', 'WHILE', 'DO', 'FOR', 'TRUE', 'FALSE']

reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'bool': 'BOOL',
    'if': 'IF',
    'else': 'ELSE',
    'elif': 'ELIF',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'true': 'TRUE',
    'false': 'FALSE'
}

t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXP = r'\^'
t_ASSIGN = r'='
t_EQUALS = r'=='
t_NE = r'!='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


t_INT = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
t_STRING = r'\"([^\\\n]|(\\.))*?\"'

lexico = lex.lex()

route = sys.argv[-1]

if len(sys.argv) != 2:
    print("Importante: python lexico.py <NombreArchivoALeer>")
    sys.exit(0)

filename = codecs.open(route, "r", "utf-8")
texto = filename.read()
filename.close()

lexico.input(texto)

newfile = codecs.open("lex.txt", "w", "utf-8")

while True:
    tok = lexico.token()
    if not tok:
        break
    newfile.write(tok.type+" ")
