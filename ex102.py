def fatorial(n, show=False):
    """Calculates the factorial of a number.

            Args:
                n (int): Number that the user wants the factorial of.
                show (bool): (optional) If True the function will show the user the calculations step by step,
                if False the function will only show the result.

            Return:
                The factorial of a number.
        """
    f = 1
    print(f'{n}!', end=' = ')
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
print(fatorial(4, show=False))
help(fatorial)
