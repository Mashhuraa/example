

class Solution(object):
    def lengthOfLastWord(self, s):
        """ 
        :type s: str
        :rtype: int
        """
        words = s.split(" ")
        print(f'words: {words}')
        words_only = []
        for word in words:
            if len(word)>0:
                words_only.append(word)
        print(f'words only: {words_only}')
        last_word = words_only[-1]
        print(f'last word: {last_word}')
        print(len(last_word))
        return len(last_word)
    

sl = Solution()

s = ' Hi world  again   '

lng = sl.lengthOfLastWord(s)
print(f'length: {lng}') 
