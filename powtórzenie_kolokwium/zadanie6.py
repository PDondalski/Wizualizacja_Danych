def rosnace():
	with open('plik.txt', 'r+') as f:
		n = [int(i) for i in f.read().split()]
		f.seek(0)
		f.write('\n'.join([str(i) for i in sorted(n)]))

rosnace()