def indice():
    INDICE = 12
    SOMA = 0
    K = 1

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    
    print(f"SOMA: {SOMA}")

print(indice())