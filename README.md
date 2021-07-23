<h1 align='center'>TINGE</h1>
<h2 align='center'>Output colored text in terminal</h2>

<p align='center'>
<a href="https://www.python.com"><img alt="made with python" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/Code%20Style-Black-000000.svg"></a>
<a href="https://github.com/g-paras/tinge/blob/master/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="https://pypi.org/project/tinge/"><img alt="PyPI" src="https://img.shields.io/pypi/v/tinge"></a>
<a href="https://pepy.tech/project/tinge"><img alt="Downloads" src="https://pepy.tech/badge/tinge"></a>
</p>

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
These method prints by default & return None

```python
from tinge import warn, error, info, success

warn("This is warning") # yellow bold text
info("This is to inform") # blue bold text
success("Success", strong=False) # green normal text
error("Error: File Missing") # red bold text
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
| `colored`   | *text*, *color*, *on_color*  | Colored text               |
| `italic`    | *text*, *color*, *on_color*  | Italic colored text        |
| `underline` | *text*, *color*, *on_color*  | Underlined colored text    |
| `bold`      | *text*, *color*, *on_color*  | Bold colored text          |
| `warn`      | *text*                       | Yellow Bold Warning text   |
| `error`     | *text*                       | Red Bold Error text        |
| `info`      | *text*                       | Blue Bold Information text |
| `success`   | *text*                       | Green Bold Success text    |
