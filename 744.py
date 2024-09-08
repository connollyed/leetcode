class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        letters.sort()
        print(letters)

        for idx,val in enumerate(letters):
            if val == target:
                ret = (idx + 1) % len(letters)

        return letters[ret]