# AST: Expresion puede ser una BinOp, Id o Num

'''
AST
<Expr> ::
BinOp('+', expr1, expr2) |
BinOp('-', expr1, expr2) |
BinOp('*', expr1, expr2) |
BinOp('/', expr1, expr2) |
Num(n) |
Id(symbol)
'''
import random

from Global import min_number, max_number, MAX_DEPTH
from Math import sumar_num, restar_num, dividir_num, multip_num


class BinOp:
    """ Contiene una operacion (String, +,  -, * y /), y dos Expresiones las cuales sumar."""

    def __init__(self, op, expr1, expr2):
        """BinOp :: String x Expr x Expr -> BinOp
        """
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.op == other.op and \
                   self.expr1 == other.expr1 and \
                   self.expr2 == other.expr2
        return False


class Id:
    """ Contiene un String de Python"""

    def __init__(self, symbol):
        """ Id :: String -> Id"""
        self.symbol = symbol

    def __hash__(self):
        # Para usar directamente como key de dict
        return hash(self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.symbol == other.symbol
        return False

    def __ne__(self, other):
        return not (self == other)


class Num:
    """ Contenedor para un Integer de python"""

    def __init__(self, number):
        """Num :: Int -> Num"""
        self.value = number

    def __eq__(self, other):
        # Metodo __eq__ para comparar con ==
        if isinstance(other, self.__class__):
            return self.value == other.value
        return False


class Ast:
    @staticmethod
    def interp_expr(expr, xval):
        """interp :: Expr x Float -> Float
        Toma una Expresion y valor de X, e interpreta (evalua) la Expresion  retornando el Valor resultante."""

        if expr.__class__.__name__ == 'Num':
            return expr.value

        elif expr.__class__.__name__ == 'Id':
            return xval

        elif expr.__class__.__name__ == 'BinOp' and expr.op == '+':
            left_val = Ast.interp_expr(expr.expr1, xval)
            right_val = Ast.interp_expr(expr.expr2, xval)
            return sumar_num(left_val, right_val)

        elif expr.__class__.__name__ == 'BinOp' and expr.op == '-':
            left_val = Ast.interp_expr(expr.expr1, xval)
            right_val = Ast.interp_expr(expr.expr2, xval)
            return restar_num(left_val, right_val)

        elif expr.__class__.__name__ == 'BinOp' and expr.op == '/':
            left_val = Ast.interp_expr(expr.expr1, xval)
            right_val = Ast.interp_expr(expr.expr2, xval)
            return dividir_num(left_val, right_val)

        elif expr.__class__.__name__ == 'BinOp' and expr.op == '*':
            left_val = Ast.interp_expr(expr.expr1, xval)
            right_val = Ast.interp_expr(expr.expr2, xval)
            return multip_num(left_val, right_val)

        else:
            print("error: Not matching clause for " + str(expr))
            raise Exception

    @staticmethod
    def print_expr(expr, prefix):
        """interp :: Expr x Float -> Float
        Toma una Expresion y valor de X, e interpreta (evalua) la Expresion  retornando el Valor resultante."""

        if expr.__class__.__name__ == 'Num':
            if expr.value < 0:
                print("(" + str(expr.value) + ")")
            else:
                print(str(expr.value))

        elif expr.__class__.__name__ == 'Id':
            print(expr.symbol)

        elif expr.__class__.__name__ is "BinOp":
            print("( " + expr.op + " )")
            print(prefix + "|--", end='')
            Ast.print_expr(expr.expr1, prefix + "|  ")
            print(prefix + "└--", end='')
            Ast.print_expr(expr.expr2, prefix + "  ")

        else:
            print("error: Not matching clause for " + str(expr.__class__.__name__))
            raise Exception

    @staticmethod
    def random_ast(max_depth):
        """ random_ast :: None -> Expr (root)
        Genera un AST aleatorio, concatenando nodos (funciones y/o terminales) hasta que no se puedan más, 
        o hasta que se cumpla la profundidad maxima.

        :return: 
        """

        if max_depth <= 0:  # caso base, elijo un terminal random
            if random.random() < 0.5:  # terminal es numero
                return Num(random.uniform(min_number, max_number))
            else:
                return Id('x')
        else:  # caso recursivo, elijo funcion o terminal random
            rand = random.random()
            prob = 1.0 / 6  # distribucion uniforme
            if rand <= prob:
                return Num(random.uniform(min_number, max_number))
            elif rand <= prob * 2:
                return Id('x')
            elif rand <= prob * 3:
                return BinOp('+', Ast.random_ast(max_depth - 1), Ast.random_ast(max_depth - 1))
            elif rand <= prob * 4:
                return BinOp('-', Ast.random_ast(max_depth - 1), Ast.random_ast(max_depth - 1))
            elif rand <= prob * 5:
                return BinOp('/', Ast.random_ast(max_depth - 1), Ast.random_ast(max_depth - 1))
            else:
                return BinOp('*', Ast.random_ast(max_depth - 1), Ast.random_ast(max_depth - 1))

    def __init__(self):
        self.root_expr = Ast.random_ast(MAX_DEPTH)

    def evaluate(self, xval):
        return Ast.interp_expr(self.root_expr, xval)

    def print(self):
        Ast.print_expr(self.root_expr, "")

    # def copy(self):




    def mutate(self):
        """ mutate :: Ast -> None
        Randomly selects a mutation point in a tree, and
        substitutes the subtree with a randomly generated
        subtree
        Subtree mutation may be implemented as a
        crossover between a program and a newly generated
        random program
        """
        rand_ast = Ast()
        self.root_expr = Ast.cross_over(self, rand_ast)

    def cross_over(dad, mon):
        """ tree_sex :: Ast x Ast -> Expr (root) 
        Given two parents, subtree crossover randomly and
        independently selects a crossover point (a node) in
        each parent tree
        Then, an offspring is created by 
            (i) copying the first parent
            (ii) selecting a crossover point in that copy
            (iii) selecting a subtree in the second parent
            (iv) replace the subtree in the copy by a copy of the second
        subtree
        """
        return None
