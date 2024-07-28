# File Handeling
Types of file: txt, dat and csv
Object contains the file address and the operation that we have to perform on that file

#opening files
1. `f = open("myFile.txt",'w')`
2. `f = open(r'E:\new folder\data.txt','r')`

<table>
        <thead>
            <tr>
                <th>Text Files</th>
                <th>Binary Files</th>
                <th>Function</th>
                <th>Details</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>'r'</td>
                <td>'rb'</td>
                <td>read</td>
                <td>File must exist, else error.</td>
            </tr>
            <tr>
                <td>'w'</td>
                <td>'wb'</td>
                <td>write</td>
                <td>If file exists &rarr; overwrite, if not create new file.</td>
            </tr>
            <tr>
                <td>'r+'</td>
                <td>'r+b' or 'rb+'</td>
                <td>read & write</td>
                <td>File must exist, else error. Both read & write works.</td>
            </tr>
            <tr>
                <td>'w+'</td>
                <td>'w+b' or 'wb+'</td>
                <td>write & read</td>
                <td>If file exists &rarr; overwrite, if not create new file. Both read & write works.</td>
            </tr>
            <tr>
                <td>'a'</td>
                <td>'ab'</td>
                <td>append</td>
                <td>Same as 'write', data is not overwritten. It's appended.</td>
            </tr>
            <tr>
                <td>'a+'</td>
                <td>'a+b' or 'ab+'</td>
                <td>append & read</td>
                <td>Same as 'write', data is not overwritten. It's appended. Both read & write works.</td>
            </tr>
        </tbody>
    </table>
# Text Files
