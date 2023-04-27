# to open text fie
#file = open ("path of the file ","'type") rt= read text  wt = write text
file = open ("C:\\Users\\TUSER\Desktop\\soh.txt" ,"rt")
file_Data = file.read()
initial_Index = 0
x= file_Data.find("b",initial_Index)
print(x)