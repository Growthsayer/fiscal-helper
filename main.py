import pandas as pd

class Fiscal_Helper:

    def __init__(self):
        self.calendar = pd.read_csv('./fiscal_calendar.csv')

        # create a list of week_ids
        weeks = self.calendar['week_id']
        self.weeks = weeks.drop_duplicates().to_list()

        # create a list of date_ids
        dates = self.calendar['date_id']
        self.dates = dates.drop_duplicates().to_list()


    def offset(self, inp_str: str, offset: int = 1):
        '''Returns week_id or date_id offset by specified periods'''

        # make sure offset is an int
        if type(offset) != int: raise Exception(f'Offset should be an int')

        if(len(inp_str) == 7): # fiscal week string
            idx = self.weeks.index(inp_str)
            out_str = self.weeks[idx + offset]

        elif(len(inp_str) == 10): # Date string
            idx = self.dates.index(inp_str)
            out_str = self.dates[idx + offset]

        else:
            raise Exception(f"Input type should be 'YYYY_WW' for week ID and 'YYYY_MM_DD' for date_id")

        return out_str