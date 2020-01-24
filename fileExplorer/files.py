import glob
a = []
print("Enter the directory:")
s1 = str(input())
s2 = s1+"/*"
a = glob.glob(s1+"/*")



for i in range(len(a)):
    s = a[i]
    print(s[len(s1):])