import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

print([port.name for port in ports])