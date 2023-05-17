import json

with open(r"C:\Users\akhila.vk\Downloads\sample_data.json", "r") as file:
    content = json.load(file)

outer_dict = {}
parameter_content = content["parametersList"]
for one in parameter_content:
    inner_dict = {}
    key = one["parameterName"]
    inner_dict["min"] = one["min"]
    inner_dict["max"] = one["max"]
    inner_dict["avg"] = one["avg"]
    outer_dict[key] = inner_dict

print(outer_dict)
with open(r"C:\Users\akhila.vk\Downloads\sample_data_output.json", "w") as file:
    json.dump(outer_dict, file)
