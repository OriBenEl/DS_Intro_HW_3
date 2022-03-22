# for running the function in the "file" place we need to add ".txt" in the end 
## question 1
def read_line(n,file):
    count=0
    if type(n)==int:
        try:
            with open(file,"r") as handle:
                for line in handle:
                    count +=1
                    check=count
                    if n == count:
                        print(line)
                if n>check:
                    print("line " , n , " doesn't exist")
        except:
            print("file not found")
    else:
        print("invalid input detected")
print(read_line(7,"romeo.txt"))


# question 2
five_longest_list=[]
big_list=[]
def longest_words(file):
    try:
        with open(file,"r") as handle:
            for line in handle:
                words=line.split()
                for word in words:
                    big_list.append(word)
            count=0
            while count<5:
                count+=1
                five_longest_list.append(max(big_list,key=len))
                big_list.remove(max(big_list,key=len))
            print(five_longest_list)
    except:
        print("file not found")
print(longest_words("ex3_text.txt"))
                    

























