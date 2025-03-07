# Changelog

## [1.12.1](https://github.com/googleapis/google-cloud-python/compare/google-cloud-recaptcha-enterprise-v1.12.0...google-cloud-recaptcha-enterprise-v1.12.1) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11448](https://github.com/googleapis/google-cloud-python/issues/11448)) ([4d2c35a](https://github.com/googleapis/google-cloud-python/commit/4d2c35a1cd0b68b6d481d5611ff820451273e859))

## [1.12.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.11.1...v1.12.0) (2023-03-23)


### Features

* Add reCAPTCHA Enterprise Fraud Prevention API ([#350](https://github.com/googleapis/python-recaptcha-enterprise/issues/350)) ([5f841d7](https://github.com/googleapis/python-recaptcha-enterprise/commit/5f841d782c6e5ef3f4e5f4a9fa36a96d13e5849a))


### Documentation

* Fix formatting of request arg in docstring ([#352](https://github.com/googleapis/python-recaptcha-enterprise/issues/352)) ([a0ab5c3](https://github.com/googleapis/python-recaptcha-enterprise/commit/a0ab5c3abcd70aff6c1cc220fbb6afc14a5de436))

## [1.11.1](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.11.0...v1.11.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([54613d7](https://github.com/googleapis/python-recaptcha-enterprise/commit/54613d74af6c1cc95cad33465309fc0ef66402b8))


### Documentation

* Add documentation for enums ([54613d7](https://github.com/googleapis/python-recaptcha-enterprise/commit/54613d74af6c1cc95cad33465309fc0ef66402b8))

## [1.11.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.10.0...v1.11.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#330](https://github.com/googleapis/python-recaptcha-enterprise/issues/330)) ([ed41bb8](https://github.com/googleapis/python-recaptcha-enterprise/commit/ed41bb8f8ea270827a7c4255915492e5b462eb89))

## [1.10.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.9.0...v1.10.0) (2022-12-14)


### Features

* Add account_verification field to Assessment for MFA ([2e8b6f2](https://github.com/googleapis/python-recaptcha-enterprise/commit/2e8b6f2ee3cf082f89c5f05f5945f262871f8e48))
* Add support for `google.cloud.recaptchaenterprise.__version__` ([faccae1](https://github.com/googleapis/python-recaptcha-enterprise/commit/faccae1397d5face106d7b5cbb02fcdc6af4e572))
* Add typing to proto.Message based class attributes ([faccae1](https://github.com/googleapis/python-recaptcha-enterprise/commit/faccae1397d5face106d7b5cbb02fcdc6af4e572))


### Bug Fixes

* Add dict typing for client_options ([faccae1](https://github.com/googleapis/python-recaptcha-enterprise/commit/faccae1397d5face106d7b5cbb02fcdc6af4e572))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([2e8b6f2](https://github.com/googleapis/python-recaptcha-enterprise/commit/2e8b6f2ee3cf082f89c5f05f5945f262871f8e48))
* Drop usage of pkg_resources ([2e8b6f2](https://github.com/googleapis/python-recaptcha-enterprise/commit/2e8b6f2ee3cf082f89c5f05f5945f262871f8e48))
* Fix timeout default values ([2e8b6f2](https://github.com/googleapis/python-recaptcha-enterprise/commit/2e8b6f2ee3cf082f89c5f05f5945f262871f8e48))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([faccae1](https://github.com/googleapis/python-recaptcha-enterprise/commit/faccae1397d5face106d7b5cbb02fcdc6af4e572))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([2e8b6f2](https://github.com/googleapis/python-recaptcha-enterprise/commit/2e8b6f2ee3cf082f89c5f05f5945f262871f8e48))

## [1.9.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.8.3...v1.9.0) (2022-10-26)


### Features

* add annotation reasons REFUND, REFUND_FRAUD, TRANSACTION_ACCEPTED, TRANSACTION_DECLINED and SOCIAL_SPAM ([1d254d0](https://github.com/googleapis/python-recaptcha-enterprise/commit/1d254d0f4b2aab473b41505a0c31d8a46469a8e4))
* Add RetrieveLegacySecretKey method ([#311](https://github.com/googleapis/python-recaptcha-enterprise/issues/311)) ([1d254d0](https://github.com/googleapis/python-recaptcha-enterprise/commit/1d254d0f4b2aab473b41505a0c31d8a46469a8e4))

## [1.8.3](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.8.2...v1.8.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#308](https://github.com/googleapis/python-recaptcha-enterprise/issues/308)) ([c772e63](https://github.com/googleapis/python-recaptcha-enterprise/commit/c772e63fde35b93e73da67fde3d311e91569185c))

## [1.8.2](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.8.1...v1.8.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf &gt;= 3.20.2 ([#304](https://github.com/googleapis/python-recaptcha-enterprise/issues/304)) ([20ce864](https://github.com/googleapis/python-recaptcha-enterprise/commit/20ce864c6f65fca9f5c267d8ba8c9cdf1fc35cff))

## [1.8.1](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.8.0...v1.8.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#282](https://github.com/googleapis/python-recaptcha-enterprise/issues/282)) ([0499b5a](https://github.com/googleapis/python-recaptcha-enterprise/commit/0499b5a8ba88c373576b8fd673e3146a148ce51a))
* **deps:** require proto-plus >= 1.22.0 ([0499b5a](https://github.com/googleapis/python-recaptcha-enterprise/commit/0499b5a8ba88c373576b8fd673e3146a148ce51a))

## [1.8.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.7.1...v1.8.0) (2022-07-14)


### Features

* add audience parameter ([b833a31](https://github.com/googleapis/python-recaptcha-enterprise/commit/b833a318dfa71cd6a941b35ad8e95d903fa3de45))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#271](https://github.com/googleapis/python-recaptcha-enterprise/issues/271)) ([90479fc](https://github.com/googleapis/python-recaptcha-enterprise/commit/90479fca8fd002c3c6deae2aedbfff7943d14af3))
* require python 3.7+ ([#270](https://github.com/googleapis/python-recaptcha-enterprise/issues/270)) ([a370851](https://github.com/googleapis/python-recaptcha-enterprise/commit/a370851f88e72026ace4f13f87e19a642367a737))
* set the right field number for reCAPTCHA private password leak ([#266](https://github.com/googleapis/python-recaptcha-enterprise/issues/266)) ([6632149](https://github.com/googleapis/python-recaptcha-enterprise/commit/663214989b8d4cbf3f84e1b4e9b2c1856eefb59b))

## [1.7.1](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.7.0...v1.7.1) (2022-06-06)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#258](https://github.com/googleapis/python-recaptcha-enterprise/issues/258)) ([56b014a](https://github.com/googleapis/python-recaptcha-enterprise/commit/56b014a1781fdb1636797bca24af306fdcbd68b9))


### Documentation

* fix changelog header to consistent size ([#259](https://github.com/googleapis/python-recaptcha-enterprise/issues/259)) ([ad6402b](https://github.com/googleapis/python-recaptcha-enterprise/commit/ad6402b20391b1ae3e6a38343612260a51c8bfdc))

## [1.7.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.6.1...v1.7.0) (2022-05-19)


### Features

* Add support for Password Check through the private_password_leak_verification field in Assessment ([#233](https://github.com/googleapis/python-recaptcha-enterprise/issues/233)) ([38c7a96](https://github.com/googleapis/python-recaptcha-enterprise/commit/38c7a9685437b4503e16b0a7b3db0b8d3063709d))
* introduced WafSettings ([86096a4](https://github.com/googleapis/python-recaptcha-enterprise/commit/86096a4edab2304edd469cbd2049f466a009ef2f))


### Bug Fixes

* rename parent to project in SearchRelatedAccountGroupMembershipsRequest ([#227](https://github.com/googleapis/python-recaptcha-enterprise/issues/227)) ([86096a4](https://github.com/googleapis/python-recaptcha-enterprise/commit/86096a4edab2304edd469cbd2049f466a009ef2f))

## [1.6.1](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.6.0...v1.6.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#198](https://github.com/googleapis/python-recaptcha-enterprise/issues/198)) ([beee21d](https://github.com/googleapis/python-recaptcha-enterprise/commit/beee21d72f3d165d77d1d096e54e5b9c143f122d))
* **deps:** require proto-plus>=1.15.0 ([beee21d](https://github.com/googleapis/python-recaptcha-enterprise/commit/beee21d72f3d165d77d1d096e54e5b9c143f122d))

## [1.6.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.5.0...v1.6.0) (2022-02-28)


### Features

* add api key support ([#181](https://github.com/googleapis/python-recaptcha-enterprise/issues/181)) ([e9935ce](https://github.com/googleapis/python-recaptcha-enterprise/commit/e9935ce310b44d076e4590034b392f9681748f31))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([d5cc843](https://github.com/googleapis/python-recaptcha-enterprise/commit/d5cc843a1c6789c85751abe610b16fc6622029df))

## [1.5.0](https://github.com/googleapis/python-recaptcha-enterprise/compare/v1.4.1...v1.5.0) (2022-01-14)


### Features

* add new reCAPTCHA Enterprise fraud annotations ([#163](https://github.com/googleapis/python-recaptcha-enterprise/issues/163)) ([3c638f9](https://github.com/googleapis/python-recaptcha-enterprise/commit/3c638f97a966efdc6809016b9a50d63ffe4b380c))

## [1.4.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.4.0...v1.4.1) (2021-11-16)


### Documentation

* **samples:** added sample and tests for annotate assessment API ([#155](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/155)) ([353f0ff](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/353f0ffa27119bf3a8a8f6cddecb41d1ca8dbd31))

## [1.4.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.3.1...v1.4.0) (2021-11-03)


### Features

* add reCAPTCHA Enterprise account defender API methods ([#146](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/146)) ([8149df9](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/8149df9e3038bf02483fb2ee0c9dfc9d713a6152))


### Documentation

* **samples:** removed assessment name in create_assessment sample ([#147](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/147)) ([f11134d](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/f11134da5e9e9770b73dadd96c08ba69c99b968f))

## [1.3.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.3.0...v1.3.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([22ed89d](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/22ed89dcaa628790d09584b3bd20c35115647bb7))
* **deps:** require google-api-core >= 1.28.0 ([22ed89d](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/22ed89dcaa628790d09584b3bd20c35115647bb7))


### Documentation

* list oneofs in docstring ([22ed89d](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/22ed89dcaa628790d09584b3bd20c35115647bb7))

## [1.3.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.2.0...v1.3.0) (2021-10-14)


### Features

* add support for python 3.10 ([#137](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/137)) ([fda16a4](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/fda16a44a84b173a8866090021e03eef0cb82025))


### Documentation

* **samples:** add reCAPTCHA Enterprise code samples  ([#112](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/112)) ([879acf1](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/879acf12d24b5148e372f0f76a243ea0fc66286e))

## [1.2.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.1.2...v1.2.0) (2021-10-08)


### Features

* add context manager support in client ([#131](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/131)) ([69d2b34](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/69d2b347f9aab3f30a3b0265fc9dcd9a3926f62d))

## [1.1.2](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.1.1...v1.1.2) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([cab9a71](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/cab9a71083b2482396ecd53051bb694937c7fe7d))

## [1.1.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.1.0...v1.1.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([7d49e68](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/7d49e6830e0f914d8fb2f20961a3ae6953244ed4))

## [1.1.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v1.0.0...v1.1.0) (2021-09-16)


### Features

* add GetMetrics and MigrateKey methods to reCAPTCHA enterprise API ([#119](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/119)) ([6c8bf2f](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/6c8bf2f7f9fabb7fb23257fe5978ba59160d6875))

## [1.0.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.4.2...v1.0.0) (2021-08-03)


### Features

* bump release level to production/stable ([#105](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/105)) ([fab3e48](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/fab3e48b6ddc31bed65e9bedfd9f06aa33fd2c02))

## [0.4.2](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.4.1...v0.4.2) (2021-07-28)


### Bug Fixes

* enable self signed jwt for grpc ([#101](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/101)) ([2a9cba8](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/2a9cba89af89d76a1e9a4922e2901bd4847de949))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#97](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/97)) ([ffcc165](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/ffcc1651929337be437250e440b75548c453ced9))


### Miscellaneous Chores

* release as 0.4.2 ([#102](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/102)) ([ff137b0](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/ff137b00f5282dc061941b6645143db7c66a6718))

## [0.4.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.4.0...v0.4.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#96](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/96)) ([dafb540](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/dafb540844946190af288039b745f77ac08d90ab))

## [0.4.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.3.3...v0.4.0) (2021-07-12)


### Features

* add always_use_jwt_access ([#87](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/87)) ([d0851c8](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/d0851c8df866f4a5604523fcd23cfbba2a5fd51c))


### Bug Fixes

* disable always_use_jwt_access ([#91](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/91)) ([de8c214](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/de8c214bbbbe1aaf55ebabca35ab005540180be6))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/1127)) ([#82](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/82)) ([fd4b1b4](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/fd4b1b4af92ff9027675b7bd1b494870225eccaa)), closes [#1126](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/1126)

## [0.4.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.3.3...v0.4.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#87](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/87)) ([d0851c8](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/d0851c8df866f4a5604523fcd23cfbba2a5fd51c))


### Bug Fixes

* disable always_use_jwt_access ([#91](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/91)) ([de8c214](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/de8c214bbbbe1aaf55ebabca35ab005540180be6))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/1127)) ([#82](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/82)) ([fd4b1b4](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/fd4b1b4af92ff9027675b7bd1b494870225eccaa)), closes [#1126](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/1126)

## [0.3.3](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.3.2...v0.3.3) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#79](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/79)) ([1d39b4b](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/1d39b4bbf30aadafaa407c4911e2368d9330ccef)), closes [#74](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/74)

## [0.3.2](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.3.1...v0.3.2) (2021-06-09)


### Documentation

* fix package name ([#78](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/78)) ([6de2981](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/6de298111482e205d90895674fd19db401df70ea))
* fix package name and package info in README ([#76](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/76)) ([0e719bb](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/0e719bb23c9680f46bf36ef2344a98eb73ac70dc))

## [0.3.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.3.0...v0.3.1) (2021-05-28)


### Bug Fixes

* **deps:** add packaging requirement ([#68](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/68)) ([176bbe9](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/176bbe954a38c0dbbe4669035bb4a807031c7a9d))

## [0.3.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.2.1...v0.3.0) (2021-02-08)


### Features

* add async client, add common resource helpers, add from_service_account_info factory ([#30](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/30)) ([7f9db72](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/7f9db7203246c0911ad1760ffc8e56cc61acd224))

## [0.2.1](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.2.0...v0.2.1) (2020-06-01)


### Bug Fixes

* corrects link to client library documentation ([#13](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/13)) ([1ea5be7](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/1ea5be722147a7386afa5320eef7266b3eb9d984)), closes [#12](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/12)

## [0.2.0](https://www.github.com/googleapis/python-recaptcha-enterprise/compare/v0.1.0...v0.2.0) (2020-05-28)


### Features

* add mtls support and resource path parse methods (via synth) ([#4](https://www.github.com/googleapis/python-recaptcha-enterprise/issues/4)) ([c20fa3f](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/c20fa3f09365b2d1bc172df35c06110c989f688e))

## 0.1.0 (2020-04-20)


### Features

* generate v1 ([a7da83d](https://www.github.com/googleapis/python-recaptcha-enterprise/commit/a7da83ddb1d622584fb442d38c28419e7708b946))
