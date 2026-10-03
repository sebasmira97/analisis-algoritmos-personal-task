# 200. Number of Islands — https://leetcode.com/problems/number-of-islands/
# Familia: grafos (componentes conexas en un grafo implícito)
#
# Modelo: cada celda '1' es un vértice; hay arista NO dirigida entre dos
# celdas '1' vecinas arriba/abajo/izquierda/derecha (no diagonal).
# Contar islas = contar componentes conexas.
#
# Idea: recorrer la grilla; cada '1' no visitado abre una componente nueva
# (+1) y un BFS la "hunde" entera (la marca como '0') para no contarla dos veces.
#
# Tiempo:  Θ(m·n) — cada celda entra a la cola a lo sumo una vez.
# Espacio: O(m·n) — la cola en el peor caso (grilla toda de tierra).
#          Se usa BFS iterativo para no chocar con el límite de recursión.

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))  # sin diagonales
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '1':
                    continue  # agua o tierra ya visitada

                # Nueva componente conexa.
                islands += 1
                grid[r][c] = '0'  # marcar al encolar
                queue = deque([(r, c)])
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                            grid[nx][ny] = '0'
                            queue.append((nx, ny))

        return islands
