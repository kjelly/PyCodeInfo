from .utils import disassemble


def count_loop(code):
    """ count loop in code object.

        >>> count_loop(disassemble.__code__)
        1

        >>> count_loop(count_loop.__code__)
        1

        >>> def test(n):
        ...    for i in xrange(1, n):
        ...        if i < 5:
        ...            continue
        ...        if i > 8:
        ...            break
        ...        print i


        >>> count_loop(test.__code__)
        1

    """
    opcode_list = disassemble(code)
    count_setup_loop = 0

    for i in opcode_list:
        opcode = i[0].lower()
        if opcode == 'setup_loop':
            count_setup_loop += 1
    return count_setup_loop


if __name__ == '__main__':
    import doctest
    doctest.testmod()