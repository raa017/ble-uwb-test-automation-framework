# BLE UWB Test Automation Simulation Framework

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-8+-green.svg)](https://pytest.org/)

A simulation-based test automation framework for BLE/UWB transceiver systems, featuring CAN bus communication simulation, device simulation, firmware flashing via UDS, and automated testing capabilities.

## Table of Contents

- [Motivation](#motivation)
- [Features](#features)
- [Installation](#installation)
- [CI/CD](#cicd)
- [Limitations](#limitations)

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

