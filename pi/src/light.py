class Light:
    def __init__(self, num, state, controller):
        self._num = num
        self._state = state
        self._controller = controller

    def get_num(self):
        return self._num

    def set_state(self, state):
        self._state = state
        response = self._controller.send(
            str(str(self._num) + str(self._state)).encode()
        )
        #todo: return boolean value from response
        return self

    def get_state(self):
        return self._state
