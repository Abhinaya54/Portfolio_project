import random
uppercase_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case=uppercase_letter.lower()
digits="0123456789"
symbols="(){}[]./;''/\/!@#$%^&*_-+=:"

upper,lower,nums,syms=True,True,True,True
all=""
if upper:
    all=uppercase_letter
if lower:
    all=lower_case
if nums:
    all=digits
if syms:
    all=symbols


length=20
amount=10

for x in range(amount):
    Password="".join(random.sample(all,length))
    print(Password)