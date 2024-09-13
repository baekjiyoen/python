import json
with open('ex/json상품.json', 'r', encoding='utf-8') as a :
    obj = json.load(a)
    print(obj['p_name'])
    print(obj['price'])
    print(obj['sp'])
    
    for o in obj['sp'] : 
        print(o)
   
    