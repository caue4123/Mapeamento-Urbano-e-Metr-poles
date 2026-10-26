# Análise Forense Computacional e Computação Gráfica - Caso TerraVision

## 👤 Identificação do Estudante
* **Nome:** Cauê de Mattos Amaral
* **Tema Designado:** 1. Mapeamento Urbano e Metrópoles (Alta Densidade de Edificações)
* **Disciplinas Integradas:** Ciência de Dados, Computação Gráfica, UX/UI, Lógica de Programação e Perícia Forense.
* **Professora:** Angélica Neckel

---

## 🌆 1. Processamento e Tratamento de Imagem no Cenário Urbano

O mapeamento de regiões metropolitanas de alta densidade apresenta desafios severos para os algoritmos de computação gráfica e processamento de imagens de satélite. Os principais problemas enfrentados no cenário urbano são:

* **Desafio do Mosaico e Costura de Imagem (*Stitching*):** Imagens urbanas capturadas em momentos ou ângulos ligeiramente diferentes sofrem com o deslocamento de paralaxe dos edifícios. Ao tentar "costurar" duas fotos adjacentes, os arranha-céus podem parecer cortados, tortos ou duplicados nas emendas das texturas caso o algoritmo não execute uma ortorretificação precisa (projeção nadir corrigida).
* **Oclusão por Sombra e Uniformização de Cor:** Edificações altas projetam grandes sombras sobre vias públicas e construções menores. Essas sombras geram áreas de baixíssimo contraste e perda de dados cromáticos. O algoritmo precisa aplicar correções de histograma locais e balanceamento de luminosidade para evitar que o tecido urbano pareça manchado ou escurecido artificialmente.
* **Aliasing em Altas Frequências Espaciais:** Telhados, janelas de prédios e faixas de trânsito criam padrões repetitivos de alta frequência. Sem filtros de decimação e *mipmapping* adequados durante a redução do zoom, essas texturas geram o indesejado **Efeito Moiré** (linhas cintilantes falsas na tela).

---

## 🎨 2. Design de Interface e Leis da Gestalt na Navegação

A transição suave do espaço orbital para o nível da rua exige que a interface gráfica guie a percepção espacial do usuário de forma imediata. Identificamos as seguintes leis aplicadas:

1. **Lei da Continuidade:** Conforme o usuário aproxima o zoom na metrópole, as grandes linhas estruturais (como rios urbanos, rodovias e avenidas principais) mantêm uma trajetória visual fluida. O cérebro do usuário acompanha essas linhas contínuas para se localizar geograficamente, mesmo quando texturas de alta resolução ainda estão sendo carregadas em blocos (*tiles*).
2. **Lei da Proximidade:** Elementos visuais muito próximos no mapa são agrupados mentalmente como uma unidade. No zoom macro, uma grande concentração de polígonos cinzas e retangulares próximos indica instantaneamente uma **zona central densa (centro da metrópole)**, separando-a visualmente de áreas verdes ou industriais periféricas antes mesmo da leitura de rótulos textuais.

O design gráfico orienta a navegação através de marcadores de escala flutuantes e vetores de relevo 3D que se inclinam de forma intuitiva à medida que a câmera cruza a barreira dos 1.000 metros de altitude, alterando o foco de visão ortogonal (plana) para perspectiva (tridimensional).

---

## 📸 3. Evidência Visual (Captura de Tela do Google Earth)

> **⚠️ Instrução Importante para o Estudante:** Abra o Google Earth Pro ou Web, dê zoom em uma metrópole altamente densa (como São Paulo, Nova York ou Tóquio) até que os prédios 3D fiquem visíveis. Tire um print, salve a imagem na pasta do seu repositório como `metropole.png` e certifique-se de que a linha abaixo carregará a imagem corretamente no seu GitHub.

![Mapeamento de Alta Densidade Urbana](https://www.quintoandar.com.br/regioes-atendidas/sao-paulo-sp-brasil-41d49u4ekw)

---

## ⏱️ Histórico de Commits Padronizado
* `feat: estrutura inicial do repositorio e escopo do tema 1`
* `feat: implementacao da funcao de LoD urbano em script.py`
* `docs: redacao tecnica dos desafios de processamento urbano e leis da Gestalt`
* `docs: inclusao da captura de tela da metropole mapeada 3D`
