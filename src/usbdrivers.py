import struct
import sys

if len(sys.argv) != 2:
    print("Usage: python3 usbDriver <EventNumber>")
    sys.exit(1)

event_num = sys.argv[1]

event_file = f'/dev/input/event{event_num}'

key_map = {
    2: '1', 3: '2', 4: '3', 5: '4', 6: '5', 7: '6', 8: '7', 9: '8', 10: '9', 11: '0',
    12: "'", 13: '¡', 16: 'Q', 17: 'W', 18: 'E', 19: 'R', 20: 'T', 
    21: 'Y', 22: 'U', 23: 'I', 24: 'O', 25: 'P', 26: '`', 27: '+', 
    30: 'A', 31: 'S', 32: 'D', 33: 'F', 34: 'G', 35: 'H', 36: 'J', 37: 'K', 38: 'L', 
    39: 'Ñ', 40: '´', 41: 'Ç', 43: '<', 44: 'Z', 45: 'X', 46: 'C', 47: 'V', 48: 'B', 
    49: 'N', 50: 'M', 51: ',', 52: '.', 53: '-', 57: ' '
}

buffer = []

with open(event_file, 'rb') as f:
    while True:
        event = f.read(24)
        if len(event) < 24:
            break

        (sec, usec, type, code, value) = struct.unpack('llHHI', event)

        if type == 1 and value == 1:
            if code == 28:
                sys.stdout.write("".join(buffer) + "\n")
                sys.stdout.flush()
                buffer = []
            else:
                char = key_map.get(code, '')
                if char:
                    buffer.append(char)
