# File Handeling
Types of file: txt, dat and csv
Object contains the file address and the operation that we have to perform on that file

# Opening files
1. `f = open("myFile.txt",'w')`
2. `f = open(r'E:\new folder\data.txt','r')`


    <table>
        <thead>
            <tr>
                <th>Text Files</th>
                <th>Binary Files</th>
                <th>CSV Files</th>
                <th>Function</th>
                <th>Details</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>'r'</td>
                <td>'rb'</td>
                <td>'r'</td>
                <td>read</td>
                <td>File must exist, else error.</td>
            </tr>
            <tr>
                <td>'w'</td>
                <td>'wb'</td>
                <td>'w'</td>
                <td>write</td>
                <td>If file exists &rarr; overwrite, if not create new file.</td>
            </tr>
            <tr>
                <td>'r+'</td>
                <td>'r+b' or 'rb+'</td>
                <td>'r+'</td>
                <td>read & write</td>
                <td>File must exist, else error. Both read & write works.</td>
            </tr>
            <tr>
                <td>'w+'</td>
                <td>'w+b' or 'wb+'</td>
                <td>'w+'</td>
                <td>write & read</td>
                <td>If file exists &rarr; overwrite, if not create new file. Both read & write works.</td>
            </tr>
            <tr>
                <td>'a'</td>
                <td>'ab'</td>
                <td>'a'</td>
                <td>append</td>
                <td>Same as 'write', data is not overwritten. It's appended.</td>
            </tr>
            <tr>
                <td>'a+'</td>
                <td>'a+b' or 'ab+'</td>
                <td>'a+'</td>
                <td>append & read</td>
                <td>Same as 'write', data is not overwritten. It's appended. Both read & write works.</td>
            </tr>
        </tbody>
    </table>
    

# Text files
- ## Reading in the text files
    ```python
    f = open(r'd:\\new folder\\list.txt')
    result = f.read()
    print(result)
    ```
    Types of function's
    1. `f.read()`: writes all the bytes of the file
    2. `f.readline()`: returns a single line, if given parameter returns that number of characters from that line, everytime we use readline it goes to next line
    3. `f.readlines()`: returns all the lines in the form of list
    
    alternate way of reading the lines
    1. ```python
       f=open("lyrics.txt")
       for i in f:
           print(i)
       ```
    2. ```python
       while s:
           s = f.readline()
           print(s)
       ```


- ## Writing in the text files
    1. Write function
        ```python
           f = open('d:\\New Folder\\list.txt','w')
           f.write('Hi friends, chaai peelo')
        ```
    2. Writelines
       write all the strings from the list to the file
       ```python
       f = open('list.txt','w')
       tasks = ['gym','chapter 3','water plants','dog's walk']
       f.writelines(tasks)
       ```
       
- ## Strip function
    `strip()`: removes the given character from both ends
    `lstrip()`: removes the given character from leading end/left(left end).
    `rstrip()`: removes the given character from trailing end/right(right end)

 - ## file Pointer


# Binary Files
Using pickle module
`import pickle`
 - ## Reading in the binary files
   ```python
    global fb
    f = open(fb,"rb")
    try:
        while True:
            
            rec = pickle.load(f)
            print(rec)
    except EOFError:
        print("ALL RECORDS PRINTED")
        f.close()
        
   ```
 - ## Writing in the binary files
    ```python
    rec  = [sno,name,phoneno]
    pickle.dump(rec,f)

 - ## Deleting from the binary files
   ```
    fb = "file.dat"
    ft = "temp.dat"
    f = open(fb,"rb")
    f2 = open(ft,"ab")
    try:
        while True:
            rec = pickle.load(f)
            if rec[0] == sno:
                continue
            else:
                pickle.dump(rec,f2)
    except EOFError:
       print("RECORD DELETED,NOW THE PERSON MAY NOT BE ABLE TO EXIT THE PARKING")
       f.close()
       f2.close()
       os.remove(fb)
       os.rename(ft,fb)

   ```
- # Updating in the binary file
  ```
  def update():
    global fb,ft
    print("RECORDS CAN ONLY BE UPDATED UNTIL CAR IS PARKED NOT AFTER THE EXIT")
    sno = int(input("Enter the sno you want to update"))
    f = open(fb,"rb")
    f2 = open(ft,"ab")
    try:
        while True:
            rec = pickle.load(f)
            if rec[0] == sno:
                print(rec)
                name = input("ENTER NEW NAME")
                rec[1] = name
                pno = int(input("Enter Phoneno"))
                rec[2] = pno
                pickle.dump(rec,f2)
            else:
                pickle.dump(rec,f2)
    except EOFError:
       print("RECORD UPDATED")
       f.close()
       f2.close()
       os.remove(fb)
       os.rename(ft,fb)

  
  ```

 # CSV Files
   `import csv`
   - ## reading in the CSV file
     ```python
     f = open('file.csv','r')
     b = csv.reader(f,delimiter = ',')
     print(next(b))
     print(next(b))
           # or
     for i in b:
         print(i)
     
     ```
  - ## Writing in the CSV files
    ```python
    f = open('list.csv','w',newline = '')
    b = csv.writer(a,delimiter = ',')
    b.writerow(['Panda','B&W'])
    b.writerow(['Bear','brown'])
             #or
    for i in l:
        b.writerow(i)
    ```


