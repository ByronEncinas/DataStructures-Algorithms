
"""             Video Analysis: https://www.youtube.com/watch?v=gqXU1UyA8pk


- Two Pointers


"""

## NeetCode Simple Solution


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## NeetCode Simple Solution
        WindowCount = {}
        res = 0
        maxfreq = 0
        lp = 0

        for rp in range(len(s)):
            ## add count of freqs in window [lp -> rp]
            WindowCount[s[rp]] = 1 + WindowCount.get(s[rp], 0)

            # compare current maximum in window with last maximum count
            maxfreq = max(maxfreq, WindowCount[s[rp]])

            # pan to all element that don't belong to window anymore
            while (rp - lp + 1) - maxfreq > k:
                WindowCount[s[lp]] -= 1
                lp += 1
            res = max(res, rp - lp + 1)

        return res