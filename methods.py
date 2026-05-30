import math

def get_dict()-> dict:
    return{
        "x": x,
        "y": y,
        "ln" : math.log,
        "sen": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "pi": math.pi
    }

def get_interval_length(intervalo: str) -> int:
    return len(intervalo)

def get_error(intervalo: list[float]) -> float: 
    return (intervalo[1] - intervalo[0])/2 #TODO: colocar casas decimais no print do resultado

def get_resultado_da_funcao(funcao:str):
    return eval(funcao, get_dict())

def get_midpoint(intervalo: list[float]) -> float:
    return (intervalo[0] + intervalo[1]) / 2

def bissecao(funcao:str, intervalo: list[float], erro_maximo: float):
    while get_error(intervalo) > erro_maximo:
        a = intervalo[0] # [-2;-1.5] e [-1,5;-1]
        b = intervalo[1]
        ponto_medio = get_midpoint(intervalo)

        fa = get_resultado_da_funcao(funcao, a)
        fm = get_resultado_da_funcao(funcao, ponto_medio)
        fb = get_resultado_da_funcao(funcao, b)

        if (fa < 0 and fm > 0) or (fa > 0 and fm < 0):
            print(f"Logo, x0 E {{a}; {ponto_medio}}")
            intervalo[1] = ponto_medio
            
        elif (fm < 0 and fb > 0) or (fm > 0 and fb < 0):
            intervalo[0] = ponto_medio

        estimativa = get_midpoint(intervalo)
        print(f"x0 pertence {estimativa}")
        print(f"|e| <= {get_error(intervalo)}")
    return get_midpoint(intervalo)

def bissecao_x(funcao:str, intervalo: list[int], precisao: int):
    a = intervalo[0]
    b = intervalo[1]
    erro = get_error(intervalo)
    resultado = get_resultado_da_funcao(funcao)
    while erro > precisao:
        if resultado == 0:
            return a
        elif resultado * get_resultado_da_funcao(funcao.replace("x", str(a))) < 0:
            b = (a + b) / 2
        else:
            a = (a + b) / 2
        erro = get_error([a, b])
        resultado = get_resultado_da_funcao(funcao.replace("x", str((a + b) / 2)))
    return (a + b) / 2


