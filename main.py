"""
gramatica
<arithmetic expression>::= <arithmetic operating> <arithmetic sum> | <arithmetic operating>
<arithmetic sum>::= '+' <arithmetic operating> <arithmetic sum> | '-' <arithmetic operating> <arithmetic sum> | '+' <arithmetic operating> | '-' <arithmetic operating>

<arithmetic operating>::= <arithmetic value> <arithmetic multiplication> | <arithmetic value>
<arithmetic multiplication>::= '*' <arithmetic value> <arithmetic multiplication> | '/' <arithmetic value> <arithmetic multiplication> | '*' <arithmetic value> | '/' <arithmetic value>

<arithmetic value>::= number | <function call> | <attribute> | '(' <arithmetic expression> ')' 

automato com pilha
δ(q, ∈, <arithmetic expression>) = (q, <arithmetic operating> <arithmetic sum>)
δ(q, ∈, <arithmetic expression>) = (q, <arithmetic operating>)
δ(q, ∈, <arithmetic sum>) = (q, '+' <arithmetic operating> <arithmetic sum>)
δ(q, ∈, <arithmetic sum>) = (q, '+' <arithmetic operating>)
δ(q, ∈, <arithmetic sum>) = (q, '-' <arithmetic operating> <arithmetic sum>)
δ(q, ∈, <arithmetic sum>) = (q, '-' <arithmetic operating>)
δ(q, ∈, <arithmetic operating>) = (q, <arithmetic value> <arithmetic multiplication>)
δ(q, ∈, <arithmetic operating>) = (q, <arithmetic value>)
δ(q, ∈, <arithmetic multiplication>) = (q, '*'  <arithmetic value> <arithmetic multiplication>)
δ(q, ∈, <arithmetic multiplication>) = (q, '*' <arithmetic value> )
δ(q, ∈, <arithmetic multiplication>) = (q, '/'  <arithmetic value> <arithmetic multiplication>)
δ(q, ∈, <arithmetic multiplication>) = (q, '/' <arithmetic value> )
δ(q, ∈,  <arithmetic value>) = (q, number)
δ(q, ∈,  <arithmetic value>) = (q, '(' <arithmetic expression> ')')

δ(q, '+', '+') = (q, ∈)
δ(q, '-', '-') = (q, ∈)
δ(q, '*', '*') = (q, ∈)
δ(q, '/', '/') = (q, ∈)
δ(q, '(', '(') = (q, ∈)
δ(q, ')', ')') = (q, ∈)
δ(q, number, number) = (q, ∈)
"""

class StackAutomaton:
    def __init__(self):
        self.stack = []  # Pilha para o autômato
        self.state = 'q'  # Estado inicial
    
    def transition(self, token, next_token, stack_top):
        # Aplicando a formalização de acordo com as transições fornecidas
        if stack_top == "<arithmetic expression>":
            if next_token in ['+', '-']:
                self.stack.append("<arithmetic sum>")
                self.stack.append("<arithmetic operating>")
            else:
                self.stack.append("<arithmetic operating>")
        elif stack_top == "<arithmetic sum>":
            if token in ['+', '-']:
                self.stack.append("<arithmetic sum>")
                self.stack.append("<arithmetic operating>")
                self.stack.append("+")
            else:
                self.stack.append("<arithmetic operating>")
        elif stack_top == "<arithmetic operating>":
            if token in ['*', '/']:
                self.stack.append("<arithmetic multiplication>")
                self.stack.append("<arithmetic value>")
            else:
                self.stack.append("<arithmetic value>")
        elif stack_top == "<arithmetic multiplication>":
            if token in ['*', '/']:
                self.stack.append("<arithmetic multiplication>")
                self.stack.append("<arithmetic value>")
                self.stack.append("*")
            else:
                self.stack.append("<arithmetic value>")
        elif stack_top == "<arithmetic value>":
            if token.isdigit():
                return token  # Nó folha, é um número
            elif token == '(':
                self.stack.append(")")
                self.stack.append("<arithmetic expression>")
                self.stack.append("(")
        elif token in ['+', '-', '*', '/', '(', ')']:
            return token  # Operador ou parênteses
    
    def parse(self, token_list):
        self.stack.append("<arithmetic expression>")  # Empilhando a regra inicial
        i = 0
        while self.stack:
            stack_top = self.stack.pop()  # Remove o topo da pilha
            token = token_list[i]
            if i < len(token_list) - 1:
                next_token = token_list[i+1]
            result = self.transition(token, next_token, stack_top)
            print(result)
            if result != None:
                i += 1
        return


# Exemplo de uso com a lista de tokens
token_list = ["(", "1", "+", "2", ")", "*", "3"]
automaton = StackAutomaton()
tree_root = automaton.parse(token_list)

