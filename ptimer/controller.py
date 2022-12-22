import logger
import model
import view

def run():
    while True:
        mode=view.choose_mode()
        if mode=='1':  
            contact=view.new_employee()
            logger.add_new(contact)
        elif mode=='2':
             contact=view.contact_to_s()
             base=logger.get_base()
             result=model.search_contact(base,contact)
             view.show_found(result)    
        elif mode=='3':
            employee=view.employee_to_s()
            base=logger.get_base()
            result=model.search_contact(base,employee)
            view.show_found(result)
            if 'не найден' not in result[0] and len(base.split('\n'))>1:
                result =model.search_contact(base,view.clarification())[0]
                new_employee=view.new_employee()
                upd=model.edit_employee(base,result,new_employee)
                logger.update_base(upd)
            elif 'не найден' not in result[0]:
                result=base.split('\n')[0]
                new_employee=view.new_employee()
                upd=model.edit_employee(base,result,new_employee)
                logger.update_base(upd)
        elif mode=='4':
             employee=view.employee_to_s()
             base=logger.get_base()
             result=model.search_contact(base,employee)
             view.show_found(result)
             if 'не найден' not in result[0] and len(base.split('\n'))>1:
                result =model.search_contact(base,view.clarification())[0]
                upd=model.delete_employee(base,result)
                logger.update_base(upd)
             elif 'не найден' not in result[0]:
                result=base.split('\n')[0]
                upd=model.delete_employee(base,result)
                logger.update_base(upd)   
        else:
            view.error()                 