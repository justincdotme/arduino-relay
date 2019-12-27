class Arduino:
    def __init__(self, serial, time):
        self._serial = serial
        self._serial.flush()
        self._time = time

    def send(self, val):
        self._serial.write(val)
        self._time.sleep(1)
        i=0
        msg = ""
        while (i<2):
            msg += str(self._serial.read(
                self._serial.inWaiting()
            ))

            i = i+1
        return msg
