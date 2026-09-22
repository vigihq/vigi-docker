# CLAUDE.md — vigi-docker

The container image. It runs Vigilance in a container.

Remotes: `origin` GitHub `git@github-personal:vigihq/vigi-docker.git`, public. `bb`
is a Bitbucket mirror, kept in sync.

## Layout

- `Dockerfile` — the image.
- `verify.py` — checks the built image.
- `.github/workflows/publish.yml` — builds and publishes the image.

## Writing

Plain English, ASD-STE100. Comments say why, not what.
