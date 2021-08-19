alphabets=" abcdefghijklmnopqrstuvwxyz"
num=int(input("Enter the number of alphabet you want:"))
alphai=input("Enter the alphabet:")
num_ans=alphabets[num]
alphai_ans = alphabets.index(alphai)
suffix="0"

if num == 1:
    suffix="st"
elif num == 21:
    suffix="st"
elif num == 2:
    suffix="nd"
elif num == 22:
    suffix="nd"
elif num == 3:
    suffix="rd"
elif num == 23:
    suffix="rd"
else:
    suffix="th"

print()
print("The "+str(num)+suffix+" alphabet is= "+num_ans.upper())


if alphai_ans == 1:
    suffix="st"
elif alphai_ans == 21:
    suffix="st"
elif alphai_ans == 2:
    suffix="nd"
elif alphai_ans == 22:
    suffix="nd"
elif alphai_ans == 3:
    suffix="rd"
elif alphai_ans == 23:
    suffix="rd"
else:
    suffix="th"

print()
print(alphai.upper()+" is "+str(alphai_ans)+suffix+" alphabet")