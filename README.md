# Open Dynamic Clamp Firmware

Firmware code and Hardware schematics

## References

- Niraj Desai - [dynamic_clamp](https://github.com/nsdesai/dynamic_clamp)
- Christian Rickert - [dyClamp](https://github.com/christianrickert/dyClamp/)
- Christian Rickert - [pyClamp](https://github.com/christianrickert/pyClamp)

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