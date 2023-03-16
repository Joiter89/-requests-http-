import requests
def smartest_superhero(superheroes_list):
  url = 'https://akabab.github.io/superhero-api/api/all.json'
  superheroes_list = ['Hulk', 'Captain America', 'Thanos']
  responce = requests.get(url)
  superheroes = {}
  for i in responce.json():
    if i['name'] in superheroes_list:
      superheroes[i['name']] = i['powerstats']['intelligence']
  sorted_superheroes = sorted(superheroes.items(), key = lambda x: x[1], reverse=True)
  return print('Самый умный супергерой', sorted_superheroes[0][0], 'с интеллектом', sorted_superheroes[0][1], '!')

if __name__ == '__main__':
  smartest_superhero(['Hulk', 'Captain America', 'Thanos'])