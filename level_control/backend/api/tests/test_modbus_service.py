import pytest
from unittest.mock import MagicMock, patch
from api.services.modbus_service import ModbusService
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def modbus_service():
    """
    Fixture to initialize the ModbusService with mock parameters.
    """
    return ModbusService(
        host=os.getenv("MODBUS_HOST"),
        port=int(os.getenv("MODBUS_PORT")),
        slave_id=int(os.getenv("MODBUS_SLAVE_ID")),
        timeout=int(os.getenv("MODBUS_TIMEOUT")),
        retries=int(os.getenv("MODBUS_RETRIES")),
        delay=float(os.getenv("MODBUS_RETRY_DELAY")),
    )


@patch("api.services.modbus_service.ModbusTcpClient")
def test_connect(mock_modbus_client, modbus_service):
    """
    Test successful connection to the PLC.
    """
    mock_modbus_client.return_value.connect.return_value = True
    modbus_service.connect()
    assert modbus_service.is_connected()
    modbus_service.disconnect()


@patch("api.services.modbus_service.ModbusTcpClient")
def test_connect_failure(mock_modbus_client, modbus_service):
    """
    Test connection failure handling.
    """
    mock_modbus_client.return_value.connect.return_value = False
    with pytest.raises(ConnectionError):
        modbus_service.connect()


@patch("api.services.modbus_service.ModbusTcpClient")
def test_read_holding_registers(mock_modbus_client, modbus_service):
    """
    Test reading holding registers from the PLC.
    """
    mock_response = MagicMock()
    mock_response.isError.return_value = False
    mock_response.registers = [123, 456, 789]
    mock_modbus_client.return_value.read_holding_registers.return_value = mock_response

    modbus_service.connect()
    result = modbus_service.read_holding_registers(address=0, count=3)
    assert result == [123, 456, 789]
    modbus_service.disconnect()


@patch("api.services.modbus_service.ModbusTcpClient")
def test_read_holding_registers_failure(mock_modbus_client, modbus_service):
    """
    Test handling errors during reading holding registers.
    """
    mock_response = MagicMock()
    mock_response.isError.return_value = True
    mock_modbus_client.return_value.read_holding_registers.return_value = mock_response

    modbus_service.connect()
    with pytest.raises(Exception):
        modbus_service.read_holding_registers(address=0, count=3)
    modbus_service.disconnect()


@patch("api.services.modbus_service.ModbusTcpClient")
def test_write_register(mock_modbus_client, modbus_service):
    """
    Test writing a value to a PLC register.
    """
    mock_response = MagicMock()
    mock_response.isError.return_value = False
    mock_modbus_client.return_value.write_register.return_value = mock_response

    modbus_service.connect()
    modbus_service.write_register(address=5, value=1234)
    modbus_service.disconnect()


@patch("api.services.modbus_service.ModbusTcpClient")
def test_write_register_failure(mock_modbus_client, modbus_service):
    """
    Test handling errors while writing to a register.
    """
    mock_response = MagicMock()
    mock_response.isError.return_value = True
    mock_modbus_client.return_value.write_register.return_value = mock_response

    modbus_service.connect()
    with pytest.raises(Exception):
        modbus_service.write_register(address=5, value=1234)
    modbus_service.disconnect()


def test_retry_operation(modbus_service):
    """
    Test the retry mechanism for transient errors.
    """
    operation = MagicMock(side_effect=[Exception(
        "Failed"), Exception("Failed"), "Success"])

    result = modbus_service._retry_operation(operation)
    assert result == "Success"
    assert operation.call_count == 3
