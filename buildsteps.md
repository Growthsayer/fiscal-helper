# Creating a new build

1. After making final updates, update the `pyproject.toml` file to have a new version number
2. Run build command: `make build`
4. Deploy new version with: `make deploy`
5. Commit build changes to repo


When testing locally, the file would be installed for live editing in a dir like this:
* /usr/local/lib/python3.7/site-packages/fiscal_calendar_helper