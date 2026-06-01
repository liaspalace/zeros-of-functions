import math

def get_dict(x) -> dict:
    return {
        "x": x,
        "ln": math.log,
        "sen": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "pi": math.pi,
        "e": math.e
    } 

def get_error_length(erro: float) -> int:
    casas = 4
    try:
        casas = len(str(erro).split(".")[1])
    except IndexError:
        pass
    return casas

def get_error(intervalo: list[float]) -> float: 
    return (intervalo[1] - intervalo[0]) / 2 

def get_resultado_da_funcao(funcao: str, x: float):
    return eval(funcao, {"__builtins__": None}, get_dict(x))

def get_midpoint(intervalo: list[float]) -> float:
    return (intervalo[0] + intervalo[1]) / 2

def bissecao(funcao: str, intervalo: list[float], erro_maximo: float):
    casas = get_error_length(erro_maximo)
    casas_trace = max(casas + 2, 4) 
    casas_x0 = casas + 1 

    while get_error(intervalo) > erro_maximo:
        a = intervalo[0] 
        b = intervalo[1]
        ponto_medio = get_midpoint(intervalo)

        fa = get_resultado_da_funcao(funcao, a)
        fm = get_resultado_da_funcao(funcao, ponto_medio)
        fb = get_resultado_da_funcao(funcao, b)

        # Lógica para identificar e guardar o sinal de cada resultado
        sinal_fa = "> 0" if fa > 0 else ("< 0" if fa < 0 else "= 0")
        sinal_fm = "> 0" if fm > 0 else ("< 0" if fm < 0 else "= 0")
        sinal_fb = "> 0" if fb > 0 else ("< 0" if fb < 0 else "= 0")

        print("\n*** Consideremos os intervalos: ***")
        print(f"[{a:.{casas_trace}f}; {ponto_medio:.{casas_trace}f}] e [{ponto_medio:.{casas_trace}f}; {b:.{casas_trace}f}]")
        
        # Adicionando o sinal no final do print de cada f(x)
        print(f"f({a:.{casas_trace}f}) = {fa:.{casas_trace}f} {sinal_fa}")
        print(f"f({ponto_medio:.{casas_trace}f}) = {fm:.{casas_trace}f} {sinal_fm}")
        print(f"f({b:.{casas_trace}f}) = {fb:.{casas_trace}f} {sinal_fb}")

        if fm == 0:
            print(f"*** Raiz exata encontrada: {ponto_medio:.{casas_trace}f} ***")
            intervalo[0] = ponto_medio
            intervalo[1] = ponto_medio
        elif fa * fm < 0:
            print(f"*** Logo, x0 E [{a:.{casas_trace}f}; {ponto_medio:.{casas_trace}f}] ***")
            intervalo[1] = ponto_medio
        else:
            print(f"*** Logo, x0 E [{ponto_medio:.{casas_trace}f}; {b:.{casas_trace}f}] ***")
            intervalo[0] = ponto_medio

        estimativa = get_midpoint(intervalo)

        if get_error(intervalo) > erro_maximo:
            print("*** Assim, uma nova estimativa é: ***")
            print(f"x0 pertence a {estimativa:.{casas_trace}f}")
            print(f"|e| <= {get_error(intervalo):.{casas_trace}f}")
            
    estimativa_final = get_midpoint(intervalo)
    erro_final = get_error(intervalo)
    
    print("\n*** ------------------------------------------------ ***")
    print(f"*** Assim, a raiz aproximada final encontrada é: ***")
    print(f"*** x0 pertence a {estimativa_final:.{casas_x0}f} ***")
    print(f"*** |e| <= {erro_final:.{casas}f} ***")
    print("*** ------------------------------------------------ ***\n")

    return estimativa_final, erro_final