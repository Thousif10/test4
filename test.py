class NegNumErr(Exception):
   def __init__(self, message="Negative number not allowed!"):
      self.message = message
      super().__init__(self.message)

class check_num(num):
   if num < 0:
      raise NegNumErr(f"Invalid input: {num} is negative")
   else:
      print(f"Valid input {num}")

try:
   check_num(-5)
except NegNumErr as e:
   print("Caught Exception:", e)