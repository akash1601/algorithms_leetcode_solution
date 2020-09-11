 def wordBreak(s,wordDict):
            wordDict = set(wordDict)
            print(wordDict)
            words = [0]
            for i in range(0,len(s)):
                for word in reversed(words):
                    if s[word:i+1] in wordDict:
                        words.append(i+1)
                        if i == len(s) - 1:
                            return True
                        break

            return False