import network
import socket
from machine import Pin, PWM
from utime import sleep, sleep_ms

SSID = "ITEK 2nd"
PASSWORD = "2nd_Semester_E24a"
UDP_PORT = 5005

# LED Setup for direction indicators
led_right = Pin(0, Pin.OUT)
led_forward = Pin(1, Pin.OUT)
led_left = Pin(2, Pin.OUT)
led_backward = Pin(3, Pin.OUT)
led_forward_right = Pin(4, Pin.OUT)
led_forward_left = Pin(5, Pin.OUT)

# Onboard LED
led = Pin("LED", Pin.OUT)


def blink_connecting():
    for _ in range(10):  # Fast blinking while attempting connection
        led.value(1)
        sleep_ms(100)
        led.value(0)
        sleep_ms(100)


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.ifconfig(('10.120.0.63', '255.255.255.0', '10.120.0.1', '1.1.1.1'))

    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(SSID, PASSWORD)

        # Start blinking while trying to connect
        connection_attempts = 0
        while not wlan.isconnected() and connection_attempts < 10:
            blink_connecting()
            connection_attempts += 1

        if wlan.isconnected():
            print('Network config:', wlan.ifconfig())
            led.value(1)  # Solid LED on successful connection
        else:
            print('Connection failed')
            led.value(0)  # LED off on connection failure
            return None
    return wlan


def turn_off_all_leds():
    led_right.value(0)
    led_forward.value(0)
    led_left.value(0)
    led_backward.value(0)
    led_forward_right.value(0)
    led_forward_left.value(0)


def handle_direction(direction):
    turn_off_all_leds()

    # Map directions to LEDs
    direction_map = {
        "RIGHT": led_right,
        "FORWARD": led_forward,
        "LEFT": led_left,
        "BACKWARD": led_backward,
        "FORWARD_RIGHT": led_forward_right,
        "FORWARD_LEFT": led_forward_left,
        "BACKWARD_RIGHT": led_right,
        "BACKWARD_LEFT": led_left,
        "STOP": None
    }

    if direction in direction_map and direction_map[direction]:
        direction_map[direction].value(1)


def main():
    if not connect_wifi():
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', UDP_PORT))
    print(f"UDP server listening on port {UDP_PORT}...")

    while True:
        try:
            data, addr = sock.recvfrom(1024)
            direction = data.decode().strip()
            print(f"Received from {addr}: {direction}")

            handle_direction(direction)

            # Send confirmation back to controller
            response = f"OK: Direction {direction}"
            sock.sendto(response.encode(), addr)

        except Exception as e:
            print(f"Error: {e}")
            sleep(1)


if __name__ == "__main__":
    main()

PICO_IP = '10.120.0.63'  # This matches the static IP we set on the Pico


def send_direction(direction):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(direction.encode(), (PICO_IP, UDP_PORT))
    try:
        sock.settimeout(1.0)  # Wait up to 1 second for response
        response, addr = sock.recvfrom(1024)
        print(f"Received response: {response.decode()}")
    except socket.timeout:
        print("No response from Pico - check connection")
    finally:
        sock.close()
