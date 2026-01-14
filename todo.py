todo_record:list =[]
task_id = 0
class ToDoApp():
    def __init__(self, *args, **kwargs):
        self.todo_record = todo_record
        self.task_id = task_id

    def is_empty(self):
        if not self.todo_record:
            print('No Record found')
            return True
        return False
        
    def create(self):
        todo:dict = {}
        print('\n------ Add Task ------')
        
        self.task_id += 1
        id = self.task_id
        title = input('Enter Title: ')
        description = input('Enter Description: ')
        status = True
        todo = {'id':id, 'title':title,'description':description,'status':status}
        self.todo_record.append(todo)
        
    def display_active(self):
        print('\n------ Display Active Task ------')
        if self.is_empty(): return
        count=False
        for task in self.todo_record:
            if task.get('status'):
                count=True
                print(f'ID: {task.get('id')}')
                print(f'Title: {task.get('title')}')
                print(f'Description: {task.get('description')}\n')
            if not count:
                print('All tasks are Inactive')
        
    def display_inactive(self):
        print('\n------ Display Inactive Task ------')
        if self.is_empty(): return  
        count=False
        for task in self.todo_record:
            if not task.get('status'):
                count=True
                print(f'ID: {task.get('id')}')
                print(f'Title: {task.get('title')}')
                print(f'Description: {task.get('description')}\n')
        if not count:
                print('All tasks are Active')
                
    def update_status(self):
        print('\n------ Update Status ------')
        if self.is_empty(): return
        try:
            id:int = int(input('Enter Task Id: '))
        except:
            print('Enter Numeric Value...')
            return
        for task in self.todo_record:
            if task.get('id') == id:
                if task.get('status'):
                    task.update({'status':False})
                    print(f'Status Updated Successfully')
                    break
                else:
                    print(f'Status could not be Updated, because it is already Inactive')
                    break
        else:
            print('Task Id not found...')

todo_app = ToDoApp()
def menu():
    while True:
        print('\n===== TODO APP =====')
        print('1. Add Task')
        print('2. Display Active Task')
        print('3. Display Inactive Task')
        print('4. Update Task Status')
        print('5. Exit')
        
        choice = input('Enter your choice: ')
        if choice == '1': todo_app.create()
        elif choice == '2': todo_app.display_active()
        elif choice == '3': todo_app.display_inactive()
        elif choice == '4': todo_app.update_status()
        elif choice == '5':
            print('...Thank you for using...')
            exit()
        else:
            print('Invalid Choice....')

if __name__ == "__main__":
    menu()
