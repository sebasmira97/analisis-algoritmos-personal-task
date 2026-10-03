# 435. Non-overlapping Intervals — https://leetcode.com/problems/non-overlapping-intervals/
# Familia: greedy (selección de actividades, contada al revés)
#
# Candidatos: los intervalos, ordenados por end.
# Criterio:   entre los que aún caben, quedarse con el que TERMINA ANTES.
# Factible:   start >= fin del último aceptado (tocarse en un punto no es solape).
# Respuesta:  n - (cuántos se aceptaron) = cuántos hay que borrar.
#
# Por qué es óptimo: el que termina antes deja el mayor espacio libre a la
# derecha; por intercambio, cualquier óptimo puede reemplazar su primer
# intervalo por este sin empeorar.
#
# Tiempo:  O(n log n) — domina el sort; la pasada es O(n).
# Espacio: O(1) extra — sort in-place (Timsort puede usar hasta O(n) auxiliar).

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])  # por end

        kept = 0
        last_end = float('-inf')
        for start, end in intervals:
            if start >= last_end:
                # No pisa al último aceptado: elegirlo (decisión irrevocable).
                kept += 1
                last_end = end
            # Si no cabe, se "borra" (no se hace nada).

        return len(intervals) - kept
