class UberDeliveryTrip:
    def __init__(self, distance, time, total_fare, gas_price_per_liter, fuel_consumption):
        self.distance = distance  # em quilômetros
        self.time = time  # em minutos
        self.total_fare = total_fare  # em reais
        self.gas_price_per_liter = gas_price_per_liter  # em reais
        self.fuel_consumption = fuel_consumption  # em quilômetros por litro
        self.fuel_cost_per_km = 0  # custo estimado do combustível por quilômetro
        self.maintenance_cost_per_km = 0.05  # custo estimado da manutenção do veículo por quilômetro

    def calculate_fuel_cost(self):
        self.fuel_cost_per_km = (self.distance / self.fuel_consumption) * self.gas_price_per_liter
        return self.fuel_cost_per_km

    def calculate_maintenance_cost(self):
        return self.distance * self.maintenance_cost_per_km

    def calculate_profit(self):
        fuel_cost = self.calculate_fuel_cost()
        maintenance_cost = self.calculate_maintenance_cost()
        profit = self.total_fare - fuel_cost - maintenance_cost
        return profit
