data = open('./iowa-liquor-sample.csv')

numScotch = 0

for line in data:
	if 'single malt scotch' in line.lower():
		numScotch += 1

print numScotch
