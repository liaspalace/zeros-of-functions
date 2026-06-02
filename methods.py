import math

def criar_dicionario(x) -> dict:
    return {
        "x": x,
        "ln": math.log,
        "sen": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "pi": math.pi,
        "e": math.e
    } 

def calcular_erro(intervalo: list[float]) -> float: 
    return abs(intervalo[1] - intervalo[0]) / 2 

def calcular_resultado_da_funcao(funcao: str, x: float):
    return eval(funcao, criar_dicionario(x))

def calcular_ponto_medio(intervalo: list[float]) -> float:
    return (intervalo[0] + intervalo[1]) / 2

def calcular_sinal(valor):
    if valor > 0:
        return "> 0"
    elif valor < 0:
        return "< 0"
    else:
        return "= 0"

def bissecao(funcao: str, intervalo: list[float], erro_maximo: float):
   
    while calcular_erro(intervalo) > erro_maximo:
        a = intervalo[0] 
        b = intervalo[1]
        ponto_medio = calcular_ponto_medio(intervalo)

        fa = calcular_resultado_da_funcao(funcao, a)
        fm = calcular_resultado_da_funcao(funcao, ponto_medio)
        fb = calcular_resultado_da_funcao(funcao, b)

        print("\n")
        print(f"Consideremos os intervalos:")
        print(f"[{a}; {ponto_medio}] e [{ponto_medio}; {b}]")
        print(f"f({a}) ≈ {fa} ({calcular_sinal(fa)})")
        print(f"f({ponto_medio}) ≈ {fm} ({calcular_sinal(fm)})")
        print(f"f({b}) ≈ {fb} ({calcular_sinal(fb)})")

        if fa * fm < 0:
            print(f"Logo, x0 ∈ [{a}; {ponto_medio}]")
            intervalo[1] = ponto_medio
            
        else:
            print(f"Logo, x0 ∈ [{ponto_medio}; {b}]")
            intervalo[0] = ponto_medio

        estimativa = calcular_ponto_medio(intervalo)

        print("Assim, uma nova estimativa é:")
        print(f"x0 ≈ {estimativa}")
        print(f"|e| <= {calcular_erro(intervalo)}")

    print("\nErro máximo atingido.")
    print(f"x0 ≈ {calcular_ponto_medio(intervalo)}")
    print(f"|e| <= {calcular_erro(intervalo)}")
    
    return calcular_ponto_medio(intervalo), calcular_erro(intervalo)
