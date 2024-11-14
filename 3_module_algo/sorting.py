import random
# ----------------
# Fonctions d'aide
# ----------------
def swap(tab, i, j):
    """Échange la place des éléments aux indices i et j du tableau"""

    tab[i], tab[j] = tab[j], tab[i]
    
    return tab


def generate_random_array(debug=False, N=21):
    """Renvoie un tableau contenant toutes les valeurs entières de 0 (inclus)
    à N (exclus) rangées dans un ordre aléatoire

    Args:
        debug (boolean): quand debug est vrai, la fonction renvoie toujours le
                         même tableau afin de simplifier le débogage de vos
                         algorithmes de tri
        N (int): la taille du tableau à renvoyer

    Returns:
        list[int]: un tableau d'entiers, de taille N, non ordonné
    """

    if debug:
        return [3, 9, 7, 1, 6, 2, 8, 4, 5, 0]

    array = list(range(0, N))
    random.shuffle(array)

    return array

# ---------------
# Tris classiques
# ---------------
def bubble_sort(tab):
    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
    tableau, un peu comme des bulles dans l'eau qui remonteraient à la
    surface"""

    tab_tri = tab.copy()

    for i in range(len(tab_tri)):
        for j in range(i+1, len(tab_tri)):
            if tab_tri[j] <= tab_tri[i]:

                swap(tab_tri, i, j)
    
    return tab_tri

def insertion_sort(tab):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""

    tab_tri = tab.copy()

    for i in range(1, len(tab_tri)):
        
        x = tab_tri[i]
    
        while i > 0 and tab_tri[i-1] > x:
            tab_tri[i] = tab_tri[i-1]
            i -= 1

        tab_tri[i] = x

    return tab_tri

def selection_sort(tab):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""

    tab_tri = tab.copy()

    for i in range(0, len(tab_tri)):

        min = i

        for j in range(i+1, len(tab_tri)):

            if tab_tri[j] < tab_tri[min]:

                min = j
        
        if min != i:

            swap(tab_tri, i, min)
    
    return tab_tri


# --------------
# Tris récursifs
# --------------
def merge_sort(tab):
    """Trie le tableau via le principe de « diviser pour mieux régner »
    avec l'intelligence du tri qui se trouve au moment de la fusion"""

    tab_tri = tab.copy()

    merge_sort_r(tab_tri, 0, len(tab_tri))

    return tab_tri
    
def merge_sort_r(tab, start, end):

    if start < end - 1:

        m = (start + end)//2
        merge_sort_r(tab, start, m)
        merge_sort_r(tab, m, end)
        fusion(tab, start, m, end)

def fusion(tab, start, middle, end):

    i = start
    j = middle
    temp = [0]*(end - start)

    for k in range(end - start):
        if i < middle and j < end:
            if tab[i] <= tab[j]:
                temp[k] = tab[i]
                i += 1
            else:
                temp[k] = tab[j]
                j += 1
        else:
            if i < middle:
                temp[k] = tab[i]
                i += 1
            else:
                temp[k] = tab[j]
                j += 1
   
    for k in range(end - start):

        tab[start + k] = temp[k]


def quick_sort(tab):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées. L'intelligence se trouve
    dans la division du tableau."""

    tab_tri = tab.copy()

    quick_sort_r(tab_tri, 0, len(tab_tri)-1)
    
    return tab_tri

def quick_sort_r(tab, first, last):

    if first < last:
        pivot = partition(tab, first, last)
        quick_sort_r(tab, first, pivot-1)
        quick_sort_r(tab, pivot+1, last)
                
def partition(tab, first, last):

    pivot = tab[first]
    i = first
    j = last

    while i <= j:
        if tab[i] <= pivot:
            i += 1
        else:
            if tab[j] > pivot:
                j -= 1
            else:
                swap(tab, i, j)
            
    swap(tab, first, j)

    return j