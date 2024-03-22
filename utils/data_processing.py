import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def preprocess_data(engine_data, material_properties):
    # Tasarım değişkenlerinin alt ve üst sınırlarını belirle
    design_variables_bounds = {
        'fan_diameter': (100, 200),
        'compressor_diameter': (50, 100),
        'combustion_chamber_volume': (0.1, 0.5),
        'turbine_diameter': (50, 100)
    }

    # Tasarım değişkenleri ve sınırlarını bir sözlükte birleştir
    design_variables = {
        'names': list(engine_data['design_variables'].keys()),
        'bounds': [design_variables_bounds[var] for var in engine_data['design_variables'].keys()]
    }

    # İşlenmiş verileri bir sözlükte topla
    processed_data = {
        'engine_data': engine_data,
        'material_properties': material_properties,
        'design_variables': design_variables
    }

    return processed_data