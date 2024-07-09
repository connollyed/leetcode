class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        count = 0
        word = []
        for i in s:
            if i == ")":
                if count <= 0:
                    pass
                else:
                    word.append(i)
                    count -= 1
            elif i == "(":
                word.append(i)
                count += 1
            else:
                word.append(i)

        print(word)

        word = word[::-1]
        print()

        count = 0
        ret_word = []
        for i in word:
            if i == "(":
                if count <= 0:
                    pass
                else:
                    ret_word.append(i)
                    count -= 1

            elif i == ")":
                count += 1
                ret_word.append(i)
            else:
                ret_word.append(i)

        ret_word = ret_word[::-1]
        ret_word = "".join(ret_word)
        return ret_word