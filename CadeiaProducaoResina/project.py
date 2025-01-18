import pandas as pd
import matplotlib as plt

class ResinProduction: #Calcular o custo total da producao considerando a extraçao, o processameno e a mao de obra
    def __init__(self, extraction_cost, processing_cost, labor_cost):
        self.extraction_cost = extraction_cost
        self.processing_cost = processing_cost
        self.labor_cost = labor_cost

    def calculate_total_cost(self):
        return self.extraction_cost + self.processing_cost + self.labor_cost

class Logistics: #Calcular o custo de transporte com base na distancia e no custo por Km
    def __init__(self, distance, cost_per_km):
        self.distance = distance
        self.cost_per_km = cost_per_km

    def calculate_transport_cost(self):
        return self.distance * self.cost_per_km

class Market: #Estimar a receita com base na procura e no preço de venda
    def __init__(self, selling_price_per_unit, demand):
        self.selling_price_per_unit = selling_price_per_unit
        self.demand = demand

    def calculate_revenue(self):
        return self.selling_price_per_unit * self.demand

def generate_report(production_cost, transport_cost, revenue):
    data = {
        'Category': ['Production Cost', 'Transport Cost', 'Revenue'],
        'Amount': [production_cost, transport_cost, revenue]
    }
    df = pd.DataFrame(data)
    df.to_csv('resin_report.csv', index=False)
    print("Report saved as resin_report.csv")

def visualize_data(production_cost, transport_cost, revenue):
    categories = ['Production Cost', 'Transport Cost', 'Revenue']
    amounts = [production_cost, transport_cost, revenue]

    plt.bar(categories, amounts, color=['blue', 'green', 'orange'])
    plt.title('Economic Analysis of Resin Production')
    plt.xlabel('Category')
    plt.ylabel('Amount ($)')
    plt.show()

def main():
    # Input data 
    extraction_cost = 5000
    processing_cost = 3000
    labor_cost = 2000
    distance = 150  # in km
    selling_price_per_unit = 50
    demand = 400

    # CCalculos
    production = ResinProduction(extraction_cost, processing_cost, labor_cost)
    production_cost = production.calculate_total_cost()

    transport = Logistics(distance, cost_per_km)
    transport_cost = transport.calculate_transport_cost()

    market = Market(selling_price_per_unit, demand)
    revenue = market.calculate_revenue()

    generate_report(production_cost, transport_cost, revenue) #Relatorio em CSV com os custos e as receitas
    visualize_data(production_cost, transport_cost, revenue) #Cria um grafico de barras para analise visual

if __name__ == "__main__":
    main()
