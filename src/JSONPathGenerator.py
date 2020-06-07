import json

class JSONPathGenerator:

    def __init__(self):
        self.schema_string=""

    def get_nested_dict(self,json_dict) -> dict:

        if isinstance(json_dict, dict):  # already have keys, just recurse
            return {key: self.get_nested_dict(children) for key, children in json_dict.items()}
        elif isinstance(json_dict, list):  # make keys from indices
            return {idx: self.get_nested_dict(children) for idx, children in enumerate(json_dict, start=0)}
        else:  # leave node, no recursion
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
        if isinstance(json_dict, dict):  # build stack of keys
            for key, value in json_dict.items():
                keystr=self.format_notation(key,notation)
                yield from self.generate_json_path(value,notation, keys+keystr, keys+keystr)           
        else:  # print complete stack, discarding leaf data in json_dict
            yield fields

    def get_json_path(self,json_line,**kwargs):
        notation = kwargs['notation']
        J=self.generate_json_path(json_line,notation)
        for i in J:
            print(i)


def main():

    js = JSONPathGenerator()

    with open('sample_json.json', 'r') as Json_file:
        for line in Json_file:
            json_line=json.loads(line)
            json_path_list=js.get_json_path(json_line,notation='avs')
            print(json_path_list)



if __name__ == '__main__':
    main()