class Employee(object):
      def __init__(self,id,name,email):
          self.id = id
          self.name = name
          self.email = email
      def get_id(self):
          print(self.id)
      def get_name(self):
          print (self.name)
      def get_email(self):
          print (self.email)
class PM (Employee):
       def __init__(self,id,name,email):
           super(PM,self).__init__(id,name,email)
       def pm_task(self):
           print ("PM Task Started")
class Dev(Employee):
    def __init__(self,id,name,email):
         super(Dev,self).__init__(id,name,email)
    def dev_task(self):
        print ("Dev Task Started")
class QA(Employee):
    def __init__(self,id,name,email):
        super(QA,self).__init__(id,name,email)
    def qa_task(self):
        print ("Qa Task Started")
pm = PM(101,"Anand","Anand@gmail.com")
pm.get_id()
pm.get_name()
pm.get_email()
dev = Dev(102,"Richa","Richa@gmail.com")
dev.get_id()
dev.get_name()
dev.get_email()
qa = QA(103,"Poonam","Poonam@gmail.com")
qa.get_id()
qa.get_name()
qa.get_email()