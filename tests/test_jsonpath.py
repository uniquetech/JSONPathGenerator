from jsonpathgenerator import jsonpath
import json
import os


def test_jsonpath():
    script_dir = os.path.dirname(__file__)
    source_file = "sample_json.json"
    target_file1 = "bracket-output.txt"
    target_file2 = "dot-out.txt"

    js = jsonpath()

    with open(os.path.join(script_dir, source_file), 'r') as Json_file:
        for line in Json_file:
            json_line = json.loads(line)
            json_path_list1=js.get_json_path(json_line,notation='bracket')
            json_path_list2=js.get_json_path(json_line,notation='dot')

    with open(os.path.join(script_dir, target_file1), 'r') as file1:
        for line in file1:
            target_list1=line

    with open(os.path.join(script_dir, target_file2), 'r') as file2:
        for line in file2:
            target_list2=line

    assert str(json_path_list1) == target_list1

    assert str(json_path_list2) == target_list2
    
