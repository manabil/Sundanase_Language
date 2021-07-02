# Rhs-Lang

Repository of Compilation Techniques (Learning) with [Library SLY](https://sly.readthedocs.io/en/latest/sly.html).
You can read the [manual book here](https://github.com/pureism/Sundanase_Language).

## Our Grup:

- Muhammad Ammar Nabil @Pureism
- Rafli Hilan Yufandani @RafliHillany
- Wisnu Afifudin _-_

---

# Documentation

## You Must Know

- [x] This language is created using the SLY library which is supported with [PYTHON version 3.\*](https://www.python.org/ "Python")
- [x] This language has the extension .sundanase
- [x] This language based from Sunda Language, Indonesia

## Prerequisite

- [x] Python Language Installed [PYTHON version 3.\*](https://www.python.org/ "Python")
- [x] Sly Package Installed [Sly Package version 0.\*](https://pypi.org/project/sly/ "Sly Package")

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

```
py .execute.py .bahasaku.rhs
```

3. Or run file `main.py` then type your command

i.e : Type your command in cmd or terminal

```
py main2.py
Sundanase > PRINT "HELLO WORLD"
```

## Examples Sundanase Lang

### PRINT Hello World!!

**example :**

```python
Sundanase > PRINT "Hello World"
Sundanase > Hello World
```

**or :**

```python
Sundanase > a = "Hello World"
Sundanase > PRINT a
Sundanase > Hello World
```

### Addition, Subtraction, Multiplication, Division, Modulus, Power

**example :**

```python
Sundanase > a = 3 + 2
Sundanase > b = 4 - 1
Sundanase > c = 3 * 3
Sundanase > d = 4 / 2
Sundanase > e = 5 % 2
Sundanase > f = 5 ^ 2
Sundanase > PRINT a
Sundanase > 5
Sundanase > PRINT b
Sundanase > 3
Sundanase > PRINT c
Sundanase > 6
Sundanase > PRINT d
Sundanase > 2
Sundanase > PRINT e
Sundanase > 1
Sundanase > PRINT f
Sundanase > 25
```

**or :**

```python
Sundanase > a = 6
Sundanase > b = 2
Sundanase > PRINT (a + b) * b
Sundanase > 16
Sundanase > PRINT a - b * b
Sundanase > 2
Sundanase > PRINT a * b ^ b
Sundanase > 24
Sundanase > PRINT a % (a / b)
Sundanase > 0
```

### Logical Operations

> Logical Operation = `==`, `!=`, `>`, `<`, `>=`, `<=`

**example :**

```py
Sundanase > 5 == 5
Sundanase > true
Sundanase > 5 != 5
Sundanase > false
Sundanase > 7 > 5
Sundanase > true
Sundanase > 7 < 5
Sundanase > false
Sundanase > 5 <= 10
Sundanase > true
Sundanase > 5 >= 10
Sundanase > false
```

### IF ELSE

> IF _expr_ THEN _stmt1_ ELSE _stmt2_
> UPAMI _expr_ TERAS _stmt1_ HENTEU _stmt2_

**example :**

```py
Sundanase > a = 6
Sundanase > y = "true"
Sundanase > n = "false"
Sundanase > UPAMI a==6 TERAS PRINT y HENTEU PRINT n
Sundanase > "true"
```

### FOR

> FOR _expr_ TO _stmt1_ THEN _stmt2_
> KAHATUR _expr_ KANGGO _stmt1_ TERAS _stmt2_

**example :**

```python
Sundanase > KAHATUR i=0 KANGGO 5 TERAS PRINT i
0
1
2
3
4
```

### Function

> FUN functionName() -> Your Code Here...

**example :**

```py
Sundanase > FUN print() -> PRINT "Hello World"
Sundanase > print()
Sundanase > Mantap Gan!!
```

**or :**

```py
Sundanase > FUN loop() -> KAHATUR i=0 KANGGO 5 TERAS PRINT i
Sundanase > loop()
0
1
2
3
4
```

### Use Comment

> You can use `'#'` symbol to make comment in your source code.

**example:**

```py
Sundanase > I = "U" #U is a string
Sundanase > #now you know how this works
Sundanase > UPAMI I == "U" TERAS PRINT "PERFECT" HENTEU PRINT "I'm So Sorry"
Sundanase > "PERFECT"
```

Good luck, Thanks :)

## REFERENCE

This is a modified source code for the howCode programming language series and fauzaaulia repository

- [x] You can watch the video accompanying this series here: [https://www.youtube.com/playlist?list=PLBOh8f9FoHHgPEbiK-FSdSw3FiyP78fbk](https://www.youtube.com/playlist?list=PLBOh8f9FoHHgPEbiK-FSdSw3FiyP78fbk "howCode Programming Language Series")
- [x] You can view original source code in Github [fauzaaulia's Repository](https://github.com/fauzaaulia/Rhs-Lang "Reza Aulia Github")
