def check_string(string):
    string = string.lower()

    count = string.count('a')

    if count > 0:
        if count == 1:
            return f"\nA letra 'a' aparece 1 vez.\n\n"
        else:
            return f"\nA letra 'a' aparece {count} vezes.\n\n"
    else:
        return f"\nA letra 'a' não aparece nenhuma vez.\n\n"
    
string = input(f"\n\nDigite uma string para verificar a existência da letra 'a': ")

print(check_string(string))