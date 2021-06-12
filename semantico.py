
counter = 0

text = " "


def increaseCount():
    global counter
    counter += 1
    return "%d" % counter


class Node():
    pass


class NULL(Node):
    def __init__(self):
        self.n

    def translate(self):
        global text
        id = increaseCount()
        text += id + 'null\n'

        return id


class intDecl(Node):
    def __init__(self, leaf1, leaf2, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"

        return id


class floatDecl(Node):
    def __init__(self, name, leaf1, leaf2):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"

        return id


class stringDecl(Node):
    def __init__(self,  leaf1, leaf2, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"

        return id


class intAssignmentList(Node):
    def __init__(self, leaf1, leaf2, leaf3, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2
        self.leaf3 = leaf3

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()
        leaf3 = self.leaf3.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"
        text += id + leaf3 + "\n"

        return id


class floatAssignmentList(Node):
    def __init__(self, leaf1, leaf2, leaf3, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2
        self.leaf3 = leaf3

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()
        leaf3 = self.leaf3.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"
        text += id + leaf3 + "\n"

        return id


class stringAssignmentList(Node):
    def __init__(self, leaf1, leaf2, leaf3, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2
        self.leaf3 = leaf3

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()
        leaf3 = self.leaf3.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"
        text += id + leaf3 + "\n"

        return id


class identList(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class statement1(Node):
    def __init__(self, leaf1, leaf2, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf1 = leaf2

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"

        return id


class statement2(Node):
    def __init__(self, leaf1, leaf2, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"

        return id


class statement3(Node):
    def __init__(self, leaf1, leaf2, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"

        return id


class statement4(Node):
    def __init__(self, leaf1, leaf2, leaf3, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2
        self.leaf3 = leaf3

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()
        leaf3 = self.leaf3.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"
        text += id + leaf3 + "\n"

        return id


class statementList(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class condition(Node):
    def __init__(self, leaf1, leaf2, leaf3, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2
        self.leaf3 = leaf3

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()
        leaf3 = self.leaf3.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"
        text += id + leaf3 + "\n"

        return id


class relation1(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class relation2(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class relation3(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class relation4(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class relation5(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class relation6(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class relation7(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class expression1(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class expression2(Node):
    def __init__(self, leaf1, leaf2, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"

        return id


class expression3(Node):
    def __init__(self, leaf1, leaf2, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"

        return id


class expression4(Node):
    def __init__(self, leaf1, leaf2, leaf3, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2
        self.leaf3 = leaf3

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()
        leaf3 = self.leaf3.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"
        text += id + leaf3 + "\n"

        return id


class expression5(Node):
    def __init__(self, leaf1, leaf2, leaf3, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2
        self.leaf3 = leaf3

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()
        leaf3 = self.leaf3.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"
        text += id + leaf3 + "\n"

        return id


class addOp1(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class addOp2(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class multOp1(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class multOp2(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class terms1(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class terms2(Node):
    def __init__(self, leaf1, leaf2, leaf3, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2
        self.leaf3 = leaf3

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()
        leaf3 = self.leaf3.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"
        text += id + leaf3 + "\n"

        return id


class terms3(Node):
    def __init__(self, leaf1, leaf2, leaf3, name):
        self.name = name
        self.leaf1 = leaf1
        self.leaf2 = leaf2
        self.leaf3 = leaf3

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()
        leaf2 = self.leaf2.translate()
        leaf3 = self.leaf3.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"
        text += id + leaf2 + "\n"
        text += id + leaf3 + "\n"

        return id


class factor1(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class factor2(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class factor3(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class factor4(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class factor5(Node):
    def __init__(self, leaf1, name):
        self.name = name
        self.leaf1 = leaf1

    def translate(self):
        global text
        id = increaseCount()

        leaf1 = self.leaf1.translate()

        text += id + self.name + "\n"
        text += id + leaf1 + "\n"

        return id


class empty(Node):
    def __init__(self, name):
        self.name = name

    def translate(self):
        global text
        id = increaseCount()

        return id


class ID(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class PLUS(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class MINUS(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class TIMES(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class DIVIDE(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class ASSIGN(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class EQUALS(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class NE(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class GT(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class LT(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class GE(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class LE(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class INT(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class FLOAT(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id


class STRING(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + str(self.name))

    def translate(self):
        global text
        id = increaseCount()
        text += id + self.name + "\n"

        return id
