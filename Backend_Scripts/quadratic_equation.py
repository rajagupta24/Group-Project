import math

def change_signs(equation):
    equation = spacer(equation)
    if equation[0]!="-" or equation[0]!="+":
        equation = "+" + equation
    if "=" in equation:
        splits = equation.split("=") # ["4x + 5x ", "9 + 14"]
        required_terms = spacer(splits[1])
        bare = spacer(splits[0])

        for term in required_terms.split():
            if term[0]!="+" and term[0]!="-":
                bare += "-" + term
            elif term[0]=="+":
                bare += "-" + term[1:]
            else:
                bare += "+" + term[1:]
        return spacer(bare)
    return spacer(equation)

def spacer(equation):
    equation = equation.replace(" ","")
    if("=0") in equation:
        equation = equation.replace("=0", "")
    equation = equation.replace("+"," +").replace("-"," -")
    return equation
    


def classifier(equation):
    dict = {"a":0, "b":0, "c":0}
    terms = equation.split()
    for term in terms:
        term = term.lower()
        if term.endswith("x"):
            if len(term) == 2:
                dict["b"] += int(term[0] + "1")
            else:
                dict["b"] += int(term.split("x")[0])
        elif  "x2" in term or "x^2" in term:
            if len(term) == 3:
                dict["a"] += int(term[0] + "1")
            else:
                dict["a"] += int(term.split("x2")[0] if "x2" in term else term.split("x^2")[0])
        else:
            dict["c"] += int(term)
    return dict

def quad(coeff):
    # print(coeff)
    delta = coeff["b"]**2 - 4*coeff["a"]*coeff["c"]
    if delta < 0:
        print("There are no real roots.")
        return None
    elif delta == 0:
        sol1 = -coeff["b"] / (2*coeff["a"])
        print(f"The only real root is {sol1}")
        return [sol1]
    else:
        sol1 = (-coeff["b"] + math.sqrt(delta)) / (2*coeff["a"])
        sol2 = (-coeff["b"] - math.sqrt(delta)) / (2*coeff["a"])
        print(f"The two real roots are {sol1} and {sol2}")
        return [sol1,sol2]

def calculate(equation):
    # print(spacer(equation))
    # print(change_signs(equation))
    # print(classifier(equation))
    return quad(classifier(change_signs(equation)))

calculate("3x - 7x^2 = -4")