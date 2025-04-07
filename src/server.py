import socket
import struct

def checksum(data):
    """Compute checksum (same logic as in client)."""
    if len(data) % 2:
        data += b'\x00'
    s = sum(struct.unpack("!%dH" % (len(data) // 2), data))
    s = (s >> 16) + (s & 0xffff)
    s += (s >> 16)
    return ~s & 0xffff

def parse_packet(packet):
    if len(packet) < 8:
        raise ValueError("Packet too short to contain a UDP header")

    header = packet[:8]
    data = packet[8:]
    src_port, dst_port, length, received_checksum = struct.unpack("!HHHH", header)
    computed_checksum = checksum(header[:6] + b'\x00\x00' + data)

    valid = received_checksum == computed_checksum

    return {
        "source_port": src_port,
        "destination_port": dst_port,
        "length": length,
        "checksum": received_checksum,
        "valid_checksum": valid,
        "data": data
    }

def main():
    bind_ip = "127.0.0.1"
    bind_port = 9999

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((bind_ip, bind_port))
    print(f"Listening on {bind_ip}:{bind_port}")

    while True:
        packet, addr = sock.recvfrom(65535)
        parsed = parse_packet(packet)

        print(f"\nReceived packet from {addr}")
        print(f"Source Port: {parsed['source_port']}")
        print(f"Destination Port: {parsed['destination_port']}")
        print(f"Length: {parsed['length']}")
        print(f"Checksum: {parsed['checksum']} (Valid: {parsed['valid_checksum']})")
        print(f"Data: {parsed['data'].decode(errors='ignore')}")

if __name__ == "__main__":
    main()
# This server listens for UDP packets, parses them, and prints their details.