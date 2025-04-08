# CHANGELOG


## v1.8.1 (2025-04-08)

### Bug Fixes

- **fathomnet-generate**: Use new DTO BaseModel syntax for model copy and JSON dump
  ([`8611d68`](https://github.com/fathomnet/fathomnet-py/commit/8611d68e8a8df66bf1ce1a429776e10f0e348dbc))

### Chores

- Add CITATION.cff
  ([`d4cc5a5`](https://github.com/fathomnet/fathomnet-py/commit/d4cc5a55881f35a1c4e0e8900f5d8f7d365b89f8))

### Testing

- Temporarily disable tests for broken endpoints
  ([`efdbede`](https://github.com/fathomnet/fathomnet-py/commit/efdbede410560ad068bffb5e611b1f482e9d94ad))


## v1.8.0 (2025-03-03)

### Bug Fixes

- Fix typing for Python 3.8, 3.9
  ([`bb29e5f`](https://github.com/fathomnet/fathomnet-py/commit/bb29e5f3bf892ddf993fee4679d6ab71d5437ef4))

### Chores

- Correct syntax for setting PATH in CI/CD workflow
  ([`a694975`](https://github.com/fathomnet/fathomnet-py/commit/a6949752624ae318b07c56a817948d556e9d7707))

### Features

- Migrate from fathomnet.org to database.fathomnet.org; rye -> uv; dataclasses_json -> pydantic
  ([`fc86d07`](https://github.com/fathomnet/fathomnet-py/commit/fc86d070cb6696fa8e86803c5c48fe951baa52e6))


## v1.7.1 (2024-11-11)

### Bug Fixes

- Remove debug print statements from find_by_display_name function, worms test
  ([`092d807`](https://github.com/fathomnet/fathomnet-py/commit/092d807b223d7c3c8718c7c40d42332a5577a6db))

### Chores

- Update CI/CD workflow to set PATH for Rye installation
  ([`6959642`](https://github.com/fathomnet/fathomnet-py/commit/6959642b5264ec8d60d97ad8140a19d078d60642))


## v1.7.0 (2024-11-04)

### Chores

- Add `docs` rye script for building docs
  ([`66e97f5`](https://github.com/fathomnet/fathomnet-py/commit/66e97f5485b64aed8e4c917a7de7591097f7e55a))

- Swap Poetry for Rye build system
  ([`e698cd6`](https://github.com/fathomnet/fathomnet-py/commit/e698cd67841e9cb0c63e0d90d57ee31dcfc4aa28))

### Code Style

- Apply ruff linting & formatting
  ([`1bdc3d8`](https://github.com/fathomnet/fathomnet-py/commit/1bdc3d81ec7134a0f05129bc5d642a4ddbb8eb48))

### Documentation

- Add CONTRIBUTING.md
  ([`befbcf0`](https://github.com/fathomnet/fathomnet-py/commit/befbcf0071ef6967729ca11d5233e404e0c601a1))

- Fix badge display in README.md
  ([`7c6dd4b`](https://github.com/fathomnet/fathomnet-py/commit/7c6dd4ba56358c25e99612bca0526bdfbd667cbb))

- Slight tweaks to README.md
  ([`0895d5c`](https://github.com/fathomnet/fathomnet-py/commit/0895d5c276fe00276ae4b5220401aaeb8257497a))

- Update README.md with badges
  ([`2fe5256`](https://github.com/fathomnet/fathomnet-py/commit/2fe52561d94172a345598aa6a925d33c6035a756))

### Features

- Add function to retrieve owner institution codes by image UUID
  ([`773290a`](https://github.com/fathomnet/fathomnet-py/commit/773290a46f93970371129bfc9c7596044f91814c))


## v1.6.1 (2024-08-01)

### Bug Fixes

- Fix bbox conversion to Pascal VOC to use 1-based pixel index
  ([`440afb0`](https://github.com/fathomnet/fathomnet-py/commit/440afb0f02ab5a88d3ea6827fb2b3d3e244f7653))


## v1.6.0 (2024-07-18)

### Features

- Allow a start page number in fathomnet.util.page
  ([`62ca914`](https://github.com/fathomnet/fathomnet-py/commit/62ca91421765328c7c47c63962e144ce074463b1))


## v1.5.1 (2024-07-16)

### Bug Fixes

- Fix typo in -f option for fathomnet-generate
  ([`c304ce1`](https://github.com/fathomnet/fathomnet-py/commit/c304ce1d165e1afe9cecce932dbcd3ebe82aea2b))


## v1.5.0 (2024-07-16)

### Bug Fixes

- Make TEST_X_API_KEY use an environment variable of the same name
  ([`22508cf`](https://github.com/fathomnet/fathomnet-py/commit/22508cf16695621183c0a5f5fe76d14ffaf48bae))

### Chores

- Add formatting/linting pre-commit setup
  ([`ca07b19`](https://github.com/fathomnet/fathomnet-py/commit/ca07b193aa8562161fd02375641ea050d7d632d7))

- Add Python 3.12 to CI pipeline targets
  ([`cf979cf`](https://github.com/fathomnet/fathomnet-py/commit/cf979cf18d5db307f6adea5d7b632045e1c6e353))

- Apply pre-commit hook on all files
  ([`0190345`](https://github.com/fathomnet/fathomnet-py/commit/01903453d9e16c7716d91e7aacf165857c982dbf))

### Documentation

- Fix broken readthedocs build #27
  ([`3154b79`](https://github.com/fathomnet/fathomnet-py/commit/3154b790399aa7ce6def6c00b639679f6ac3bdb9))

Install the current package (fathomnet-py) prior to building the Sphinx docs via RTD

- Move tutorial notebook into examples dir
  ([`c4db176`](https://github.com/fathomnet/fathomnet-py/commit/c4db176c211235a1ce7479dacba237c68c0da6fc))

- Switch order of imports/pip install in tutorial notebook
  ([`48afc49`](https://github.com/fathomnet/fathomnet-py/commit/48afc496c0792d662709b2b9c28826afb78914b7))

switched order of imports to avoid ipyleaflet error with fathomnet install and added explanation on
  running outside of colab. (#28)

### Features

- Add YOLO dataset generation to fathomnet-generate
  ([`1bacb1f`](https://github.com/fathomnet/fathomnet-py/commit/1bacb1fbbaf8802de23351fdaa9af7e8de6df73c))


## v1.4.0 (2024-04-09)

### Features

- Add accepted flag to `worms.get_descendants_names`
  ([`de0aec2`](https://github.com/fathomnet/fathomnet-py/commit/de0aec2e04915a922b7026189e7cfc0b55aabfd6))

Add support for worms-server 0.5.2


## v1.3.0 (2024-02-29)

### Features

- Support worms-server 0.5.1
  ([`f1989bc`](https://github.com/fathomnet/fathomnet-py/commit/f1989bcfea8225d38749241709b9c98a9e47bae0))

Add support for worms-server 0.5.1. This adds the `acceptedAphiaId` field to the `WormsNode` DTOs as
  well as a new endpoint for getting a `WormsNames` DTO by Aphia ID.


## v1.2.2 (2024-02-21)

### Bug Fixes

- Correct typo in WormsNode.aphiaId
  ([`5feeeb0`](https://github.com/fathomnet/fathomnet-py/commit/5feeeb0fa5fd95efd22fdc0e67e5dd69b9302408))

Fixes #25

### Chores

- Add missing v for ref spec
  ([`3212b13`](https://github.com/fathomnet/fathomnet-py/commit/3212b13afcb285bb7fea482c16150bbd1971cb4c))

### Documentation

- Add worms API module documentation
  ([`11c0112`](https://github.com/fathomnet/fathomnet-py/commit/11c0112e08afc4050bce8877cf43e1bb47419e63))


## v1.2.1 (2024-02-06)


## v1.2.0 (2024-02-06)

### Bug Fixes

- Make the linter happy
  ([`6cc52f6`](https://github.com/fathomnet/fathomnet-py/commit/6cc52f6b6abbd1cbe1b14a435d82a9acb91e4f58))

- Use worms API directly for fathomnet taxa provider
  ([`f887a95`](https://github.com/fathomnet/fathomnet-py/commit/f887a950cfe4741869b667410a1ceee9c92a11c9))

This is a temporary workaround for a bug in Micronaut that causes the fathomnet taxa provider to
  fail for large trees (e.g., Scleractinia).

### Chores

- Merge CI/CD workflows
  ([`8e0d760`](https://github.com/fathomnet/fathomnet-py/commit/8e0d76006cec956cab009bf330a068f6e7a6adf4))

- Use released ref for publish in CI/CD pipeline
  ([`d39c482`](https://github.com/fathomnet/fathomnet-py/commit/d39c4827ea612c6ea7e8b3eabfea4f08638c98e8))

### Documentation

- Add Sphinx RTD theme build requirement
  ([`fccd808`](https://github.com/fathomnet/fathomnet-py/commit/fccd8086997330059094baeadac5162b1d17a7e4))

- Add sphinx-rtd-theme as a dev dependency
  ([`9be9dee`](https://github.com/fathomnet/fathomnet-py/commit/9be9deeb42636a17f0d36d37100e5406dd0778f6))

- Update copyright year to 2024
  ([`1650bc5`](https://github.com/fathomnet/fathomnet-py/commit/1650bc5d836d80c6b6d8e2238e184834952cdf20))

- Update Python version and build configuration for readthedocs
  ([`ef96d8d`](https://github.com/fathomnet/fathomnet-py/commit/ef96d8d46cbf83c9c5d5d0eb03b8b927be487383))

### Features

- Add functions to call fast WoRMS API directly
  ([`21942b8`](https://github.com/fathomnet/fathomnet-py/commit/21942b837b817de9aea02d4abc399802aa55ce8f))


## v1.1.5 (2024-01-10)

### Bug Fixes

- Quote boundingboxes.audit_by_concepts URL fragment, add test case
  ([`5ea7b45`](https://github.com/fathomnet/fathomnet-py/commit/5ea7b459278c540a31fbe63e263f9208c234e123))

- Quote display/org names in users find functions
  ([`591e67a`](https://github.com/fathomnet/fathomnet-py/commit/591e67a3e43af9e15ca0a0140de465a1da8018f3))

- Quote observer name in boundingboxes.audit_by_observer
  ([`b94c87e`](https://github.com/fathomnet/fathomnet-py/commit/b94c87e9351fbde116dc8ef22c58867059999bec))

- Quote provider name and concept in taxa find functions, remove print from test
  ([`dde9eb5`](https://github.com/fathomnet/fathomnet-py/commit/dde9eb51a5da79a07a94fe5d93a7604681c035d6))

- Update activity find functions for new DTO
  ([`cdf5617`](https://github.com/fathomnet/fathomnet-py/commit/cdf56179cc802085ff1f8adbba2f717be550f08b))


## v1.1.4 (2024-01-09)

### Bug Fixes

- Quote concept in images.find_by_concept, add test
  ([`33aa430`](https://github.com/fathomnet/fathomnet-py/commit/33aa4301a30dd15f64aebfef57dd21914ed060e1))

### Documentation

- Fix broken tests badge
  ([`dbfbea8`](https://github.com/fathomnet/fathomnet-py/commit/dbfbea8ab261d285a691c6f92a740ce8ba893166))


## v1.1.3 (2023-09-13)

### Bug Fixes

- **api**: Improve client error exception
  ([`6b0b911`](https://github.com/fathomnet/fathomnet-py/commit/6b0b91110be90d7e41e7c2a8dab87cd29b331395))

Add the fathomnet.util.debug_format_response to the ValueError exception raised when a status code <
  500 and != 401 / 403 is returned. Fixes #16

### Documentation

- Add script documentation
  ([`1eadc8f`](https://github.com/fathomnet/fathomnet-py/commit/1eadc8ff627307fec7cefde19918da45c086195e))

Closes #5


## v1.1.2 (2023-09-12)

### Bug Fixes

- Add CD
  ([`8979d75`](https://github.com/fathomnet/fathomnet-py/commit/8979d75b049d39c673feb0d78153d4e5a4de11c5))

- Add condition to CD workflow
  ([`df3432d`](https://github.com/fathomnet/fathomnet-py/commit/df3432d1b5685414c64d6a8a21b020497d1b6313))


## v1.1.1 (2023-09-12)

### Bug Fixes

- Remove publish step from CI (for now)
  ([`3ba596b`](https://github.com/fathomnet/fathomnet-py/commit/3ba596b2b240ba841cecf98f20c74d30a5e386a5))

- Version in pyproject.toml
  ([`dd2d9a2`](https://github.com/fathomnet/fathomnet-py/commit/dd2d9a2d3e9a27610e17c119337e821fcea8bcbc))


## v1.1.0 (2023-09-12)

### Features

- Set up python-semantic-release
  ([`4019f18`](https://github.com/fathomnet/fathomnet-py/commit/4019f1811cabc207f5972eb39b8a9a7720345f95))


## v1.0.2 (2023-09-12)


## v1.0.1 (2023-08-29)


## v1.0.0 (2023-08-03)


## v0.7.0 (2023-08-03)


## v0.6.0 (2023-02-07)


## v0.5.2 (2022-04-07)


## v0.5.1 (2022-03-31)


## v0.5.0 (2022-03-31)


## v0.4.2 (2022-03-09)


## v0.4.1 (2022-02-09)


## v0.4.0 (2022-02-09)


## v0.3.0 (2022-02-08)


## v0.2.1 (2021-11-30)


## v0.2.0 (2021-11-29)


## v0.1.0 (2021-10-19)


## v0.0.2 (2021-09-29)
