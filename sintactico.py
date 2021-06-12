from semantico import *

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

"""
def p_intDecl(p):
    '''intDecl: INT intAssignmentList '''
    print("intDecl")
    p[0] = intDecl(INT(p[1]), intAssignmentList(p[2]), "intDecl")


def p_floatDecl(p):
    '''floatDecl: FLOAT floatAssignmentList '''
    print("floatDecl")
    p[0] = floatDecl(FLOAT(p[1]), floatAssignmentList(p[2]), "floatDecl")

"""

"""
def p_stringDecl(p):
    '''stringDecl: STRING stringAssignmentList'''
    print("stringDecl")
    p[0] = stringDecl(STRING(p[1]), stringAssignmentList(p[2]), "stringDecl")
"""


def p_intAssignmentList(p):
    '''intAssignmentList : ID ASSIGN INT SEMICOLON'''
    print("intAssignmentList1")
    p[0] = intAssignmentList(ID(p[1]), ASSIGN(
        p[2]), INT(p[3]), "intAssignmentList")


def p_floatAssignmentList(p):
    '''floatAssignmentList : ID ASSIGN FLOAT SEMICOLON'''
    print("floatAssignmentList1")
    p[0] = floatAssignmentList(ID(p[1]), ASSIGN(
        p[2]), FLOAT(p[3]), "floatAssignmentList")


def p_stringAssignmentList(p):
    '''stringAssignmentList : ID ASSIGN STRING SEMICOLON'''
    print("stringAssignmentList")
    p[0] = stringAssignmentList(ID(p[1]), ASSIGN(
        p[2]), INT(p[3]), "stringAssignmentList")


def p_identList(p):
    '''identList : ID '''
    print("identList")
    p[0] = identList(ID(p[1]), "identList")


def p_statement1(p):
    '''statement : IF LPAREN condition RPAREN LBRACE statement RBRACE'''
    print("statemen1")
    p[0] = statement1(p[3], p[6], "statement1")


def p_statement2(p):
    '''statement : WHILE LPAREN condition RPAREN LBRACE statement RBRACE'''
    print("statement2")
    p[0] = statement2(p[3], p[6], "statement2")


def p_statement3(p):
    '''statement : DO LBRACE statement RBRACE WHILE LPAREN condition RPAREN SEMICOLON'''
    print("statement3")
    p[0] = statement3(p[3], p[7], "statement3")


def p_statement4(p):
    '''statement : IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE'''
    print("statement4")
    p[0] = statement4(p[3], p[6], p[10], "statement4")


def p_statementEmpty(p):
    '''statement : empty'''
    print("empty")
    p[0] = NULL()


def p_statementList(p):
    '''statement : statement'''
    print("statementList")
    p[0] = statementList(p[1], "statementList")


def p_condition(p):
    '''condition : expression relation expression'''
    print("condition")
    p[0] = condition(p[1], p[2], p[3], condition)


def p_relation1(p):
    '''relation : ASSIGN'''
    print("relation1")
    p[0] = relation1(ASSIGN(p[1]), "relation1")


def p_relation2(p):
    '''relation : EQUALS '''
    print("relation2")
    p[0] = relation2(EQUALS(p[1]), "relation2")


def p_relation3(p):
    '''relation : NE'''
    print("relation3")
    p[0] = relation3(NE(p[1]), "relation3")


def p_relation4(p):
    '''relation : GT'''
    print("relation4")
    p[0] = relation4(GT(p[1]), "relation4")


def p_relation5(p):
    '''relation : LT'''
    print("relation5")
    p[0] = relation5(LT(p[1]), "relation5")


def p_relation6(p):
    '''relation : GE'''
    print("relation6")
    p[0] = relation6(GE(p[1]), "relation6")


def p_relation7(p):
    '''relation : LE'''
    print("relation7")
    p[0] = relation7(LE(p[1]), "relation7")


def p_expression1(p):
    '''expression : terms'''
    print("expression1")
    p[0] = expression1(p[1], "expression1")


def p_expression2(p):
    '''expression : addOp terms'''
    print("expression2")
    p[0] = expression2(p[1], p[2], "expression2")


def p_expression3(p):
    '''expression : multOp terms'''
    print("expression3")
    p[0] = expression3(p[1], p[2], "expression3")


def p_expression4(p):
    '''expression : expression addOp terms'''
    print("expression4")
    p[0] = expression4(p[1], p[2], p[3], "expression4")


def p_expression5(p):
    '''expression : expression multOp terms'''
    print("expression5")
    p[0] = expression5(p[1], p[2], p[3], "expression5")


def p_addOp1(p):
    '''addOp : PLUS'''
    print("addOp1")
    p[0] = addOp1(PLUS(p[0]), "addOp1")


def p_addOp2(p):
    '''addOp : MINUS'''
    print("addOp2")
    p[0] = addOp2(MINUS(p[0]), "addOp2")


def p_multOp1(p):
    '''multOp : TIMES'''
    print("multOp1")
    p[0] = multOp1(TIMES(p[0]), "multOp1")


def p_multOp2(p):
    '''multOp : DIVIDE'''
    print("multOp2")
    p[0] = multOp2(DIVIDE(p[0]), "multOp2")


def p_terms1(p):
    '''terms : factor'''
    print("terms1")
    p[0] = terms1(p[1], "terms1")


def p_terms2(p):
    '''terms : terms addOp factor'''
    print("terms2")
    p[0] = terms2(p[1], p[2], p[3], "terms2")


def p_terms3(p):
    '''terms : terms multOp factor'''
    print("terms3")
    p[0] = terms3(p[1], p[2], p[3], "terms3")


def p_factor1(p):
    '''factor : ID'''
    print("factor1")
    p[0] = factor1(ID(p[1]), "factor1")


def p_factor2(p):
    '''factor : INT'''
    print("factor2")
    p[0] = factor2(INT(p[1]), "factor2")


def p_factor3(p):
    '''factor : FLOAT'''
    print("factor3")
    p[0] = factor3(FLOAT(p[1]), "factor3")


def p_factor4(p):
    '''factor : STRING'''
    print("factor4")
    p[0] = factor4(STRING(p[1]), "factor4")


def p_factor5(p):
    '''factor : LPAREN expression RPAREN'''
    print("factor5")
    p[0] = factor5(p[2], "factor5")


def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    print("error de sintaxis", p)
    print("error en la linea" + str(p.lineno))


route = sys.argv[-1]

if len(sys.argv) != 2:
    print("Importante: python lexico.py <NombreArchivoALeer>")
    sys.exit(0)

filename = codecs.open(route, "r", "utf-8")
texto = filename.read()
filename.close()

yacc.yacc()
resultados = yacc.parse(texto)

print(resultados)

"""
newfile = codecs.open("tree.txt", "w")

newfile.write(resultados)

newfile.close()

print(resultados)
"""
