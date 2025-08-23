# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [1.3.4](https://gitlab.com/adm.standev/cookiecutter-python-template/compare/v1.3.3...v1.3.4) (2025-08-23)

### [1.3.3](https://gitlab.com/adm.standev/cookiecutter-python-template/compare/v1.3.2...v1.3.3) (2025-08-23)

### [1.3.2](https://gitlab.com/adm.standev/cookiecutter-python-template/compare/v1.3.1...v1.3.2) (2025-08-23)

### [1.3.1](https://gitlab.com/adm.standev/cookiecutter-python-template/compare/v1.0.1...v1.3.1) (2025-08-23)


### Bug Fixes

* CI pipeline for versioning and dependency handling ([9415bc9](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/9415bc9644b5b0c5b80b47e8405ecea0dc9b48bf))
* **ci:** implement robust version tag handling system ([1a7e8c5](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/1a7e8c5df0269214e8c95a5cca3b9041ccf03efe))
* **ci:** Improve versioning fallback in GitLab CI pipeline ([10c6b78](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/10c6b785ecfb7ea694e2079bcc55845cae06387c))
* **ci:** install jq explicitly and translate comments to English ([5871943](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/5871943f38121e8d9cd5cc693d06a03879733796))
* **ci:** Set project version to 1.0.0 and update dependencies ([34a9394](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/34a93949cd0756a95cbf846f683c0c0b9c7b6792))
* **ci:** Update GitLab CI versioning process and streamline steps ([d800dcd](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/d800dcdc66491bee4746c65d1d16dcba0109931b))
* **ci:** Update GitLab CI versioning process and streamline steps ([8a9e7b1](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/8a9e7b1eadf1cc1f248f469a2daf4f73ecdd4c56))
* force version increment ([861778f](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/861778f58349827d5fab3e65085bc9725be5f878))
* Handle existing version tags in GitLab CI release process ([17b9b57](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/17b9b57672215857154b234e339931b54147f44b))

### 1.0.1 (2025-08-23)


### Features

* Add versioning and release stages to CI pipeline ([2ea751f](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/2ea751fc01c779b7543d88f1bd672c875af7aeff))
* test husky integration and hooks ([9d6d358](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/9d6d3586e5e7e1ce564fdd679358662dbd7e89be))


### Bug Fixes

