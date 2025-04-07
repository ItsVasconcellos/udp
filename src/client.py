import socket
import struct

def checksum(data):
    """Compute a simple checksum of the data."""
    if len(data) % 2:
        data += b'\x00'
    s = sum(struct.unpack("!%dH" % (len(data) // 2), data))
    s = (s >> 16) + (s & 0xffff)
    s += (s >> 16)
    return ~s & 0xffff

def create_packet(src_port, dst_port, data):
    src_port = src_port or 0  # Optional field
    length = 8 + len(data)  # header (8 bytes) + data
    pseudo_header = struct.pack("!HHHH", src_port, dst_port, length, 0)
    chksum = checksum(pseudo_header + data)
    header = struct.pack("!HHHH", src_port, dst_port, length, chksum)
    return header + data

def main():
    dst_ip = "127.0.0.1"
    dst_port = 9999
    src_port = 12345  # Optional, set to 0 if unused

    data = b"Hello from client!"
    packet = create_packet(src_port, dst_port, data)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(packet, (dst_ip, dst_port))
    print(f"Sent packet to {dst_ip}:{dst_port}")

if __name__ == "__main__":
    main()
