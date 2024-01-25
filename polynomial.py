import sys
class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    #Takes a value for x and returns that value
    def evaluate(self, x):
        return x

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, x):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)
    
#Implementing Sub class, which is very similar to the Add class

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # If p2 is an add, we want parentheses to ensure the negative is distributed
        if isinstance(self.p2, Add):
            return repr(self.p1) + " - ( " + repr(self.p2) + " )"
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)
    
class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub)):
            if isinstance(self.p2, (Add, Sub)):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub)):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        #To ensure PEMDAS, we need parentheses around any Add or Sub expressions within a Mul or Div
        if isinstance(self.p1, (Add, Sub)):
            if isinstance(self.p2, (Add, Sub)):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub)):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)
    
    def evaluate(self, x):
        #If p2 evaluates to 0, print DivByZero error and stop program execution
        try:
            return self.p1.evaluate(x) / self.p2.evaluate(x)
        except ZeroDivisionError:
            print("Error: Cannot Divide by Zero. Try a different value for X")
            sys.exit(1)
            

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(-1))

p = Mul(Sub(Int(4), X()), X())
print(p)
print(p.evaluate(2))



