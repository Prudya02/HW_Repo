import pandas as pd
import json

EXCHANGE_RATES = {'USD': 1.0, 'EUR': 1.1, 'GBP': 1.3}



with open('AllPricesToday.json', 'r') as f:
    data = json.load(f)


encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
for encoding in encodings:
    try:
        with open('AllIdentifiers.json', 'r', encoding=encoding) as f:
            data2 = json.load(f)
        print(f"Успешно прочитано с кодировкой: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Ошибка с кодировкой: {encoding}")
    except Exception as e:
        print(f"Другая ошибка с {encoding}: {e}")


# Создаем список только с ID и именами
id_to_name = {}
for card_id, card_info in data2['data'].items():
    name = card_info.get('name')
    frameVersion = card_info.get('frameVersion')
    if name:  # Только если есть имя
        id_to_name[card_id] = {
            'name': name,
            'frame_version': frameVersion
        }
results = []
for card_id, card_data in data['data'].items():
    normal_prices = []
    foil_prices = []
    if 'paper' in card_data:
        for vendor, vendor_data in card_data['paper'].items():  # Исправлено: .items() вместо .values()
            if vendor.lower() == 'cardmarket':
                continue
            currency = vendor_data.get('currency', 'USD')
            rate = EXCHANGE_RATES.get(currency.upper(), 1.0)
            retail = vendor_data.get('retail', {})

            if 'normal' in retail and retail['normal']:
                price = list(retail['normal'].values())[0] * rate
                normal_prices.append(price)

            if 'foil' in retail and retail['foil']:
                price = list(retail['foil'].values())[0] * rate
                foil_prices.append(price)

    # Вычисляем средние значения ТОЛЬКО если есть цены
    avg_normal = sum(normal_prices) / len(normal_prices) if normal_prices else None
    avg_foil = sum(foil_prices) / len(foil_prices) if foil_prices else None
    # Добавляем в результаты только если есть foil цены
    if len(foil_prices) > 0 and len(normal_prices) > 0:
        results.append({
            'card_id': card_id,
            'normal_price': avg_normal,
            'foil_price': avg_foil,
            'foil_ratio': avg_foil/avg_normal,
            'name': id_to_name.get(card_id, ['name'])
        })

df = pd.DataFrame(results)
foil_df = df.sort_values('foil_ratio', ascending=False).head(500)
normal_df = df.sort_values('foil_ratio', ascending=True).head(500)
with pd.ExcelWriter('top500foil.xlsx', engine='openpyxl') as writer:
    foil_df.to_excel(writer, sheet_name='Top 100 Foil', index=False)
with pd.ExcelWriter('top500norm.xlsx', engine='openpyxl') as writer:
    normal_df.to_excel(writer, sheet_name='Top 100 Normal', index=False)

#normal_df.to_csv('top100norm_20.08.2025.csv', index=False, float_format='%.2f')
#print(foil_df)