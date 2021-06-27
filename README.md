<h1 style="text-align: center; font-weight: bold">
    <span style="color: red">T</span>
    <span style="color: blue">I</span>
    <span style="color: yellow">N</span>
    <span style="color:green">G</span>
    <span style="color:magenta">E</span>
</h1>
<p style="text-align: center">Output colored text in terminal</p>

## Example
### Foreground
```python
from tinge import colored

print("This is red text", color="red")
```
Output
<p style="color: red">This is red text</p>

### Foreground and Background
```python
from tinge import colored

print("Green on white","green", "white")
```
Output:
<p><span style="color: green; background: white">Green on White</span></p>
