## Prepare Package Metadata 

- [x] Set up a License
- [x] Update pyproject.toml
- [x] Update README.md
- [x] Upload any README image assets to assets folder
- [x] Update CHANGELOG section of READM.md



## Setup PyPI Account (One-time)

- [x] Create PyPI account at https://pypi.org/account/register/
- [x] Verify your email
- [x] Go to Account Settings → API tokens (https://pypi.org/manage/account/token/)
- [x] Click "Add API token"

## Store API Token

- [x] Install dev depnency for .env file management `uv add python-dotenv --dev`
- [x] Create .env file in project root
- [x] add two variables `UV_PUBLISH_USERNAME=__token__` + `UV_PUBLISH_PASSWORD={secret}`
- [x] Abstract secrete management and publishing into `publish.py`


### Real Publish

- [x] Build the package `uv build`
- [ ] Publish the package `uv run publish.py`
- [ ] Verify at https://pypi.org/project/cli-pets/
- [ ] Test install: `pip install cli-pets` 