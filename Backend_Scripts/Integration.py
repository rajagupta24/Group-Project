from parser_evaluater import evaluate_equation

def integrate(equation:str, upper_limit:float, lower_limit:float, decimals:int = 4, divisions:int = 6):
    try:
        h = (upper_limit - lower_limit)/divisions

        dict_of_values = {}
        i = lower_limit
        while(i<=upper_limit):
            if i == 0.9999999999999999:
                i = 1.0
            dict_of_values[i] = evaluate_equation(equation, i)
            i += h

        #print(dict_of_values)
        result = (h/2) * (dict_of_values[lower_limit]+ dict_of_values[upper_limit])
        i = lower_limit + h
        while(i<=upper_limit-h):
            result += h*dict_of_values[i]
            i += h

        return (round(result,decimals))
    
    except: 
        return "Unknown Error: Try Using Brackets and Checking the Spelling"

if __name__=="__main__":
    print(integrate("1/(1-(0.25*sin(x)^2))", 1, 0))
