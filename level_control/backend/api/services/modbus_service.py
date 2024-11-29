# api/services/modbus_service.py

import os
import time
import logging
# from dotenv import load_dotenv
from pymodbus.client import AsyncModbusTcpClient

class ModbusService:
    """
    A robust service for managing Modbus TCP communication with a PLC.
    """

    def __init__(self, host: str, port: int = 502, slave_id: int = 1, timeout: int = 5, retries: int = 3, delay: int = 2):
        """
        Initialize the ModbusService.

        :param host: The IP address of the PLC.
        :param port: The Modbus TCP port (default: 502).
        :param slave_id: The slave ID of the PLC (default: 1).
        :param timeout: Timeout for Modbus operations in seconds (default: 5).
        :param retries: Number of retries for transient errors (default: 3).
        :param delay: Delay between retries in seconds (default: 2).
        """
        self.host = host
        self.port = port
        self.slave_id = slave_id
        self.timeout = timeout
        self.retries = retries
        self.delay = delay
        self.client = None
        self.logger = self._setup_logging()

    def _setup_logging(self):
        """
        Configure logging for the ModbusService.

        :return: Logger instance.
        """
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(message)s",
            level=logging.INFO
        )
        return logging.getLogger(self.__class__.__name__)

    def connect(self):
        """
        Establish a connection to the PLC.

        :raises ConnectionError: If the connection fails.
        """
        try:
            self.client = ModbusTcpClient(
                self.host, port=self.port, timeout=self.timeout)
            if not self.client.connect():
                raise ConnectionError(
                    f"Failed to connect to PLC at {self.host}:{self.port}.")
            self.logger.info(f"Connected to PLC at {self.host}:{self.port}.")
        except Exception as e:
            self.logger.error(f"Error while connecting to PLC: {e}")
            raise

    def disconnect(self):
        """
        Close the connection to the PLC.
        """
        try:
            if self.client:
                self.client.close()
                self.logger.info("Disconnected from PLC.")
        except Exception as e:
            self.logger.error(f"Error while disconnecting from PLC: {e}")
            raise

    def _retry_operation(self, operation, *args, **kwargs):
        """
        Retry a Modbus operation in case of transient errors.

        :param operation: The operation (method) to retry.
        :param args: Arguments for the operation.
        :param kwargs: Keyword arguments for the operation.
        :return: Result of the operation.
        :raises Exception: If all retries fail.
        """
        for attempt in range(self.retries):
            try:
                return operation(*args, **kwargs)
            except Exception as e:
                if attempt < self.retries - 1:
                    self.logger.warning(
                        f"Operation failed, retrying in {self.delay} seconds... (Attempt {attempt + 1})")
                    time.sleep(self.delay)
                else:
                    self.logger.error(f"All retries failed: {e}")
                    raise

    def read_holding_registers(self, address: int, count: int):
        """
        Read holding registers from the PLC.

        :param address: The starting address of the registers to read.
        :param count: The number of registers to read.
        :return: List of register values.
        :raises Exception: If the read operation fails.
        """
        return self._retry_operation(self._read_holding_registers, address, count)

    def _read_holding_registers(self, address: int, count: int):
        """
        Internal method to read holding registers.

        :param address: The starting address of the registers to read.
        :param count: The number of registers to read.
        :return: List of register values.
        :raises Exception: If the read operation fails.
        """
        try:
            response = self.client.read_holding_registers(
                address=address, count=count, unit=self.slave_id)
            if response.isError():
                raise Exception(
                    f"Failed to read holding registers at address {address}.")
            self.logger.info(
                f"Read holding registers at address {address}: {response.registers}")
            return response.registers
        except Exception as e:
            self.logger.error(f"Error reading holding registers: {e}")
            raise

    def write_register(self, address: int, value: int):
        """
        Write a value to a single register.

        :param address: The address of the register to write.
        :param value: The value to write.
        :raises Exception: If the write operation fails.
        """
        self._retry_operation(self._write_register, address, value)

    def _write_register(self, address: int, value: int):
        """
        Internal method to write a value to a single register.

        :param address: The address of the register to write.
        :param value: The value to write.
        :raises Exception: If the write operation fails.
        """
        try:
            response = self.client.write_register(
                address=address, value=value, unit=self.slave_id)
            if response.isError():
                raise Exception(
                    f"Failed to write value {value} to register at address {address}.")
            self.logger.info(
                f"Successfully wrote value {value} to register at address {address}.")
        except Exception as e:
            self.logger.error(f"Error writing to register: {e}")
            raise

    def is_connected(self):
        """
        Check if the client is connected to the PLC.

        :return: True if connected, False otherwise.
        """
        return self.client.is_socket_open() if self.client else False


# # Load environment variables (e.g., from a .env file)
# load_dotenv()

# # Example configuration from environment variables
# HOST = os.getenv("MODBUS_HOST", "192.168.0.10")
# PORT = int(os.getenv("MODBUS_PORT", 502))
# SLAVE_ID = int(os.getenv("MODBUS_SLAVE_ID", 1))
# TIMEOUT = int(os.getenv("MODBUS_TIMEOUT", 5))
# RETRIES = int(os.getenv("MODBUS_RETRIES", 3))
# DELAY = int(os.getenv("MODBUS_RETRY_DELAY", 2))

# # Instantiate the ModbusService
# modbus_service = ModbusService(host=HOST, port=PORT, slave_id=SLAVE_ID, timeout=TIMEOUT, retries=RETRIES, delay=DELAY)
