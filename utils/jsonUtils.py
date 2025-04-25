import json

def update_json(path:str, data:dict, indent:int, sort_by_id:bool):
        lista=[]
        lista.append(data)
        try:
            with open(path, 'r', encoding="utf-8") as file:
                json_data = json.loads(file.read())
                for item in json_data:
                    lista.append(item)
                    if sort_by_id:
                        lista.sort(key=lambda task: task['id'])
            with open(path, 'w', encoding="utf-8") as file:
                json.dump(lista, file, indent=indent)
        except:   
            with open(path, 'w', encoding="utf-8") as file:
                json.dump(lista, file, indent=indent)

def delete_data_json(path:str):
    lista = []
    with open(path, 'r') as file:
        json_data = json.load(file)
        for item in json_data:
            lista.append(item)
        for i in lista:
            json_data.pop(i)
        
    with open(path, 'w') as file:
        json.dump(json_data, file, indent=4)
                