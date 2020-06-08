class jsonpath:

    def __init__(self):
        pass

    def get_nested_dict(self,json_dict) -> dict:

        if isinstance(json_dict, dict): 
            return {key: self.get_nested_dict(children) for key, children in json_dict.items()}
        elif isinstance(json_dict, list):
            return {id: self.get_nested_dict(children) for id, children in enumerate(json_dict, start=0)}
        else: 
            return json_dict
    
    def format_notation(self,key,notation):

        if isinstance(key,int):
            keystr = "["+str(key)+"]"
        elif notation == "dot" :
            keystr = "."+str(key)
        else:
            keystr = "['"+str(key)+"']"
        return keystr
            
    def generate_json_path(self,json_line,notation,fields="",keys="$"):
        json_dict=self.get_nested_dict(json_line)
        if isinstance(json_dict, dict): 
            for key, value in json_dict.items():
                keystr=self.format_notation(key,notation)
                yield from self.generate_json_path(value,notation, keys+keystr, keys+keystr)           
        else:
            yield fields

    def get_json_path(self,json_line,**kwargs):
        json_path_list=[]
        notation = kwargs['notation']
        json_paths=self.generate_json_path(json_line,notation)
        json_path_list = [json_path for json_path in json_paths]
        return json_path_list
    