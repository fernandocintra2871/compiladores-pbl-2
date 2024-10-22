"""
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

class Parse:
    def __init__(self, token_list):
        self.token_list = token_list
        self.lookahead = token_list.pop(0)

    def match(self,t):
        print(t + str(self.lookahead))
        if len(token_list) > 0:
            self.lookahead = token_list.pop(0)

    def arithmetic_expression(self, t=""):
        print(t + "arithmetic_expression")
        t = t + "\t"
        if self.arithmetic_operating(t):
            if self.lookahead in ['+', '-']:
                self.match(t)
                if self.arithmetic_sum(t):
                    return True
                return False
            return True
        return False
    
    def arithmetic_operating(self, t):
        print(t + "arithmetic_operating")
        t = t + "\t"
        if self.arithmetic_value(t):
            if self.lookahead in ['*', '/']:
                self.match(t)
                if self.arithmetic_multiplication(t):
                    return True
                return False
            return True
        return False

    def is_float(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def arithmetic_value(self, t):
        print(t + "arithmetic_value")
        t = t + "\t"
        if self.is_float(self.lookahead):
            self.match(t)
            return True
        if self.lookahead == "(":
            self.match(t)
            if self.arithmetic_expression(t):
                if self.lookahead == ")":
                    self.match(t)
                    return True
                return False
            return False
        return False

    def arithmetic_sum(self, t):
        print(t + "arithmetic_sum")
        t = t + "\t"
        if self.arithmetic_operating(t):
            if self.lookahead in ['+', '-']:
                self.match(t)
                self.arithmetic_sum(t)
                return True
            return True
        return False

    def arithmetic_multiplication(self, t):
        print(t + "arithmetic_multiplication")
        t = t + "\t"
        if self.arithmetic_value(t):
            if self.lookahead in ['*', '/']:
                self.match(t)
                self.arithmetic_multiplication(t)
                return True
            return True
        return False
    
# Testando a classe
token_list = ["(", "1", "+", "3", ")", "*", "3"]
print(token_list)
arithmetic_expression = Parse(token_list)
print(arithmetic_expression.arithmetic_expression())
