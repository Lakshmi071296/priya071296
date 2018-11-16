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
                        print(condition)
                        trace1=dictonary_list[index].get("url_blocks")
                        ind=0
                        while ind <len(trace1):
                            for key in trace1[ind]:
                                header=trace1[ind].get("header")
                                urls=trace1[ind].get("urls")
                                ind3=0
                                resultdic={}
                                while ind3 < len(urls):
                                    for key3 in urls[ind3]:
                                        result=urls[ind3].get("result")
                                        ind3=ind3+1
                                        for key4 in result.items():
                                            argu=result.get("args")
                                            forma=result.get("format")
                                           
                                            ind5=0
                                            while ind5 < len(argu):
                                                for key5 in argu[ind5]:
                                                    valuee=argu[ind5].get("localized_value")
                                                    key=argu[ind5].get("placeholder_key")
                                                    resultdic[key]=valuee
                                                    t=0
                                                    ind5=ind5+1
                                                    
                                                    
                                                
                                                    break
                                          
                                           
                                                                                   
                                            r2=forma.replace("{{URL}}",resultdic['URL'])
                                            
                                            r3=r2.replace("{{PERCENTAGE}}",resultdic['PERCENTAGE'])
                                            
                                            r4=r3.replace("{{ORIGINAL_HEIGHT}}",resultdic['ORIGINAL_HEIGHT'])
                                           
                                            r5=r4.replace("{{ORIGINAL_WIDTH}}",resultdic['ORIGINAL_WIDTH'])
                                            
                                            r6=r5.replace("{{FINAL_HEIGHT}}",resultdic['FINAL_HEIGHT'])
                                            
                                            r7=r6.replace("{{FINAL_WIDTH}}",resultdic['FINAL_WIDTH'])
                                            
                                            r8=r7.replace("{{SIZE_IN_BYTES}}",resultdic['SIZE_IN_BYTES'])
                                            print(r8)
                                            
                                           
                                                    
 
                                            
                                            break
                                                
                                            
                                            
                                     
                                    
                                ind=ind+1
                                headerdic={}
                                for key1 in header.items():
                                    args=header.get("args")
                                    forma=header.get("format")
                                    
                                    
                                    ind1=0
                                    while ind1 < len(args):
                                        for key2 in args[ind1]:
                                            t1=args[ind1].get("localized_value")
                                            t2=args[ind1].get("placeholder_key")
                                            
                                            headerdic[t2]=t1
                                           
                                                
                                            
                                            ind1=ind1+1
                                                                                     
                                                                                 
                                            
                                            break

                                    j=headerdic['SIZE_IN_BYTES']
                                    k=headerdic['PERCENTAGE']
                                  
                                    h1=forma.replace("{{SIZE_IN_BYTES}}",j)
                                  
                                    h2=h1.replace("{{PERCENTAGE}}",k)
                                    print(h2)
                                    break
                                break
                       
                                
                                
                  
                    index=index+1
                    
                    
                    break
            break
        break
