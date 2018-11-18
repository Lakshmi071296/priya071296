import json
with open('result.json') as data_file:
    data = json.load(data_file)
    for x,y in data.items():
        for key in data.items():
            results=data.get("results") 
        for key1 in results.items():
            rule_results=results.get("rule_results")
            index = 0
            while index < len(rule_results):
                for key in rule_results[index]:
                    rule_name=rule_results[index].get("rule_name")
                    url_blocks=rule_results[index].get("url_blocks")
                    index=index+1
                    if url_blocks is None:
                        continue
                    ind1=0
                    print(rule_name)
                    while ind1 < len(url_blocks):
                        for key in url_blocks[ind1]:
                            header=url_blocks[ind1].get("header")
                            for key5 in header.items():
                                args=header.get("args")
                                forma=header.get("format")
                                if args is None:
                                    print(forma)
                                    continue
                                headerdic={}
                                ind2=0
                                while ind2<len(args):
                                    for key3 in args[ind2]:
                                        t1=args[ind2].get("localized_value")
                                        t2=args[ind2].get("placeholder_key")
                                        headerdic[t2]=t1
                                        ind2=ind2+1
                                        break
                                print(headerdic)
                                print(forma)
                                    
                                    
                                break
                                
                            urls=url_blocks[ind1].get("urls")
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
                                        print(resultdic)
                                        print(forma)
                                        break     
                                    break
                                break
                            ind1=ind1+1
                            break
                    index=index+1
                    break
            break
        break


