import pytest
from project import ResinProduction, Logistics, Market

def test_resin_production():
    production = ResinProduction(5000, 3000, 2000)
    assert production.calculate_total_cost() == 10000, "Production cost calculation is incorrect"

def test_logistics():
    logistics = Logistics(150, 2)
    assert logistics.calculate_transport_cost() == 300, "Transport cost calculation is incorrect"

def test_market():
    market = Market(50, 400)
    assert market.calculate_revenue() == 20000, "Revenue calculation is incorrect"

if __name__ == "__main__":
    pytest.main()
