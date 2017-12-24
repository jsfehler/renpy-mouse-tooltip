Mouse Tooltip
=============

A Tooltip whose x/y position follows the mouse's.


Basic Usage
-----------

A MouseTooltip can be created with any type of Displayable as the default value.

It can then be placed onto a screen using the `add` statement.

Like a normal Tooltip, changing the value is done through the Action() method.


.. code-block:: python
    
    default mtt = MouseTooltip(Text("No button selected."))
    
    screen tooltip_test:
    add mtt
    
    vbox:
        textbutton "One.":
            action Return(1)
            hovered mtt.Action(Text("The loneliest number."))


License & Usage
-------------------
The icon used in the demo is from https://icons8.com/

All the code is under the MIT license, just like Ren'Py. Do whatever you want with it.