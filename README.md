## Projeto: Cadeia de Produção da Resina

### Descrição
Este projeto simula a cadeia de produção da resina, abrangendo desde a extração até a comercialização. O programa visa analisar os custos de produção e transporte, além de estimar a receita com base em parâmetros definidos. O resultado é apresentado por meio de relatórios em CSV e visualizações gráficas.

### Funcionalidades
1. **Cálculo de Custos**:
   - Custos de extração, processamento e mão de obra.
   - Custos logísticos com base na distância(km) e no custo por quilômetro.
2. **Estimativa de Receita**:
   - Baseada no preço de venda por unidade e na procura estimada.
3. **Relatórios**:
   - Gera relatórios detalhados em CSV.
   - Exibe gráficos de barras para facilitar a análise visual dos resultados.

### Estrutura do Projeto
```
/resin_project
├── project.py          # Código principal do projeto
├── test_project.py     # Testes automatizados
├── requirements.txt    # Dependências do projeto
├── README.md           # Documentos do projeto
└── data/               # Arquivos do projeto
```

### Requesitos
- **Python**
- Bibliotecas estao referidas no arquivo `requirements.txt`

### Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone <https://github.com/acmenoita/CadeiaProducaoResina.git>
   cd resin_project
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o programa:
   ```bash
   python project.py
   ```
4. Para fazer os testes:
   ```bash
   pytest test_project.py
   ```

### Entrada e Saída
- **Entrada**: Os parâmetros do processo (custos, distâncias, procura) são definidos no código.
- **Saída**:
  - Relatório em CSV: `resin_report.csv`
  - Gráfico de barras exibido no ecrã.

### Melhoria Futura
- Expandir o modelo para incluir análise de outros parametros como o sequestro de carbono.

### Autoria
Este projeto foi desenvolvido como parte de um trabalho universitario (IntPython), com o objetivo de explorar os aspetos economicos e logisticos da cadeia de produção da resina "natural".
