class Light:
    def __init__(self, num, state, controller):
        self._num = num
        self._state = state
        self._controller = controller

    def get_num(self):
        return self._num

    def set_state(self, state):
        if state != self._state:
            if 1 == state:
                result = self._controller.turn_on(self._num)
            else:
                result = self._controller.turn_off(self._num)

            if result:
                self._state = state

            return result

        return False

    def get_state(self):
        return self._state
