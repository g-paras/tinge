<h1 align='center'>TINGE</h1>
<p align='center'>Output Colored text in terminal</p>


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

Installation Complete :thumbs_up:


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
