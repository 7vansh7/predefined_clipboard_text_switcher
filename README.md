# User-Guide

1. Define some list of strings in the array variable of the main.py file
2. When you press alt/option on your keyboard you will have the first string in your clipboard
3. As you keep pressing option/alt, the text in the clipboard will change to the value at that index in the array variable
4. Now just use cmd+v/ctrl+v to paste from the list incremently without copying anything
5. The script should be manually run in the background to work using the terminal command (in the project root)

```shell
python main.py || python3 main.py
```

e.g. ->

if the varible array has strings hello and bye, as you press option/alt in the clipboard you will have hello and bye alternatively without the need of having to copy anything
