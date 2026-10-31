# Vigilance Docker image

> **Vigilance 1.0 is retired.** It gets no more updates. Vigilance 2.0 installs from the join link your company gets at https://vigihq.com/watch.

```sh
docker run --rm -v "$PWD:/scan" ghcr.io/vigihq/vigi:latest /scan
```

The image carries the free `vigi` binary on a distroless base. Activate the free
tier inside the container, or pass a Pro license. Vigilance is commercial
software from Modul4r Solutions. See <https://vigihq.com>.
