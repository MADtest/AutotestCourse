def eval_object(v):
    if v.get('operation') == '+':
        return v.get('a') + v.get('b')
    elif v.get('operation') == '-':
        return v.get('a') - v.get('b')
    elif v.get('operation') == '/':
        return v.get('a') / v.get('b')
    elif v.get('operation') == '*':
        return v.get('a') * v.get('b')
    elif v.get('operation') == '%':
        return v.get('a') % v.get('b')
    elif v.get('operation') == '**':
        return v.get('a') ** v.get('b')
