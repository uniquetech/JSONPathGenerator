# JSONPathGenerator
Python project to generate Json path notations





# USAGE

   js = JSONPathGenerator()

   js.get_json_path(<json-line>,notation='<str>')

   notation = "dot"

   notation = "bracket"


# Usage Examples

    js = JSONPathGenerator()

    with open('sample_json.json', 'r') as Json_file:
        for line in Json_file:
            json_line=json.loads(line)
            json_path_list=js.get_json_path(json_line,notation='dot')
            print(json_path_list)


