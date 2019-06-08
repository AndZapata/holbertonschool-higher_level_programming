# 0x0B. Python - Proyect from Holberton School

## Python - Almost a circle

### Task

Number-Name | Task
----------- | ----
0. If it's not tested it doesn't work | classes and methods must be unit tested and be PEP 8 validated
1. Base class | first class Base
2. First Rectangle | class Rectangle that inherits from Base
3. Validate attributes | class Rectangle by adding validation of all setter methods and instantiation
4. Area first | Update the class Rectangle by adding the public method def area(self)
5. Display #0 | Update the class Rectangle by adding the public method def display(self)
6. __str__ | the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
7. Display #1 | Update the class Rectangle by improving the public method def display(self)
8. Update #0 | Update the class Rectangle by adding the public method def update(self, *args):
9. Update #1 | Update the class Rectangle by updating the public method def update(self, *args):
10. And now, the Square! | Write the class Square that inherits from Rectangle
11. Square size | Update the class Square by adding the public getter and setter size
12. Square update | Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes
13. Rectangle instance to dictionary representation | Update the class Rectangle by adding the public method def to_dictionary(self)
14. Square instance to dictionary representation | Update the class Square by adding the public method def to_dictionary(self):
15. Dictionary to JSON string | JSON is one of the standard formats for sharing data representation.
16. JSON string to file | Update the class Base by adding the class method def save_to_file(cls, list_objs):
17. JSON string to dictionary | Update the class Base by adding the static method def from_json_string(json_string):
18. Dictionary to Instance | Update the class Base by adding the class method def create(cls, **dictionary):
19. File to instances | Update the class Base by adding the class method def load_from_file(cls):
20. JSON ok, but CSV? | Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls):
21. Let's draw it | Update the class Base by adding the static method def draw(list_rectangles, list_squares):
