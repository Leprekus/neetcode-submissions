class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        M = {}
        ret = []
        # track last occurrence of each char
        for i, char in enumerate(s):
            M[char] = i
        
        # track partition
        currentPartition = 0
        start = 0
        isFirst = True
        for i, char in enumerate(s):
            # if we are inside a partition
            # grab the maximum element of it
            if i <= currentPartition and M[char] > currentPartition:
                currentPartition = M[char]
            if i == currentPartition:
                if isFirst : 
                    ret.append(currentPartition + 1 - start)
                    isFirst = False
                else: ret.append(currentPartition - start)
                start = i
                currentPartition = M[ s[min(i + 1, len(s) - 1)]]
        #print(ret)
        return ret

            

        

            
        
            
        