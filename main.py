#### Imports et définition des variables globales
"""imports et définition des variables globales"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        for line in f :
            l.append([int(x) for x in line.strip().split(';')])
    return l

def get_list_k(data, k):
    """Retourne la k-ième liste dans les données.

    Args : data (list): liste de listes
        k (int): indice de la liste souhaitée

    Returns :
        list : la k-ième liste ou liste vide si l'indice est invalide
    """
    if 0<= k < len(data):
        return data[k]
    return []

def get_first(l):
    """Retourne le premier élement de la liste.

    Args:
        l (list): une liste

    Returns:
        any: le premier élément ou None si la liste est vide
    """
    return l[0] if l else None

def get_last(l):
    """Retourne le dernier élément d'une liste.

    Args:
        l (list): une liste

    Returns:
        any: le dernier élément ou None si la liste est vide
    """
    return l[-1] if l else None

def get_max(l):
    """Retourne le maximum d'une liste.

    Args:
        l (list): une liste

    Returns:
        any: le maximum ou None si la liste est vide
    """
    return max(l) if l else None

def get_min(l):
    """Retourne le minimum d'une liste.

    Args:
        l (list): une liste

    Returns:
        any: le minimum ou None si la liste est vide
    """
    return min(l) if l else None

def get_sum(l):
    """Retourne la somme des éléments d'une liste.

    Args:
        l (list): une liste

    Returns:
        int: la somme ou None si la liste est vide
    """
    return sum(l) if l else None


#### Fonction principale

def main():
    """Appels des fonctions pour checker leur bon fonctionnement"""
    data = read_data(FILENAME)
    print("Contenue du fichier", data)
    k_list = get_list_k(data,2)
    print("La list k:", k_list)
    print("Le premier élément de la liste", get_first(k_list))
    print("Le dernier élément de la liste", get_last(k_list))
    print("Le maximum :", get_max(k_list))
    print("Le minimum :", get_min(k_list))
    print("La somme", get_sum(k_list))
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
