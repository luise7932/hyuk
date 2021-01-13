with open('test.txt','w') as f:
    f.write("Life is too short\nyou need java")
    
with open('test.txt','r') as f:
    data = f.read()

data = data.replace("java","python")

with open('test.txt','w') as f:
    f.write(data)