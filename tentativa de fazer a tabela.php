
1   <arithmetic expression> ::= <arithmetic operating> <arithmetic sum> 
2   <arithmetic expression> ::= <arithmetic operating>

3   <arithmetic sum> ::= '+' <arithmetic operating> <arithmetic sum> 
4   <arithmetic sum> ::= '-' <arithmetic operating> <arithmetic sum> 
5   <arithmetic sum> ::= '+' <arithmetic operating> 
6   <arithmetic sum> ::= '-' <arithmetic operating>

7   <arithmetic operating> ::= <arithmetic value> <arithmetic multiplication> | 
8   <arithmetic operating> ::= <arithmetic value>

9   <arithmetic multiplication> ::= '*' <arithmetic value> <arithmetic multiplication> 
10  <arithmetic multiplication> ::= '/' <arithmetic value> <arithmetic multiplication>
11  <arithmetic multiplication> ::= '*' <arithmetic value> 
12  <arithmetic multiplication> ::= '/' <arithmetic value>

13  <arithmetic value> ::= number 
14  <arithmetic value> ::= '(' <arithmetic expression> ')' 
<arithmetic value> ::= <function call> 
<arithmetic value> ::= <attribute> 
 

first(<arithmetic expression>) = {number, first(<function call>), first(<attribute>), '('}
first(<arithmetic sum>) = {'+', '-'}
first(<arithmetic operating>) = {number, first(<function call>), first(<attribute>), '('}
first(<arithmetic multiplication>) = {'*', '/'}
first(<arithmetic value>) = {number, first(<function call>), first(<attribute>), '('}

follow(<arithmetic expression>) = {number, '(', '*', '/', ')', first(<function call>), first(<attribute>)}
follow(<arithmetic sum>) = {number, '(', '*', '/', ')', first(<function call>), first(<attribute>)}
follow(<arithmetic operating>) = {'+', '-'}
follow(<arithmetic multiplication>) = {'+', '-'}
follow(<arithmetic value>) = {'*', '/'}


utilizando para exemplo

first(<arithmetic expression>) = {number, '('}
first(<arithmetic sum>) = {'+', '-'}
first(<arithmetic operating>) = {number,, '('}
first(<arithmetic multiplication>) = {'*', '/'}
first(<arithmetic value>) = {number, '('}

follow(<arithmetic expression>) = {number, '(', '*', '/', ')'}
follow(<arithmetic sum>) = {number, '(', '*', '/', ')'}
follow(<arithmetic operating>) = {'+', '-'}
follow(<arithmetic multiplication>) = {'+', '-'}
follow(<arithmetic value>) = {'*', '/'}

1 + 2 + 3


matriz =
                            number      '+'     '-'     '*'     '/'     '('     ')'
<arithmetic expression>     1/2                                            1/2
<arithmetic sum>                         3/5    4/6           
<arithmetic operating>      7/8                                         7/8
<arithmetic multiplication>                             9/11    10/12
<arithmetic value>          13                                           14