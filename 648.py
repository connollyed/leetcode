class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        res = []
        sentence = sentence.split(" ")
        for word in sentence:
            shortest_derivative = word
            for derivative in dictionary:
                n = len(derivative)
                if derivative == word[0:n]:               
                    if len(shortest_derivative) > len(derivative):
                       shortest_derivative = derivative
            
            res.append(shortest_derivative)

        return " ".join(res)