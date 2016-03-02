""" TUNNEL_MIB 

The MIB module for management of IP Tunnels,
independent of the specific encapsulation scheme in
use.

Copyright (C) The Internet Society (2005).  This
version of this MIB module is part of RFC 4087;  see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.ianaiftype.IANAifType_MIB import IANAtunnelType_Enum
from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class TUNNELMIB(object):
    """
    
    
    .. attribute:: tunnelconfigtable
    
    	The (conceptual) table containing information on configured tunnels.  This table can be used to map a set of tunnel endpoints to the associated ifIndex value.  It can also be used for row creation.  Note that every row in the tunnelIfTable with a fixed IPv4 destination address should have a corresponding row in the tunnelConfigTable, regardless of whether it was created via SNMP.  Since this table does not support IPv6, it is deprecated in favor of tunnelInetConfigTable
    	**type**\: :py:class:`TunnelConfigTable <ydk.models.tunnel.TUNNEL_MIB.TUNNELMIB.TunnelConfigTable>`
    
    .. attribute:: tunneliftable
    
    	The (conceptual) table containing information on configured tunnels
    	**type**\: :py:class:`TunnelIfTable <ydk.models.tunnel.TUNNEL_MIB.TUNNELMIB.TunnelIfTable>`
    
    .. attribute:: tunnelinetconfigtable
    
    	The (conceptual) table containing information on configured tunnels.  This table can be used to map a set of tunnel endpoints to the associated ifIndex value.  It can also be used for row creation.  Note that every row in the tunnelIfTable with a fixed destination address should have a corresponding row in the tunnelInetConfigTable, regardless of whether it was created via SNMP
    	**type**\: :py:class:`TunnelInetConfigTable <ydk.models.tunnel.TUNNEL_MIB.TUNNELMIB.TunnelInetConfigTable>`
    
    

    """

    _prefix = 'tunnel-mib'
    _revision = '2005-05-16'

    def __init__(self):
        self.tunnelconfigtable = TUNNELMIB.TunnelConfigTable()
        self.tunnelconfigtable.parent = self
        self.tunneliftable = TUNNELMIB.TunnelIfTable()
        self.tunneliftable.parent = self
        self.tunnelinetconfigtable = TUNNELMIB.TunnelInetConfigTable()
        self.tunnelinetconfigtable.parent = self


    class TunnelConfigTable(object):
        """
        The (conceptual) table containing information on
        configured tunnels.  This table can be used to map a
        set of tunnel endpoints to the associated ifIndex
        value.  It can also be used for row creation.  Note
        that every row in the tunnelIfTable with a fixed IPv4
        destination address should have a corresponding row in
        the tunnelConfigTable, regardless of whether it was
        created via SNMP.
        
        Since this table does not support IPv6, it is
        deprecated in favor of tunnelInetConfigTable.
        
        .. attribute:: tunnelconfigentry
        
        	An entry (conceptual row) containing the information on a particular configured tunnel.  Since this entry does not support IPv6, it is deprecated in favor of tunnelInetConfigEntry
        	**type**\: list of :py:class:`TunnelConfigEntry <ydk.models.tunnel.TUNNEL_MIB.TUNNELMIB.TunnelConfigTable.TunnelConfigEntry>`
        
        

        """

        _prefix = 'tunnel-mib'
        _revision = '2005-05-16'

        def __init__(self):
            self.parent = None
            self.tunnelconfigentry = YList()
            self.tunnelconfigentry.parent = self
            self.tunnelconfigentry.name = 'tunnelconfigentry'


        class TunnelConfigEntry(object):
            """
            An entry (conceptual row) containing the information
            on a particular configured tunnel.
            
            Since this entry does not support IPv6, it is
            deprecated in favor of tunnelInetConfigEntry.
            
            .. attribute:: tunnelconfigencapsmethod
            
            	The encapsulation method used by the tunnel.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigEncapsMethod
            	**type**\: :py:class:`IANAtunnelType_Enum <ydk.models.ianaiftype.IANAifType_MIB.IANAtunnelType_Enum>`
            
            .. attribute:: tunnelconfigid
            
            	An identifier used to distinguish between multiple tunnels of the same encapsulation method, with the same endpoints.  If the encapsulation protocol only allows one tunnel per set of endpoint addresses (such as for GRE or IP\-in\-IP), the value of this object is 1.  For encapsulation methods (such as L2F) which allow multiple parallel tunnels, the manager is responsible for choosing any ID which does not conflict with an existing row, such as choosing a random number.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigID
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: tunnelconfiglocaladdress
            
            	The address of the local endpoint of the tunnel, or 0.0.0.0 if the device is free to choose any of its addresses at tunnel establishment time.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigLocalAddress
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tunnelconfigremoteaddress
            
            	The address of the remote endpoint of the tunnel.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigRemoteAddress
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tunnelconfigifindex
            
            	If the value of tunnelConfigStatus for this row is active, then this object contains the value of ifIndex corresponding to the tunnel interface.  A value of 0 is not legal in the active state, and means that the interface index has not yet been assigned.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigIfIndex
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: tunnelconfigstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table.  The agent need not support setting this object to createAndWait or notInService since there are no other writable objects in this table, and writable objects in rows of corresponding tables such as the tunnelIfTable may be modified while this row is active.  To create a row in this table for an encapsulation method which does not support multiple parallel tunnels with the same endpoints, the management station should simply use a tunnelConfigID of 1, and set tunnelConfigStatus to createAndGo.  For encapsulation methods such as L2F which allow multiple parallel tunnels, the management station may select a pseudo\-random number to use as the tunnelConfigID and set tunnelConfigStatus to createAndGo.  In the event that this ID is already in use and an inconsistentValue is returned in response to the set operation, the management station should simply select a new pseudo\-random number and retry the operation.  Creating a row in this table will cause an interface index to be assigned by the agent in an implementation\-dependent manner, and corresponding rows will be instantiated in the ifTable and the tunnelIfTable.  The status of this row will become active as soon as the agent assigns the interface index, regardless of whether the interface is operationally up.  Deleting a row in this table will likewise delete the corresponding row in the ifTable and in the tunnelIfTable.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigStatus
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'tunnel-mib'
            _revision = '2005-05-16'

            def __init__(self):
                self.parent = None
                self.tunnelconfigencapsmethod = None
                self.tunnelconfigid = None
                self.tunnelconfiglocaladdress = None
                self.tunnelconfigremoteaddress = None
                self.tunnelconfigifindex = None
                self.tunnelconfigstatus = None

            @property
            def _common_path(self):
                if self.tunnelconfigencapsmethod is None:
                    raise YPYDataValidationError('Key property tunnelconfigencapsmethod is None')
                if self.tunnelconfigid is None:
                    raise YPYDataValidationError('Key property tunnelconfigid is None')
                if self.tunnelconfiglocaladdress is None:
                    raise YPYDataValidationError('Key property tunnelconfiglocaladdress is None')
                if self.tunnelconfigremoteaddress is None:
                    raise YPYDataValidationError('Key property tunnelconfigremoteaddress is None')

                return '/TUNNEL-MIB:TUNNEL-MIB/TUNNEL-MIB:tunnelConfigTable/TUNNEL-MIB:tunnelConfigEntry[TUNNEL-MIB:tunnelConfigEncapsMethod = ' + str(self.tunnelconfigencapsmethod) + '][TUNNEL-MIB:tunnelConfigID = ' + str(self.tunnelconfigid) + '][TUNNEL-MIB:tunnelConfigLocalAddress = ' + str(self.tunnelconfiglocaladdress) + '][TUNNEL-MIB:tunnelConfigRemoteAddress = ' + str(self.tunnelconfigremoteaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.tunnelconfigencapsmethod is not None:
                    return True

                if self.tunnelconfigid is not None:
                    return True

                if self.tunnelconfiglocaladdress is not None:
                    return True

                if self.tunnelconfigremoteaddress is not None:
                    return True

                if self.tunnelconfigifindex is not None:
                    return True

                if self.tunnelconfigstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tunnel._meta import _TUNNEL_MIB as meta
                return meta._meta_table['TUNNELMIB.TunnelConfigTable.TunnelConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TUNNEL-MIB:TUNNEL-MIB/TUNNEL-MIB:tunnelConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tunnelconfigentry is not None:
                for child_ref in self.tunnelconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tunnel._meta import _TUNNEL_MIB as meta
            return meta._meta_table['TUNNELMIB.TunnelConfigTable']['meta_info']


    class TunnelIfTable(object):
        """
        The (conceptual) table containing information on
        configured tunnels.
        
        .. attribute:: tunnelifentry
        
        	An entry (conceptual row) containing the information on a particular configured tunnel
        	**type**\: list of :py:class:`TunnelIfEntry <ydk.models.tunnel.TUNNEL_MIB.TUNNELMIB.TunnelIfTable.TunnelIfEntry>`
        
        

        """

        _prefix = 'tunnel-mib'
        _revision = '2005-05-16'

        def __init__(self):
            self.parent = None
            self.tunnelifentry = YList()
            self.tunnelifentry.parent = self
            self.tunnelifentry.name = 'tunnelifentry'


        class TunnelIfEntry(object):
            """
            An entry (conceptual row) containing the information
            on a particular configured tunnel.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: tunnelifaddresstype
            
            	The type of address in the corresponding tunnelIfLocalInetAddress and tunnelIfRemoteInetAddress objects
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: tunnelifencapslimit
            
            	The maximum number of additional encapsulations permitted for packets undergoing encapsulation at this node.  A value of \-1 indicates that no limit is present (except as a result of the packet size)
            	**type**\: int
            
            	**range:** \-1..255
            
            .. attribute:: tunnelifencapsmethod
            
            	The encapsulation method used by the tunnel
            	**type**\: :py:class:`IANAtunnelType_Enum <ydk.models.ianaiftype.IANAifType_MIB.IANAtunnelType_Enum>`
            
            .. attribute:: tunnelifflowlabel
            
            	The method used to set the IPv6 Flow Label value. This object need not be present in rows where tunnelIfAddressType indicates the tunnel is not over IPv6.  A value of \-1 indicates that a traffic conditioner is invoked and more information may be available in a traffic conditioner MIB.  Any other value indicates that the Flow Label field is set to the indicated value
            	**type**\: int
            
            	**range:** \-1..100
            
            .. attribute:: tunnelifhoplimit
            
            	The IPv4 TTL or IPv6 Hop Limit to use in the outer IP header.  A value of 0 indicates that the value is copied from the payload's header
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: tunneliflocaladdress
            
            	The address of the local endpoint of the tunnel (i.e., the source address used in the outer IP header), or 0.0.0.0 if unknown or if the tunnel is over IPv6.  Since this object does not support IPv6, it is deprecated in favor of tunnelIfLocalInetAddress
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tunneliflocalinetaddress
            
            	The address of the local endpoint of the tunnel (i.e., the source address used in the outer IP header).  If the address is unknown, the value is  0.0.0.0 for IPv4 or \:\: for IPv6.  The type of this object is given by tunnelIfAddressType
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: tunnelifremoteaddress
            
            	The address of the remote endpoint of the tunnel (i.e., the destination address used in the outer IP header), or 0.0.0.0 if unknown, or an IPv6 address, or  the tunnel is not a point\-to\-point link (e.g., if it is a 6to4 tunnel).  Since this object does not support IPv6, it is deprecated in favor of tunnelIfRemoteInetAddress
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tunnelifremoteinetaddress
            
            	The address of the remote endpoint of the tunnel (i.e., the destination address used in the outer IP header).  If the address is unknown or the tunnel is not a point\-to\-point link (e.g., if it is a 6to4 tunnel), the value is 0.0.0.0 for tunnels over IPv4 or \:\: for tunnels over IPv6.  The type of this object is given by tunnelIfAddressType
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: tunnelifsecurity
            
            	The method used by the tunnel to secure the outer IP header.  The value ipsec indicates that IPsec is used between the tunnel endpoints for authentication or encryption or both.  More specific security\-related information may be available in a MIB module for the security protocol in use
            	**type**\: :py:class:`TunnelIfSecurity_Enum <ydk.models.tunnel.TUNNEL_MIB.TUNNELMIB.TunnelIfTable.TunnelIfEntry.TunnelIfSecurity_Enum>`
            
            .. attribute:: tunneliftos
            
            	The method used to set the high 6 bits (the  differentiated services codepoint) of the IPv4 TOS or IPv6 Traffic Class in the outer IP header.  A value of \-1 indicates that the bits are copied from the payload's header.  A value of \-2 indicates that a traffic conditioner is invoked and more information may be available in a traffic conditioner MIB module. A value between 0 and 63 inclusive indicates that the bit field is set to the indicated value.  Note\: instead of the name tunnelIfTOS, a better name would have been tunnelIfDSCPMethod, but the existing name appeared in RFC 2667 and existing objects cannot be renamed
            	**type**\: int
            
            	**range:** \-2..63
            
            

            """

            _prefix = 'tunnel-mib'
            _revision = '2005-05-16'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.tunnelifaddresstype = None
                self.tunnelifencapslimit = None
                self.tunnelifencapsmethod = None
                self.tunnelifflowlabel = None
                self.tunnelifhoplimit = None
                self.tunneliflocaladdress = None
                self.tunneliflocalinetaddress = None
                self.tunnelifremoteaddress = None
                self.tunnelifremoteinetaddress = None
                self.tunnelifsecurity = None
                self.tunneliftos = None

            class TunnelIfSecurity_Enum(Enum):
                """
                TunnelIfSecurity_Enum

                The method used by the tunnel to secure the outer IP
                header.  The value ipsec indicates that IPsec is used
                between the tunnel endpoints for authentication or
                encryption or both.  More specific security\-related
                information may be available in a MIB module for the
                security protocol in use.

                """

                NONE = 1

                IPSEC = 2

                OTHER = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.tunnel._meta import _TUNNEL_MIB as meta
                    return meta._meta_table['TUNNELMIB.TunnelIfTable.TunnelIfEntry.TunnelIfSecurity_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/TUNNEL-MIB:TUNNEL-MIB/TUNNEL-MIB:tunnelIfTable/TUNNEL-MIB:tunnelIfEntry[TUNNEL-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.tunnelifaddresstype is not None:
                    return True

                if self.tunnelifencapslimit is not None:
                    return True

                if self.tunnelifencapsmethod is not None:
                    return True

                if self.tunnelifflowlabel is not None:
                    return True

                if self.tunnelifhoplimit is not None:
                    return True

                if self.tunneliflocaladdress is not None:
                    return True

                if self.tunneliflocalinetaddress is not None:
                    return True

                if self.tunnelifremoteaddress is not None:
                    return True

                if self.tunnelifremoteinetaddress is not None:
                    return True

                if self.tunnelifsecurity is not None:
                    return True

                if self.tunneliftos is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tunnel._meta import _TUNNEL_MIB as meta
                return meta._meta_table['TUNNELMIB.TunnelIfTable.TunnelIfEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TUNNEL-MIB:TUNNEL-MIB/TUNNEL-MIB:tunnelIfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tunnelifentry is not None:
                for child_ref in self.tunnelifentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tunnel._meta import _TUNNEL_MIB as meta
            return meta._meta_table['TUNNELMIB.TunnelIfTable']['meta_info']


    class TunnelInetConfigTable(object):
        """
        The (conceptual) table containing information on
        configured tunnels.  This table can be used to map a
        set of tunnel endpoints to the associated ifIndex
        value.  It can also be used for row creation.  Note
        that every row in the tunnelIfTable with a fixed
        destination address should have a corresponding row in
        the tunnelInetConfigTable, regardless of whether it
        was created via SNMP.
        
        .. attribute:: tunnelinetconfigentry
        
        	An entry (conceptual row) containing the information on a particular configured tunnel.  Note that there is a 128 subid maximum for object OIDs.  Implementers need to be aware that if the total number of octets in tunnelInetConfigLocalAddress and tunnelInetConfigRemoteAddress exceeds 110 then OIDs of column instances in this table will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.  In practice this is not expected to be a problem since IPv4 and IPv6 addresses will not cause the limit to be reached, but if other types are supported by an agent, care must be taken to ensure that the sum of the lengths do not cause the limit to be exceeded
        	**type**\: list of :py:class:`TunnelInetConfigEntry <ydk.models.tunnel.TUNNEL_MIB.TUNNELMIB.TunnelInetConfigTable.TunnelInetConfigEntry>`
        
        

        """

        _prefix = 'tunnel-mib'
        _revision = '2005-05-16'

        def __init__(self):
            self.parent = None
            self.tunnelinetconfigentry = YList()
            self.tunnelinetconfigentry.parent = self
            self.tunnelinetconfigentry.name = 'tunnelinetconfigentry'


        class TunnelInetConfigEntry(object):
            """
            An entry (conceptual row) containing the information
            on a particular configured tunnel.  Note that there is
            a 128 subid maximum for object OIDs.  Implementers
            need to be aware that if the total number of octets in
            tunnelInetConfigLocalAddress and
            tunnelInetConfigRemoteAddress exceeds 110 then OIDs of
            column instances in this table will have more than 128
            sub\-identifiers and cannot be accessed using SNMPv1,
            SNMPv2c, or SNMPv3.  In practice this is not expected
            to be a problem since IPv4 and IPv6 addresses will not
            cause the limit to be reached, but if other types are
            supported by an agent, care must be taken to ensure
            that the sum of the lengths do not cause the limit to
            be exceeded.
            
            .. attribute:: tunnelinetconfigaddresstype
            
            	The address type over which the tunnel encapsulates packets
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: tunnelinetconfigencapsmethod
            
            	The encapsulation method used by the tunnel
            	**type**\: :py:class:`IANAtunnelType_Enum <ydk.models.ianaiftype.IANAifType_MIB.IANAtunnelType_Enum>`
            
            .. attribute:: tunnelinetconfigid
            
            	An identifier used to distinguish between multiple tunnels of the same encapsulation method, with the same endpoints.  If the encapsulation protocol only allows one tunnel per set of endpoint addresses (such as for GRE or IP\-in\-IP), the value of this object is 1.  For encapsulation methods (such as L2F) which allow multiple parallel tunnels, the manager is responsible for choosing any ID which does not  conflict with an existing row, such as choosing a random number
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: tunnelinetconfiglocaladdress
            
            	The address of the local endpoint of the tunnel, or 0.0.0.0 (for IPv4) or \:\: (for IPv6) if the device is free to choose any of its addresses at tunnel establishment time
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: tunnelinetconfigremoteaddress
            
            	The address of the remote endpoint of the tunnel
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: tunnelinetconfigifindex
            
            	If the value of tunnelInetConfigStatus for this row is active, then this object contains the value of ifIndex corresponding to the tunnel interface.  A value of 0 is not legal in the active state, and means that the interface index has not yet been assigned
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: tunnelinetconfigstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table.  The agent need not support setting this object to createAndWait or notInService since there are no other writable objects in this table, and writable objects in rows of corresponding tables such as the tunnelIfTable may be modified while this row is active.  To create a row in this table for an encapsulation method which does not support multiple parallel tunnels with the same endpoints, the management station should simply use a tunnelInetConfigID of 1, and set tunnelInetConfigStatus to createAndGo.  For encapsulation methods such as L2F which allow multiple parallel tunnels, the management station may select a pseudo\-random number to use as the tunnelInetConfigID and set tunnelInetConfigStatus to createAndGo.  In the event that this ID is already in use and an inconsistentValue is returned in response to the set operation, the management station should simply select a new pseudo\-random number and retry the operation.  Creating a row in this table will cause an interface index to be assigned by the agent in an implementation\-dependent manner, and corresponding rows will be instantiated in the ifTable and the  tunnelIfTable.  The status of this row will become active as soon as the agent assigns the interface index, regardless of whether the interface is operationally up.  Deleting a row in this table will likewise delete the corresponding row in the ifTable and in the tunnelIfTable
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: tunnelinetconfigstoragetype
            
            	The storage type of this row.  If the row is permanent(4), no objects in the row need be writable
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'tunnel-mib'
            _revision = '2005-05-16'

            def __init__(self):
                self.parent = None
                self.tunnelinetconfigaddresstype = None
                self.tunnelinetconfigencapsmethod = None
                self.tunnelinetconfigid = None
                self.tunnelinetconfiglocaladdress = None
                self.tunnelinetconfigremoteaddress = None
                self.tunnelinetconfigifindex = None
                self.tunnelinetconfigstatus = None
                self.tunnelinetconfigstoragetype = None

            @property
            def _common_path(self):
                if self.tunnelinetconfigaddresstype is None:
                    raise YPYDataValidationError('Key property tunnelinetconfigaddresstype is None')
                if self.tunnelinetconfigencapsmethod is None:
                    raise YPYDataValidationError('Key property tunnelinetconfigencapsmethod is None')
                if self.tunnelinetconfigid is None:
                    raise YPYDataValidationError('Key property tunnelinetconfigid is None')
                if self.tunnelinetconfiglocaladdress is None:
                    raise YPYDataValidationError('Key property tunnelinetconfiglocaladdress is None')
                if self.tunnelinetconfigremoteaddress is None:
                    raise YPYDataValidationError('Key property tunnelinetconfigremoteaddress is None')

                return '/TUNNEL-MIB:TUNNEL-MIB/TUNNEL-MIB:tunnelInetConfigTable/TUNNEL-MIB:tunnelInetConfigEntry[TUNNEL-MIB:tunnelInetConfigAddressType = ' + str(self.tunnelinetconfigaddresstype) + '][TUNNEL-MIB:tunnelInetConfigEncapsMethod = ' + str(self.tunnelinetconfigencapsmethod) + '][TUNNEL-MIB:tunnelInetConfigID = ' + str(self.tunnelinetconfigid) + '][TUNNEL-MIB:tunnelInetConfigLocalAddress = ' + str(self.tunnelinetconfiglocaladdress) + '][TUNNEL-MIB:tunnelInetConfigRemoteAddress = ' + str(self.tunnelinetconfigremoteaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.tunnelinetconfigaddresstype is not None:
                    return True

                if self.tunnelinetconfigencapsmethod is not None:
                    return True

                if self.tunnelinetconfigid is not None:
                    return True

                if self.tunnelinetconfiglocaladdress is not None:
                    return True

                if self.tunnelinetconfigremoteaddress is not None:
                    return True

                if self.tunnelinetconfigifindex is not None:
                    return True

                if self.tunnelinetconfigstatus is not None:
                    return True

                if self.tunnelinetconfigstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tunnel._meta import _TUNNEL_MIB as meta
                return meta._meta_table['TUNNELMIB.TunnelInetConfigTable.TunnelInetConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TUNNEL-MIB:TUNNEL-MIB/TUNNEL-MIB:tunnelInetConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tunnelinetconfigentry is not None:
                for child_ref in self.tunnelinetconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tunnel._meta import _TUNNEL_MIB as meta
            return meta._meta_table['TUNNELMIB.TunnelInetConfigTable']['meta_info']

    @property
    def _common_path(self):

        return '/TUNNEL-MIB:TUNNEL-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.tunnelconfigtable is not None and self.tunnelconfigtable._has_data():
            return True

        if self.tunnelconfigtable is not None and self.tunnelconfigtable.is_presence():
            return True

        if self.tunneliftable is not None and self.tunneliftable._has_data():
            return True

        if self.tunneliftable is not None and self.tunneliftable.is_presence():
            return True

        if self.tunnelinetconfigtable is not None and self.tunnelinetconfigtable._has_data():
            return True

        if self.tunnelinetconfigtable is not None and self.tunnelinetconfigtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.tunnel._meta import _TUNNEL_MIB as meta
        return meta._meta_table['TUNNELMIB']['meta_info']


