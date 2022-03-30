'''
  JSON
  JavaScript Object Notation
  웹 환경에서 데이터를 주고 받는 가장 표준적인 방식
  키를 이용하여 원하는 데이터만 빠르게 추출 가능
  데이터가 쉽게 오염 되지 않음
  다른 포맷에 비에 용량이 조금 큰 편 => 늘 키를 저장해야되기 때문

  JSON ------loads()-----> dictionary load + string
  JSON <------dumps()----- dictionary 쏟아 부어라 dumps

'''

import json
import os
currentPath = os.getcwd()

src = currentPath +'\\basic\\netflix.json'

def create_dict(filename):
    with open(filename) as file:
        json_string = file.read()

        return json.loads(json_string)


def create_json(dictionary, filename):
    with open(filename, 'w') as file:

        json_string = json.dumps(dictionary)
        file.write(json_string)
        


netflix_dict = create_dict(src)
print(str(netflix_dict))

netflix_dict['Dark Knight'] = 39217
create_json(netflix_dict, src)
updated_dict = create_dict(src)
print('수정된 데이터: ' + str(updated_dict))

