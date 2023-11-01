# ArrayList

The `ArrayList` class represents a list-like data structure in Python that allows dynamic resizing. This implementation uses a data store based on a `ConstrainedList` and provides various methods to manipulate and query the elements of the list.

## Class Structure

### `ArrayList`

- The main class representing the list data structure.

#### Constructor

- `__init__(self)`: Initializes an empty ArrayList with a data store using a `ConstrainedList`.

#### Subscript-Based Access

- `__getitem__(self, idx)`: Allows you to access elements using square brackets. Returns the element at the specified index.
- `__setitem__(self, idx, value)`: Allows you to set the value at the specified index.
- `__delitem__(self, idx)`: Allows you to delete the element at the specified index.

#### Stringification

- `__str__(self)`: Returns a string representation of the list enclosed in square brackets, with elements separated by commas.
- `__repr__(self)`: Returns the same string representation as `__str__`.

#### Single-Element Manipulation

- `append(self, value)`: Appends a new element to the end of the list.
- `insert(self, idx, value)`: Inserts a value at the specified index, shifting the original elements down the list as needed.
- `pop(self, idx=-1)`: Deletes and returns the element at the specified index (the last element by default).
- `remove(self, value)`: Removes the first instance of the specified value from the list.

#### Predicates (True/False Queries)

- `__eq__(self, other)`: Compares this ArrayList to another and returns `True` if they contain the same elements in the same order.
- `__contains__(self, value)`: Checks if a specific value is present in the list.

#### Queries

- `__len__(self)`: Returns the number of elements in the list.
- `min(self)`: Returns the minimum value in the list.
- `max(self)`: Returns the maximum value in the list.
- `index(self, value, i=0, j=None)`: Returns the index of the first instance of a value within a specified range.
- `count(self, value)`: Returns the number of times a value appears in the list.

#### Bulk Operations

- `__add__(self, other)`: Concatenates this list with another and returns a new ArrayList containing all the elements in order.
- `clear(self)`: Removes all elements from the list and resets it to an empty state.
- `copy(self)`: Creates a copy of the ArrayList, including separate data storage.
- `extend(self, other)`: Appends all elements from another iterable to the end of the list.

#### Iteration

- `__iter__(self)`: Allows for iteration through the list.

## Example Usage

```python
# Create an ArrayList
my_list = ArrayList()

# Add elements
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Access elements
element = my_list[1]  # Access the element at index 1 (2)

# Modify elements
my_list[0] = 0  # Set the element at index 0 to 0

# Remove elements
del my_list[2]  # Delete the element at index 2

# Check if an element is in the list
if 3 in my_list:
    print("3 is in the list")

# Iterate through the list
for item in my_list:
    print(item)

# Other operations are also available, such as min, max, and more.
```
