class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score1 = score.copy()
        score1.sort(reverse = True)

        rank = {}
        for i in range(len(score1)):
            if i == 0:
                rank[score1[i]] = "Gold Medal"
            elif i == 1:
                rank[score1[i]] = "Silver Medal"
            elif i == 2:
                rank[score1[i]] = "Bronze Medal"
            else:
                rank[score1[i]] = str(i + 1)
        ans = []
        for i in score:
            ans.append(rank[i])
        
        return ans

        