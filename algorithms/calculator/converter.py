"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import (Digit, Op, ReversePolishNotation)
from data_structures.queue_ import Queue_
from data_structures.stack import Stack


class ReversePolishNotationConverterState:
    """
    Class to store the state of RPN convert process
    """
    def __init__(self, expression_in_infix_notation: str):
        """
        :param expression_in_infix_notation: string with expression in infix notation
        """
        self.expression_in_infix_notation = Queue_(expression_in_infix_notation)
        self.expression_in_postfix_notation = ReversePolishNotation()
        self.stack = Stack()

    def pop_from_stack_until_opening_bracket(self):
        """
        Help function
        :return:
        """
        #cмотрим на верхний элемент, если это открывающаяся скобка, то элемент кладется
        #иначе выбрасывание верхнего из стека
        el = self.stack.top()

        while not isinstance(el, OpenBracket):
            self.expression_in_postfix_notation.put(el)
            self.stack.pop()
            el = self.stack.top()




class ReversePolishNotationConverter:
    """
    Class for converting infix expressions to reverse polish notation
    """
    point = '.'

    @staticmethod
    def convert(expression_in_infix_notation: str) -> ReversePolishNotation:
        """
        Main method of the class.
        Convert an infix expression to reverse polish notation

        :return: ReversePolishNotation object
        """

        while not state.expression_in_infix_notation.empty():

            #тут проверка: это диджит, откр скобка, закр скобка или

    @staticmethod
    def pop_from_stack_until_prioritizing(operator: Op, state: ReversePolishNotationConverterState):
        """
        Help function to move elements from stack to state elements (operators)
        until element on the top of the stack  has less priority then current operator
        :param operator: Instance of Op class - current operator
        :param state: State of the RPN convert process
        """
        stack = state.stack
        while (not stack.empty() and ReversePolishNotationConverter.is_binary_operation(stack.top())
        and stack.top() > operator):
            state.expression_in_postfix_notation.put(stack.top())
            stack.pop()
        stack.push(operator)

    @staticmethod
    def read_digit(state) -> Digit:
        """
        Method to read a digit from self._infix_notation

        :param state: expression in Reverse Polish Notation Format
        :return: Instance of Digit class
        """

    @staticmethod
    def is_part_of_digit(character: str) -> bool:
        """
        Help function to check if symbol is a part of floating point number
        :param character: current symbol
        :return: True if character can be part of a digit, else False
        """
        #циклом класть в строку?? типа проверка на то, цельное ли число, проверка на налицие == "."
        #проверка на int()


    @staticmethod
    def is_open_bracket(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is open bracket

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the open bracket operator else False
        """
        #op = OpFactory.get('+')
        #isinstance (op, скобка/BinaryOp)

    @staticmethod
    def is_close_bracket(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is close bracket

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the close bracket operator else False
        """

    @staticmethod
    def is_binary_operation(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is binary operator

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the binary operator else False
        """
