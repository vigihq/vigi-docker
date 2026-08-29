# Vigilance Docker image

```sh
docker run --rm -v "$PWD:/scan" ghcr.io/fathermarz/vigi:latest /scan
```

The image carries the free `vigi` binary on a distroless base. Activate the free
tier inside the container, or pass a Pro license. Vigilance is commercial
software from Modul4r Solutions. See <https://vigihq.com>.
