class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op == "+":
                score1 = scores.pop()
                score2 = scores.pop()
                new_score = score1 + score2
                scores.append(score2)
                scores.append(score1)
                scores.append(new_score) 
            elif op == "D":
                score_double = scores.pop()
                score_doubled = score_double * 2
                scores.append(score_double)
                scores.append(score_doubled)
            elif op == "C":
                scores.pop()
            else:
                scores.append(int(op))
            

        score = sum(scores)
        return score