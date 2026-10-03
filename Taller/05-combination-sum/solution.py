# 39. Combination Sum — https://leetcode.com/problems/combination-sum/
# Familia: backtracking (elegir, explorar, deshacer)
#
# Estado de la búsqueda: (start, remaining, path)
#   start     -> índice desde el que se puede elegir (no se vuelve a índices
#                menores, así [2,3,2] no aparece como permutación de [2,2,3])
#   remaining -> lo que falta para llegar a target
#   path      -> la combinación que se está construyendo
#
# Qué se elige:   candidates[i] (con i >= start); se puede reutilizar, por eso
#                 la llamada recursiva sigue en i y no en i + 1.
# Qué se deshace: al regresar se hace path.pop() -> se quita el último elegido
#                 y se prueba el siguiente candidato (eso es el backtrack).
# Poda:           con candidates ordenado, si candidates[i] > remaining,
#                 ningún candidato posterior cabe -> se corta la rama.
#
# Con n = len(candidates), t = target, m = min(candidates):
# Tiempo:  O(n^(t/m + 1)) en el peor caso — el árbol tiene profundidad máxima
#          t/m y hasta n ramas por nivel (más copiar cada solución hallada).
# Espacio: O(t/m) de pila de recursión y de path, más la salida.

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # solo para poder podar con break
        result: List[List[int]] = []
        path: List[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])  # copiar: path se seguirá modificando
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate > remaining:
                    break  # poda: este y los siguientes se pasan de target

                path.append(candidate)                 # elegir
                backtrack(i, remaining - candidate)    # explorar (reutiliza i)
                path.pop()                             # deshacer

        backtrack(0, target)
        return result
