# AST: Expresion puede ser una BinOp, Id o Num

import copy
import random

from Global import MIN_NUMBER, MAX_NUMBER, MAX_DEPTH, NUMBER_OF_OPERATIONS
from Utils import sumar_num, restar_num, dividir_num, multip_num, fitness_fun

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


'''
AST
Expr container
'''
class Ast:
    @classmethod
    def random_generate(cls):
        """
        Genera AST aleatorio.
        
        """

        def random_ast(max_depth):
            """ random_ast :: None -> Expr (root)
            Genera un AST aleatorio, concatenando nodos (funciones y/o terminales) hasta que no se puedan más, 
            o hasta que se cumpla la profundidad maxima.
            :return: Raiz del arbol generado.
            """
            if max_depth <= 0:  # caso base, elijo un terminal random
                if random.random() < 0.5:  # terminal es numero
                    return Num(random.uniform(MIN_NUMBER, MAX_NUMBER))
                else:
                    return Id('x')
            else:  # caso recursivo, elijo funcion o terminal random
                rand = random.random()
                prob = 1.0 / 6  # distribucion uniforme
                if rand <= prob:
                    return Num(random.uniform(MIN_NUMBER, MAX_NUMBER))
                elif rand <= prob * 2:
                    return Id('x')
                elif rand <= prob * 3:
                    return BinOp('+', random_ast(max_depth - 1), random_ast(max_depth - 1))
                elif rand <= prob * 4:
                    return BinOp('-', random_ast(max_depth - 1), random_ast(max_depth - 1))
                elif rand <= prob * 5:
                    return BinOp('/', random_ast(max_depth - 1), random_ast(max_depth - 1))
                else:
                    return BinOp('*', random_ast(max_depth - 1), random_ast(max_depth - 1))

        root_expr = random_ast(MAX_DEPTH)
        return cls(root_expr)

    @classmethod
    def from_parents(cls, dad, mom):
        """
        Crea AST a partir de cross-over de dos padres.
        :param dad: AST padre
        :param mom: AST madre
        :return: AST hijo
        """
        this = cls(Ast.cross_over(dad, mom))
        this.count_nodes()
        while this.binop_count > NUMBER_OF_OPERATIONS * 5:
            # print("dropped in cross over due max depth")
            this = cls(Ast.cross_over(dad, mom))
            this.count_nodes()
        return this

    def __init__(self, root_expr):
        """
        Inicia AST a partir de una expresión raiz.
        :param root_expr: 
        """
        self.root_expr = root_expr
        self.node_count = -1
        self.binop_count = -1
        self.fitness = -1

    def get_fitness(self):
        """
        Calcula y retorna fitness de este AST.
        :return: fitness
        """
        self.fitness = fitness_fun(self)
        return self.fitness

    def evaluate(self, xval):
        """
        Evalua AST con 'xval' como parametro.
        :param xval: Valor de x con el cual se evaluará el AST.
        :return: Valor final de interpretar el AST.
        """

        def interp_expr(expr, xval):
            """interp :: Expr x Float -> Float
            Toma una Expresion y valor de X, e interpreta (evalua) la Expresion  retornando el Valor resultante."""
            if expr.__class__.__name__ == 'Num':
                return expr.value
            elif expr.__class__.__name__ == 'Id':
                return xval
            elif expr.__class__.__name__ == 'BinOp' and expr.op == '+':
                left_val = interp_expr(expr.expr1, xval)
                right_val = interp_expr(expr.expr2, xval)
                return sumar_num(left_val, right_val)
            elif expr.__class__.__name__ == 'BinOp' and expr.op == '-':
                left_val = interp_expr(expr.expr1, xval)
                right_val = interp_expr(expr.expr2, xval)
                return restar_num(left_val, right_val)
            elif expr.__class__.__name__ == 'BinOp' and expr.op == '/':
                left_val = interp_expr(expr.expr1, xval)
                right_val = interp_expr(expr.expr2, xval)
                return dividir_num(left_val, right_val)
            elif expr.__class__.__name__ == 'BinOp' and expr.op == '*':
                left_val = interp_expr(expr.expr1, xval)
                right_val = interp_expr(expr.expr2, xval)
                return multip_num(left_val, right_val)
            else:
                print("error: Not matching clause for " + str(expr))
                raise Exception

        return interp_expr(self.root_expr, xval)

    def get_random_node(self):
        """
        Retorna indice de un nodo aleatorio.
        :return: Indice de nodo aleatorio.
        """
        self.node_count = self.count_nodes()
        if self.node_count > 1:
            randomly_chosen_node = random.randint(1, self.node_count - 1)
            return randomly_chosen_node
        return 0

    @classmethod
    def recursive_counting_probe(self, expr):
        """recursive_counting_probe :: Expr  -> Int
        Cuenta cantidad de nodos y cantidad de operaciones binarias en Expr."""
        if expr.__class__.__name__ == 'Num':
            return 1,0
        elif expr.__class__.__name__ == 'Id':
            return 1, 0
        elif expr.__class__.__name__ == 'BinOp':
            left_val, left_bin_ops = Ast.recursive_counting_probe(expr.expr1)
            right_val, right_bin_ops = Ast.recursive_counting_probe(expr.expr2)
            return 1 + left_val + right_val, 1 + left_bin_ops + right_bin_ops
        else:
            print("error: Not matching clause for " + str(expr))
            raise Exception

    def count_nodes(self):
        """
        Calcula cantidad de nodos y de operaciones binarias en el AST.
        :return: Cantidad de nodos 
        """
        self.node_count, self.binop_count = Ast.recursive_counting_probe(self.root_expr)
        return self.node_count

    def extract_node(self, node_id):
        """
        Dado una id de nodo, extrae el padre de este nodo e indica si es el hijo izquierdo o derecho.
        :param node_id: Id del nodo
        :return: Padre del nodo con esa id y una flag que indica si es hijo izquierdo.
        """

        def recursive_node_extractor_probe(expr, actual_count, node_id):
            """recursive_node_extractor_probe :: Expr  -> Expr
            Busca padre del nodo.
            
            :returns father of node and if_is_left_son flag"""
            if actual_count == node_id:
                return None, None
            else:
                if expr.__class__.__name__ == 'BinOp':
                    if actual_count + 1 == node_id:
                        return expr, True
                    actual_count += 1
                    if actual_count + Ast.recursive_counting_probe(expr.expr1)[0] == node_id:
                        return expr, False

                    left_search, flag = recursive_node_extractor_probe(expr.expr1, actual_count, node_id)
                    if left_search is not None:
                        return left_search, flag
                    actual_count += Ast.recursive_counting_probe(expr.expr1)[0]
                    right_search, flag = recursive_node_extractor_probe(expr.expr2, actual_count, node_id)
                    if right_search is not None:
                        return right_search, flag
                return None, None

        search_result, flag = recursive_node_extractor_probe(self.root_expr, 0, node_id)
        if search_result is None:
            search_result = BinOp('*', Num(1.0), Num(1.0))
            flag = None
        return search_result, flag

    def mutate(self):
        """ mutate :: Self(Ast) -> None
        Randomly selects a mutation point in a tree, and
        substitutes the subtree with a randomly generated
        subtree
        Subtree mutation may be implemented as a
        crossover between a program and a newly generated
        random program
        """
        rand_ast = Ast.random_generate()
        self.root_expr = Ast.cross_over(self, rand_ast)
        self.count_nodes()
        while self.binop_count > NUMBER_OF_OPERATIONS * 5:
            # work around for AST size control
            #print("dropped in mutation due max depth")

            rand_ast = Ast.random_generate()
            self.root_expr = Ast.cross_over(self, rand_ast)
            self.count_nodes()

    @classmethod
    def cross_over(self, dad, mom):
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
        copy_of_dad = dad.copy()
        copy_of_mom = mom.copy()

        dad_cross_point = copy_of_dad.get_random_node()
        mom_cross_point = copy_of_mom.get_random_node()

        dad_subtree_father, is_left_son_dad = copy_of_dad.extract_node(dad_cross_point)
        if is_left_son_dad is None:
            # work around if root gets selected, tree is expanded
            dad_subtree_father.expr1 = copy_of_dad.root_expr
            copy_of_dad.root_expr = dad_subtree_father
            is_left_son_dad = True

        mom_subtree_father, is_left_son_mom = copy_of_mom.extract_node(mom_cross_point)
        if is_left_son_mom is None:
            # work around if root gets selected, tree is expanded
            mom_subtree_father.expr1 = copy_of_mom.root_expr
            copy_of_mom.root_expr = mom_subtree_father
            is_left_son_mom = True

        if random.random() < 0.5:
            # dad's subtree get replaced by mom's
            modified_node = dad_subtree_father
            new_subtree = mom_subtree_father.expr1 if is_left_son_mom else mom_subtree_father.expr2
            left_son_flag = is_left_son_dad
            modified_tree_root = copy_of_dad.root_expr
        else:
            # mom's subtree get replaced by dad's
            modified_node = mom_subtree_father
            new_subtree = dad_subtree_father.expr1 if is_left_son_dad else dad_subtree_father.expr2
            left_son_flag = is_left_son_mom
            modified_tree_root = copy_of_mom.root_expr

        # actual replace
        if left_son_flag:
            modified_node.expr1 = new_subtree
        else:
            modified_node.expr2 = new_subtree
        # return root expr
        return modified_tree_root

    def print(self):
        """
        Imprime AST estilizadamente.
        :return: None
        """

        def print_expr(expr, prefix):
            """print_expr :: Expr x String -> None
            Toma una Expresion y prefijio, e imprime arbol AST desde expresion estilizado."""
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
                print_expr(expr.expr1, prefix + "|  ")
                print(prefix + "└--", end='')
                print_expr(expr.expr2, prefix + "  ")
            else:
                print("error: Not matching clause for " + str(expr.__class__.__name__))
                raise Exception

        print_expr(self.root_expr, "")

    def copy(self):
        """ copy :: self -> Ast
        Hace una copia del AST.

        :return: Copia del AST.
        """
        copied_expr = copy.deepcopy(self.root_expr)  # recursive object copy
        return Ast(copied_expr)
