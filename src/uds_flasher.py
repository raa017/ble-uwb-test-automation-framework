class UDSFlasher:
    def __init__(self):
        self.firmware_version = "1.0"

    def flash_firmware(self, new_version):
        self.firmware_version = new_version
        return True