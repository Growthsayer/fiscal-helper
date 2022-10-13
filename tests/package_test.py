'''
    - This import is the actual installed package, and will not be live to the code in this repo.
    - To edit the live code directly, edit the package files in the folder by running:
        $ Code /usr/local/lib/python3.7/site-packages/fiscal_calendar_helper
'''


from fiscal_calendar_helper import fiscal

x = fiscal.convert('2022_36', 'week_id', 'date')

print(x)