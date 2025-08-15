import re

def count_unsatisfied_checks(password):
    checks_failed = 0
    
    if not (6 <= len(password) <= 22):
        checks_failed += 1
    
    if not any(char.isupper() for char in password):
        checks_failed += 1
    
    if not any(char.islower() for char in password):
        checks_failed += 1
    if not any(char.isdigit() for char in password):   
        checks_failed += 1.
    
    special_chars = "@!&^%\"#"
    if sum(1 for char in password if char in special_chars) < 2:
        checks_failed += 1
    
    if any(password[i] == password[i+1] for i in range(len(password)-1)):
        checks_failed += 1 
    
    return checks_failed 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
password = input().strip()
print(count_unsatisfied_checks(password))
