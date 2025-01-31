ascending = '1 2 3 4 5 6 7 8'

music = input()

if music == ascending:
    print("ascending")
elif music == ascending[::-1]:
    print("descending")
else :
    print("mixed")
