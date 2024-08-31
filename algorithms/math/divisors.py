import math

class divisors:

    def findAllDivisors(self, n):
        result = list()

        for i in range(1, n+1):
            if (n%i == 0): 
                result.append(i)
        
        return result

    def divisorsCount(self, n):
        divs = self.findAllDivisors(n)
        return len(divs)

    def oddFactors(self, n):
        result = list()

        for i in range(1, n+1):
            if (n%i == 0 and i%2==1): 
                result.append(i)
        
        return result

    def oddFactorsSum(self, n):
        divs = self.oddFactors(n)
        return sum(divs)

    def evenFactors(self, n):
        result = list()

        for i in range(1, n+1):
            if (n%i == 0 and i%2==0): 
                result.append(i)
        
        return result

    def evenFactorsSum(self, n):
        divs = self.evenFactors(n)
        return sum(divs)

    def primeFactors(self, n):
        result = list()

        while n % 2 == 0: 
            result.append(2) 
            n = n / 2

        for i in range(3,int(math.sqrt(n))+1,2): 
            while n % i== 0: 
                result.append(i) 
                n = n / i 
                
        if n > 2: 
            result.append(n)
        
        return result

    def primeFactorsSum(self, n):
        divs = self.primeFactors(n)
        return sum(divs)
