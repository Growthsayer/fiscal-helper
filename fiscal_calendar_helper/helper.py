from .fiscal_calendar import calendar
import pandas as pd

class Fiscal_Helper:

    def __init__(self):
        
        # read the calendar
        self.calendar = pd.DataFrame.from_dict(calendar)
        self.calendar = self.calendar.astype(str)
        self.calendar['date'] = pd.to_datetime(self.calendar['date'])

        # valid calendar levels - the higher the level, the higher the number
        self.levels = {
            'key': 1,
            'year' : 5,
            'quarter' : 4,
            'quarter_id': 4,
            'month' : 3,
            'month_id': 3,
            'week_id': 2,
            'week_num': 2,
            'day_of_week': 1,
            'date' : 1,
            'date_id' : 1
        }

        # create a list of week_ids
        weeks = self.calendar['week_id']
        self.weeks = weeks.drop_duplicates().to_list()

        # create a list of date_ids
        dates = self.calendar['date_id']
        self.dates = dates.drop_duplicates().to_list()


    # PUBLIC METHODS

    def convert(self, input: str, inp_level: str, out_level: str):
        '''
            - Converts one fiscal time period to another
            - Will return the first time in a list if levels are not 1:1 compatable (i.e. days : years)
            - Example: `fiscal.convert('2022_36', 'week_id', 'date')` => `2022-10-02 00:00:00`
        '''
        self._validate_level(inp_level)
        self._validate_level(out_level)

        cal = self.calendar
        input_df = cal.loc[cal[inp_level] == input]
        output_df = input_df[out_level].drop_duplicates().to_list()

        return output_df[0]

    def next(self, inp_str: str):
      ''' 
            - METHOD ONLY WORKS FOR DATE_ID or WEEK_ID
            - Returns next week_id or date_id
            - Example: fiscal.next('2022_36') => '2022_37'
      '''
      return self.offset(inp_str, 1)

    def offset(self, inp_str: str, offset: int):
        ''' 
            - METHOD only works for DATE_ID or WEEK_ID
            - Returns week_id or date_id offset by specified periods
            - Example: `fiscal.offset('2022_36', 1)` => `'2022_37'`

        '''

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

    def previous(self, inp_str: str):
      ''' 
            - METHOD only works for `DATE_ID` or `WEEK_ID`
            - Returns previous `week_id` or `date_id`
            - Example: `fiscal.next('2022_36')` => `'2022_37'`
      '''
      return self.offset(inp_str, -1)



    def fill_to(self, inp: str, child_level: str = 'date_id', parent_level: str = 'week_id', direction: str = 'start'):
        ''' 
            - Take in a child value along with child and parent levels and returns all the children after/before the current date
            - Does not ever return the original date in list
            - Example: `fiscal.fill_to('2016_02_18', 'date_id', 'week_id', 'start')` => ['2016_02_14', '2016_02_15', '2016_02_16', '2016_02_17']
        '''
        self._validate_relationship(child_level, parent_level)
        
        # convert the child to it's parent
        parent = self.convert(inp, child_level, parent_level)
        # list all children in the parent
        child_list = self.unpack(parent, parent_level, child_level)
        # return all remaining after/before the index of the child
        inp_index = child_list.index(inp)

        if direction == 'start':
            return child_list[:inp_index]
        elif direction == 'end':
            return child_list[inp_index + 1:]
        else:
            raise Exception(f'Unknown fill_to direction "{direction}" - must be "start" or "end"') 

    
    def unpack(self, input, parent_level, child_level):
        ''' 
            - Converts a parent level into all it's children
            - Returns a list of children
            - Example: `fiscal.unpack('2016_01', 'week_id', 'date_id')` => `['2016_02_07', '2016_02_08', '2016_02_09', '2016_02_10', '2016_02_11', '2016_02_12', '2016_02_13']`
        '''
        self._validate_relationship(child_level, parent_level)
        cal = self.calendar
        parent_df = cal.loc[cal[parent_level] == input]
        child_df = parent_df[child_level]
        return child_df.drop_duplicates().to_list()

    # PRIVATE METHODS
  
    def _validate_input(self, input, level):
        ''' 
           Validates an input exists for that level
        '''
        raise Exception('Input validation has not been set up yet')

    def _validate_level(self, level):
        ''' 
           Validates a given level is valid key in fiscal table
        '''
        if level not in self.levels:
            raise Exception(f'"{level}" is not a known fiscal key')
        else: return True
  
    # Verfies a child -> parent relationship is accurate
    # Also validates the levels
    def _validate_relationship(self, child, parent):
        '''
            Ensures that child -> parent relationship exists between two levels
        '''

        self._validate_level(child)
        self._validate_level(parent)
    
        c_index = self.levels[child]
        p_index = self.levels[parent]
        
        if c_index >= p_index:
            raise Exception(f'"{parent}" is not a parent to {child}')
        else: return True

