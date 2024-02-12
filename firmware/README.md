# Open Dynamic Clamp Firmware

Firmware code and Hardware schematics

## Quick Start

First install [PlatformIO](https://platformio.org/)

```shell
# ensure code builds
$ make build
```

## Upload Firmware

Connect your device. Compatible hardware is required.

PlatformIO will attempt to auto-discover the correct com port.

```shell
$ make upload
```

## Tests

Run unit tests.

```shell
$ make test
```