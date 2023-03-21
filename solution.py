class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        substrl = len(words[0])
        reverse = (len(words) - 1)*substrl
        wordMap = defaultdict(int)
        for word in words:
            wordMap[word] += 1
        # print(wordMap)
        tempMap = copy.deepcopy(wordMap)
        found = True
        location = []
        for i in range(0, len(s)):
            for j in range(i, i+len(words)*substrl, substrl):
                if j > len(s):
                    break 
                
                substr = s[j:j+substrl]
                # print(f"substring: {substr}, I: {i}, J: {j}")
                if substr in wordMap:
                    if wordMap[substr] > 0:
                        wordMap[substr] -= 1
                    else:
                        wordMap = copy.deepcopy(tempMap)
                        break
                else:
                    wordMap = copy.deepcopy(tempMap)
                    break
                # values = wordMap.values()
                # print(wordMap)
                for k in wordMap: 
                    if wordMap[k] == 0:
                        continue
                    else:
                        found = False
                        break
                # print(found)
                if found: 
                    if i > 0:
                        location.append(j-reverse)
                    else:
                        location.append(0)
                    wordMap = copy.deepcopy(tempMap)
                else:
                    found = True
        return location
            
                    


        