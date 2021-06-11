import ply.ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['ID', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EXP', 'ASSIGN', 'EQUALS', 'NE', 'GT',
          'LT', 'GE', 'LE', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON',
          'INT', 'FLOAT', 'STRING', 'BOOL', 'IF', 'ELSE', 'ELIF', 'WHILE', 'DO', 'FOR']

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
    'for': 'FOR'
}

t_ignore = '\t'
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

t_ID = r'[A-Za-z_][A-Za-z0-9_]*'
t_INT = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
t_STRING = r'\"([^\\\n]|(\\.))*?\"'
