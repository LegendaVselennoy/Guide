def search_contact(base,contact):
    base=base.split('\n')
    flag=True
    results=[]
    for i in base:
        if contact in i:
            flag=False
            results.append(i)
    if flag:
        results.append(f'Конткт |{contact}| не найден')
    return results  

def create_id(base):
    if len(base.split('/n'))==0:
        return 1
    else:
        return int(base.split('\n')[len(base.split('\n'))-1].split(' || ')[0])+1        

# def edit_employee(base,employee,new_employee):
#     base=base.split('\n')
#     base[base.index(employee)]=new_employee
#     return base 

def delete_employee(base,result):
    base=base.split('\n')
    base.remove(result)
    return base  

def edit_employee(base,employee,new_employee):
    base=base.split('\n')
    id=employee.split(' || ')[0]
    base[base.index(employee)]=id+' || '+new_employee
    return base                   