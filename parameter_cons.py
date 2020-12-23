class Sum:
    first_value=0
    second_value=0
    result=0
    
    #PARAMETERISED CONSRTRUCTOR
    def __init__(self, f,s):
        self.first_value = f
        self.second_value = s 

    def view(self):
        print('First value = ' + str(self.first_value))
        print('Second value = ' + str(self.second_value))
        print('Sum of two values = ' +str(self.result))

    def calculation(self):
        self.result = self.first_value + self.second_value

obj = Sum(10,20)
obj.calculation()
obj.view()
