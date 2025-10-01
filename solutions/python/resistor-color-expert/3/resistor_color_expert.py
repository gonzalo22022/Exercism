colores = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
tolerancia = {'grey':'0.05%','violet':'0.1%','blue':'0.25%','green':'0.5%','brown':'1%','red':'2%','gold':'5%','silver':'10%'}
def resistor_label(colors):
 
    
    

    if len(colors) not in (1, 4, 5):
        return "Invalid input"  

    
    if len(colors) == 1:
        return f'{colores.index(colors[0])} ohms'
    
    if len(colors) == 4:
        numero_str = ''.join(str(colores.index(color))for color in colors[:2])  
        multiplicador = colores.index(colors[2])
    else:
        numero_str= ''.join(str(colores.index(color))for color in colors[:3])
        multiplicador = colores.index(colors[3])
    
    valor = int(numero_str)*(10 ** multiplicador)
    

    tol = ""
    if len(colors) >= 4:
        tol_val = tolerancia.get(colors[-1], '')
        if tol_val:
             tol = f" ±{tol_val}"


    if valor <1_000:
        return f'{valor} ohms{tol}' 
    elif valor < 1_000_000:
        num_formateado = f'{valor/1_000:.2f}'.rstrip('0').rstrip('.')
        return f'{num_formateado} kiloohms{tol}'
    elif valor < 1_000_000_000:
        num_formateado1 = f'{valor/1_000_000:.2f}'.rstrip('0').rstrip('.')
        return f'{num_formateado1} megaohms{tol}'
    else:
        num_formateado2 = f'{valor/1_000_000_000:.2f}'.rstrip('0').rstrip('.')
        return f'{num_formateado2} gigaohms{tol}'