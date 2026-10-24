graph = {
    'Germany': ['Poland', 'Czech', 'Austria', 'Switzerland'],
    'Poland': ['Germany', 'Czech', 'Slovakia'],
    'Czech': ['Germany', 'Poland', 'Austria', 'Slovakia'],
    'Slovakia': ['Poland', 'Czech', 'Austria', 'Hungary'],
    'Austria': ['Germany', 'Czech', 'Slovakia', 'Hungary', 'Slovenia', 'Italy', 'Switzerland'],
    'Switzerland': ['Germany', 'Austria', 'Italy', 'Slovenia'],
    'Italy': ['Switzerland', 'Austria', 'Slovenia'],
    'Slovenia': ['Austria', 'Italy', 'Hungary'],
    'Hungary': ['Austria', 'Slovakia', 'Slovenia']
}

colors = ['Red', 'Green', 'Blue']
result = {}

for country in graph:
    used = [result[n] for n in graph[country] if n in result]

    for color in colors:
        if color not in used:
            result[country] = color
            break

for country, color in result.items():
    print(country, ":", color)
