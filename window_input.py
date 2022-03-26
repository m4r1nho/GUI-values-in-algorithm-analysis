import PySimpleGUI as sg  # Importing
import numpy as np

def function_layout():
    layout = [[sg.Text("Enter the value:")],  # The Layout
              # ↓ Where insert the number, I put a key for identification and size
              [sg.Input(key='number_str', size=5)],
              [sg.Button('Ok')]]  # Button
    # Create the window
    window = sg.Window('Welcome!', layout, size=(500, 400), element_justification='center')  # Window Definition

    # Display and interact with the Window
    event, values = window.read()  # Event loop or Window.read call

    value = float(values['number_str'])  # String to float conversion
    window.close()  # Close the Window

    # The values of fundamental functions in algorithm analysis
    # Assigning value to variables
    value_log = np.log2(value)
    value_n_log = np.log2(value) * value
    value_squared = value ** 2
    value_cubed = value ** 3
    value_power = 2 ** value

    # layout for other windows with so much texts for values in their situation
    layout = [[sg.Text(f'Log {value} is {value_log}')],
              [sg.Text(f'N is {value}')],
              [sg.Text(f'Log {value} is {value_log}')],
              [sg.Text(f'{value} plus Log{value} is {value_n_log}')],
              [sg.Text(f'{value} to the power of 2 is {value_squared}')],
              [sg.Text(f'{value} to the power of 3 is {value_cubed}')],
              [sg.Text(f'2 to the power of {value} is {value_power}')]

              ]
    # Window Definition
    window = sg.Window("The values of fundamental functions in algorithm analysis", layout, size=(500, 400))
    event, values = window.read()