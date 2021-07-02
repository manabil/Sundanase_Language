import sundanase_lexer
import sundanase_parser
import sundanase_interpreter

from sys import *

# DIRECT COMMAND
if __name__ == '__main__':
    lexer = sundanase_lexer.SundanaseLexer()
    parser = sundanase_parser.SundanaseParser()
    env = {}
    while True:
        try:
            text = input('Sundanase > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            sundanase_interpreter.SundanaseInterpreter(tree, env)
