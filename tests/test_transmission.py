from src.device_simulator import Transceiver

def test_packet_success_rate():
    device = Transceiver()
    success = 0

    for _ in range(100):
        if device.send_packet():
            success += 1

    success_rate = success / 100
    assert success_rate > 0.9