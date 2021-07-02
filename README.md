# Sundanase-Lang

Repository of Compilation Techniques (Learning) with [Library SLY](https://sly.readthedocs.io/en/latest/sly.html).
You can read the [manual book here](https://github.com/Pureism/Sundanase_Language/blob/master/LAPORAN%20TEKNIK%20KOMPILASI%20v0.9.pdf).

## Our Grup:

- Muhammad Ammar Nabil [@Pureism](https://github.com/pureism)
- Rafli Hilan Yufandani [@RafliHillany](https://github.com/RafliHillany/)
- Wisnu Afifudin

---

# Documentation

## You Must Know

- This language is created using the SLY library which is supported with [Python v3.\*](https://www.python.org/ "Python")
- This language has the extension .sundanase
- This language based from Sunda Language, Indonesia

## Prerequisite

- [x] Python Language Installed [Python v3.\*](https://www.python.org/ "Python")
- [x] Sly Package Installed [Sly Package v0.\*](https://pypi.org/project/sly/ "Sly Package")

**Check your package**

```py
py -m pip lis
```

## Command in Sundanase-Lang

| SUNDANASE-LANG | MEAN  |
| -------------- | ----- |
| UPAMI          | IF    |
| PRINT          | PRINT |
| TERAS          | THEN  |
| HENTEU         | ELSE  |
| KAHATUR        | FOR   |
| FUN            | FUN   |
| KANGGO         | TO    |
| ->             | ARROW |

## How To Use

**Follow this steps**

1. Open CMD or TERMINAL with the directory this folder directory `cd .../Sundanase/`
2. And then run file `execute.py` in the `Sundanase/` folder

   i.e : Copy paste this text to your cmd or terminal

   ```py
   py execute.py helloworld.sundanase
   ```

3. Or run file `main.py` then type your command

   i.e : Type your command in cmd or terminal

   ```py
   py main2.py
   PRINT "HELLO WORLD"
   ```

## Examples Sundanase Lang

### PRINT

**example :**

```python
PRINT "Hello World"
Sundanase > Hello World
```

**or :**

```python
a = "Hello World"
PRINT a
Sundanase > Hello World
```

### Arithmetic Operations

> Arithmetic Operation = `+` `-` `*` `/` `%` `^`

**example :**

```python
a = 3 + 2
b = 4 - 1
c = 3 * 3
d = 4 / 2
e = 5 % 2
f = 5 ^ 2
PRINT a
Sundanase > 5
PRINT b
Sundanase > 3
PRINT c
Sundanase > 6
PRINT d
Sundanase > 2
PRINT e
Sundanase > 1
PRINT f
Sundanase > 25
```

**or :**

```python
a = 6
b = 2
PRINT (a + b) * b
Sundanase > 16
PRINT a - b * b
Sundanase > 2
PRINT a * b ^ b
Sundanase > 24
PRINT a % (a / b)
Sundanase > 0
```

### Logical Operations

> Logical Operation = `==` `!=` `>` `<` `>=` `<=`

**example :**

```py
5 == 5
Sundanase > true
5 != 5
Sundanase > false
7 > 5
Sundanase > true
7 < 5
Sundanase > false
5 <= 10
Sundanase > true
5 >= 10
Sundanase > false
```

### IF ELSE

> IF _expr_ THEN _stmt1_ ELSE _stmt2_

> UPAMI _expr_ TERAS _stmt1_ HENTEU _stmt2_

**example :**

```py
a = 6
y = "true"
n = "false"
UPAMI a==6 TERAS PRINT y HENTEU PRINT n
Sundanase > "true"
```

### FOR

> FOR _expr_ TO _stmt1_ THEN _stmt2_

> KAHATUR _expr_ KANGGO _stmt1_ TERAS _stmt2_

**example :**

```python
KAHATUR i=0 KANGGO 5 TERAS PRINT i
Sundanase > 0
            1
            2
            3
            4
```

### Function

> FUN functionName() -> Your Code Here...

**example :**

```py
FUN print() -> PRINT "Hello World"
print()
Sundanase > Hello World
```

**or :**

```py
FUN loop() -> KAHATUR i=0 KANGGO 5 TERAS PRINT i
loop()
Sundanase > 0
            1
            2
            3
            4
```

### Use Comment

> You can use `'#'` symbol to make comment in your source code.

**example:**

```py
I = "U" #U is a string
#now you know how this works
UPAMI I == "U" TERAS PRINT "PERFECT" HENTEU PRINT "I'm So Sorry"
Sundanase > "PERFECT"
```

Good luck, Thanks :)

## REFERENCE

This is a modified source code for the howCode programming language series and fauzaaulia repository

- [x] You can watch the video accompanying this series here: [https://www.youtube.com/playlist?list=PLBOh8f9FoHHgPEbiK-FSdSw3FiyP78fbk](https://www.youtube.com/playlist?list=PLBOh8f9FoHHgPEbiK-FSdSw3FiyP78fbk "howCode Programming Language Series")
- [x] You can view original source code in Github [fauzaaulia's Repository](https://github.com/fauzaaulia/Rhs-Lang "Reza Aulia Github")
