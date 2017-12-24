default mtt = MouseTooltip(Text("No button selected."), padding={"x": 10, "y": -10})


label start:

    call screen tooltip_test

    return

    
screen tooltip_test:
    add mtt
    
    vbox:
        textbutton "One.":
            action Return(1)
            hovered mtt.Action(Text("The loneliest number."))

        textbutton "Two.":
            action Return(2)
            hovered mtt.Action(Text("Is what it takes."))

        textbutton "Three.":
            action Return(3)
            hovered mtt.Action(Text("A crowd."))

        textbutton "Hearts.":
            action Return(3)
            hovered mtt.Action(Image("icons8-heart-outline-48.png"))
