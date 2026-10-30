class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()

        for word in words:
            code = ""
            for i in word:
                index = ord(i) - ord('a')
                code += morse[index]
            # if code not in res:
            res.add(code)
        return len(res)
        
