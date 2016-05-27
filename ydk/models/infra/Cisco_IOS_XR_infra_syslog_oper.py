""" Cisco_IOS_XR_infra_syslog_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-syslog package operational data.

This module contains definitions
for the following management objects\:
  logging\: Logging History data
  syslog\: syslog

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class SystemMessageSeverityEnum(Enum):
    """
    SystemMessageSeverityEnum

    System message severity

    .. data:: MESSAGE_SEVERITY_UNKNOWN = -1

    	Unknown

    .. data:: MESSAGE_SEVERITY_EMERGENCY = 0

    	Emergency

    .. data:: MESSAGE_SEVERITY_ALERT = 1

    	Alert

    .. data:: MESSAGE_SEVERITY_CRITICAL = 2

    	Critical

    .. data:: MESSAGE_SEVERITY_ERROR = 3

    	Error

    .. data:: MESSAGE_SEVERITY_WARNING = 4

    	Warning

    .. data:: MESSAGE_SEVERITY_NOTICE = 5

    	Notice

    .. data:: MESSAGE_SEVERITY_INFORMATIONAL = 6

    	Informational

    .. data:: MESSAGE_SEVERITY_DEBUG = 7

    	Debug

    """

    MESSAGE_SEVERITY_UNKNOWN = -1

    MESSAGE_SEVERITY_EMERGENCY = 0

    MESSAGE_SEVERITY_ALERT = 1

    MESSAGE_SEVERITY_CRITICAL = 2

    MESSAGE_SEVERITY_ERROR = 3

    MESSAGE_SEVERITY_WARNING = 4

    MESSAGE_SEVERITY_NOTICE = 5

    MESSAGE_SEVERITY_INFORMATIONAL = 6

    MESSAGE_SEVERITY_DEBUG = 7


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
        return meta._meta_table['SystemMessageSeverityEnum']



class Logging(object):
    """
    Logging History data
    
    .. attribute:: history
    
    	Syslog Info 
    	**type**\: :py:class:`History <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Logging.History>`
    
    

    """

    _prefix = 'infra-syslog-oper'
    _revision = '2015-12-01'

    def __init__(self):
        self.history = Logging.History()
        self.history.parent = self


    class History(object):
        """
        Syslog Info 
        
        .. attribute:: properties
        
        	Syslog Properties
        	**type**\: str
        
        .. attribute:: message
        
        	Syslog Message
        	**type**\: str
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2015-12-01'

        def __init__(self):
            self.parent = None
            self.properties = None
            self.message = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-oper:logging/Cisco-IOS-XR-infra-syslog-oper:history'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.properties is not None:
                return True

            if self.message is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
            return meta._meta_table['Logging.History']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-syslog-oper:logging'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.history is not None and self.history._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
        return meta._meta_table['Logging']['meta_info']


