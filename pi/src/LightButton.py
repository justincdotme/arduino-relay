from tkinter import Tk, Checkbutton, BooleanVar


class LightButton:
    def __init__(self, light, appContainer):
        self._light = light
        self._container = appContainer
        self._state = BooleanVar()
        self._state.set(self._light.get_state())
        self._button = Checkbutton(
            self._container,
            text="Light " + str(self._light.get_num()),
            variable=self._state,
            command=self.toggle_state
        )
        self._button.pack()

    def toggle_state(self):
        newState = 0 if self._light.get_state() == 1 else 1

        if self._light.set_state(newState):
            self._state.set(newState)
            return True
        else:
            return False
