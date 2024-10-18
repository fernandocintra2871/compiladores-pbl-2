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

def arithmetic_expression(token):
    if arithmetic_operating(token):
        if arithmetic_sum(token):
            return True
        return True
    return False

def arithmetic_operating(token):
    if arithmetic_value(token):
        return True
    return False

def arithmetic_value(token):
    global pos
    if token[pos] in "1234567890":
        print(token[pos])
        pos += 1
        return True
    if token[pos] == "(":
        print(token[pos])
        pos += 1
        if arithmetic_expression(token):
            if token[pos] == ")":
                print(token[pos])
                pos += 1
                return True
        return False
    return False

def arithmetic_sum(token):
    global pos
    if token[pos] == "+":
        print(token[pos])
        pos += 1
        if arithmetic_operating(token):
            if arithmetic_sum(token):
                return True
            return True
        return False
    return False

pos = 0
token_list = ["(", "1", "+", "3", ")", "+", "3"]
print(arithmetic_expression(token_list))