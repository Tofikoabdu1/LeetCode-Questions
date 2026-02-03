class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0
        while right < len(chars):
            curr = chars[right]
            count =0
            while right < len(chars) and curr == chars[right]:
                count+=1
                right+=1
            chars[left] = curr
            left+=1
            if count > 1:
                for i in str(count):
                    chars[left] = i
                    left+=1
        return left


        