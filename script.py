import numpy as np

def carregar_camada_satelite(lista_altitudes):
    """
    Simula o carregamento adaptativo de camadas de satélite (LoD)
    para o cenário de Mapeamento Urbano e Metrópoles.
    """
    print(f"=== INICIANDO RENDERIZAÇÃO: MAPEAMENTO URBANO E METRÓPOLES ===")
    
    # Garantindo o processamento via estrutura de dados/arrays
    altitudes_array = np.array(lista_altitudes)
    
    for i, altitude in enumerate(altitudes_array, start=1):
        print(f"\n[Leitura {i}] Altitude da Câmera: {altitude:.2f} metros")
        
        # Estrutura Condicional para determinação do LoD
        if altitude > 10000:
            print(">> Camada de BAIXA RESOLUÇÃO carregada.")
            print("   [Renderizando]: Mosaico global do planeta. Silhueta dos continentes, manchas urbanas macroscópicas e grandes eixos continentais.")
            
        elif 1000 <= altitude <= 10000:
            print(">> Camada de MÉDIA RESOLUÇÃO carregada.")
            print("   [Renderizando]: Mosaico regional metropolitano. Divisão de distritos, grandes avenidas, anéis rodoviários, aeroportos e contornos de bairros densos.")
            
        else: # altitude < 1000m
            print(">> Camada de ALTA RESOLUÇÃO carregada.")
            print("   [Renderizando]: Detalhes urbanos finos. Modelagem 3D de edifícios, projeção de sombras prediais, mobiliário urbano, malha de ruas locais e telhados de alta densidade.")

# Massa de dados de teste simulando a aproximação (zoom in) da câmera sobre a metrópole
simulacao_voo = [25000.0, 12000.5, 7500.0, 3200.2, 850.0, 120.7]

# Execução da função
carregar_camada_satelite(simulacao_voo)
