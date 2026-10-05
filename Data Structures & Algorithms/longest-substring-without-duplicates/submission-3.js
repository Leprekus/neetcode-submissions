class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const NULL = 256;
        let start = 0; // start contains the position for last seen char
        const hash = new Uint16Array(257).fill(NULL);
        let maxLen = 0;
        /*
        0  1  2 ..
        |__|__|

        - we make 'start' point to the 'beginning' of the container
        - and 'i' points to the 'end' of the contaner.
        each time we update 'start' it must point to where 'i' previously was.
        

              a b b a
        hash  1 2 3 4
        start 0 0 2 1
        len
        */
        s.split('').forEach((char, i) => {
            const key = char.charCodeAt(0);
            // a. hash track the ith+1 pos for new chars
            if(hash[key] === NULL) {
                hash[key] = i + 1;
            } else {
                // b. hash updates start & then does a. 
                start = hash[key] > start ? 
                    hash[key]:
                    start++;
                hash[key] = i + 1;
            }
            if(hash[key] - start > maxLen) 
                maxLen = hash[key] - start;
        });
    
        return maxLen;
    }
}
