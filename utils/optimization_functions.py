def thrust_objective(particle, data):
    # İtki amaç fonksiyonunu hesapla
    fan_diameter = particle[0]
    compressor_diameter = particle[1]
    combustion_chamber_volume = particle[2]
    turbine_diameter = particle[3]

    # İtki hesaplama formülü (örnek)
    thrust = fan_diameter * 100 + compressor_diameter * 50 + combustion_chamber_volume * 1000 + turbine_diameter * 75

    return -thrust  # Maximize etmek için negatifini döndür

def sfc_objective(particle, data):
    # Özgül yakıt tüketimi amaç fonksiyonunu hesapla
    fan_diameter = particle[0]
    compressor_diameter = particle[1]
    combustion_chamber_volume = particle[2]
    turbine_diameter = particle[3]

    # Özgül yakıt tüketimi hesaplama formülü (örnek)
    sfc = (fan_diameter * 0.1 + compressor_diameter * 0.05 + combustion_chamber_volume * 0.2 + turbine_diameter * 0.08) / 1000

    return sfc

def weight_objective(particle, data):
    # Ağırlık amaç fonksiyonunu hesapla
    fan_diameter = particle[0]
    compressor_diameter = particle[1]
    combustion_chamber_volume = particle[2]
    turbine_diameter = particle[3]

    # Ağırlık hesaplama formülü (örnek)
    weight = fan_diameter * 50 + compressor_diameter * 30 + combustion_chamber_volume * 100 + turbine_diameter * 40

    return weight

def cost_objective(particle, data):
    # Maliyet amaç fonksiyonunu hesapla
    fan_diameter = particle[0]
    compressor_diameter = particle[1]
    combustion_chamber_volume = particle[2]
    turbine_diameter = particle[3]

    # Maliyet hesaplama formülü (örnek)
    cost = fan_diameter * 1000 + compressor_diameter * 750 + combustion_chamber_volume * 2000 + turbine_diameter * 1200

    return cost

def evaluate_constraints(particle, data):
    # Kısıtlamaları değerlendir
    fan_diameter = particle[0]
    compressor_diameter = particle[1]
    combustion_chamber_volume = particle[2]
    turbine_diameter = particle[3]

    # Örnek kısıtlamalar
    constraints = [
        fan_diameter - 200,                    # fan_diameter <= 200
        50 - compressor_diameter,              # compressor_diameter >= 50
        combustion_chamber_volume - 0.5,       # combustion_chamber_volume <= 0.5
        50 - turbine_diameter                  # turbine_diameter >= 50
    ]

    return constraints