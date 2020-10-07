from covid import Covid

# inicializar
covid = Covid()

# Print dos dados
print('Mundo')
print("Número de casos ativos:", covid.get_total_active_cases())
print("Número de casos recuperados:", covid.get_total_recovered())
print("Nímero de mortes:", covid.get_total_deaths())

# Dados de Países
print('País')
casos = covid.get_status_by_country_name("brazil")

# print dados dos países
for x in casos:
    print(x, ":", casos[x])
