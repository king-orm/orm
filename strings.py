def pluralize(noun: str):
    if noun.endswith('s') or noun.endswith('x') or noun.endswith('z') or noun.endswith('sh') or noun.endswith('ch'):
        return noun + 'es'
    elif noun.endswith('y') and noun[-2] not in 'aeiou':
        return noun[:-1] + 'ies'
    else:
        return noun + 's'