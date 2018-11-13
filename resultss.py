import json


with open('result.json') as data_file:
    data = json.load(data_file)
    for x,y in data.items():
        for key in data.items():
            trace_1=data.get("results")
        for key in trace_1.items():
            dictonary_list=trace_1.get("rule_results")
            index = 0
            while index < len(dictonary_list):
                for key in dictonary_list[index]:
                    trace1=dictonary_list[index].get("url_blocks")
                    print(trace1)
                    while index < len(trace1):
                        for key in trace1[index]:
                            urls=dictonary_list[index].get("urls")
                            print(urls)
                            while index< len(urls):
                                for key in urls[index]:
                                    args=dictonary_list[index].get("args")
                                    print(args)
                                    value=dictonary_list[index].get("localized_value")
                                    Key=dictonary_list[index].get("placeholder_key")
                                    d={}
                                    for i in value:
                                        d['key'] = value  
                                        print(d)
                            
                             
                                        

                    
