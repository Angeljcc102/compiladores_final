import ply.ply.yacc as yacc

import codecs
import re

precedence = (
    ('right', 'ASSIGN'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQUALS', 'NE'),
    ('left', 'GT', 'LT', 'GE', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'EXP'),
    ('left', 'LPAREN', 'RPAREN'),
    ('left', 'LBRACE', 'RBRACE'),
)
