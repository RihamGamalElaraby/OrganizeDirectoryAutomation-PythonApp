import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))
print('welcome in organize.py script - happy clean folder')
for filename in os.listdir(current_dir):
    
    #organize photos 
    if filename.endswith((".png" , "jpg" , 'jpeg' , 'gif')):
        if not os.path.exists('Images'):
         os.mkdir('Images')
        shutil.copy(filename , "Images")
        os.remove(filename)
        print('Done Images')
        
    #organize code files 
    if filename.endswith((".py" , "css" , 'html' , 'bash')):
        if not os.path.exists('Codes'):
         os.mkdir('Codes')
        shutil.copy(filename , "Codes")
        os.remove(filename)
        print('Done Codes')
        
    #organize Vedios files 
    if filename.endswith((".mp4" , "wben")):
        if not os.path.exists('Vedios'):
         os.mkdir('Vedios')
        shutil.copy(filename , "Vedios")
        os.remove(filename)
        print('Done Vedios')
        
    #organize Docs files 
    if filename.endswith((".pdf" , ".word")):
        if not os.path.exists('Docs'):
         os.mkdir('Docs')
        shutil.copy(filename , "Docs")
        os.remove(filename)
        print('Done Docs')
        
    #organize Archives files 
    if filename.endswith((".zip" , ".rar" , ".tar")):
        if not os.path.exists('Archives'):
         os.mkdir('Archives')
        shutil.copy(filename , "Archives")
        os.remove(filename)
        print('Done Archives')
         
        
    #organize Apps files 
    if filename.endswith((".dmg" , ".exe")):
        if not os.path.exists('Apps'):
         os.mkdir('Apps')
        shutil.copy(filename , "Apps")
        os.remove(filename)
        print('Done Apps')
    
    
    
print("Done all")
        
        