import re

variables = {}


def remove_comments(program):
    program = re.sub(r'/\*(?:.|[\r\n])*?\*/', '', program)
    program = re.sub(r'#.*', '', program)
    return program


def parse(program):
    program = remove_comments(program)
    lines = [line.strip() for line in program.splitlines() if line.strip()]
    for line in lines:
        try:
            parse_line(line)
        except Exception as e:
            print(e)
            return


def parse_line(line):
    if line.startswith('print'):
        parse_print(line)
    else:
        parse_assignment(line)


def parse_print(line):
    expr = line[5:].strip()
    try:
        exprs = [parse_expression(e.strip()) for e in expr.split(',')]
    except ZeroDivisionError:
        print("divide by zero")
        return
    except Exception as e:
        print("parse error")
        return
    print(*exprs)


def parse_assignment(line):
    op_equals_match = re.match(
        r'([A-Za-z_][A-Za-z0-9_]*)\s*([\+\-\*/%^]=)', line)
    if op_equals_match:
        var, op = op_equals_match.groups()
        expr = line[op_equals_match.end():].strip()
        op = op[:-1]
        try:
            expr_value = parse_expression(expr)
        except Exception:
            raise Exception("parse error")
        variables[var] = operators[op][2](variables.get(var, 0), expr_value)
        return

    try:
        var, expr = line.split('=')
    except ValueError:
        raise Exception("parse error")

    var = var.strip()
    variables[var] = parse_expression(expr.strip())


def parse_expression(expr):
    output, op_stack = [], []

    def apply_operator():
        op = op_stack.pop()
        if op == '!':
            a = output.pop()
            output.append(operators[op][2](a))
        else:
            b, a = output.pop(), output.pop()
            output.append(operators[op][2](a, b))

    def greater_precedence(op1, op2):
        prec1, assoc1 = operators[op1][:2]
        prec2, assoc2 = operators[op2][:2]
        if prec1 > prec2:
            return True
        if prec1 == prec2 and assoc1 == 'left':
            return True
        return False

    tokens = re.findall(
        r'\d+\.\d+|\d+|[A-Za-z_][A-Za-z0-9_]*|[+\-*/%^()]|==|!=|<=|>=|<|>|&&|\|\||!', expr)
    prev_token = None
    if not tokens:
        raise Exception("parse error")

    prev_is_operator = False
    for token in tokens:
        if token.isdigit() or re.match(r'\d+\.\d+', token):
            if prev_token == '-' and prev_is_operator:
                if op_stack:
                    op_stack.pop()
                output.append(float(token) * -1)
            else:
                output.append(float(token))
        elif token in operators:
            prev_is_operator = True
            if prev_token is None or (prev_token in operators and prev_token not in ['(', ')']):
                if token == '-':
                    prev_token = token
                    continue
                elif token == '!':
                    operators['!'] = (-3, 'nonassoc',
                                      lambda x: float(not bool(x)))
                else:
                    raise ValueError("Invalid expression")
            while (op_stack and op_stack[-1] != '('
                   and greater_precedence(op_stack[-1], token)
                   and not (operators[op_stack[-1]][1] == 'nonassoc' and operators[token][1] == 'nonassoc')):
                apply_operator()
            op_stack.append(token)
        elif token == '(':
            prev_is_operator = False
            op_stack.append(token)
        elif token == ')':
            prev_is_operator = False
            while op_stack[-1] != '(':
                apply_operator()
            op_stack.pop()
        elif token in variables:
            prev_is_operator = False
            output.append(variables[token])
        prev_token = token

    while op_stack:
        apply_operator()

    return output[0]


operators = {
    '+': (1, 'left', lambda x, y: x + y),
    '-': (1, 'left', lambda x, y: x - y),
    '*': (2, 'left', lambda x, y: x * y),
    '/': (2, 'left', lambda x, y: x / y),
    '%': (2, 'left', lambda x, y: x % y),
    '^': (3, 'right', lambda x, y: x ** y),
    '==': (0, 'left', lambda x, y: int(x == y)),
    '!=': (0, 'left', lambda x, y: int(x != y)),
    '<': (0, 'left', lambda x, y: int(x < y)),
    '>': (0, 'left', lambda x, y: int(x > y)),
    '<=': (0, 'left', lambda x, y: int(x <= y)),
    '>=': (0, 'left', lambda x, y: int(x >= y)),
    '&&': (-1, 'left', lambda x, y: int(bool(x) and bool(y))),
    '||': (-2, 'left', lambda x, y: int(bool(x) or bool(y))),
    '!': (-3, 'nonassoc', lambda x: int(not bool(x))),
}


def main():
    program = ''
    try:
        while True:
            line = input().rstrip()
            program += line + '\n'
    except EOFError:
        pass
    parse(program)


if __name__ == "__main__":
    main()
