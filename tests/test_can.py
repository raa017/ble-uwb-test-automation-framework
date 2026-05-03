from src.can_interface import CANInterface

def test_can_send_receive():
    can_if = CANInterface()

    can_if.send_message(0x123, [1, 2, 3])
    msg = can_if.receive_message()

    assert msg is not None
    assert msg.arbitration_id == 0x123