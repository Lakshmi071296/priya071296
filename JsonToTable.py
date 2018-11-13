#code to print a json file as table - Pragatheeswaran R

from prettytable import PrettyTable
import json


with open("C:/Users/css117728/Downloads/result.json", "r") as read_file:
    data = json.load(read_file)
    table = PrettyTable()
    table.field_names = ["Rule Name(Localized)", "Rule impact", "Priority", "color"]
    for key in data.items():
        trace_1=data.get("results")
        for key in trace_1.items():
            dictonary_list=trace_1.get("rule_results")
            index = 0
            while index < len(dictonary_list):
                for key in dictonary_list[index]:
                    impact=dictonary_list[index].get("rule_impact")
                    name=dictonary_list[index].get("rule_name")
                    index += 1
                    if impact < 1:
                        priority="Low"
                        color="Green"
                    else:
                        priority="Normal"
                        color="Amber"
                    result=table.add_row([name, impact, priority, color])        
                break
            break
        
        print(table)


