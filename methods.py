import math

def get_dict(x, y)-> dict:
    return{
        "x": x,
        "y": y,
        "ln" : math.log,
        "sen": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "pi": math.pi
    } 

def get_error_length(erro: float) -> int:
    return len(str(erro).split(".")[1]) 

def get_error(intervalo: list[float]) -> float: 
    return (intervalo[1] - intervalo[0])/2 #TODO: colocar casas decimais no print do resultado

def get_resultado_da_funcao(funcao:str, x: float, y: float):
    return eval(funcao, get_dict(x, y))

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

        print(f"Consideremos os intervalos:")
        print(
            f"[{a:.2f}; {ponto_medio:.2f}] e [{ponto_medio:.2f}; {b:.2f}]"
        )
        print(f"f({a:.2f}) = {fa:.2f}")
        print(f"f({ponto_medio:.2f}) = {fm:.2f}")
        print(f"f({b:.2f}) = {fb:.2f}")

        if (fa < 0 and fm > 0) or (fa > 0 and fm < 0):
            print(f"Logo, x0 E [{a:.2f}; {ponto_medio:.2f}]")
            intervalo[1] = ponto_medio
            
        elif (fm < 0 and fb > 0) or (fm > 0 and fb < 0):
            print(f"Logo, x0 E [{ponto_medio:.2f}; {b:.2f}]")
            intervalo[0] = ponto_medio

        estimativa = get_midpoint(intervalo)

        print("Assim, uma nova estimava é:")
        print(f"x0 pertence {estimativa}")
        print(f"|e| <= {get_error(intervalo):.{get_error_length(get_error(intervalo))}f}")
    return get_midpoint(intervalo), get_error(intervalo)




