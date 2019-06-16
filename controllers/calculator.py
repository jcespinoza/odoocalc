class Calculator():
    def add(self, x, y):
        return x + y

    def evalute(self, reqObj):
        return {
            'success': True,
            'errorMessage': "Something went pretty bad",
            'output': 5 + 9
        }