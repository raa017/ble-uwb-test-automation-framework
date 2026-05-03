import random
import time

class Transceiver:
    def __init__(self):
        self.connected = True
        self.packet_loss_rate = 0.02

    def send_packet(self):
        if not self.connected:
            return False

        time.sleep(0.01)

        if random.random() < self.packet_loss_rate:
            return False
        return True