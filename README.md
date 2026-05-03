# BLE UWB Test Automation Simulation Framework

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-8+-green.svg)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simulation-based test automation framework for BLE/UWB transceiver systems, featuring CAN bus communication simulation, device simulation, firmware flashing via UDS, and automated testing capabilities.

## Table of Contents

- [Motivation](#motivation)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [CI/CD](#cicd)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Motivation

This project was developed to demonstrate concepts relevant to embedded software testing, including automated test case generation, CAN communication, and firmware flashing workflows, aligned with real-world automotive and wireless system development.

## Features

### Core Components

- **Device Simulator**: Transceiver simulation with configurable packet loss rates
- **CAN Interface**: Simulated CAN communication using python-can (virtual interface)
- **UDS Flasher**: Firmware update simulation via Unified Diagnostic Services (UDS)
- **Fault Logger**: Basic logging system for test failures and anomalies
- **Virtual CAN Bus**: Support for virtual CAN interfaces for testing without hardware

### Testing Capabilities

- **Transmission Testing**: Packet success rate validation with statistical analysis
- **CAN Communication**: Message sending/receiving verification
- **Firmware Flashing**: Automated firmware update testing
- **Integration Testing**: End-to-end test scenarios

### Development Features

- **Modular Architecture**: Clean separation of concerns with extensible design
- **Test Suite**: Automated testing with pytest framework
- **CI/CD Integration**: Jenkins pipeline for automated testing
- **Python 3.10+ Support**: Modern Python with best practices

## Architecture

```
ble_uwb_test_automation/
├── src/
│   ├── __init__.py
│   ├── can_interface.py      # CAN bus communication simulation
│   ├── device_simulator.py   # BLE/UWB device simulation
│   ├── logger.py             # Fault logging system
│   └── uds_flasher.py        # Firmware flashing via UDS
├── tests/
│   ├── __init__.py
│   ├── test_can.py           # CAN interface tests
│   ├── test_flash.py         # Firmware flashing tests
│   └── test_transmission.py  # Transmission reliability tests
├── main.py                   # Demo script
├── requirements.txt          # Python dependencies
├── pytest.ini               # Test configuration
├── Jenkinsfile              # CI/CD pipeline
└── README.md
```

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager
- (Optional) CAN hardware interface for real testing

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/ble-uwb-test-automation.git
   cd ble-uwb-test-automation
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) For CAN hardware support, install additional drivers as needed.

## Usage

### Basic Usage

Run the demo script to see the framework in action:

```bash
python main.py
```

This will simulate 10 packet transmissions and display the results.

### Using Components

#### Device Simulator

```python
from src.device_simulator import Transceiver

# Initialize transceiver
device = Transceiver()

# Send packets
for i in range(100):
    success = device.send_packet()
    if success:
        print(f"Packet {i}: SUCCESS")
    else:
        print(f"Packet {i}: FAILED")
```

#### CAN Interface

```python
from src.can_interface import CANInterface

# Initialize CAN interface
can_if = CANInterface()

# Send message
can_if.send_message(0x123, [1, 2, 3, 4])

# Receive message
msg = can_if.receive_message()
print(f"Received: ID={msg.arbitration_id}, Data={msg.data}")
```

#### UDS Flasher

```python
from src.uds_flasher import UDSFlasher

# Initialize flasher
flasher = UDSFlasher()

# Flash new firmware
success = flasher.flash_firmware("2.1.0")
if success:
    print(f"Firmware updated to {flasher.firmware_version}")
```

#### Logger

```python
from src.logger import log_fault

# Log faults
log_fault("CAN bus timeout detected")
log_fault("Packet loss rate exceeded threshold")
```

## Configuration

### CAN Interface Configuration

The CAN interface uses a virtual bus by default. For hardware CAN interfaces, modify the `CANInterface` class:

```python
# In can_interface.py
self.bus = can.Bus(interface='socketcan', channel='can0')  # For Linux
# or
self.bus = can.Bus(interface='pcan', channel='PCAN_USBBUS1')  # For PCAN
```

### Device Simulator Configuration

Configure packet loss rates and other parameters in the `Transceiver` class:

```python
def __init__(self, packet_loss_rate=0.02):
    self.packet_loss_rate = packet_loss_rate
    # Add more configuration parameters as needed
```

## Testing

### Running Tests

Execute the complete test suite:

```bash
pytest tests/ -v
```

### Test Coverage

- **test_can.py**: Validates CAN message sending and receiving
- **test_flash.py**: Tests firmware flashing functionality
- **test_transmission.py**: Verifies packet transmission reliability (>90% success rate)

### Adding New Tests

Create new test files in the `tests/` directory following the naming convention `test_*.py`:

```python
# tests/test_new_feature.py
def test_new_functionality():
    # Test implementation
    assert True
```

## CI/CD

The project includes a Jenkins pipeline for automated testing:

- **Install Dependencies**: Installs Python requirements
- **Run Tests**: Executes the full test suite
- **Build Status**: Reports test results and coverage

### Local CI Simulation

Run the same steps locally:

```bash
pip install -r requirements.txt
pytest tests/
```

## Limitations

- BLE/UWB communication is simulated (no physical hardware integration)
- CAN communication uses a virtual interface (python-can)
- UDS flashing workflow is simplified for demonstration purposes
- No real-time performance guarantees
- Limited error handling and edge case coverage

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes and add tests
4. Run the test suite: `pytest tests/`
5. Commit your changes: `git commit -am 'Add new feature'`
6. Push to the branch: `git push origin feature/new-feature`
7. Submit a pull request

### Code Standards

- Follow PEP 8 style guidelines
- Add type hints for new functions
- Include comprehensive docstrings
- Write tests for all new functionality
- Update documentation as needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions, issues, or contributions:

- Create an issue on GitHub
- Contact the development team
- Check the documentation for common solutions

## Roadmap

- [ ] Hardware CAN interface support
- [ ] BLE protocol stack integration
- [ ] UWB ranging algorithm implementation
- [ ] Performance benchmarking tools
- [ ] GUI test interface
- [ ] Cloud-based test result storage