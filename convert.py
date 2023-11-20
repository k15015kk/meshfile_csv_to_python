import csv
import json
import os

# 別途、inputフォルダでデータを用意してください

for year in range(2019, 2022):
    for month in range(1, 13):
        with open(f'input/{year}/{str(month).zfill(2)}/monthly_mdp_mesh1km.csv') as input_file:
            
			# csvファイルをDicで読み取ってリスト化
            reader = csv.DictReader(input_file)
            l = [row for row in reader]
			
			# ディレクトリを作成
            output_dir = f'output/{year}/{str(month).zfill(2)}'
            os.makedirs(output_dir, exist_ok=True)

			# JSONで出力
            with open(f'{output_dir}/monthly_mdp_mesh1km.json', 'w') as output_file:
                json.dump(l, output_file, indent=2)
