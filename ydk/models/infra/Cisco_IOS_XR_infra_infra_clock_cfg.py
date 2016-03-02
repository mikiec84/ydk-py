""" Cisco_IOS_XR_infra_infra_clock_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra\-clock package configuration.

This module contains definitions
for the following management objects\:
  clock\: Configure time\-of\-day clock

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class ClockMonth_Enum(Enum):
    """
    ClockMonth_Enum

    Clock month

    """

    """

    January

    """
    JANUARY = 0

    """

    February

    """
    FEBRUARY = 1

    """

    March

    """
    MARCH = 2

    """

    April

    """
    APRIL = 3

    """

    May

    """
    MAY = 4

    """

    June

    """
    JUNE = 5

    """

    July

    """
    JULY = 6

    """

    August

    """
    AUGUST = 7

    """

    September

    """
    SEPTEMBER = 8

    """

    October

    """
    OCTOBER = 9

    """

    November

    """
    NOVEMBER = 10

    """

    December

    """
    DECEMBER = 11


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_infra_clock_cfg as meta
        return meta._meta_table['ClockMonth_Enum']


class ClockSummerTimeMode_Enum(Enum):
    """
    ClockSummerTimeMode_Enum

    Clock summer time mode

    """

    """

    Recurring summer time

    """
    RECURRING = 0

    """

    Absolute summer time

    """
    DATE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_infra_clock_cfg as meta
        return meta._meta_table['ClockSummerTimeMode_Enum']



class Clock(object):
    """
    Configure time\-of\-day clock
    
    .. attribute:: summer_time
    
    	Configure summer (daylight savings) time
    	**type**\: :py:class:`SummerTime <ydk.models.infra.Cisco_IOS_XR_infra_infra_clock_cfg.Clock.SummerTime>`
    
    .. attribute:: time_zone
    
    	Configure time zone
    	**type**\: :py:class:`TimeZone <ydk.models.infra.Cisco_IOS_XR_infra_infra_clock_cfg.Clock.TimeZone>`
    
    

    """

    _prefix = 'infra-infra-clock-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.summer_time = None
        self.time_zone = None


    class SummerTime(object):
        """
        Configure summer (daylight savings) time
        
        .. attribute:: end_hour
        
        	Hour to end 
        	**type**\: int
        
        	**range:** 0..23
        
        .. attribute:: end_minute
        
        	Minute to end 
        	**type**\: int
        
        	**range:** 0..59
        
        .. attribute:: end_month
        
        	 Month to end 
        	**type**\: :py:class:`ClockMonth_Enum <ydk.models.infra.Cisco_IOS_XR_infra_infra_clock_cfg.ClockMonth_Enum>`
        
        .. attribute:: end_week_number_or_end_date
        
        	If Mode is set to 'Recurring' specify Week number of the Month to end (first and last strings are not allowed as they are in CLI), if Mode is set to 'Date' specify Date to End
        	**type**\: int
        
        	**range:** 1..31
        
        .. attribute:: end_weekday_or_end_year
        
        	If Mode is set to 'Recurring' specify Weekday to end , if Mode is set to 'Date' specify Year to end
        	**type**\: int
        
        	**range:** 0..2035
        
        .. attribute:: mode
        
        	Summer time mode
        	**type**\: :py:class:`ClockSummerTimeMode_Enum <ydk.models.infra.Cisco_IOS_XR_infra_infra_clock_cfg.ClockSummerTimeMode_Enum>`
        
        .. attribute:: offset
        
        	Offset to add in minutes 
        	**type**\: int
        
        	**range:** 1..1440
        
        .. attribute:: start_hour
        
        	Hour to start 
        	**type**\: int
        
        	**range:** 0..23
        
        .. attribute:: start_minute
        
        	Minute to start 
        	**type**\: int
        
        	**range:** 0..59
        
        .. attribute:: start_month
        
        	 Month to start 
        	**type**\: :py:class:`ClockMonth_Enum <ydk.models.infra.Cisco_IOS_XR_infra_infra_clock_cfg.ClockMonth_Enum>`
        
        .. attribute:: start_week_number_or_start_date
        
        	 If Mode is set to 'Recurring' specify Week number of the Month to start (first and last strings are not allowed as they are in CLI) , if Mode is set to 'Date' specify Date to start 
        	**type**\: int
        
        	**range:** 1..31
        
        .. attribute:: start_weekday_or_start_year
        
        	 If Mode is set to 'Recurring' specify Weekday to start , if Mode is set to 'Date' specify Year to start 
        	**type**\: int
        
        	**range:** 0..2035
        
        .. attribute:: time_zone_name
        
        	Name of time zone in summer
        	**type**\: str
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-infra-clock-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.end_hour = None
            self.end_minute = None
            self.end_month = None
            self.end_week_number_or_end_date = None
            self.end_weekday_or_end_year = None
            self.mode = None
            self.offset = None
            self.start_hour = None
            self.start_minute = None
            self.start_month = None
            self.start_week_number_or_start_date = None
            self.start_weekday_or_start_year = None
            self.time_zone_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-infra-clock-cfg:clock/Cisco-IOS-XR-infra-infra-clock-cfg:summer-time'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.end_hour is not None:
                return True

            if self.end_minute is not None:
                return True

            if self.end_month is not None:
                return True

            if self.end_week_number_or_end_date is not None:
                return True

            if self.end_weekday_or_end_year is not None:
                return True

            if self.mode is not None:
                return True

            if self.offset is not None:
                return True

            if self.start_hour is not None:
                return True

            if self.start_minute is not None:
                return True

            if self.start_month is not None:
                return True

            if self.start_week_number_or_start_date is not None:
                return True

            if self.start_weekday_or_start_year is not None:
                return True

            if self.time_zone_name is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_infra_clock_cfg as meta
            return meta._meta_table['Clock.SummerTime']['meta_info']


    class TimeZone(object):
        """
        Configure time zone
        
        .. attribute:: hour_offset
        
        	Hours offset from UTC
        	**type**\: int
        
        	**range:** \-23..23
        
        .. attribute:: minute_offset
        
        	Minutes offset from UTC
        	**type**\: int
        
        	**range:** 0..59
        
        .. attribute:: time_zone_name
        
        	Name of time zone
        	**type**\: str
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-infra-clock-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.hour_offset = None
            self.minute_offset = None
            self.time_zone_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-infra-clock-cfg:clock/Cisco-IOS-XR-infra-infra-clock-cfg:time-zone'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.hour_offset is not None:
                return True

            if self.minute_offset is not None:
                return True

            if self.time_zone_name is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_infra_clock_cfg as meta
            return meta._meta_table['Clock.TimeZone']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-infra-clock-cfg:clock'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.summer_time is not None and self.summer_time._has_data():
            return True

        if self.summer_time is not None and self.summer_time.is_presence():
            return True

        if self.time_zone is not None and self.time_zone._has_data():
            return True

        if self.time_zone is not None and self.time_zone.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_infra_clock_cfg as meta
        return meta._meta_table['Clock']['meta_info']


