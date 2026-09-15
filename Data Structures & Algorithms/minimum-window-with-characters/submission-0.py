class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # что нужно набрать
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        window = {}                     # что сейчас в окне
        have, need = 0, len(countT)     # сколько требований выполнено / всего
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)          # добавили букву в окно

            if c in countT and window[c] == countT[c]:
                have += 1                             # закрыли ещё одно требование

            while have == need:                       # окно подходит — жмём его
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1                     # выбрасываем левую букву
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1                         # требование сломалось
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""