import ply.ply.yacc as yacc

import codecs
import re
import sys

from lexico import tokens

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


def p_intDecl(p):
    '''intDecl : INT intAssignmentList '''
    print("intDecl")


def p_floatDecl(p):
    '''floatDecl : FLOAT floatAssignmentList '''
    print("floatDecl")


def p_stringDecl(p):
    '''stringDecl : STRING stringAssignmentList '''
    print("stringDecl")


def p_intAssignmentList(p):
    '''intAssignmentList : ID ASSIGN INT SEMICOLON'''
    print("intAssignmentList1")


def p_floatAssignmentList(p):
    '''floatAssignmentList : ID ASSIGN FLOAT SEMICOLON'''
    print("floatAssignmentList1")


def p_stringAssignmentList(p):
    '''stringAssignmentList : ID ASSIGN STRING SEMICOLON'''


def p_identList(p):
    '''identList : ID '''
    print("identList")


def p_statement1(p):
    '''statement : IF LPAREN condition RPAREN LBRACE statement RBRACE'''
    print("statemen1")


def p_statement2(p):
    '''statement : WHILE LPAREN condition RPAREN LBRACE statement RBRACE'''
    print("statement2")


def p_statement3(p):
    '''statement : DO LBRACE statement RBRACE WHILE LPAREN condition RPAREN SEMICOLON'''
    print("statement3")


"""
for statement
def p_statement3(p):
    '''statement: FOR LPAREN intDecl SEMICOLON condition SEMICOLON
"""


def p_statement4(p):
    '''statement : IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE'''
    print("statement4")


def p_statement5(p):
    '''statement : empty'''
    print("empty")


def p_statementList(p):
    '''statement : statement'''
    print("statementList")


def p_condition(p):
    '''condition : expression relation expression'''
    print("condition")


def p_relation1(p):
    '''relation : ASSIGN'''
    print("relation1")


def p_relation2(p):
    '''relation : EQUALS '''
    print("relation2")


def p_relation3(p):
    '''relation : NE'''
    print("relation3")


def p_relation4(p):
    '''relation : GT'''
    print("relation4")


def p_relation5(p):
    '''relation : LT'''
    print("relation5")


def p_relation6(p):
    '''relation : GE'''
    print("relation6")


def p_relation7(p):
    '''relation : LE'''
    print("relation7")


def p_expression1(p):
    '''expression : terms'''
    print("expression1")


def p_expression2(p):
    '''expression : addOp terms'''
    print("expression2")


def p_expression3(p):
    '''expression : multOp terms'''
    print("expression3")


def p_expression3(p):
    '''expression : expression addOp terms'''
    print("expression3")


def p_addOp1(p):
    '''addOp : PLUS'''
    print("addOp1")


def p_addOp2(p):
    '''addOp : MINUS'''
    print("addOp2")


def p_multOp1(p):
    '''multOp : TIMES'''
    print("multOp1")


def p_multOp2(p):
    '''multOp : DIVIDE'''
    print("multOp2")


def p_terms1(p):
    '''terms : factor'''
    print("terms1")


def p_terms2(p):
    '''terms : terms addOp factor'''
    print("terms2")


def p_terms3(p):
    '''terms : terms multOp factor'''
    print("terms3")


def p_factor1(p):
    '''factor : ID'''
    print("factor1")


def p_factor2(p):
    '''factor : INT'''
    print("factor2")


def p_factor3(p):
    '''factor : FLOAT'''
    print("factor3")


def p_factor4(p):
    '''factor : STRING'''
    print("factor4")


def p_factor5(p):
    '''factor : LPAREN expression RPAREN'''
    print("factor5")


def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    print("error de sintaxis", p)
    print("error en la linea" + str(p.lineno))


parser = yacc.yacc()

route = sys.argv[-1]

if len(sys.argv) != 2:
    print("Importante: python lexico.py <NombreArchivoALeer>")
    sys.exit(0)

filename = codecs.open(route, "r", "utf-8")
texto = filename.read()
filename.close()

resultados = parser.parse(texto)

newfile = codecs.open("lex.txt", "w", "utf-8")

print(resultados)
