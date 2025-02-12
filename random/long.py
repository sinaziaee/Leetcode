class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol_set = list()
        size = len(s)
        flag = False
        for i in range(size):
            new_set = set()
            l1 = s[i]
            new_set.add(l1)
            flag = False
            for j in range(i, size):
                l2 = s[j]
                temp_set = set()
                for word in new_set:
                    if l2 not in word:
                        word = word + l2
                        temp_set.add(word)
                    else:
                        flag = True
                        break
                for word in temp_set:
                    new_set.add(word)
                if flag == True:
                    break
            sol_set.append(new_set)
        print(sol_set)

sol = Solution()
result = sol.lengthOfLongestSubstring("pwwkew")
print(result)