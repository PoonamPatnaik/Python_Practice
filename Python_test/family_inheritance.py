class father:
      def __init__(self,money=1000):
          self.money = money

      def money_trans(self, debit):
          self.debit = debit
          if (self.money) < self.debit:
              print("-1")
          else:
              print("Gave money successfully")
              return self.money - self.debit

class child:
      def __init__(self,money=0):
          self.money = money

      def get_money(self,b_money):
          self.b_money = b_money
          father().money_trans(self.b_money)

class mother:
      def __init__(self, money=0):
          self.money = money
      def ask_money(self,ask_money):
          self.ask_money = ask_money
          child().get_money(self.ask_money)

obj_m = mother()
obj_m.ask_money(50)
