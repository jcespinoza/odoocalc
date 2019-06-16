import re
class Calculator():
    def add(self, x, y):
        return x + y

    def evalute(self, reqObj):
        strInput = reqObj['input']
        inputMatches = re.match(r"^(\d)*\s*([+\-\/*÷]\s*(\d)*)*\s*$", strInput)
        if inputMatches == None:
            return {
                'success': False,
                'errorMessage': "I'm confused. Is that an arithmetic expression?",
                'output': None
            }
        try:
            evalResult = eval(strInput)

            return {
                'success': True,
                'errorMessage': "All cool",
                'output': evalResult
            }
        except:
            return {
                'success': False,
                'errorMessage': "Sorry, I haven't learned how to process that",
                'output': None
            }