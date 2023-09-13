import pandas as pd

# Загрузка данных из Excel файла
excel_file = 'file.xlsx'  # Укажите путь к вашему файлу Excel
df = pd.read_excel(excel_file)

fixed_template_base = '''{id},simple,,"{name}",1,0,visible,,"{content}",,,taxable,,1,,,0,0,,{d},{h},{v},1,,,{price20},"{category}",,,https://dev.gofropack.com/wp-content/uploads/2023/09/korobka34.jpg,,,,,,,,,0,"100:{price100},200:{price200},500:{price500},1000:{price1000}",fixed,20,,"Длина, мм",{d},1,1,"Ширина, мм",{h},1,1,"Высота, мм",{v},1,1,"Марка картона",{mark},1,1,"Тип картона",{type},1,1,Цвет,{color},1,1,"Размеры коробки",{d}x{h}x{v},0,1,default,20,table,fixed,20,5,2000,"{metaday}",field_64b622bf3a496,"{name}",field_63c3e58dae8bc,331,"{name}","{name}: Заказать по низкой цене от производителя Гофродом с доставкой по Москве и России","Картонная коробка {name} от производителя Гофродом. Идеальное решение для упаковки вашего товара. ✔Оптовые цены ✔Высокое качество материалов ✔Быстрая доставка по Москве и России. Заказывайте у нас: +7 (499) 288-55-69.",43,90,1,,3,,,,,,,,,,,,,,,,,,,,,,,,,,'''

# Создайте пустой список для хранения строк
output_lines = []

# Цикл для замены номера индекса
for index, row in df.iterrows():
    # Замена NaN на пустую строку
    row = row.fillna('')  # Заменяет все NaN на пустую строку
    fixed_template = fixed_template_base.format(id=2562 + index + 1,  # Используйте индекс + 1 вместо d=index
                                               name=row['name'],
                                               content=row['content'],
                                               d=row['d'],
                                               h=row['h'],
                                               v=row['v'],
                                               category=row['category'],
                                               price20=row['price20'],
                                               price100=row['price100'],  # Замените 100 на имя столбца, если это название столбца
                                               price200=row['price200'],  # Замените 200 на имя столбца, если это название столбца
                                               price500=row['price500'],  # Замените 500 на имя столбца, если это название столбца
                                               price1000=row['price1000'],  # Замените 1000 на имя столбца, если это название столбца
                                               metaday=row['metaday'],
                                               mark=row['mark'],
                                               type=row['type'],
                                               color=row['color'])


    output_lines.append(fixed_template)

# Экспорт шаблона в CSV файл
csv_file = 'output.csv'  # Укажите путь для сохранения CSV файла
with open(csv_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print(f'Данные успешно заменены в шаблоне и сохранены в {csv_file}')
