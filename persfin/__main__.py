import modules.analyze as analyze
import modules.classify as classify
import tomli
import sys
from exceptions import Unexpected_Input

commands = ["classify","analyze","help"]
options = {"classify":["--analyze","--add_to_master","--complete_pending"],"analyze":[]}
execution_path = {"classify":classify.main, "analyze":analyze.main}

def main():
    execute()
    pass

def get_inputs():
    inputs = sys.argv
    parsed_inputs = {}
    if len(inputs) < 2 or len(inputs) > 4:
        raise Unexpected_Input
    if inputs[1] not in commands:
        raise Unexpected_Input
    match inputs[1]:
        case "classify":
            if len(inputs) < 3:
                raise Unexpected_Input
            if len(inputs) == 4:
                if inputs[3] not in options["classify"]:
                    raise Unexpected_Input
                print("Options processing is not active yet")
                #parsed_inputs["options"] = inputs[3]
                #parsed_inputs["path"] = inputs[2]
                #parsed_inputs["command"] = inputs[1]
            else:
                parsed_inputs["path"] = inputs[2]
                parsed_inputs["command"] = inputs[1]
        case "analyze":
            if len(inputs) != 3:
                raise Unexpected_Input
            else:
                parsed_inputs["command"] = inputs[1]
                parsed_inputs["filter"] = inputs[2]
        case "collect":
            if len(inputs) > 2:
                raise Unexpected_Input
            else:
                parsed_inputs["command"] = inputs[1]
    return(parsed_inputs)

def execute():
    configurations = getconfig("config.toml")
    canonical_schema = getconfig(configurations["paths"]["schema_mapper"])
    execute_params = get_inputs()
    execution_path[execute_params["command"]](execute_params, configurations, canonical_schema)

def getconfig(path):
    with open(path, mode="rb") as tommlfile:
        config = tomli.load(tommlfile)
    return config
main()