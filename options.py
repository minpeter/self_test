import requests

URL = 'https://senhcs.eduro.go.kr/v2/validatePassword'

response = requests.options(URL)
print('CODE:')
print(response.status_code)
print(response.text)

data = {"password":"fo4+ToHKFKIjyqbdMEUjZSI+C+JrNReHfyWUFzg9/LgE3b3uyoOD4Ab+LUefOZx3ZlTNF45gKrneAL024uBz6AhDpXABpoX3deVgDfKcTjhkpV81SCF5ubnWFRL1u/MD2baXkq+HYUff+nbgOd60UX8EWxwlFEy7StXTDmoPFBEYQFTq2gdibLaQ/M2gKGw4QBklLdr7LF8jWloVd8XWd2mRbe50fV+C/qjE2LtXWtD0kCQdxYku0YpHFrMn6U7MExHghPyoteASP2M8K7tPei5k1cFfjzoKf95kOro8jqMmtBFHt713pAi/B3y8lD4JL2I71kxz9F/vHb3Qtv7TlQ==","deviceUuid":""}

headers = {
"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlhdCI6MTYxODUyOTE4MDIyNX0.eyJubyI6IjIwMjEwMDAwNzYiLCJzZWNyZXRLZXkiOiJhUkhoIiwib3JnIjoiQjEwMDAwMDY2MiIsImV4cCI6MTY1MDA2NTE4MCwicm4iOiJudWxsIiwiaWF0IjoxNjE4NTI5MTgwMjI1fQ.iItfjyvUTsVUVYI89cMmbUYfl3HAHAaiRz9m0FhTAic"
}
cookies = {
    
}
response = requests.post(URL, data=data, headers=headers, verify=False)
print('CODE:')
print(response.status_code)
print(response.text)