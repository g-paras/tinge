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

```python
from tinge import italic, underline, bold

print(italic("This is italic"))
print(underline("This is underlined"))
print(bold("This is bold"))
```

### Styling with Foreground and Background

```python
from tinge import colored, italic, underline, bold

print(colored(
    underlined("This is red on white"),
    color="red",
    on_color="white"))

print(colored(
    italic("This is italic"),
    color="green"))
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

| Function    | Parameters            | Use for               |
| ----------- | --------------------- | --------------------- |
| `colored`   | text, color, on_color | Colored text          |
| `italic`    | text                  | Italic text           |
| `underline` | text                  | Underlined text       |
| `bold`      | text                  | Bold text             |
| `warn`      | text                  | Yellow Warning text   |
| `error`     | text                  | Red Error text        |
| `info`      | text                  | Blue Information text |
| `success`   | text                  | Green Success text    |
