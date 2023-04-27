class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # L or R: Definitely no change
        # if .: If start/before is left, change all . to L if there is a L on the right.
        #                                Else, just continue
        #      Else, if before is right, change all to R if there is a R on the right or end
        #                               Else if there is L on the right, build towards the
        #                               centre. 

        dominoes = list(dominoes)
        isLeftBefore = True
        firstDotIndex = -1
        i = 0
        while i < len(dominoes):
            val = dominoes[i]
            if val == ".":
                if firstDotIndex == -1:
                    firstDotIndex = i
            elif val == "L":
                if firstDotIndex == -1:
                    i += 1
                    isLeftBefore = True
                    continue
                if isLeftBefore:
                    for j in range(firstDotIndex, i):
                        dominoes[j] = "L"
                else:
                    # Build towards centre
                    l, r = firstDotIndex, i - 1
                    while l < r:
                        dominoes[l] = "R"
                        dominoes[r] = "L"
                        l += 1
                        r -= 1
                firstDotIndex = -1
                isLeftBefore = True
            else:
                # "R"
                if firstDotIndex == -1:
                    i += 1
                    isLeftBefore = False
                    continue
                if isLeftBefore:
                    firstDotIndex = -1
                    i += 1
                    isLeftBefore = False
                    continue
                else:
                    for j in range(firstDotIndex, i):
                        dominoes[j] = "R"
                firstDotIndex = -1
                isLeftBefore = False
            
            i += 1

        if firstDotIndex != -1 and not isLeftBefore:
            for j in range(firstDotIndex, len(dominoes)):
                dominoes[j] = "R"
        
        return "".join(dominoes)
