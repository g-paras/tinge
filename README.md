<h1 align='center'>TINGE</h1>
<p align='center'>Output colored text in terminal</p>



## Setup and Installation

### Using pip

```bash
pip install tinge
```

### For developers / Contributors

1. Clone this repository

```bash
git clone https://github.com/g-paras/tinge.git
cd tinge
```

2. Install the module

```python
python setup.py install
```

Installation Complete :thumbsup:

## Example


### Foreground

```python
from tinge import colored

print(colored("This is red text", color="red"))
```

### Foreground and Background

```python
from tinge import colored

print(colored("Green on white", color="green", on_color="white"))
```

### Styling

> underline & italic are not supported on windows

```python
from tinge import italic, underline, bold

print(italic("This is italic"))
print(underline("This is underlined"))
print(bold("This is bold"))
```

### Styling with Foreground and Background

```python
from tinge import colored, italic, underline, bold

print(
    underline("This is red on white",
    color="red",
    on_color="white")
)

print(
    italic("This is italic",
    color="green")
)
```

### Specific Use Case

```python
from tinge import warn, error, info, success

print(warn("This is warning")) # yellow bold text
print(info("This is to inform")) # blue bold text
print(success("Success", strong=False)) # green normal text
print(error("Error: File Missing")) # red bold text
```

## Available Colors and Styles

| Foreground(color) | Background(on_color) |
| ----------------- | -------------------- |
| Black             | Grey                 |
| Red               | Red                  |
| Green             | Green                |
| Yellow            | Yellow               |
| Blue              | Blue                 |
| Magenta           | Magenta              |
| Cyan              | Cyan                 |
| White             | White                |

| Style | Bold | Italic | Underline |
| ----- | ---- | ------ | --------- |

| Function    | Parameters                   | Use for                    |
| ----------- | ---------------------------- | -------------------------- |
| `colored`   | *text8*, *color*, *on_color* | Colored text               |
| `italic`    | *text8*, *color*, *on_color* | Italic colored text        |
| `underline` | *text8*, *color*, *on_color* | Underlined colored text    |
| `bold`      | *text8*, *color*, *on_color* | Bold colored text          |
| `warn`      | *text8*                      | Yellow Bold Warning text   |
| `error`     | *text8*                      | Red Bold Error text        |
| `info`      | *text8*                      | Blue Bold Information text |
| `success`   | *text8*                      | Green Bold Success text    |
