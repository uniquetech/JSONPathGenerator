# JSONPathGenerator
Python project to generate Json path notations





# USAGE

   js = JSONPathGenerator()

   js.get_json_path(<json-line>,notation='<str>')

   notation = "dot"

   notation = "bracket"


# Usage Examples

def main():

    js=jsonpath()

    with open('sample_json.json','r') as file:
        json_line=json.load(file)
        json_path_list=js.get_json_path(json_line,notation="bracket")
        print(json_path_list)

i

