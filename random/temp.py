class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol_set = set()
        for letter in s:
            if len(sol_set) == 0:
                sol_set.add(letter)
            else:
                temp_set = set()
                for item in sol_set:
                    if letter not in item:
                        item = item + letter
                        temp_set.add(item)
                    
                for item in temp_set:
                    sol_set.add(item)
        print(sol_set)
        # max_string = ""
        # for item in sol_set:
        #     if len(item) > len(max_string):
        #         max_string = item
        # return len(max_string)

sol = Solution()
result = sol.lengthOfLongestSubstring("pwwkew")
print(result)