* **ci:** clean up version conflicts and regenerate package-lock.json" ([75d8a69](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/75d8a693a154b8f425a0c38b70e8ed70cc6f026f))
* **ci:** configure git user and email to fix author identity error in generate_changelog job ([9ef94bf](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/9ef94bf94af040ba3e886e8b8fa0ad20fcb375d2))
* **ci:** configure github remote and SSH key for git push ([87a5e37](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/87a5e3707931f4b5cbb9b4d67e3e46b0d049622a))
* **ci:** handle detached HEAD state and branch names in pipeline ([2abd8bc](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/2abd8bc1fd7ac32309a618f4da3add468b32347d))
* **ci:** improve version validation in generate_changelog ([689262e](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/689262e2ff01f8e8954667446188f2b9768a5003))
* **ci:** install jq to fix missing command in generate_changelog job ([ac40758](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/ac40758a88c194fe2931150546d4344717e0ad2c))
* **ci:** Refactor CI pipeline by removing redundant comments ([87c5613](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/87c561389e71609b55425c6619744d8b55e30e0d))
* **ci:** Refactor GitLab CI to improve versioning and release validation ([df724b4](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/df724b4ed4f80026f5fe06df40b9adbbfb346f3e))
* **ci:** Remove CHANGELOG.md and reset package version to 1.0.0 ([25ab4c2](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/25ab4c2fb26d81d65ba09d5441dbf7bc328ac635))
* **ci:** remove package-lock.json and generation to create version 1.0.0 ([19c855e](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/19c855e705997607ca578ad59b89277b8c67ef61))
* **ci:** resolve `git push both` remote issue in pipeline ([55ed999](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/55ed9997807828f39b2e83ee0e4dbd511eb08603))
* **ci:** resolve branch conflict during checkout in CI ([46a76c5](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/46a76c505078086468ceb7bfc431638b5d662b6b))
* **ci:** resolve Git configuration issue in generate_changelog stage ([0a4fcdb](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/0a4fcdb3a883790728345f6963d78946551ae60f))
* **ci:** resolve SSH key compatibility issue for GitLab deploy keys ([a63ff64](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/a63ff6457b2f7a3fa1743e224a678c28c2bdbbbc))
* **ci:** resolve syntax error in branch checkout script ([d0909ed](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/d0909edc29cfb6c5e85149ea7d535ccf30178ce7))
* **ci:** set Git remote URL to use SSH for proper push permissions ([740521c](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/740521cf7f4e7b3cf0d3b29645ac18e91219bd54))
* **ci:** Set version to 1.0.0 in package.json ([80a7f3d](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/80a7f3dc21acf36284f94e8c8f2130bc791ce18f))
* **ci:** Set version to 1.0.0 in package.json ([857bdd5](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/857bdd55edd3e8b0ba8e4929545afa18cbb250bc))
* **ci:** update release version ([6940c2d](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/6940c2d0ebb7d132ae6f663fcad6e7c538b8e021))
* corrections for GitLab CI branch support ([78aeb24](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/78aeb243441985bdffe7d2f77828c650ade29c87))
* corrections for GitLab CI branch support ([d0179a1](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/d0179a1f2d2489542fb0151d729f4e9ec4c3b25a))
* set version in package-lock.json to match package.json ([381af89](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/381af894ae7176d6d87f21aa0a272a08d4399ab9))
* set version in package-lock.json to match package.json ([c4a8c16](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/c4a8c165e7f1ad2f0468e150db1390d86e98ea93))

## 1.0.0 (2025-08-23)


### Features

* Add versioning and release stages to CI pipeline ([2ea751f](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/2ea751fc01c779b7543d88f1bd672c875af7aeff))
* test husky integration and hooks ([9d6d358](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/9d6d3586e5e7e1ce564fdd679358662dbd7e89be))


### Bug Fixes

* **ci:** configure github remote and SSH key for git push ([87a5e37](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/87a5e3707931f4b5cbb9b4d67e3e46b0d049622a))
* **ci:** handle detached HEAD state and branch names in pipeline ([2abd8bc](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/2abd8bc1fd7ac32309a618f4da3add468b32347d))
* **ci:** Remove CHANGELOG.md and reset package version to 1.0.0 ([25ab4c2](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/25ab4c2fb26d81d65ba09d5441dbf7bc328ac635))
* **ci:** resolve `git push both` remote issue in pipeline ([55ed999](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/55ed9997807828f39b2e83ee0e4dbd511eb08603))
* **ci:** resolve branch conflict during checkout in CI ([46a76c5](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/46a76c505078086468ceb7bfc431638b5d662b6b))
* **ci:** resolve Git configuration issue in generate_changelog stage ([0a4fcdb](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/0a4fcdb3a883790728345f6963d78946551ae60f))
* **ci:** resolve SSH key compatibility issue for GitLab deploy keys ([a63ff64](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/a63ff6457b2f7a3fa1743e224a678c28c2bdbbbc))
* **ci:** resolve syntax error in branch checkout script ([d0909ed](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/d0909edc29cfb6c5e85149ea7d535ccf30178ce7))
* **ci:** set Git remote URL to use SSH for proper push permissions ([740521c](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/740521cf7f4e7b3cf0d3b29645ac18e91219bd54))
* corrections for GitLab CI branch support ([78aeb24](https://gitlab.com/adm.standev/cookiecutter-python-template/commit/78aeb243441985bdffe7d2f77828c650ade29c87))
