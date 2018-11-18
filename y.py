import json

dic={}
with open('result.json') as data_file:
    data = json.load(data_file)
    for x,y in data.items():
        for key in data.items():
            results=data.get("results")
            
            
        for key1 in results.items():
            rule_results=results.get("rule_results")
            #print(rule_results)
            index = 0
            while index < len(rule_results):
                for key in rule_results[index]:
                    rule_name=rule_results[index].get("rule_name")
                    #print("rule_name "+rule_name)

                    url_blocks=rule_results[index].get("url_blocks")
                    #print("url_blocks "+url_blocks)
                    #print(len(url_blocks))
                    index=index+1
                    if url_blocks is None:
                        continue
                    ind1=0
                    #print(rule_name)
                    #print(len(url_blocks))
                    while ind1 < len(url_blocks):
                        
                        for key in url_blocks[ind1]:
                            if key=="header":
                                header=url_blocks[ind1].get("header")
                                
                                
                                #print(header)
                                ind1=ind1+1
                                headerdic={}
                                #print("1")
                                
                                for key2 in header.items():
                                    args=header.get("args")
                                    forma=header.get("format")
                                    #print(forma)
                                    #print("2")
                                    
                                    if args is None:
                                        continue
                                    #print(rule_name)
                                    #print(args)
                                    ind2=0
                                    

                                       
                                    
                                    
                                    while ind2 < len(args):
                                        
                                        for key3 in args[ind2]:
                                            print(len(args))
                                            
                                            
                                           # print(args)
                                            t1=args[ind2].get("localized_value")
                                            print(t1)
                                           
                                            t2=args[ind2].get("placeholder_key")
                                            print(t2)
                                         
                                            headerdic[t2]=t1
                                            ind2=ind2+1
                                           
                                            print(headerdic)
                                                   
                                    
                                            #print(rule_name)
                                            #print(forma)
                                            
                                            #print(headerdic)
                                            break

                                        break    
                                                                        
                                    break
                            
                     

                                            
                                    
                                    
                    
                            
                        
                    
                    
                    
                    
                    index=index+1
                    #print(rule_name)
                    break
            break
        break


