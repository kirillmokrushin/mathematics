from typing import List

Matrix = List[List[int]]

def is_reflexive(m: Matrix) -> bool:
    for i in range(len(m)):
        if m[i][i] != 1:
            return False
    return True

def is_anti_reflexive(m: Matrix) -> bool:
    for i in range(len(m)):
        if m[i][i] != 0:
            return False
    return True

def is_symmetric(m: Matrix) -> bool:
    n = len(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[j][i]:
                return False
    return True

def is_antisymmetric(m: Matrix) -> bool:
    n = len(m)
    for i in range(n):
        for j in range(n):
            if i != j and m[i][j] == 1 and m[j][i] == 1:
                return False
    return True

def is_linear(m: Matrix) -> bool:
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            if m[i][j] == 0 and m[j][i] == 0:
                return False
    return True

# Демонстрация работы
if __name__ == "__main__":
    # Пример 1: отношение "≤" для {1,2,3}
    le_matrix = [
        [1, 1, 1],
        [0, 1, 1],
        [0, 0, 1]
    ]

    # Пример 2: отношение равенства  для {1,2,3}
    eq_matrix = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    # Пример 3: строгое неравенство  для {1,2,3}
    lt_matrix = [
        [0, 1, 1],
        [0, 0, 1],
        [0, 0, 0]
    ]
  
   # Пример 4: антисимметричность
    divides = [[1,1,1],
               [0,1,1],
               [0,0,1]]
    
    # Пример 5: нелинейность 
    not_linear = [[0,1,0],
                  [0,0,0],
                  [0,1,0]]
