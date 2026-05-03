from src.uds_flasher import UDSFlasher

def test_flash():
    flasher = UDSFlasher()
    result = flasher.flash_firmware("2.0")

    assert result is True
    assert flasher.firmware_version == "2.0"