import json
def GenJson():
    keys = ['first_name','last_name','age','sex']
    while True:
        data = input("Want to enter the details: [y/n]")
        if data.lower() != 'y':
            break;
        else:
            a = input("Enter first Name: ")
            b = input("Enter last Name: ")
            sex = input("Enter Gender: ")
            age = int(input("Enter age: "))
            values = [a, b, sex, age]
            with open('beats.json', 'a+') as f:
                data_dict = {k:v for k,v in zip(keys, values)}
                j_data = json.dumps(data_dict)
                f.write(j_data)

def hack():
    a = ['model', 'pk', 'fields']
    field_ref = ['first_name','last_name','age','sex']
    b = input("Enter Model Name: ")
    c = int(input("Enter pk value: "))
    d = input("Enter First Name: ")
    e = input("Enter last Name: ")
    f = int(input("Enter age: "))
    g = input("Enter Gender: ")
    h = [d,e,f,g]
    fie_dic = {k:v for k,v in zip(field_ref, h)}
    k = [b,c,fie_dic]
    main_dic = {k:v for k,v in zip(a, k)}
    return main_dic

def hack2():
    j_data = []
    c=1
    while True:
        Q = input("Want to enter the data[Y/N]: ")
        if Q.lower() != 'y':
            break
        else:
            a = ['model', 'pk', 'fields']
            field_ref = ['first_name','last_name','age','sex']
            b = input("Enter Model Name: ")
            d = input("Enter First Name: ")
            e = input("Enter last Name: ")
            f = int(input("Enter age: "))
            g = input("Enter Gender: ")
            h = [d,e,f,g]
            fie_dic = {k:v for k,v in zip(field_ref, h)}
            k = [b,c,fie_dic]
            main_dic = {k:v for k,v in zip(a, k)}
            c += 1
            j_data.append(main_dic)
    if main_dic:
    	with open('beat2.json', 'a+') as f:
    		f.write(json.dumps(j_data))
    else:
    	return "No data Entered"

if __name__ == '__main__':
	# GenJson()
	# print(hack())
	hack2()