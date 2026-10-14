"""
Projeto: analise-forense-terravision
Disciplina: Ciência de Dados & Lógica Computacional
Tema: Mapeamento Urbano e Metrópoles (Alta Densidade de Edificações)
Professora: Angélica Neckel
"""

def carregar_camada_satelite(lista_altitudes):
    """
    Determina o nível de renderização (LoD) com base na altitude da câmera
    para cenários de alta densidade urbana.
    """
    print(f"--- Iniciando Processamento de LoD Urbano (Total de Amostras: {len(lista_altitudes)}) ---")
    
    for i, altitude in enumerate(lista_altitudes, start=1):
        print(f"\n[Amostra {i}] Altitude: {altitude:,} metros")
        
        if altitude > 10000:
            # Altitude > 10.000m: Baixa Resolução (Mosaico Geral)
            print(">> Renderizando: Camada de Baixa Resolução.")
            print(">> Detalhe: Exibindo macro-mosaico continental e limites biogeográficos globais. Malha urbana invisível.")
            
        elif 1000 <= altitude <= 10000:
            # Altitude entre 1.000m e 10.000m: Média Resolução (Mosaico Regional)
            print(">> Renderizando: Camada de Média Resolução.")
            print(">> Detalhe: Delimitando manchas urbanas metropolitanas, grandes eixos rodoviários, contornos de bairros e corpos d'água principais.")
            
        else:
            # Altitude < 1.000m: Alta Resolução (Detalhes Finos do Tema)
            print(">> Renderizando: Camada de Alta Resolução (Foco Temático).")
            print(">> Detalhe: Renderizando malha fina tridimensional (3D Mesh) de arranha-céus, sombreamento de fachadas, rampa de prédios e projeção de tráfego local.")

# Simulação de aproximação de câmera virtual (mínimo de 5 valores exigidos)
altitudes_simuladas = [15000, 8500, 3200, 850, 250]

# Execução do algoritmo forense
carregar_camada_satelite(altitudes_simuladas)
