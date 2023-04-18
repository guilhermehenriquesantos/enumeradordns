import sys
import dns.resolver


resolver = dns.resolver.Resolver()

try:
	alvo = sys.argv[1]
	arquivo_subdominios = sys.argv[2]
except:
	print('Entre com -> python3 {enumeradordns.py} {dominio} {arquivo_subdominios.txt}')
	sys.exit()

try:
	with open(arquivo_subdominios, 'r') as arquivo:
		subdominios = arquivo.read().splitlines()
except:
	print('Arquivo das worlists não encontrado.')
	sys.exit()

for subdominio in subdominios:
	try:
		sub_alvo = '{}.{}'.format(subdominio, alvo)
		resultados = resolver.resolve(sub_alvo, 'A')

		for resultado in resultados:
			print('{} -> {}'.format(sub_alvo, resultado))
	except Exception as error:
		print('Subdomínio não existe')
