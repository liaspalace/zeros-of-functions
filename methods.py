import math

def get_dict(x)-> dict:
    return{
        "x": x,
        "ln" : math.log,
        "sen": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "pi": math.pi,
        "e" : math.e
    } 

def get_error_length(erro: float) -> int:
    return len(str(erro).split(".")[1]) 

def get_error(intervalo: list[float]) -> float: 
    return (intervalo[1] - intervalo[0])/2 #TODO: colocar casas decimais no print do resultado

def get_resultado_da_funcao(funcao:str, x: float):
    return eval(funcao, get_dict(x))

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
        print(f"[{a:.4f}; {ponto_medio:.4f}] e [{ponto_medio:.4f}; {b:.4f}]")
        print(f"f({a:.4f}) = {fa:.4f}")
        print(f"f({ponto_medio:.4f}) = {fm:.4f}")
        print(f"f({b:.4f}) = {fb:.4f}")

        if fa * fm < 0:
            print(f"Logo, x0 E [{a:.4f}; {ponto_medio:.4f}]")
            intervalo[1] = ponto_medio
            
        else:
            print(f"Logo, x0 E [{ponto_medio:.4f}; {b:.4f}]")
            intervalo[0] = ponto_medio

        estimativa = get_midpoint(intervalo)

        print("Assim, uma nova estimava é:")
        print(f"x0 pertence {estimativa}")
        print(f"|e| <= {get_error(intervalo):.4f}")
    return get_midpoint(intervalo), get_error(intervalo)