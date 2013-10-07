from .utils import disassemble, is_module_or_class, generate_space


def count_branch(code):
    """ count how many branch in code object.

        >>> count_branch(disassemble.__code__)
        10

        >>> count_branch(count_branch.__code__)
        2

        >>> count_branch(count_branch_in_model.__code__)
        7

    """
    opcode_list = disassemble(code)
    count = 0
    for i in opcode_list:
        opcode = i[0].lower()
        if opcode.find('jump') != -1 and opcode.find('if') != -1:
            count += 1
    return count


def count_branch_in_model(module, branch_threshold=0, indent=0, module_list=[]):
    """ display branch for each function(or method) in module(or class).
    """
    if not is_module_or_class(module):
        return []
    model_member = dir(module)
    total_branch = 0
    code_count = 0
    for member in model_member:
        obj = getattr(module, member, None)
        if not obj:
            continue
        if getattr(obj, '__code__', False):
            branch = count_branch(obj.__code__)
            total_branch += branch
            code_count += 1
            if branch > branch_threshold:
                print generate_space(4 * indent), '{name}: {count_branch}'.format(name=obj.__name__, count_branch=branch)
        elif is_module_or_class(obj):
            if obj.__name__ in module_list:
                continue
            module_list.append(obj.__name__)
            print generate_space(4 * indent), '{name}-'.format(name=obj.__name__)
            cls_info = count_branch_in_model(obj, branch_threshold=branch_threshold,
                                             indent=indent+1, module_list=module_list)
            total_branch += cls_info[0]
            code_count += cls_info[1]
    if code_count != 0:
        print generate_space(4 * indent), '*- averge -*: {averge}'.format(averge=float(total_branch) / code_count)
    return total_branch, code_count


if __name__ == '__main__':
    import doctest
    doctest.testmod()