class Syslog(object):
    """
    syslog
    
    .. attribute:: an_remote_servers
    
    	Logging AN remote servers information
    	**type**\: :py:class:`AnRemoteServers <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.AnRemoteServers>`
    
    .. attribute:: messages
    
    	Message table information
    	**type**\: :py:class:`Messages <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.Messages>`
    
    .. attribute:: logging_statistics
    
    	Logging statistics information
    	**type**\: :py:class:`LoggingStatistics <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics>`
    
    

    """

    _prefix = 'infra-syslog-oper'
    _revision = '2015-12-01'

    def __init__(self):
        self.an_remote_servers = Syslog.AnRemoteServers()
        self.an_remote_servers.parent = self
        self.messages = Syslog.Messages()
        self.messages.parent = self
        self.logging_statistics = Syslog.LoggingStatistics()
        self.logging_statistics.parent = self


    class AnRemoteServers(object):
        """
        Logging AN remote servers information
        
        .. attribute:: an_remote_log_server
        
        	AN Remote Log Servers
        	**type**\: list of :py:class:`AnRemoteLogServer <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.AnRemoteServers.AnRemoteLogServer>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2015-12-01'

        def __init__(self):
            self.parent = None
            self.an_remote_log_server = YList()
            self.an_remote_log_server.parent = self
            self.an_remote_log_server.name = 'an_remote_log_server'


        class AnRemoteLogServer(object):
            """
            AN Remote Log Servers
            
            .. attribute:: ip_address
            
            	IP Address
            	**type**\: str
            
            .. attribute:: vrf_name
            
            	VRF Name
            	**type**\: str
            
            .. attribute:: vrf_severity
            
            	VRF Severity
            	**type**\: str
            
            .. attribute:: rh_discriminator
            
            	Remote\-Host Discriminator
            	**type**\: str
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2015-12-01'

            def __init__(self):
                self.parent = None
                self.ip_address = None
                self.vrf_name = None
                self.vrf_severity = None
                self.rh_discriminator = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:an-remote-servers/Cisco-IOS-XR-infra-syslog-oper:an-remote-log-server'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ip_address is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.vrf_severity is not None:
                    return True

                if self.rh_discriminator is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.AnRemoteServers.AnRemoteLogServer']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:an-remote-servers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.an_remote_log_server is not None:
                for child_ref in self.an_remote_log_server:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
            return meta._meta_table['Syslog.AnRemoteServers']['meta_info']


    class Messages(object):
        """
        Message table information
        
        .. attribute:: message
        
        	A system message
        	**type**\: list of :py:class:`Message <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.Messages.Message>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2015-12-01'

        def __init__(self):
            self.parent = None
            self.message = YList()
            self.message.parent = self
            self.message.name = 'message'


        class Message(object):
            """
            A system message
            
            .. attribute:: message_id  <key>
            
            	Message ID of the system message
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: card_type
            
            	Message card location\: 'RP', 'DRP', 'LC', 'SC', 'SP' or 'UNK' 
            	**type**\: str
            
            .. attribute:: node_name
            
            	Message source location
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: time_stamp
            
            	Time in milliseconds since 00\:00\:00 UTC, January 11970 of when message was generated
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: time_of_day
            
            	Time of day of event in DDD MMM DD  YYYY HH\:MM \:SS format, e.g Wed Apr 01 2009  15\:50\:26
            	**type**\: str
            
            .. attribute:: time_zone
            
            	Time Zone in UTC+/\-HH\:MM format,  e.g UTC+5\:30, UTC\-6
            	**type**\: str
            
            .. attribute:: process_name
            
            	Process name
            	**type**\: str
            
            .. attribute:: category
            
            	Message category
            	**type**\: str
            
            .. attribute:: group
            
            	Message group
            	**type**\: str
            
            .. attribute:: message_name
            
            	Message name
            	**type**\: str
            
            .. attribute:: severity
            
            	Message severity
            	**type**\: :py:class:`SystemMessageSeverityEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverityEnum>`
            
            .. attribute:: text
            
            	Additional message text
            	**type**\: str
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2015-12-01'

            def __init__(self):
                self.parent = None
                self.message_id = None
                self.card_type = None
                self.node_name = None
                self.time_stamp = None
                self.time_of_day = None
                self.time_zone = None
                self.process_name = None
                self.category = None
                self.group = None
                self.message_name = None
                self.severity = None
                self.text = None

            @property
            def _common_path(self):
                if self.message_id is None:
                    raise YPYDataValidationError('Key property message_id is None')

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:messages/Cisco-IOS-XR-infra-syslog-oper:message[Cisco-IOS-XR-infra-syslog-oper:message-id = ' + str(self.message_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.message_id is not None:
                    return True

                if self.card_type is not None:
                    return True

                if self.node_name is not None:
                    return True

                if self.time_stamp is not None:
                    return True

                if self.time_of_day is not None:
                    return True

                if self.time_zone is not None:
                    return True

                if self.process_name is not None:
                    return True

                if self.category is not None:
                    return True

                if self.group is not None:
                    return True

                if self.message_name is not None:
                    return True

                if self.severity is not None:
                    return True

                if self.text is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.Messages.Message']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:messages'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.message is not None:
                for child_ref in self.message:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
            return meta._meta_table['Syslog.Messages']['meta_info']


    class LoggingStatistics(object):
        """
        Logging statistics information
        
        .. attribute:: logging_stats
        
        	Logging statistics
        	**type**\: :py:class:`LoggingStats <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.LoggingStats>`
        
        .. attribute:: console_logging_stats
        
        	Console logging statistics
        	**type**\: :py:class:`ConsoleLoggingStats <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.ConsoleLoggingStats>`
        
        .. attribute:: monitor_logging_stats
        
        	Monitor loggingstatistics
        	**type**\: :py:class:`MonitorLoggingStats <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.MonitorLoggingStats>`
        
        .. attribute:: trap_logging_stats
        
        	Trap logging statistics
        	**type**\: :py:class:`TrapLoggingStats <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.TrapLoggingStats>`
        
        .. attribute:: buffer_logging_stats
        
        	Buffer logging statistics
        	**type**\: :py:class:`BufferLoggingStats <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.BufferLoggingStats>`
        
        .. attribute:: remote_logging_stat
        
        	Remote logging statistics
        	**type**\: list of :py:class:`RemoteLoggingStat <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.RemoteLoggingStat>`
        
        .. attribute:: file_logging_stat
        
        	File logging statistics
        	**type**\: list of :py:class:`FileLoggingStat <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.Syslog.LoggingStatistics.FileLoggingStat>`
        
        

        """

        _prefix = 'infra-syslog-oper'
        _revision = '2015-12-01'

        def __init__(self):
            self.parent = None
            self.logging_stats = Syslog.LoggingStatistics.LoggingStats()
            self.logging_stats.parent = self
            self.console_logging_stats = Syslog.LoggingStatistics.ConsoleLoggingStats()
            self.console_logging_stats.parent = self
            self.monitor_logging_stats = Syslog.LoggingStatistics.MonitorLoggingStats()
            self.monitor_logging_stats.parent = self
            self.trap_logging_stats = Syslog.LoggingStatistics.TrapLoggingStats()
            self.trap_logging_stats.parent = self
            self.buffer_logging_stats = Syslog.LoggingStatistics.BufferLoggingStats()
            self.buffer_logging_stats.parent = self
            self.remote_logging_stat = YList()
            self.remote_logging_stat.parent = self
            self.remote_logging_stat.name = 'remote_logging_stat'
            self.file_logging_stat = YList()
            self.file_logging_stat.parent = self
            self.file_logging_stat.name = 'file_logging_stat'


        class LoggingStats(object):
            """
            Logging statistics
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\: bool
            
            .. attribute:: drop_count
            
            	Number of messages dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: flush_count
            
            	Number of messages flushed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: overrun_count
            
            	Number of messages overrun
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2015-12-01'

            def __init__(self):
                self.parent = None
                self.is_log_enabled = None
                self.drop_count = None
                self.flush_count = None
                self.overrun_count = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:logging-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_log_enabled is not None:
                    return True

                if self.drop_count is not None:
                    return True

                if self.flush_count is not None:
                    return True

                if self.overrun_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.LoggingStats']['meta_info']


        class ConsoleLoggingStats(object):
            """
            Console logging statistics
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\: bool
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\: :py:class:`SystemMessageSeverityEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverityEnum>`
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2015-12-01'

            def __init__(self):
                self.parent = None
                self.is_log_enabled = None
                self.severity = None
                self.message_count = None
                self.buffer_size = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:console-logging-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_log_enabled is not None:
                    return True

                if self.severity is not None:
                    return True

                if self.message_count is not None:
                    return True

                if self.buffer_size is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.ConsoleLoggingStats']['meta_info']


        class MonitorLoggingStats(object):
            """
            Monitor loggingstatistics
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\: bool
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\: :py:class:`SystemMessageSeverityEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverityEnum>`
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2015-12-01'

            def __init__(self):
                self.parent = None
                self.is_log_enabled = None
                self.severity = None
                self.message_count = None
                self.buffer_size = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:monitor-logging-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_log_enabled is not None:
                    return True

                if self.severity is not None:
                    return True

                if self.message_count is not None:
                    return True

                if self.buffer_size is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.MonitorLoggingStats']['meta_info']


        class TrapLoggingStats(object):
            """
            Trap logging statistics
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\: bool
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\: :py:class:`SystemMessageSeverityEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverityEnum>`
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2015-12-01'

            def __init__(self):
                self.parent = None
                self.is_log_enabled = None
                self.severity = None
                self.message_count = None
                self.buffer_size = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:trap-logging-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_log_enabled is not None:
                    return True

                if self.severity is not None:
                    return True

                if self.message_count is not None:
                    return True

                if self.buffer_size is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.TrapLoggingStats']['meta_info']


        class BufferLoggingStats(object):
            """
            Buffer logging statistics
            
            .. attribute:: is_log_enabled
            
            	Is log enabled
            	**type**\: bool
            
            .. attribute:: severity
            
            	Configured severity
            	**type**\: :py:class:`SystemMessageSeverityEnum <ydk.models.infra.Cisco_IOS_XR_infra_syslog_oper.SystemMessageSeverityEnum>`
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: buffer_size
            
            	Buffer size in bytes if logging buffer isenabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2015-12-01'

            def __init__(self):
                self.parent = None
                self.is_log_enabled = None
                self.severity = None
                self.message_count = None
                self.buffer_size = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:buffer-logging-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_log_enabled is not None:
                    return True

                if self.severity is not None:
                    return True

                if self.message_count is not None:
                    return True

                if self.buffer_size is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.BufferLoggingStats']['meta_info']


        class RemoteLoggingStat(object):
            """
            Remote logging statistics
            
            .. attribute:: remote_host_name
            
            	Remote hostname
            	**type**\: str
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2015-12-01'

            def __init__(self):
                self.parent = None
                self.remote_host_name = None
                self.message_count = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:remote-logging-stat'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.remote_host_name is not None:
                    return True

                if self.message_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.RemoteLoggingStat']['meta_info']


        class FileLoggingStat(object):
            """
            File logging statistics
            
            .. attribute:: file_name
            
            	File name for logging messages
            	**type**\: str
            
            .. attribute:: message_count
            
            	Message count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-syslog-oper'
            _revision = '2015-12-01'

            def __init__(self):
                self.parent = None
                self.file_name = None
                self.message_count = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics/Cisco-IOS-XR-infra-syslog-oper:file-logging-stat'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.file_name is not None:
                    return True

                if self.message_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
                return meta._meta_table['Syslog.LoggingStatistics.FileLoggingStat']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-syslog-oper:syslog/Cisco-IOS-XR-infra-syslog-oper:logging-statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.logging_stats is not None and self.logging_stats._has_data():
                return True

            if self.console_logging_stats is not None and self.console_logging_stats._has_data():
                return True

            if self.monitor_logging_stats is not None and self.monitor_logging_stats._has_data():
                return True

            if self.trap_logging_stats is not None and self.trap_logging_stats._has_data():
                return True

            if self.buffer_logging_stats is not None and self.buffer_logging_stats._has_data():
                return True

            if self.remote_logging_stat is not None:
                for child_ref in self.remote_logging_stat:
                    if child_ref._has_data():
                        return True

            if self.file_logging_stat is not None:
                for child_ref in self.file_logging_stat:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
            return meta._meta_table['Syslog.LoggingStatistics']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-syslog-oper:syslog'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.an_remote_servers is not None and self.an_remote_servers._has_data():
            return True

        if self.messages is not None and self.messages._has_data():
            return True

        if self.logging_statistics is not None and self.logging_statistics._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_syslog_oper as meta
        return meta._meta_table['Syslog']['meta_info']


