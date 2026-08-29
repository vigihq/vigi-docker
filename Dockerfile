# The scan binary on a minimal base that still carries CA certificates, so the
# free tier can reach the registry. Root by default, so activation can write to
# the root-owned state folder. Pro needs no network at all.
#
# Built for more than one CPU. buildx sets TARGETARCH per platform, and the
# matching binary is copied in.
FROM gcr.io/distroless/static-debian12
ARG TARGETARCH
COPY vigi-${TARGETARCH} /usr/local/bin/vigi
ENTRYPOINT ["/usr/local/bin/vigi"]
