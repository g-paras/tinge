<h1 style="text-align: center; font-weight: bold">
    <span style="color: red">T</span>
    <span style="color: blue">I</span>
    <span style="color: yellow">N</span>
    <span style="color:green">G</span>
    <span style="color:magenta">E</span>
</h1>
<p style="text-align: center">Output colored text in terminal</p>


## Setup and Installation

1. Clone this repository
```bash
git clone https://github.com/g-paras/tinge.git
cd tinge
```

2. Install the module 
```python
python setup.py install
```

Installation Complete 👍


## Example
### Foreground
```python
from tinge import colored

print(colored("This is red text", color="red"))
```


### Foreground and Background
```python
from tinge import colored

print(colored("Green on white","green", "white"))
```

## Available Colors
| Foreground | Background |
|----------- | -----------|
| Black | Grey |
| Red | Red |
| Green | Green |
| Yellow | Yellow |
| Blue | Blue |
| Magenta | Magenta |
| Cyan | Cyan |
| White | White |
