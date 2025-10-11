# Graphical User Interfaces
Tkinter Used for creating Graphical user interfaces in python
1. import module
2. create GUI application
3. Add widgets
4. Enter the main Event Loop

# Starting
```python
import tkinter as tk    # alias name(short name) = tk 
win = tk Tk()            # assign the variable, Tk function, creats the screen
win.title("Hello World")  # creating title component
win.mainloop()             # Important to write
```
- `Tk()` function is used

![image](https://github.com/user-attachments/assets/e2513d4d-c891-4b13-b2d5-40248de94920)

![image](https://github.com/user-attachments/assets/7cf67b13-a835-4ee3-a36d-45798bc7a5b9)

 - **container** : Parent container container contains chile container
 - **Event drivin programming**: behaviour of widgets
 - ### Important Widgets
    - Button
    - Canvas : to draw
    - CheckBox
    - Entry : to take text inputs
    - Label: provides single line caption for other widgets
    - Frame: used as a container widget to organise other widgets
    - Menu Button: used to display menu in your application
    - Menu: menu widgets used to provide option 
    - Message:
    - Radio Button:
    - Text Box
    - Scale: silder widget
    - Scroll Bar: adds scrolling vabpalbility to the other widgets

   ### Other Widgets
    - Panedwindow ...


# Example
```python
  import tkinter as tk

  root =  tk.Tk()
  root.title("Tkinter Widget")

  label = tk.Label(root, text = "welcome")
  label.pack()

  entry = tk.Entry(root)
  entry.pack()

  button = tk.Button(root, text = "Click Me")
  button.pack()

   root.mainloop()
  
```
# Arranging the Widgets
## `.pack()`
  - Arranges the component one by one (vertically or horizontally)

## `.grid()`
  - format: rows and coloumns
  - ```py
    widget.grid(options)

    ```
## `place()`
   
  - put stuff anywhere using coordinates
![image](https://github.com/user-attachments/assets/aeb05a52-b5ce-4329-8888-9996e6094923)

