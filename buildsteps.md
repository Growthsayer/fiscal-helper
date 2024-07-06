# Creating a new build

1. After making final updates, update the `pyproject.toml` file to have a new version number

# NOTE:
There's something about the build process that seems to require a virtual environment, but i haven't figured out how to do that fully with makefiles. You can look at the current makefile fullDeploy script for the commands, but you need to create, activate, and install libs into the venv before building and deploying

2. Run build command: `make build`
4. Deploy new version with: `make deploy` (you will need the API key for this part)
5. Commit build changes to repo


When testing locally, the file would be installed for live editing in a dir like this:
* /usr/local/lib/python3.7/site-packages/fiscal_calendar_helper