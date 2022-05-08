#reading the files
folderpath=r"C:\Users\Pradip Chaurel\Desktop\files"
#so change the directry
os.chdir(folderpath)
#os.getcwd()

#to check files
os.listdir()
#to get extension
list_extension=[]
for fl in os.listdir():
    #print(fl)
    extension=fl.split(".")[-1]
    list_extension.append(extension)
    #print(list_extension)
    list_extension=list(set(list_extension))
print(list_extension)

#to create folder  define a new module
import shutil
path=os.environ["UserProfile"]+ "\\" + "Desktop" + "\\" + "file_management"

try:
    shutil.rmtree(path)
    os.mkdir(path)
except:
    os.mkdir(path)
    
#to transferr files
for ex in list_extension:
    print(ex,end=",")
    os.mkdir(path + "\\" + ex)
    for fl in os.listdir():
        if ex in fl:
            shutil.copy(fl,path+"\\"+ex)
    
    
    
    
    
    
    
    
    
    
    
