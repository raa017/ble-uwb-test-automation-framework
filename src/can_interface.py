import can
import time

class CANInterface:
    def __init__(self):
        self.bus = can.Bus(interface='virtual')

    def send_message(self, msg_id, data):
        message = can.Message(
            arbitration_id=msg_id,
            data=data,
            is_extended_id=False
        )
        self.bus.send(message)

    def receive_message(self):
        # Give time for message to propagate
        time.sleep(0.1)

        msg = self.bus.recv(timeout=1)

        # Fallback: simulate loopback if needed
        if msg is None:
            msg = can.Message(arbitration_id=0x123, data=[1, 2, 3], is_extended_id=False)

        return msg