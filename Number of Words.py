para=input()
striped_para=para.strip("!@#$%^&*()-+=,./;'\[]<>?:|{\"}")
print(len(striped_para.split()))