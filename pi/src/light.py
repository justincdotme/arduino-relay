class Light:
    def __init__(self, num, state, controller):
        self._num = num
        self._state = state
        self._controller = controller

    def get_num(self):
        return self._num

    def set_state(self, state):

        if state != self._state:
            result = self._controller.send(
                str(str(self._num) + str(state)).encode()
            )

            if result:
                self._state = state

            return result

        return False

    def get_state(self):
        return self._state
