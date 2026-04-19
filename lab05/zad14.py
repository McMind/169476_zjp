import re
info = "PIOTR   Wiśniewski(ur.2000)"
step1 = re.sub(r'\(.*?\)', '', info)
step2 = re.sub(r'\s+', ' ', step1)
final_result = step2.strip().title()

if __name__ == '__main__':
    print(final_result)