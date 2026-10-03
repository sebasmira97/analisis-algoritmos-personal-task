# 1143. Longest Common Subsequence — https://leetcode.com/problems/longest-common-subsequence/
# Familia: programación dinámica (tabla 2D de prefijos)
#
# Estado:      dp[i][j] = longitud de la LCS de text1[0..i) y text2[0..j)
# Base:        dp[0][j] = dp[i][0] = 0   (un prefijo vacío no comparte nada)
# Recurrencia: si text1[i-1] == text2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
#              si no:                       dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# Respuesta:   dp[n][m]
#
# Con n = len(text1), m = len(text2):
# Tiempo:  Θ(n·m) — se llena cada celda una vez en O(1).
# Espacio: Θ(n·m) — la tabla completa.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        # (n+1) x (m+1): fila 0 y columna 0 son los casos base en 0.
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Las letras coinciden: extender la LCS de la diagonal.
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # No coinciden: descartar la última letra de una u otra.
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]
