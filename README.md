#  SRI - Sistema de Reconhecimento de Imagem

> Uma ferramenta de Inteligência Artificial capaz de classificar objetos em imagens com alta precisão utilizando Deep Learning (EfficientNet V2).

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Model](https://img.shields.io/badge/Model-EfficientNet%20V2%20(Large)-success)

##  Sobre o Projeto

O **SRI (Sistema de Reconhecimento de Imagem)** é uma aplicação desenvolvida em Python que utiliza redes neurais convolucionais (CNNs) de última geração para analisar e identificar o conteúdo de imagens provenientes da internet.

O núcleo do projeto baseia-se no modelo **EfficientNet V2 Large**, uma arquitetura conhecida pela sua eficiência e elevada taxa de acerto no dataset ImageNet. O sistema foi desenhado para ser interativo, robusto a falhas e educativo, demonstrando como integrar modelos de visão computacional pré-treinados em aplicações reais.

### Funcionalidades Principais
* **Análise via URL:** Processa imagens diretamente da web sem necessidade de download manual.
* **Deep Learning de Ponta:** Utiliza o modelo `EfficientNet_V2_L`, superior a modelos clássicos como o ResNet50.
* **Feedback Detalhado:** Apresenta a classificação principal e o grau de certeza (confiança) da IA.
* **Tratamento de Erros:** Sistema robusto (`try/except`) que previne falhas com links quebrados ou ficheiros inválidos.
* **Interface Interativa:** CLI (Linha de Comandos) com loops de repetição e menus intuitivos.

##  Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Motor de IA:** [PyTorch](https://pytorch.org/) & Torchvision
* **Processamento de Imagem:** PIL (Pillow)
* **Requisições Web:** Requests

##  Como Executar

### Pré-requisitos
Certifica-te de que tens o **Python 3.12** instalado no teu computador.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/TEU-USUARIO/SRI-Image-Recognizer.git](https://github.com/TEU-USUARIO/SRI-Image-Recognizer.git)
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Utilização

Execute o ficheiro principal através do terminal:
```bash
python main.py
