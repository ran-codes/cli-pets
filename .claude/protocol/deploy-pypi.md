## Prepare Package Metadata 

- [ ] Set up a License
- [ ] Update README.md
- [ ] Update CHANGELOG.md
- [ ] pyproject.toml 


## Setup PyPI Account (One-time)

- [ ] Create PyPI account at https://pypi.org/account/register/
- [ ] Verify your email
- [ ] Go to Account Settings → API tokens (https://pypi.org/manage/account/token/)
- [ ] Click "Add API token"

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