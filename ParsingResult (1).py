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
                    condition=dictonary_list[index].get("rule_name")
                    if(condition=="ServeScaledImages"):
                        trace1=dictonary_list[index].get("url_blocks")
                        #print(trace1)
                        ind=0
                        while ind <len(trace1):
                            for key in trace1[ind]:
                                header=trace1[ind].get("header")
                                urls=trace1[ind].get("urls")
                                print(header)
                                #print(urls)
                                ind3=0
                                while ind3 < len(urls):
                                    for key3 in urls[ind3]:
                                        result=urls[ind3].get("result")
                                        #print(result)
                                        ind3=ind3+1
                                        #break
                                        for key4 in result.items():
                                            argu=result.get("args")
                                            print(argu)
                                            ind5=0
                                            while ind5 < len(argu):
                                                for key5 in argu[ind5]:
                                                    valuee=argu[ind5].get("localized_value")
                                                    key=argu[ind5].get("placeholder_key")
                                                    print(valuee)
                                                    break
                                                
                                            
                                            
                                     
                                    
                                ind=ind+1
                                for key1 in header.items():
                                    args=header.get("args")
                                    forma=header.get("format")
                                    print(args)
                                   # print(forma)
                                    ind1=0
                                    while ind1 < len(args):
                                        for key2 in args[ind1]:
                                            t1=args[ind1].get("type")
                                            if (t1=="BYTES"):
                                                L1=args[ind1].get("localized_value")
                                                print(L1)
                                            elif (t1=="PERCENTAGE"):
                                                 L2=args[ind1].get("localized_value")
                                                 print(L2)
                                                
                                            #else:
                                               # print(not found)
                                            ind1=ind1+1
                                            
                                            #print(f)
                                            break
                                    break
                                break
                       
                               # for key in condition1.items():
                                  #  args=condition1.get("args")
                                  #  print(args)'''
                                    
                             
                                
                                
                  
                    index=index+1
                    
                    
                    break
            break
        break


       
                    
                    
                    
         
            
                  
                   
