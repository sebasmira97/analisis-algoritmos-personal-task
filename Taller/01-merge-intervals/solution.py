# 56. Merge Intervals — https://leetcode.com/problems/merge-intervals/
# Familia: ordenamiento (ordenar por clave + una pasada de fusión)
#
# Idea: la clave es el extremo izquierdo (start). Una vez ordenados, dos
# intervalos que se solapan quedan contiguos, así que basta una pasada
# manteniendo el intervalo "abierto" actual.
#
# Tiempo:  O(n log n)  — domina el sort (Timsort); la pasada es O(n).
# Espacio: O(n)        — la lista de salida (+ O(n) del sort de Python).

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1) Ordenar los INTERVALOS por start (no los extremos sueltos).
        intervals.sort(key=lambda interval: interval[0])

        merged = [intervals[0][:]]  # intervalo "abierto" = merged[-1]
        for start, end in intervals[1:]:
            current = merged[-1]
            if start <= current[1]:
                # Empieza antes o justo cuando termina el actual: se solapan
                # (o se tocan) -> ensanchar el end.
                current[1] = max(current[1], end)
            else:
                # No se solapan: cerrar el actual y abrir uno nuevo.
                merged.append([start, end])
        return merged
