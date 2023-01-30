# Creating a new build

1. After making final updates, update the `pyproject.toml` file to have a new version number
2. Run build command: `python -m build`
3. Delete previous builds in the `dist/` folder
4. Upload new build to PyPi via: `python -m twine upload --repository pypi dist/*`
5. Commit build changes to repo


When testing locally, the file would be installed for live editing in a dir like this:
* /usr/local/lib/python3.7/site-packages/fiscal_calendar_helper