def fibonacci():
    try:
        n = int(input(f"\n\nQual número você quer saber se pertence a sequência de Fibonacci? "))
    except ValueError:
        return f"\nPor favor, insira um número válido.\n\n"
    
    first = 0
    second = 1
    sequence = [first, second]

    while second < n:
        next = first + second
        sequence.append(next)
        first = second
        second = next

    if n in sequence:
        return f"\n{n} pertence a sequência de Fibonacci.\n\n"
    else:
        return f"\n{n} não pertence a sequência de Fibonacci.\n\n"

print(fibonacci())