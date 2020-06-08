class jsonpath:

    def __init__(self):
        pass

    def get_nested_dict(self,json_line) -> dict:
        """
        input: json_line
        output: json_dict

        Converts nested json to nested dictionary enumerating the lists arrays to dictionaries.

        can be onits own class. can be used to convert nested json to dicts

        """

        if isinstance(json_line, dict): 
            return {key: self.get_nested_dict(children) for key, children in json_line.items()}
        elif isinstance(json_line, list):
            return {id: self.get_nested_dict(children) for id, children in enumerate(json_line, start=0)}
        else: 
            return json_line
    
    def format_notation(self,key,notation):

        """
        To format json keys to json path notation.

        A JSONPath expression specifies a path to an element (or a set of elements) in a JSON structure. Paths can use the dot notation:

        $.store.book[0].title

        or the bracket notation:

        $['store']['book'][0]['title']

        Filter expressions no implemented!

        """

        if isinstance(key,int):
            keystr = "["+str(key)+"]"
        elif notation == "dot" :
            keystr = "."+str(key)
        else:
            keystr = "['"+str(key)+"']"
        return keystr
            
    def generate_json_path(self,json_line,notation,fields="",keys="$"):
        
        """
        generator to form json keys recursivly from json dictionalry. 

        """

        json_dict=self.get_nested_dict(json_line)
        if isinstance(json_dict, dict): 
            for key, value in json_dict.items():
                keystr=self.format_notation(key,notation)
                yield from self.generate_json_path(value,notation, keys+keystr, keys+keystr)           
        else:
            yield fields

    def get_json_path(self,json_line,**kwargs):
        
        """
        function to return list of keys. takes dictionary variable notation="dot" or "bracket". defaults to bracket

        returned list can be used to parse a json document. fully formed list can be used for losless parsing of a json doc.

        """
        
        json_path_list=[]
        
        notation = kwargs['notation']

        json_paths=self.generate_json_path(json_line,notation)
        
        json_path_list = [json_path for json_path in json_paths]

        return json_path_list
    