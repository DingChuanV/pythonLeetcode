class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)

        right, ans = -1, 0

        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while right + 1 < n and s[right + 1] not in occ:
                occ.add(s[right + 1])
                right += 1
            ans = max(ans, right - i + 1)
        return ans

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len =0
        cur_len=0
        for i in range(n):
            cur_len+=1
            while s[i] in lookup:
                lookup.remove(s[left])
                left+=1
                cur_len-=1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
