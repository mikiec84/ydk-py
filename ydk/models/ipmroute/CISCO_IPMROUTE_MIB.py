""" CISCO_IPMROUTE_MIB 

The MIB module for management of IP Multicast routing,
but independent of the specific multicast routing protocol
in use.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class CISCOIPMROUTEMIB(object):
    """
    
    
    .. attribute:: ciscoipmroute
    
    	
    	**type**\: :py:class:`CiscoIpMRoute <ydk.models.ipmroute.CISCO_IPMROUTE_MIB.CISCOIPMROUTEMIB.CiscoIpMRoute>`
    
    .. attribute:: ciscoipmrouteheartbeattable
    
    	The (conceptual) table listing sets of IP Multicast heartbeat parameters.  If no IP Multicast heartbeat is configured, this table would be empty
    	**type**\: :py:class:`CiscoIpMRouteHeartBeatTable <ydk.models.ipmroute.CISCO_IPMROUTE_MIB.CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable>`
    
    

    """

    _prefix = 'cisco-ipmroute'
    _revision = '2005-03-07'

    def __init__(self):
        self.ciscoipmroute = CISCOIPMROUTEMIB.CiscoIpMRoute()
        self.ciscoipmroute.parent = self
        self.ciscoipmrouteheartbeattable = CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable()
        self.ciscoipmrouteheartbeattable.parent = self


    class CiscoIpMRoute(object):
        """
        
        
        .. attribute:: ciscoipmroutenumberofentries
        
        	Maintains a count of the number of entries in the ipMRouteTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-ipmroute'
        _revision = '2005-03-07'

        def __init__(self):
            self.parent = None
            self.ciscoipmroutenumberofentries = None

        @property
        def _common_path(self):

            return '/CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB/CISCO-IPMROUTE-MIB:ciscoIpMRoute'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoipmroutenumberofentries is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipmroute._meta import _CISCO_IPMROUTE_MIB as meta
            return meta._meta_table['CISCOIPMROUTEMIB.CiscoIpMRoute']['meta_info']


    class CiscoIpMRouteHeartBeatTable(object):
        """
        The (conceptual) table listing sets of IP Multicast
        heartbeat parameters.  If no IP Multicast heartbeat is
        configured, this table would be empty.
        
        .. attribute:: ciscoipmrouteheartbeatentry
        
        	An entry (conceptual row) representing a set of IP Multicast heartbeat parameters
        	**type**\: list of :py:class:`CiscoIpMRouteHeartBeatEntry <ydk.models.ipmroute.CISCO_IPMROUTE_MIB.CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable.CiscoIpMRouteHeartBeatEntry>`
        
        

        """

        _prefix = 'cisco-ipmroute'
        _revision = '2005-03-07'

        def __init__(self):
            self.parent = None
            self.ciscoipmrouteheartbeatentry = YList()
            self.ciscoipmrouteheartbeatentry.parent = self
            self.ciscoipmrouteheartbeatentry.name = 'ciscoipmrouteheartbeatentry'


        class CiscoIpMRouteHeartBeatEntry(object):
            """
            An entry (conceptual row) representing a set of IP
            Multicast heartbeat parameters.
            
            .. attribute:: ciscoipmrouteheartbeatgroupaddr
            
            	Multicast group address used to receive heartbeat packets
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ciscoipmrouteheartbeatalerttime
            
            	The value of sysUpTime on the most recent occasion at which a missing IP multicast heartbeat condition occured for the group address specified in this entry.  If no such condition have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmrouteheartbeatcount
            
            	Number of time intervals where multicast packets were received in the last ciscoIpMRouteHeartBeatWindowSize intervals
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoipmrouteheartbeatinterval
            
            	Number of seconds in which a Cisco multicast router expects a valid heartBeat packet from a source.  This value must be a multiple of 10
            	**type**\: int
            
            	**range:** 10..3600
            
            .. attribute:: ciscoipmrouteheartbeatminimum
            
            	The minimal number of heartbeat packets expected in the last ciscoIpMRouteHeartBeatWindowSize intervals. If ciscoIpMRouteHeartBeatCount falls below this value, an SNMP trap/notification, if configured, will be sent to the NMS
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: ciscoipmrouteheartbeatsourceaddr
            
            	Source address of the last multicast heartbeat packet received
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ciscoipmrouteheartbeatstatus
            
            	This object is used to create a new row or delete an existing row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ciscoipmrouteheartbeatwindowsize
            
            	Number of ciscoIpMRouteHeartBeatInterval intervals a Cisco multicast router waits before checking if expected number of heartbeat packets are received or not
            	**type**\: int
            
            	**range:** 1..100
            
            

            """

            _prefix = 'cisco-ipmroute'
            _revision = '2005-03-07'

            def __init__(self):
                self.parent = None
                self.ciscoipmrouteheartbeatgroupaddr = None
                self.ciscoipmrouteheartbeatalerttime = None
                self.ciscoipmrouteheartbeatcount = None
                self.ciscoipmrouteheartbeatinterval = None
                self.ciscoipmrouteheartbeatminimum = None
                self.ciscoipmrouteheartbeatsourceaddr = None
                self.ciscoipmrouteheartbeatstatus = None
                self.ciscoipmrouteheartbeatwindowsize = None

            @property
            def _common_path(self):
                if self.ciscoipmrouteheartbeatgroupaddr is None:
                    raise YPYDataValidationError('Key property ciscoipmrouteheartbeatgroupaddr is None')

                return '/CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB/CISCO-IPMROUTE-MIB:ciscoIpMRouteHeartBeatTable/CISCO-IPMROUTE-MIB:ciscoIpMRouteHeartBeatEntry[CISCO-IPMROUTE-MIB:ciscoIpMRouteHeartBeatGroupAddr = ' + str(self.ciscoipmrouteheartbeatgroupaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscoipmrouteheartbeatgroupaddr is not None:
                    return True

                if self.ciscoipmrouteheartbeatalerttime is not None:
                    return True

                if self.ciscoipmrouteheartbeatcount is not None:
                    return True

                if self.ciscoipmrouteheartbeatinterval is not None:
                    return True

                if self.ciscoipmrouteheartbeatminimum is not None:
                    return True

                if self.ciscoipmrouteheartbeatsourceaddr is not None:
                    return True

                if self.ciscoipmrouteheartbeatstatus is not None:
                    return True

                if self.ciscoipmrouteheartbeatwindowsize is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipmroute._meta import _CISCO_IPMROUTE_MIB as meta
                return meta._meta_table['CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable.CiscoIpMRouteHeartBeatEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB/CISCO-IPMROUTE-MIB:ciscoIpMRouteHeartBeatTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoipmrouteheartbeatentry is not None:
                for child_ref in self.ciscoipmrouteheartbeatentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipmroute._meta import _CISCO_IPMROUTE_MIB as meta
            return meta._meta_table['CISCOIPMROUTEMIB.CiscoIpMRouteHeartBeatTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IPMROUTE-MIB:CISCO-IPMROUTE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ciscoipmroute is not None and self.ciscoipmroute._has_data():
            return True

        if self.ciscoipmroute is not None and self.ciscoipmroute.is_presence():
            return True

        if self.ciscoipmrouteheartbeattable is not None and self.ciscoipmrouteheartbeattable._has_data():
            return True

        if self.ciscoipmrouteheartbeattable is not None and self.ciscoipmrouteheartbeattable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipmroute._meta import _CISCO_IPMROUTE_MIB as meta
        return meta._meta_table['CISCOIPMROUTEMIB']['meta_info']


