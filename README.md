# JSONPathGenerator
  Python project to generate Json path in notations dot or bracket.

  funtion to convert a nested json to nested dictionary enumerating the lists to child dictionaries

# INSTALLATION
      
   pip install jsonpathgenerator

# USAGE

   from jsonpathgenerator import jsonpath
   
   js = jsonpath()

   js.get_json_path(json-line,notation='dot')

   notation = "dot"

   notation = "bracket"


# Usage Examples


    js = jsonpath()

    with open('sample_json.json','r') as file:
        json_line=json.loads(file)
        json_path_list=js.get_json_path(json_line,notation="bracket")
        print(json_path_list)





