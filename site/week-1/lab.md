.. sectnum::

# Lab 1 — Hello, world

```{important}
Write on the board:
    sun-python-23w.github.io
```

```{important}
- Hand out laptops
- Use post-its to keep track of who has which laptop ...?
```

## Set up

1. Launch the application (should be in the dock)
1. Open the folder `week-1` in the `python` folder on the desktop.

    1. You can open the folder from VSCode by clicking *Open Folder* from the explorer, and then selecting `python` and `week-1`.
    ![](images/vscode-start.png)
    ![](images/vscode-open-folder.png)

    OR

    1. You can navigate to the `week-1` folder in finder and drop it in VSCode.
    ![](images/vscode-drop-folder.png)

Once your application looks like this you are ready to commence the lab!
![](images/vscode-interface.png)



---


## Exercises

### Months

1. Start the python interactive interpreter (enter `python` in the terminal)
1. Write an expression that calculates your age in months using multiplication (`*`) and addition (`+`)

### Hello, world

Use `print()` to write a program in the file `hello-world.py` that will display **Hello, world!** when run:

```python
% python hello-word.py
"Hello, world!"
```

```{note}
The first known 'Hello world' program was written in [1974](https://en.m.wikipedia.org/wiki/%22Hello,_World!%22_program).
```

### Mad libs

```python
sentence = "The ______ brown fox ______ over the ______ dog."
#                adj              verb            adj
```

```python
"The clever brown fox sailed over the smelly dog."
```


```{important}
TIMECHECK: 85 minutes
```

---

## Challenges

```{note}
These can be done in any order; if you get stuck try a different one!
```


### Age in days

...?

### Text art

1. Visit [this site](https://www.texttoascii.com/text-art) to generate text art that says **Hello, world!**
1. Use the text art and modify your `hello-world.py` to print out the art in the terminal.

Here's an example:

```plaintext
% python hello-world.py

    dMP dMP dMMMMMP dMP     dMP    .aMMMb        dMP dMP dMP .aMMMb  dMMMMb  dMP     dMMMMb
   dMP dMP dMP     dMP     dMP    dMP"dMP       dMP dMP dMP dMP"dMP dMP.dMP dMP     dMP VMP
  dMMMMMP dMMMP   dMP     dMP    dMP dMP       dMP dMP dMP dMP dMP dMMMMK" dMP     dMP dMP
 dMP dMP dMP     dMP     dMP    dMP.aMP       dMP.dMP.dMP dMP.aMP dMP"AMF dMP     dMP.aMP
dMP dMP dMMMMMP dMMMMMP dMMMMMP VMMMP"        VMMMPVMMP"  VMMMP" dMP dMP dMMMMMP dMMMMP"

```

Hint:

```python
long_string = ("first line\n" +
               "second line\n")
```

### Colors


```{important}
If everyone finishes the lab early:

- (10-15 minutes) explain `input()` and have people augment their mad libs program
- (5 minutes) start a discussion:
    - What did people learn?
    - What was hard?
    - What can we improve for next time?
```
