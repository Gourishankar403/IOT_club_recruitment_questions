n=eval(input("Enter the no of lines: "))
senten_list=[]
for i in range(n):
    print(f"Enter the {i+1} line:")
    senten=input()
    senten_list.append(senten)

for i in senten_list:
    i.lower()
    t_count=i.count("t")
    s_count=i.count("s")
    if t_count>=s_count:
        print("English:")
        print(i)
    elif t_count<s_count:
        print("French:")
        print(i)

