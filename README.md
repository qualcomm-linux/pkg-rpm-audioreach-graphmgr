<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# pkg-rpm-audioreach-graphmgr

RPM packaging for
[audioreach-graphmgr](https://github.com/AudioReach/audioreach-graphmgr)
on CentOS Stream 10 (aarch64).

audioreach-graphmgr provides the AudioReach Audio Graph Manager (AGM) for
Qualcomm platforms. It manages audio sessions, devices, and metadata for the
AudioReach framework, and provides the AGM service library, sound card parser,
and tinyalsa PCM/mixer plugins. The package is maintained on the CentOS
Stream 10 (`c10s`) branch and uses the shared GitHub Actions build and release
workflow.

## CI Workflows

| Workflow | Trigger | Purpose |
|---|---|---|
| [`build-on-pr.yml`](.github/workflows/build-on-pr.yml) | Pull request | Build the RPM(s) so reviewers confirm the package still builds. Read-only — never publishes. |
| [`pkg-release.yml`](.github/workflows/pkg-release.yml) | Manual (`workflow_dispatch`) | Build **and** publish the RPM(s) to Artifactory, behind an approval gate. |

The GitHub Actions workflows use the shared
[`qcom-rpm-utils`](https://github.com/qualcomm-linux/qcom-rpm-utils) build
environment and run `rpmbuild` inside the prebuilt `rpm-builder` container
image for the runner's host architecture.

---

## Repository Layout

The `c10s` branch contains the RPM packaging files:

| File | Purpose |
|---|---|
| `audioreach-graphmgr.spec` | Builds the AGM runtime libraries and `-devel` subpackage. |
| `sources` | SHA-512 checksum for the upstream source archive. |
| `README.md` | Package and repository documentation. |
| `LICENSE.txt` | License for the RPM packaging repository. |

The source archive is not committed to this repository. The spec file's
`Source0` points to the upstream release, and the checksum in `sources` is
verified before the RPM is built.

---

## Packages

- `audioreach-graphmgr`: AGM service library, sound card parser, and tinyalsa
  PCM/mixer plugins.
- `audioreach-graphmgr-devel`: Headers and pkg-config files for building
  applications that use the AudioReach Graph Manager libraries.

---

## Updating the package version

This is the everyday workflow — **two edits on `c10s`, no tarball in git**:

1. Bump `Version:` in the spec (and the `Source0:` URL if its path changed).
2. Recompute the checksum for the new tarball:
   ```bash
   sha512sum --tag audioreach-graphmgr-<newversion>.tar.gz > sources
   ```
3. Commit the spec + `sources`, open a PR (build verifies it), merge, then run
   **Release**. The first release fetches the new upstream tarball, verifies it,
   and caches it back to Artifactory automatically.

## License

This project is licensed under the BSD 3-Clause License. See [LICENSE.txt](LICENSE.txt) for the complete license text.

The upstream audioreach-graphmgr source is licensed separately under
`BSD-3-Clause-Clear`, as declared by `audioreach-graphmgr.spec`.
