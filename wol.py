import socket
import struct

def create_wol_packet(mac_address):
  # MAC adresini 6 tane özel olmayan sayıya bölün
  split_mac = [int(x, 16) for x in mac_address.split(":")]

  # WOL paketini oluşturun
  data = b'\xff' * 6 + struct.pack('!6B', *split_mac) * 16
  return data

def send_wol_packet(data, broadcast_address):
  # SOCK_DGRAM ağ tipini kullanarak bir datagram socket'i oluşturun
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

  # WOL paketini gönderin
  sock.sendto(data, (broadcast_address, 9))

# WOL paketini oluşturun
mac_address = "6C:4B:90:B1:F0:E0"
data = create_wol_packet(mac_address)

# WOL paketini gönderin
broadcast_address = "192.168.100.55"
send_wol_packet(data, broadcast_address)
