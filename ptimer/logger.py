import csv

def add_new(contact):
    try:
        with open('book.txt','a',encoding='utf-8') as book:
            book.write(f'\n{contact}')
        with open('book.csv','a') as f:
            writer=csv.writer(f,delimiter=';')
            writer.writerows([contact.split(' || ')]) 
    except FileExistsError:
        with open('book.txt','w',encoding='utf-8') as book:
            book.write(f'{contact}')
        with open('book.csv','w') as f:
            writer=csv.writer(f,delimiter=';')
            writer.writerows([contact.split(' || ')])  

def get_base():
    with open('book.txt','r',encoding='utf-8') as book:
        return book.read()   

def update_base(new_info):
    new_info_csv=[i.split(' || ') for i in new_info]
    with open('book.csv','w',encoding='utf-8') as f:
        writer=csv.writer(f,delimiter=';')
        writer.writerows(new_info_csv)
    with open('book.txt','w',encoding='utf-8') as book:
        book.write('\n'.join(new_info))                      