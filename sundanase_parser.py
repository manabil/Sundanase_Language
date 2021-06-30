from sly import Parser

import sundanase_lexer

class SundanaseParser(Parser):
    tokens = sundanase_lexer.SundanaseLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
        )

    def __init__(self):
        self.env = { }



    @_('FOR var_assign TO expr THEN statement')
    def statement(self,p):
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)
    
    @_('IF condition THEN statement ELSE statement')
    def statement(self,p):
        return('if_stmt', p.condition,('branch', p.statement0, p.statement1))

    @_('FUN NAME "(" ")" ARROW statement')
    def statement(self,p):
        return ('fun_def', p.NAME, p.statement)

    @_('NAME "(" ")"')
    def statement(self,p):
        return('fun_call', p.NAME)

    @_('expr EQEQ expr')
    def condition(self, p):
        return ('condition_eqeq', p.expr0, p.expr1)
    
    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('NAME "=" expr')
    def var_assign(self,p):
        return('var_assign', p.NAME, p.expr)
    
    @_('NAME "=" STRING')
    def var_assign(self,p):
        return('var_assign', p.NAME, p.STRING)

    @_('expr')
    def statement(self,p):
        return (p.expr)
    
    @_('expr "+" expr')
    def expr(self,p):
        return('add', p.expr0, p.expr1)
    
    @_('expr "-" expr')
    def expr(self,p):
        return('sub', p.expr0, p.expr1)
    
    @_('expr "*" expr')
    def expr(self,p):
        return('mul', p.expr0, p.expr1)
    
    @_('expr "/" expr')
    def expr(self,p):
        return('div', p.expr0, p.expr1)

    @_('"-" expr %prec UMINUS')
    def expr(self,p):
        return p.expr
    
    @_('NAME')
    def expr(self,p):
        return('var', p.NAME)
    
    @_('NUMBER')
    def expr(self,p):
        return('num', p.NUMBER)

    @_('PRINT STRING')
    def statement(self,p):
        return('print', p.STRING)
    
    @_(' PRINT expr')
    def statement(self,p):
        return('print', p.expr)

    @_('PRINT ERROR')
    def statement(self,p):
        print("Syntax error in print statement. Bad expression")

# Bagian Interpreter
class BasicExecute:
	
	def __init__(self, tree, env):
		self.env = env
		result = self.walkTree(tree)
		if result is not None and isinstance(result, int):
			print(result)
		if isinstance(result, str) and result[0] == '"':
			print(result)

	def walkTree(self, node):

		if isinstance(node, int):
			return node
		if isinstance(node, str):
			return node

		if node is None:
			return None

		if node[0] == 'program':
			if node[1] == None:
				self.walkTree(node[2])
			else:
				self.walkTree(node[1])
				self.walkTree(node[2])

		if node[0] == 'num':
			return node[1]

		if node[0] == 'str':
			return node[1]

		if node[0] == 'add':
			return self.walkTree(node[1]) + self.walkTree(node[2])
		elif node[0] == 'sub':
			return self.walkTree(node[1]) - self.walkTree(node[2])
		elif node[0] == 'mul':
			return self.walkTree(node[1]) * self.walkTree(node[2])
		elif node[0] == 'div':
			return self.walkTree(node[1]) / self.walkTree(node[2])

		if node[0] == 'var_assign':
			self.env[node[1]] = self.walkTree(node[2])
			return node[1]

		if node[0] == 'var':
			try:
				return self.env[node[1]]
			except LookupError:
				print("Undefined variable '"+node[1]+"' found!")
				return 0


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