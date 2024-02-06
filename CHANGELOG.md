# CHANGELOG



## v1.2.0 (2024-02-06)

### Chore

* chore: merge CI/CD workflows ([`8e0d760`](https://github.com/fathomnet/fathomnet-py/commit/8e0d76006cec956cab009bf330a068f6e7a6adf4))

### Documentation

* docs: add Sphinx RTD theme build requirement ([`fccd808`](https://github.com/fathomnet/fathomnet-py/commit/fccd8086997330059094baeadac5162b1d17a7e4))

* docs: update copyright year to 2024 ([`1650bc5`](https://github.com/fathomnet/fathomnet-py/commit/1650bc5d836d80c6b6d8e2238e184834952cdf20))

* docs: add sphinx-rtd-theme as a dev dependency ([`9be9dee`](https://github.com/fathomnet/fathomnet-py/commit/9be9deeb42636a17f0d36d37100e5406dd0778f6))

* docs: update Python version and build configuration for readthedocs ([`ef96d8d`](https://github.com/fathomnet/fathomnet-py/commit/ef96d8d46cbf83c9c5d5d0eb03b8b927be487383))

### Feature

* feat: add functions to call fast WoRMS API directly ([`21942b8`](https://github.com/fathomnet/fathomnet-py/commit/21942b837b817de9aea02d4abc399802aa55ce8f))

### Fix

* fix: make the linter happy ([`6cc52f6`](https://github.com/fathomnet/fathomnet-py/commit/6cc52f6b6abbd1cbe1b14a435d82a9acb91e4f58))


## v1.1.5 (2024-01-10)

### Fix

* fix: quote display/org names in users find functions ([`591e67a`](https://github.com/fathomnet/fathomnet-py/commit/591e67a3e43af9e15ca0a0140de465a1da8018f3))

* fix: quote provider name and concept in taxa find functions, remove print from test ([`dde9eb5`](https://github.com/fathomnet/fathomnet-py/commit/dde9eb51a5da79a07a94fe5d93a7604681c035d6))

* fix: quote observer name in boundingboxes.audit_by_observer ([`b94c87e`](https://github.com/fathomnet/fathomnet-py/commit/b94c87e9351fbde116dc8ef22c58867059999bec))

* fix: quote boundingboxes.audit_by_concepts URL fragment, add test case ([`5ea7b45`](https://github.com/fathomnet/fathomnet-py/commit/5ea7b459278c540a31fbe63e263f9208c234e123))

* fix: update activity find functions for new DTO ([`cdf5617`](https://github.com/fathomnet/fathomnet-py/commit/cdf56179cc802085ff1f8adbba2f717be550f08b))


## v1.1.4 (2024-01-09)

### Documentation

* docs: fix broken tests badge ([`dbfbea8`](https://github.com/fathomnet/fathomnet-py/commit/dbfbea8ab261d285a691c6f92a740ce8ba893166))

### Fix

* fix: quote concept in images.find_by_concept, add test ([`33aa430`](https://github.com/fathomnet/fathomnet-py/commit/33aa4301a30dd15f64aebfef57dd21914ed060e1))

### Unknown

* Merge branch &#39;develop&#39; ([`14988d6`](https://github.com/fathomnet/fathomnet-py/commit/14988d63186d5c60e78c9e5039b1b2ca16d03dd0))


## v1.1.3 (2023-09-13)

### Documentation

* docs: Add script documentation

Closes #5 ([`1eadc8f`](https://github.com/fathomnet/fathomnet-py/commit/1eadc8ff627307fec7cefde19918da45c086195e))

### Fix

* fix(api): Improve client error exception

Add the fathomnet.util.debug_format_response to the ValueError exception
 raised when a status code &lt; 500 and != 401 / 403 is returned. Fixes #16 ([`6b0b911`](https://github.com/fathomnet/fathomnet-py/commit/6b0b91110be90d7e41e7c2a8dab87cd29b331395))


## v1.1.2 (2023-09-12)

### Fix

* fix: Add condition to CD workflow ([`df3432d`](https://github.com/fathomnet/fathomnet-py/commit/df3432d1b5685414c64d6a8a21b020497d1b6313))

* fix: Add CD ([`8979d75`](https://github.com/fathomnet/fathomnet-py/commit/8979d75b049d39c673feb0d78153d4e5a4de11c5))


## v1.1.1 (2023-09-13)

### Fix

* fix: Remove publish step from CI (for now) ([`3ba596b`](https://github.com/fathomnet/fathomnet-py/commit/3ba596b2b240ba841cecf98f20c74d30a5e386a5))

* fix: Version in pyproject.toml ([`dd2d9a2`](https://github.com/fathomnet/fathomnet-py/commit/dd2d9a2d3e9a27610e17c119337e821fcea8bcbc))


## v1.1.0 (2023-09-13)

### Feature

* feat: Set up python-semantic-release ([`4019f18`](https://github.com/fathomnet/fathomnet-py/commit/4019f1811cabc207f5972eb39b8a9a7720345f95))


## v1.0.2 (2023-09-13)

### Unknown

* Bump version ([`e7c404d`](https://github.com/fathomnet/fathomnet-py/commit/e7c404d0c0406884cfbf88d107add8152b4a3566))

* Unit tests updated for latest API changes (#20) ([`2a32d1d`](https://github.com/fathomnet/fathomnet-py/commit/2a32d1d6ccb510166c2ac30c2920f83e5542957f))

* Fix for new &#34;Entity&#34; object names in tests ([`cdcf484`](https://github.com/fathomnet/fathomnet-py/commit/cdcf48472e746cbf8285a6b3f6d3090579971df4))

* Add req/response to server error exception message ([`00f2ff6`](https://github.com/fathomnet/fathomnet-py/commit/00f2ff64bd0b19cae74042287023d5802aee7165))


## v1.0.1 (2023-08-30)

### Unknown

* Bump version ([`0ba8b2f`](https://github.com/fathomnet/fathomnet-py/commit/0ba8b2f14654b3e69cf01d098263100f68e9f5db))

* Fix for empty paged results ([`aba2c01`](https://github.com/fathomnet/fathomnet-py/commit/aba2c0157290d19b85f34f468e504d2e166d255a))

* Add page utility function ([`accad89`](https://github.com/fathomnet/fathomnet-py/commit/accad895fc4c2bb2628ac0e9a7e61e43cfab5679))

* Fix taxa tests for fathomnet provider ([`dfe44fe`](https://github.com/fathomnet/fathomnet-py/commit/dfe44fe2771e6a4f962525d6f689ffa901487df2))


## v1.0.0 (2023-08-04)

### Unknown

* Version 1.0.0 ([`b4a46a1`](https://github.com/fathomnet/fathomnet-py/commit/b4a46a1447c37a93bef1350efb47670eb4d4d795))

* Nit ([`97e25b2`](https://github.com/fathomnet/fathomnet-py/commit/97e25b27e787f7dcfa312b5eb24c4aca3d4c9ead))

* Support changes to user endpoints ([`c0ff3f7`](https://github.com/fathomnet/fathomnet-py/commit/c0ff3f796d9055c4bff5151dea084da4ebe939d2))

* Support new audit endpoints ([`45eef83`](https://github.com/fathomnet/fathomnet-py/commit/45eef8367a1143e4b6189125522af455a9cfb987))

* Add activity and topics API support ([`20a3fc4`](https://github.com/fathomnet/fathomnet-py/commit/20a3fc4fef4294713c7253dcb77be49446c49eed))

* Comments fixes ([`c3acce5`](https://github.com/fathomnet/fathomnet-py/commit/c3acce530cd5a7157ddaaeb7170a3ef380e4b59c))

* Fix users tests ([`f7768c0`](https://github.com/fathomnet/fathomnet-py/commit/f7768c082ee2b1f15575a7975a438e5ff9d55306))

* Typo ([`6c786e1`](https://github.com/fathomnet/fathomnet-py/commit/6c786e18bcedc23391aacd25619bef966a22e7ad))

* Bounding box comments ([`7aa63fd`](https://github.com/fathomnet/fathomnet-py/commit/7aa63fd5c68369b87bffb3a136fea1170973c78e))


## v0.7.0 (2023-08-04)

### Unknown

* Bump version ([`23286d7`](https://github.com/fathomnet/fathomnet-py/commit/23286d70719be412090514b11d898d0b6cce9db6))

* Use v3 checkout/setup-python actions ([`f590e28`](https://github.com/fathomnet/fathomnet-py/commit/f590e28f5241105ff15f1c42d38fc388090c9699))

* Add changes missed in last commit ([`0a10130`](https://github.com/fathomnet/fathomnet-py/commit/0a1013047e54beeb2bf3f78995a8211a8fa7d24c))

* Support for fathomnet-rest-api v1.5.0
Several fixes to pageable endpoints
Require Python 3.7 -&gt; 3.8.1
Add test suite for user endpoints
Slight tweaks to GH action linting ([`8db72d3`](https://github.com/fathomnet/fathomnet-py/commit/8db72d36bc2f9fa6becf377686e521eaf18ca5c5))

* Cleanup imports ([`19dd45f`](https://github.com/fathomnet/fathomnet-py/commit/19dd45fbd9bdc7945198d5acb21550f1fce18633))

* Added MBARI MB Benthic model ([`e7d7938`](https://github.com/fathomnet/fathomnet-py/commit/e7d79387e997d5d0f55bbad1d9a45e3d10af1176))

* Add poetry.lock to .gitignore ([`886a726`](https://github.com/fathomnet/fathomnet-py/commit/886a7269b77e585f8ba13cd34746bce0cbc278e8))

* Refactor fathomnet.models -&gt; fathomnet.dto ([`ce4ad97`](https://github.com/fathomnet/fathomnet-py/commit/ce4ad97d270e28b8773a01bce73eb5d50987e36b))

* Minor fixes ([`7206e14`](https://github.com/fathomnet/fathomnet-py/commit/7206e141486fcc99c09c8b31304df510a1e0d28f))

* More coco manipulation and reorganizing ([`582290e`](https://github.com/fathomnet/fathomnet-py/commit/582290e031fa6e7e50ea2b356a5d5c7348345dc9))

* Add coco download section to tutorial notebook ([`40369e3`](https://github.com/fathomnet/fathomnet-py/commit/40369e387144ac8ab90b61343eef0be47c2a6262))


## v0.6.0 (2023-02-08)

### Unknown

* Merge branch &#39;develop&#39; ([`4a7bc1e`](https://github.com/fathomnet/fathomnet-py/commit/4a7bc1e09b01852ee0dabe0b92d4579cc800089c))

* Add Python 3.10 to CI ([`01d48da`](https://github.com/fathomnet/fathomnet-py/commit/01d48da1a81392f001e2820d37df828a37d6b891))

* Flake8 nits ([`8477666`](https://github.com/fathomnet/fathomnet-py/commit/8477666e17a34a02b8b72f873929896b325eafdf))

* Merge branch &#39;develop&#39; ([`a25582e`](https://github.com/fathomnet/fathomnet-py/commit/a25582e2f5f201e2084789818d14ed2b714730e6))

* Add test for audit endpoints ([`5e9f4b9`](https://github.com/fathomnet/fathomnet-py/commit/5e9f4b9624ad7ef5fe4e07d0cc1d3beb5ce32f8a))

* Merge branch &#39;develop&#39; ([`1e5e69b`](https://github.com/fathomnet/fathomnet-py/commit/1e5e69b9d48e4943fcc5788ba7a2c004f110736d))

* Support boundingboxes audit endpoints ([`46a47ea`](https://github.com/fathomnet/fathomnet-py/commit/46a47ea219f1950c3cb4353cff0c9b2d40cf8774))

* Removed forced debug print statement ([`3ae2f69`](https://github.com/fathomnet/fathomnet-py/commit/3ae2f694c2a83688572254ca49a1954ee65fa420))


## v0.5.2 (2022-04-08)

### Unknown

* Merge branch &#39;develop&#39; into main ([`1f71f63`](https://github.com/fathomnet/fathomnet-py/commit/1f71f63655b9cd601cbaaca01df6a1287007d438))

* Fix missing functions in fathomnet-generate ([`31477ab`](https://github.com/fathomnet/fathomnet-py/commit/31477ab780dc409ecee044d2a5607b419bb9856c))

* Merge branch &#39;develop&#39; ([`1dc6689`](https://github.com/fathomnet/fathomnet-py/commit/1dc668977d5878f2d25741b49ea5a3c7e090251b))

* Bump version ([`ccccb89`](https://github.com/fathomnet/fathomnet-py/commit/ccccb89c75a13abb0bc845fd6f91ec030a711798))

* Merge branch &#39;develop&#39; ([`2ff153b`](https://github.com/fathomnet/fathomnet-py/commit/2ff153b6f6ac61085a832de2d762dc43ca9ee530))

* Added region endpoint per REST API 1.1.1 ([`d5cdf1a`](https://github.com/fathomnet/fathomnet-py/commit/d5cdf1ac5f49288fa1ba4c273bbc8d3d1cab3097))

* Cleaned up fathomnet_generate formatting ([`2aad07b`](https://github.com/fathomnet/fathomnet-py/commit/2aad07bdf4ae6499a094eb9f70c9dc2c9ea1d0df))


## v0.5.1 (2022-04-01)

### Unknown

* Merge branch &#39;develop&#39; into main ([`abceeea`](https://github.com/fathomnet/fathomnet-py/commit/abceeea3f483ecd549862a7bda747fba71df43dd))

* Fix fathomnet-generate bug in Python 3.7 ([`df8e25a`](https://github.com/fathomnet/fathomnet-py/commit/df8e25a5e3c77508191478d88a2fe735446124b6))


## v0.5.0 (2022-04-01)

### Unknown

* Merge branch &#39;develop&#39; into main ([`e2dc5fd`](https://github.com/fathomnet/fathomnet-py/commit/e2dc5fdf6b2762d8edc931adb4ab5bce9dd15315))

* Bump version, require newer coco-lib ([`566587e`](https://github.com/fathomnet/fathomnet-py/commit/566587e216eede27260b91df479c10e29f8691c8))

* Merge branch &#39;develop&#39; into main ([`7ff1d32`](https://github.com/fathomnet/fathomnet-py/commit/7ff1d322b10659ab512b118bc88d0a7c58284694))

* Updated README ([`dbfb2b2`](https://github.com/fathomnet/fathomnet-py/commit/dbfb2b22163fdf36426e7ccdee86a42344a14336))

* Removed unused cell ([`0bce7b3`](https://github.com/fathomnet/fathomnet-py/commit/0bce7b33f76cb5008a2429868647808e2ed55e95))

* Update CoLab link to main

Changed CoLab link in README to open main instead of dev branch notebook. ([`9c57174`](https://github.com/fathomnet/fathomnet-py/commit/9c571747bc6842a7d19f9e542585c9a001cd267e))

* Changed day two order. Removed calls to Google Drive ([`56ae925`](https://github.com/fathomnet/fathomnet-py/commit/56ae925d8e19e321fa17c168a62bd6ff90de4233))

* Workshop-ready version of tutorial notebook ([`0ca5c81`](https://github.com/fathomnet/fathomnet-py/commit/0ca5c81c04b1f652a3be645c4f9d7e5772c5de8f))

* Updated tutorial.ipynb ([`2b93d26`](https://github.com/fathomnet/fathomnet-py/commit/2b93d261c9da0969146af8542168489eafac2488))

* Colab badge for tutorial notebook ([`e3880b5`](https://github.com/fathomnet/fathomnet-py/commit/e3880b5f2a811f371654098faeb801727c96d334))

* add tutorial notebook ([`60dfa5f`](https://github.com/fathomnet/fathomnet-py/commit/60dfa5f54cb5af9854a84235d0675781ac38ce0b))


## v0.4.2 (2022-03-10)

### Unknown

* Bump version ([`507b0b1`](https://github.com/fathomnet/fathomnet-py/commit/507b0b1fddb59043ad01124fea09062d4c37625a))

* Merge pull request #7 from fathomnet/download

Download function in fathomnet-generate ([`173a9ee`](https://github.com/fathomnet/fathomnet-py/commit/173a9ee47591d0772b2684d7d5ff3f01428eda54))

* Merge remote-tracking branch &#39;origin/download&#39; into download ([`01cc97d`](https://github.com/fathomnet/fathomnet-py/commit/01cc97d7e1cc66b902c5b5ab3887f8112122ee03))

* Add progressbar2 to deps ([`b6d914c`](https://github.com/fathomnet/fathomnet-py/commit/b6d914cc7266faa886408ed8f278d2da7eda2dde))

* Context manager for image download

More responsible file management for copyfilebobj

Co-authored-by: Kevin Barnard &lt;kbarnard@mbari.org&gt; ([`7cbab3b`](https://github.com/fathomnet/fathomnet-py/commit/7cbab3bba252268eb44b269f65f95b0db903ce59))

* Delete print statement

Remove debugging print of args in main

Co-authored-by: Kevin Barnard &lt;kbarnard@mbari.org&gt; ([`25bc618`](https://github.com/fathomnet/fathomnet-py/commit/25bc618cdaf55fabae07af3d6dc79dfd82484dca))

* Added parser argument and if-loop to run download in main ([`5111f7c`](https://github.com/fathomnet/fathomnet-py/commit/5111f7cc704593d2354624a37c75d95403407c1b))

* Updated download image function to download from list ([`a07a622`](https://github.com/fathomnet/fathomnet-py/commit/a07a622bbc39b691c93831b7a9dac91ae03129ae))

* Add download function to generate ([`5195b82`](https://github.com/fathomnet/fathomnet-py/commit/5195b82adf0fce2ec0a0ba101e7c19c4f6c1996a))

* updated filename to image uuid in generate coco ([`bb71d64`](https://github.com/fathomnet/fathomnet-py/commit/bb71d6499cec0c81c8cda092b2a4fd864ba85bff))


## v0.4.1 (2022-02-10)

### Unknown

* Bump version ([`0ecaf69`](https://github.com/fathomnet/fathomnet-py/commit/0ecaf6930637e6803626879c7616dc86967572a3))

* Tags API doc typo ([`aa33b81`](https://github.com/fathomnet/fathomnet-py/commit/aa33b81f0d71415275425c2f1d202c346fb0fd4a))


## v0.4.0 (2022-02-10)

### Unknown

* Tags API ([`f48d468`](https://github.com/fathomnet/fathomnet-py/commit/f48d4685f70eb1bad7d583f6533ce175847fd807))

* Bump copyright year ([`5e126d8`](https://github.com/fathomnet/fathomnet-py/commit/5e126d81d15b5b123d8e0e555e04ae814af0228b))

* CImageSetUploadDTO -&gt; BImageSetUploadDTO ([`d8b072a`](https://github.com/fathomnet/fathomnet-py/commit/d8b072a4dd8e7f8eecf7bf09242ebddbd7ba79de))

* CDarwinCore -&gt; BDarwinCore ([`0fd8689`](https://github.com/fathomnet/fathomnet-py/commit/0fd868991466ee13e9cf0d9d4605ffd7d9157b47))

* BBoundingBoxDTO -&gt; BoundingBoxDTO ([`3c864c6`](https://github.com/fathomnet/fathomnet-py/commit/3c864c6f1a8d3cb203f570fd10773c0406c2b91e))

* Removed Python 3.6 from automated tests ([`ba34e25`](https://github.com/fathomnet/fathomnet-py/commit/ba34e25871234415848ab795c1c040c76daf8cfc))


## v0.3.0 (2022-02-09)

### Unknown

* Bump version ([`3c6437a`](https://github.com/fathomnet/fathomnet-py/commit/3c6437a0306c020c7de8e864b4449a414ccb4b62))

* Bumped required Python version to ^3.7 ([`0af9132`](https://github.com/fathomnet/fathomnet-py/commit/0af9132de148ddf0cca91629caa9c5c6c1d37149))

* Allow search unconstrained by concept (#2) ([`c278ba5`](https://github.com/fathomnet/fathomnet-py/commit/c278ba5d2395ab4250bfbc5c81daa6c8f7123dfc))

* Review changes from #4 ([`106f268`](https://github.com/fathomnet/fathomnet-py/commit/106f2688179023c8cc835e02230720992f181975))

* Added parser arg for concepts from text file (#4)

* added parser options for concept list as text file

* spelling error

* arg naming error

* arg naming error again

Co-authored-by: ecor &lt;eorenstein@mbari.org&gt; ([`5c1e799`](https://github.com/fathomnet/fathomnet-py/commit/5c1e7999859ed1afdc30fbcdb687910768c2e4e6))


## v0.2.1 (2021-12-01)

### Unknown

* Fixed ISO8601 encoding and count on empty ([`b271f42`](https://github.com/fathomnet/fathomnet-py/commit/b271f424c947276393ab1ac6c13240931a279340))


## v0.2.0 (2021-11-30)

### Unknown

* fathomnet-generate tool release ([`63e368d`](https://github.com/fathomnet/fathomnet-py/commit/63e368d0eb29c4865c107bb458f8735b270c3526))

* Added extra links and classifiers ([`0bff623`](https://github.com/fathomnet/fathomnet-py/commit/0bff6235c36d7b26e5713173273f87c05dcad029))

* Changed build to poetry ([`87be7ff`](https://github.com/fathomnet/fathomnet-py/commit/87be7ff2f3e241ac88dbfdaca0a9eede187a6c9d))

* New flags, count mechanism ([`e2d4e62`](https://github.com/fathomnet/fathomnet-py/commit/e2d4e62ff16d6b72fbfc5c3b65b674d76ad08ef6))

* Added example fathomnet-generate script ([`ab5445c`](https://github.com/fathomnet/fathomnet-py/commit/ab5445c4062fd09aeaa4acd5331f5c20ca8582b7))


## v0.1.0 (2021-10-20)

### Unknown

* Prep for release 0.1.0 ([`133f54e`](https://github.com/fathomnet/fathomnet-py/commit/133f54e7a153e12d5279d451e2eedc042191007c))

* Added missing lxml dep ([`54fbc51`](https://github.com/fathomnet/fathomnet-py/commit/54fbc518dd75441ba52a7834e7e010b6daae6ebd))

* Added AImageDTO -&gt; Pascal VOC transform ([`e67b165`](https://github.com/fathomnet/fathomnet-py/commit/e67b1657296da413c79b4fd78a236a87be3743a5))

* Improved docs ([`7fbedf7`](https://github.com/fathomnet/fathomnet-py/commit/7fbedf78fd68fda66e99dd5a8a07f967215edf5a))

* New test UUIDs due to data reload ([`d2b4f6d`](https://github.com/fathomnet/fathomnet-py/commit/d2b4f6d89d37aa84ee7dc195ba510d83eb74c961))


## v0.0.2 (2021-09-30)

### Unknown

* Fix for PyPI ([`9c60937`](https://github.com/fathomnet/fathomnet-py/commit/9c60937d7d69e6888f14e8940c0222b37da1dadb))

* Added starter text to README.md ([`a62a58c`](https://github.com/fathomnet/fathomnet-py/commit/a62a58c9f308ce03c1ab4d63c9f2327c3bfe50ef))

* Fix badge link ([`517ff68`](https://github.com/fathomnet/fathomnet-py/commit/517ff68670ebeff7270712cdd42f09e0fe0da971))

* Removed api-ci action, updated README badge ([`4ed01bb`](https://github.com/fathomnet/fathomnet-py/commit/4ed01bb6cc5650ffd3fa58677d3b6351196308de))

* Renamed api-ci to tests ([`dd291af`](https://github.com/fathomnet/fathomnet-py/commit/dd291afce23bc69af78277ddd3fee49b0494955e))

* readthedocs config patch ([`75fef58`](https://github.com/fathomnet/fathomnet-py/commit/75fef58572e6cc6dce05e0370cd11a8cf87c6571))

* readthedocs setup, badge ([`23e61d1`](https://github.com/fathomnet/fathomnet-py/commit/23e61d1d949b81f67744b79d0232aa09d4a8d98e))

* Basic Sphinx autodocs ([`61b4eee`](https://github.com/fathomnet/fathomnet-py/commit/61b4eee0c7ae3c8eb56a1314b0bce90c261e31ba))

* Added CI badge to README ([`ead322e`](https://github.com/fathomnet/fathomnet-py/commit/ead322ef42287026f2d9e9e112d6243d0f2ea605))

* Added .gitignore ([`03b07e4`](https://github.com/fathomnet/fathomnet-py/commit/03b07e4601566c78fb49c0d754d1818945b87a1d))

* Rename job build -&gt; lint-and-test ([`72e8e58`](https://github.com/fathomnet/fathomnet-py/commit/72e8e587966e2b702e104a629ac625baf1c0e6bf))

* Remove missing Python 3.10 test, rename job ([`1e9f6e8`](https://github.com/fathomnet/fathomnet-py/commit/1e9f6e8b838edc80aa7335cd0c5a4b5b08cfe12b))

* Fix github action for CI ([`6024c21`](https://github.com/fathomnet/fathomnet-py/commit/6024c212be9d7de39791b6982249577a41187376))

* Ported tests, set up github CI action ([`8f6e06d`](https://github.com/fathomnet/fathomnet-py/commit/8f6e06d33f7ab48a4700877f994bbac7d028ff53))

* Added missing docstrings ([`33ae5a3`](https://github.com/fathomnet/fathomnet-py/commit/33ae5a32486fb284bdb1d0ecc9ff99913600d0a5))

* Added __init__.py for fathomnet package ([`f0519f4`](https://github.com/fathomnet/fathomnet-py/commit/f0519f45944d71256d5e8e220053ca315d605841))

* Migrated API and setuptools config ([`1a28c25`](https://github.com/fathomnet/fathomnet-py/commit/1a28c25375310b04b2148a4497e7ee1a6ba031ae))

* Initial commit ([`b8a7fd5`](https://github.com/fathomnet/fathomnet-py/commit/b8a7fd52f024552b0044b1feaa95b8dc6d6ee688))
