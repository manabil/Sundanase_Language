from sly import Parser

import sundanase_lexer


class SundanaseParser(Parser):
    tokens = sundanase_lexer.SundanaseLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/', '%'),
        ('left', '^'),
        ('right', 'UMINUS'),
    )

    def __init__(self):
        self.env = {}

    @_('FOR var_assign TO expr THEN statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)

    @_('IF condition THEN statement ELSE statement')
    def statement(self, p):
        return('if_stmt', p.condition, ('branch', p.statement0, p.statement1))

    @_('FUN NAME "(" ")" ARROW statement')
    def statement(self, p):
        return ('fun_def', p.NAME, p.statement)

    @_('NAME "(" ")"')
    def statement(self, p):
        return('fun_call', p.NAME)

    @_('expr EQEQ expr')
    def condition(self, p):
        return ('condition_eqeq', p.expr0, p.expr1)

    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('NAME "=" expr')
    def var_assign(self, p):
        return('var_assign', p.NAME, p.expr)

    @_('NAME "=" STRING')
    def var_assign(self, p):
        return('var_assign', p.NAME, p.STRING)

    @_('expr')
    def statement(self, p):
        return (p.expr)

    @_('expr "+" expr')
    def expr(self, p):
        return('add', p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        return('sub', p.expr0, p.expr1)

    @_('expr "*" expr')
    def expr(self, p):
        return('mul', p.expr0, p.expr1)

    @_('expr "/" expr')
    def expr(self, p):
        return('div', p.expr0, p.expr1)

    @_('expr "^" expr')
    def expr(self, p):
        return('pow', p.expr0, p.expr1)

    @_('expr "%" expr')
    def expr(self, p):
        return('mod', p.expr0, p.expr1)

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('NAME')
    def expr(self, p):
        return('var', p.NAME)

    @_('NUMBER')
    def expr(self, p):
        return('num', p.NUMBER)

    @_('PRINT STRING')
    def statement(self, p):
        return('print', p.STRING)

    @_(' PRINT expr')
    def statement(self, p):
        return('print', p.expr)

    @_('PRINT ERROR')
    def statement(self, p):
        print("Syntax error in print statement. Bad expression")


if __name__ == '__main__':
    lexer = sundanase_lexer.SundanaseLexer()
    parser = SundanaseParser()
    env = {}
    while True:
        try:
            text = input('Sundanase > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)
