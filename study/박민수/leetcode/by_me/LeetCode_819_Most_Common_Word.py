import collections
import re
from typing import List
# ㅁㄹ겠음

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = [x for x in re.sub(r'[^\w]',' ',paragraph)
                .lower().split()
                    if x not in banned]
        count = collections.Counter(word)
        return count.most_common(1)[0][0]



s = Solution()
s.mostCommonWord("he is a man",["man"])
