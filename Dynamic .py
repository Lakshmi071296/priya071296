import json

dic={}
with open('newresult.json') as data_file:
    data = json.load(data_file)
    for x,y in data.items():
        for key in data.items():
            results=data.get("results")
            #print(results)
            
        for key1 in results.items():
            rule_results=results.get("rule_results")
            print(rule_results)
            index = 0
            while index < len(rule_results):
                for key in rule_results[index]:
                    rule_name=rule_results[index].get("rule_name")
                    print(rule_name)
                    url_blocks=rule_results[index].get("url_blocks")
                    print(url_blocks)
                    ind=0
                    while ind < len(url_blocks):
                        for key in url_blocks[ind]:
                            header=rule_results[ind].get("header")
                            print(header)
                            ind=ind+1
                            
                        
                    
                    
                    
                    
                    index=index+1
                    #print(rule_name)
                    break
            break
        break





            
        
        
    


