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
Use o código com cuidado.

📝 ETAPA 2: COMPUTAÇÃO GRÁFICA & UX/UI (Conteúdo para o README.md)

Substitua ou adicione o conteúdo abaixo no arquivo README.md do seu repositório.
markdown
# Análise Forense TerraVision - Mapeamento Urbano e Metrópoles
**Estudante:** [Seu Nome Completo]  
**Tema:** Mapeamento Urbano e Metrópoles (Alta Densidade de Edificações)  
**Disciplinas Integradas:** Ciência de Dados, Computação Gráfica, UX/UI & Análise Forense  
**Professora:** Angélica Neckel  

---

## 💻 1. Relatório Técnico de Computação Gráfica & UX/UI

### 1.1 Desafios de Processamento e Tratamento de Imagem (Stitching e Texturas)
O mapeamento de metrópoles com alta densidade de edificações impõe severos desafios para os algoritmos de renderização em tempo real:
* **Oclusão por Sombra Axial e Projetada:** Arranha-céus geram sombras longas que cobrem vias públicas e edificações menores. O algoritmo precisa aplicar tratamentos pontuais de exposição para evitar "pontos cegos" de informação visual nas calçadas.
* **Distorção de Perspectiva (Efeito Parallax) no Stitching:** Como as fotos de satélite/aéreas são tiradas de ângulos ligeiramente diferentes, os topos dos prédios parecem "tombar" em direções opostas nas emendas das fotos. Unificar essas imagens exige algoritmos complexos de retificação ortofotométrica (orthorectification) para alinhar as bases e as fachadas sem criar fraturas visuais na malha urbana.
* **Mapeamento de Texturas em Superfícies Especulares:** Vidro e metal (comuns em centros financeiros) refletem a luz solar diretamente para a câmera, estourando o canal de luminosidade. É necessário filtrar imagens brutas (RAW) e aplicar ajustes de contraste para homogeneizar a unidade visual.

### 1.2 Design de Interface e Leis da Gestalt aplicadas ao Tema
* **Lei da Proximidade:** Na interface do Google Earth, agrupamentos de elementos gráficos pequenos muito próximos (como blocos de prédios cinzas ou ícones de pontos de interesse sobrepostos) são instantaneamente interpretados pelo cérebro como "Zonas Comerciais/Centrais". Isso faz com que o usuário identifique o coração da metrópole antes mesmo de ler o nome das ruas.
* **Lei da Figura-Fundo:** Essencial para a navegação intuitiva. Quando o usuário executa o zoom aproximando-se do nível da rua (< 1.000m), o relevo tridimensional dos edifícios emerge como **Figura** principal em destaque, enquanto a malha cinza de asfalto assume o papel de **Fundo**. Esse contraste impede a desorientação espacial do usuário durante movimentos rápidos de rotação da câmera.

---

## 📸 2. Evidências Visuais e Capturas de Tela

*Instruções para o estudante:* Tire um print de satélite de uma metrópole muito densa (ex: Nova York, São Paulo ou Tóquio) no Google Earth, salve a imagem na pasta do seu repositório com o nome `metropole_3d.png` e certifique-se de que o link abaixo funcione.

![Mapeamento de Alta Densidade Urbana](metropole_3d.png)

---

## 🛠️ 3. Histórico de Commits Padronizado (Padrão de Auditoria Forense)

* `feat: implementado algoritmo de LoD condicional no script.py`
* `docs: estruturada análise de Gestalt e stitching urbano no README.md`
* `img: adicionada captura de tela de evidência urbana em alta resolução`
Use o código com cuidado.

