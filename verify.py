#!/usr/bin/env python3
# Match a downloaded binary against the sha256 in the signed release manifest.
# Usage: verify.py <binary> <manifest.json> <asset-name>
import json, base64, hashlib, sys

binary, manifest, asset = sys.argv[1], sys.argv[2], sys.argv[3]
env = json.load(open(manifest))
payload = json.loads(base64.b64decode(env["payload"]))
want = next(a["sha256"] for a in payload["assets"]
            if a["name"] == asset and a["tier"] == "free")
got = hashlib.sha256(open(binary, "rb").read()).hexdigest()
if want != got:
    sys.exit(f"hash mismatch for {asset}: want {want}, got {got}")
print(payload["version"])
