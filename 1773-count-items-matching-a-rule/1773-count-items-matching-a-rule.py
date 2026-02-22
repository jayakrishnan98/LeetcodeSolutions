class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleDictionary = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        sum = 0
        for item in items:
            if item[ruleDictionary[ruleKey]] == ruleValue:
                sum += 1 
        return sum