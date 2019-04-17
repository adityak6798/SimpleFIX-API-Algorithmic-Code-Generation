# SimpleFIX-API-Algorithmic-Code-Generation
Generation of an API for SimpleFIX using QuickFIX's XML file.

SimpleFIX : https://simplefix.readthedocs.io/en/latest/

QuickFIX : http://www.quickfixengine.org/

This is code to generate an API for SimpleFIX for QuickFIX (FIX4.4) using the XML file.

The generated code is availabble in the files SimpleFIX_API_1.py, SimpleFIX_API_2.py

The code to generate code is in the jupyter notebook.

To create a component : 
```python
Component_Name(Tag_1 = Val_1, Tag_2 = Val_2, ... Tag_N = Val_N)
```

To create a message : 
```python
Message_Name(Tag_1 = Val_1, Tag_2 = Val_2, ... Tag_N = Val_N)
```
Components have to be passed as :
```python
Message_Name(Component_Name = Component_Name(Tag_1 = Val_1, Tag_2 = Val_2, ... Tag_N = Val_N), ...)
```
Groups have to be passed in the following format : 
```python
Group_Name = [[Tag_Name_1, Tag_Name_2, ... Tag_Name_M],
              [Tag_1_Val, Tag_2_Val, ... Tag_M_Val], #For instance 1
              [Tag_1_Val, Tag_2_Val, ... Tag_M_Val], #For instance 2
              .
              .
              .
              [Tag_1_Val, Tag_2_Val, ... Tag_M_Val]] #For instance N
```              

To parse a message, use :
```python
parse_message(FixMessage)
```
where FixMessage is an object of type simplefix.FixMessage created after calling FixParser.get_message() (Refer simplefix documentation: https://github.com/da4089/simplefix)

This will return a dictionary of the form : 
```python
msg_dict = {Tag_Name_1 = Val_1,
            Tag_Name_2 = Val_2,
            .
            .
            .
            Tag_Name_N = Val_N}
```
Groups will be returned in the same form as above. components will not be returned, instead their fields will be returned.
