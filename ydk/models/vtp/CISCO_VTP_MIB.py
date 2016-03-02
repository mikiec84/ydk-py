""" CISCO_VTP_MIB 

The MIB module for entities implementing the VTP
protocol and Vlan management.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum

class VlanType_Enum(Enum):
    """
    VlanType_Enum

    The type of a VLAN.
    
    Note that the 'ethernet' type, is used for any ethernet or
    802.3 VLAN, including an ATM Ethernet ELAN; and the
    'tokenRing' ('trCrf') type is used for each VLAN
    representing a single logical 802.5 ring including an ATM
    Token\-Ring ELAN.
    
    The 'trCrf' type is used for token ring VLANs made up of
    (at most) one transparently bridged LAN segment.
    
    The 'trBrf' type is used for VLANs which represent the
    scope of many 'trCrf' VLANs all connected together via
    source route bridging.  The token ring 'trBrf' can be said
    to represent the bridged broadcast domain.

    """

    ETHERNET = 1

    FDDI = 2

    TOKENRING = 3

    FDDINET = 4

    TRNET = 5

    DEPRECATED = 6


    @staticmethod
    def _meta_info():
        from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
        return meta._meta_table['VlanType_Enum']


class VlanTypeExt_Bits(FixedBitsDict):
    """
    VlanTypeExt_Bits

    The additional type information of VLAN.
    vtpmanageable(0)    An user defined VLAN which is 
                        manageable through VTP protocol.
                        The value of this bit cannot be 
                        changed.
    internal(1)         An internal VLAN created by the device.
                        Internal VLANs cannot be created or
                        deleted. The value of this bit cannot
                        be changed.
    reserved(2)         A VLAN reserved by the device.
                        Reserved VLANs cannot be created or
                        deleted. The value of this bit cannot
                        be changed.
    rspan(3)            A VLAN created to exclusively carry
                        the traffic for a Remote Switched
                        Port Analyzer (RSPAN). This bit can
                        only be set or cleared during the
                        VLAN creation. Once the VLAN is
                        created, the value of this bit cannot
                        be modified.
    dynamicGvrp(4)      A VLAN dynamically created by GVRP
                        (GARP VLAN Registration Protocol)
                        propagation. The value of this bit 
                        cannot be changed.
    Keys are:- dynamicGvrp , vtpmanageable , internal , reserved , rspan

    """

    def __init__(self):
        self._dictionary = { 
            'dynamicGvrp':False,
            'vtpmanageable':False,
            'internal':False,
            'reserved':False,
            'rspan':False,
        }
        self._pos_map = { 
            'dynamicGvrp':4,
            'vtpmanageable':0,
            'internal':1,
            'reserved':2,
            'rspan':3,
        }


class CISCOVTPMIB(object):
    """
    
    
    .. attribute:: internalvlaninfo
    
    	
    	**type**\: :py:class:`InternalVlanInfo <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.InternalVlanInfo>`
    
    .. attribute:: managementdomaintable
    
    	The table containing information on the management domains in which the local system is participating.  Devices which support only one management domain will support just one row in this table, and will not let it be deleted nor let other rows be created.  Devices which support multiple management domains will allow rows to be created and deleted, but will not allow the last row to be deleted. If the device does  not support VTP, the table is read\-only
    	**type**\: :py:class:`ManagementDomainTable <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.ManagementDomainTable>`
    
    .. attribute:: vlanstatistics
    
    	
    	**type**\: :py:class:`VlanStatistics <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VlanStatistics>`
    
    .. attribute:: vlantrunkports
    
    	
    	**type**\: :py:class:`VlanTrunkPorts <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VlanTrunkPorts>`
    
    .. attribute:: vlantrunkporttable
    
    	The table containing information on the local system's VLAN trunk ports
    	**type**\: :py:class:`VlanTrunkPortTable <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VlanTrunkPortTable>`
    
    .. attribute:: vtpauthenticationtable
    
    	The table contains the authentication information of VTP in which the local system participates.  The security mechanism of VTP relies on a secret key that is used to alter the MD5 digest of the packets transmitted on the wire.  The secret value is created from a password that may be saved in plain text in the configuration or hidden from the configuration.  The device creating or modifying the VTP configuration signs it using the MD5 digest generated from the secret key before advertising it. Other devices in the domain receive this configuration use the same secret key to accept it if correctly signed or drop it otherwise.  The user has the option to hide the password from the configuration. Once the password is hidden, the secret key generated from the password is shown in the  configuration instead, and there is no other way to  show the password in plain text again but clearing  it or resetting it.   In an un\-trusted area, the password on a device can  be configured without being unveiled. After that, it has to be provided again by setting the same  value to vtpDatabaseTakeOverPassword if the user  wants to take over the whole VTP management domain of the database type.  When managementDomainVersionInUse is version3(4), the  authentication mechanism is common to all VTP database type
    	**type**\: :py:class:`VtpAuthenticationTable <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpAuthenticationTable>`
    
    .. attribute:: vtpdatabasetable
    
    	This table contains information of the VTP databases. It is not instantiated when managementDomainVersionInUse is version1(1),  version2(3) or none(3)
    	**type**\: :py:class:`VtpDatabaseTable <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpDatabaseTable>`
    
    .. attribute:: vtpdiscoverresulttable
    
    	The table containing information of discovered VTP members in the management domain in which the local system is participating. This table is not instantiated when  managementDomainVersionInUse is version1(1), version2(2) or none(3)
    	**type**\: :py:class:`VtpDiscoverResultTable <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpDiscoverResultTable>`
    
    .. attribute:: vtpdiscovertable
    
    	This table contains information related to the discovery of the VTP members in the designated management domain. This table is not instantiated when  managementDomainVersionInUse is version1(1), version2(3) or none(3)
    	**type**\: :py:class:`VtpDiscoverTable <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpDiscoverTable>`
    
    .. attribute:: vtpinternalvlantable
    
    	A vtpInternalVlanTable entry contains information on an existing internal VLAN. It is internally created by the device for a specific application program  and hence owned by the application.   It cannot be modified or deleted by (local  or network) management
    	**type**\: :py:class:`VtpInternalVlanTable <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpInternalVlanTable>`
    
    .. attribute:: vtpstatus
    
    	
    	**type**\: :py:class:`VtpStatus <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpStatus>`
    
    .. attribute:: vtpvlanedittable
    
    	The table which contains the information in the Edit Buffers, one Edit Buffer per management domain.  The information for a particular management domain is initialized, by a 'copy' operation, to be the current global VLAN information for that management domain.  After initialization, editing can be performed to add VLANs, delete VLANs, or modify their global parameters.  The information as modified through editing is local to this Edit Buffer.  An apply operation using the vtpVlanEditOperation object is necessary to instanciate the modified information as the new global VLAN information for that management domain.  To use the Edit Buffer, a manager acts as follows\:  1. ensures the Edit Buffer for a management domain is empty, i.e., there are no rows in this table for this management domain.  2. issues a SNMP set operation which sets vtpVlanEditOperation to 'copy', and vtpVlanEditBufferOwner to its own identifier (e.g., its own IP address).  3. if this set operation is successful, proceeds to edit the information in the vtpVlanEditTable.  4. if and when the edited information is to be instantiated, issues a SNMP set operation which sets vtpVlanEditOperation to 'apply'.  5. issues retrieval requests to obtain the value of vtpVlanApplyStatus, until the result of the apply is determined.  6. releases the Edit Buffer by issuing a SNMP set operation which sets vtpVlanEditOperation to 'release'.  Note that the information contained in this table is not saved across agent reboots
    	**type**\: :py:class:`VtpVlanEditTable <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanEditTable>`
    
    .. attribute:: vtpvlanlocalshutdowntable
    
    	Ths table contains the VLAN local shutdown information within management domain
    	**type**\: :py:class:`VtpVlanLocalShutdownTable <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanLocalShutdownTable>`
    
    .. attribute:: vtpvlantable
    
    	This table contains information on the VLANs which currently exist
    	**type**\: :py:class:`VtpVlanTable <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanTable>`
    
    

    """

    _prefix = 'cisco-vtp'
    _revision = '2013-10-14'

    def __init__(self):
        self.internalvlaninfo = CISCOVTPMIB.InternalVlanInfo()
        self.internalvlaninfo.parent = self
        self.managementdomaintable = CISCOVTPMIB.ManagementDomainTable()
        self.managementdomaintable.parent = self
        self.vlanstatistics = CISCOVTPMIB.VlanStatistics()
        self.vlanstatistics.parent = self
        self.vlantrunkports = CISCOVTPMIB.VlanTrunkPorts()
        self.vlantrunkports.parent = self
        self.vlantrunkporttable = CISCOVTPMIB.VlanTrunkPortTable()
        self.vlantrunkporttable.parent = self
        self.vtpauthenticationtable = CISCOVTPMIB.VtpAuthenticationTable()
        self.vtpauthenticationtable.parent = self
        self.vtpdatabasetable = CISCOVTPMIB.VtpDatabaseTable()
        self.vtpdatabasetable.parent = self
        self.vtpdiscoverresulttable = CISCOVTPMIB.VtpDiscoverResultTable()
        self.vtpdiscoverresulttable.parent = self
        self.vtpdiscovertable = CISCOVTPMIB.VtpDiscoverTable()
        self.vtpdiscovertable.parent = self
        self.vtpinternalvlantable = CISCOVTPMIB.VtpInternalVlanTable()
        self.vtpinternalvlantable.parent = self
        self.vtpstatus = CISCOVTPMIB.VtpStatus()
        self.vtpstatus.parent = self
        self.vtpvlanedittable = CISCOVTPMIB.VtpVlanEditTable()
        self.vtpvlanedittable.parent = self
        self.vtpvlanlocalshutdowntable = CISCOVTPMIB.VtpVlanLocalShutdownTable()
        self.vtpvlanlocalshutdowntable.parent = self
        self.vtpvlantable = CISCOVTPMIB.VtpVlanTable()
        self.vtpvlantable.parent = self


    class InternalVlanInfo(object):
        """
        
        
        .. attribute:: vtpinternalvlanallocpolicy
        
        	The internal VLAN allocation policy.  'ascending'  \- internal VLANs are allocated                starting from a lowwer VLAN ID and                 upwards. 'descending' \- internal VLANs are allocated                starting from a higher VLAN ID and                downwards
        	**type**\: :py:class:`VtpInternalVlanAllocPolicy_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.InternalVlanInfo.VtpInternalVlanAllocPolicy_Enum>`
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vtpinternalvlanallocpolicy = None

        class VtpInternalVlanAllocPolicy_Enum(Enum):
            """
            VtpInternalVlanAllocPolicy_Enum

            The internal VLAN allocation policy.
            
            'ascending'  \- internal VLANs are allocated
                           starting from a lowwer VLAN ID and 
                           upwards.
            'descending' \- internal VLANs are allocated
                           starting from a higher VLAN ID and
                           downwards.

            """

            ASCENDING = 1

            DESCENDING = 2


            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.InternalVlanInfo.VtpInternalVlanAllocPolicy_Enum']


        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:internalVlanInfo'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vtpinternalvlanallocpolicy is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.InternalVlanInfo']['meta_info']


    class ManagementDomainTable(object):
        """
        The table containing information on the management domains
        in which the local system is participating.  Devices which
        support only one management domain will support just one row
        in this table, and will not let it be deleted nor let other
        rows be created.  Devices which support multiple management
        domains will allow rows to be created and deleted, but will
        not allow the last row to be deleted. If the device does 
        not support VTP, the table is read\-only.
        
        .. attribute:: managementdomainentry
        
        	Information about the status of one management domain
        	**type**\: list of :py:class:`ManagementDomainEntry <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry>`
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.managementdomainentry = YList()
            self.managementdomainentry.parent = self
            self.managementdomainentry.name = 'managementdomainentry'


        class ManagementDomainEntry(object):
            """
            Information about the status of one management domain.
            
            .. attribute:: managementdomainindex
            
            	An arbitrary value to uniquely identify the management domain on the local system
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: managementdomainadminsrcif
            
            	The object specifies the interface to be used as the preferred source interface for the VTP IP updater address.  A zero length value indicates that a source interface is not specified
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: managementdomainconfigfile
            
            	The object specifies the file name where VTP configuration is stored in the format of <filename> or <devices>\:[<filename>].  <device> can be (but not limited to)\: flash, bootflash, slot0, slot1, disk0
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: managementdomainconfigrevnumber
            
            	The current Configuration Revision Number as known by the local device for this management domain when  managementDomainVersionInUse is version1(1) or  version2(2).  If managementDomainVersionInUse is version3(4), this  object has the same value with vtpDatabaseRevisionNumber  of VLAN database type.  This value is updated (if necessary) whenever a VTP advertisement is received or generated. When in the 'no management\-domain' state, this value is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: managementdomaindeviceid
            
            	The object indicates a value that uniquely identifies this device within a VTP Domain.  The value of this object is zero length string if managementDomainVersionInUse is not 'version3'
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: managementdomainlastchange
            
            	The time at which the Configuration Revision Number was (last) increased to its current value, as indicated in the most recently received VTP advertisement for this management domain when managementDomainVersionInUse is not version3(4) or in the most recently received VTP VLAN database  advertisement for this management domain when  managementDomainVersionInUse is version3(4).  The value 0x0000010100000000 indicates that the device which last increased the Configuration Revision Number had no idea of the date/time, or that no advertisement has been received
            	**type**\: str
            
            .. attribute:: managementdomainlastupdater
            
            	The IP\-address (or one of them) of the VTP Server which last updated the Configuration Revision Number, as indicated in the most recently received VTP advertisement for this management domain, when managementDomainVersionInUse is version1(1) or version2(2).   If managementDomainVersionInUse is version3(4), this object has the value of 0.0.0.0.  Before an advertisement has been received, this value is 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: managementdomainlocalmode
            
            	The local VTP mode in this management domain when managementDomainVersionInUse is version1(1) or version2(2).  If managementDomainVersionInUse is version3(4), this  object has the same value with vtpDatabaseLocalMode  of VLAN database type.  \- 'client' indicates that the local system is acting   as a VTP client.  \- 'server' indicates that the local system is acting   as a VTP server.  \- 'transparent' indicates that the local system does   not generate or listen to VTP messages, but forwards   messages. This mode can also be set by the device   itself when the amount of VLAN information is too   large for it to hold in DRAM.  \- 'off' indicates that the local system does not   generate, listen to or forward any VTP messages
            	**type**\: :py:class:`ManagementDomainLocalMode_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.ManagementDomainLocalMode_Enum>`
            
            .. attribute:: managementdomainlocalupdater
            
            	The object indicates the Internet address of the preferred source interface for the VTP IP updater
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: managementdomainlocalupdatertype
            
            	The object indicates the type of the Internet address of the preferred source interface for the VTP IP updater.  The value of this object is 'unknown' if managementDomainVersionInUse is 'version3' or managementDomainLocalMode is not 'server'
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: managementdomainname
            
            	The management name of a domain in which the local system is participating.  The zero\-length name corresponds to the 'no management\-domain' state which is the initial value at installation\-time if not configured otherwise.  Note that the zero\-length name does not correspond to an operational management domain, and a device does not send VTP advertisements while in the 'no management\-domain' state.  A device leaves the 'no management\-domain' state when it obtains a management\-domain name, either through configuration or through inheriting the management\-domain name from a received VTP advertisement.  When the value of an existing instance of this object is modified by network management, the local system should re\- initialize its VLAN information (for the given management domain) as if it had just been configured with a management domain name at installation time
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: managementdomainopersrcif
            
            	The object indicates the interface used as the preferred source interface for the VTP IP updater address.  A zero length string indicates that a source interface is not available
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: managementdomainpruningstate
            
            	An indication of whether VTP pruning is enabled or disabled in this managament domain.   This object can only be modified, either when the  corresponding instance value of managementDomainVersionInUse  is 'version1' or 'version2' and the corresponding instance  value of managementDomainLocalMode is 'server', or when the  corresponding instance value of managementDomainVersionInUse  is 'version3' and the corresponding instance value of  managementDomainLocalMode is 'server' or 'client'
            	**type**\: :py:class:`ManagementDomainPruningState_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.ManagementDomainPruningState_Enum>`
            
            .. attribute:: managementdomainpruningstateoper
            
            	Indicates whether VTP pruning is operationally enabled or disabled in this managament domain
            	**type**\: :py:class:`ManagementDomainPruningStateOper_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.ManagementDomainPruningStateOper_Enum>`
            
            .. attribute:: managementdomainrowstatus
            
            	The status of this conceptual row
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: managementdomainsourceonlymode
            
            	The object specifies whether to use only the IP address of managementDomainAdminSrcIf as the VTP IP updater address.   'true' indicates to only use the IP address of         managementDomainAdminSrcIf as the VTP IP         updater address.   'false' indicates to use the IP address of          managementDomainAdminSrcIf as the VTP IP          updater address if managementDomainAdminSrcIf          is configured with an IP address.  Otherwise, the          first available IP address of the system will         be used
            	**type**\: bool
            
            .. attribute:: managementdomaintftppathname
            
            	The complete pathname of the file at the TFTP Server identified by the value of managementDomainTftpServer in/from which VTP VLAN information for this management domain is to be stored/retrieved.  If the value of corresponding instance of managementDomainTftpServer is 0.0.0.0, the value of this object is ignored
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: managementdomaintftpserver
            
            	The IP address of a TFTP Server in/from which VTP VLAN information for this management domain is to be stored/retrieved.  If the information is being locally stored in NVRAM, this object should take the value 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: managementdomainversioninuse
            
            	The current version of the VTP that is in use by the designated management domain.   This object can be set to none(3) only when  vtpVersion is none(3)
            	**type**\: :py:class:`ManagementDomainVersionInUse_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.ManagementDomainVersionInUse_Enum>`
            
            .. attribute:: vtpconfigdigesterrors
            
            	The number of occurrences of configuration digest errors for this management domain.  A configuration digest error occurs when a device receives a VTP advertisement for which\:  \- the advertisement's Configuration Revision Number is   greater than the current locally\-held value, and  \-  the advertisement's digest value computed by the  receiving device does not match the checksum in the  summary advertisement that was received earlier. This  can happen, for example, if there is a mismatch in VTP  passwords between the VTP devices
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpconfigrevnumbererrors
            
            	The number of occurrences of configuration revision number errors for this management domain.  A configuration revision number error occurs when a device receives a VTP advertisement for which\:  \- the advertisement's Configuration Revision Number is the   same as the current locally\-held value, and  \- the advertisement's digest value is different from the   current locally\-held value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpinadvertrequests
            
            	The total number of VTP Advert Requests received for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpinsubsetadverts
            
            	The total number of VTP Subset Adverts received for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpinsummaryadverts
            
            	The total number of VTP Summary Adverts received for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpoutadvertrequests
            
            	The total number of VTP Advert Requests sent for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpoutsubsetadverts
            
            	The total number of VTP Subset Adverts sent for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpoutsummaryadverts
            
            	The total number of VTP Summary Adverts sent for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpvlanapplystatus
            
            	The current status of an 'apply' operation to instanciate the Edit Buffer as the new global VLAN information (for this management domain).  If no apply is currently active, the status represented is that of the most recently completed apply.  The possible values are\:     inProgress \- 'apply' operation in progress;     succeeded \- the 'apply' was successful (this value is           also used when no apply has been invoked since the           last time the local system restarted);     configNumberError \- the apply failed because the value of           vtpVlanEditConfigRevNumber was less or equal to           the value of current value of            managementDomainConfigRevNumber;     inconsistentEdit \- the apply failed because the modified           information was not self\-consistent;     tooBig \- the apply failed because the modified           information was too large to fit in this VTP           Server's non\-volatile storage location;     localNVStoreFail \- the apply failed in trying to store           the new information in a local non\-volatile           storage location;     remoteNVStoreFail \- the apply failed in trying to store           the new information in a remote non\-volatile           storage location;     editBufferEmpty \- the apply failed because the Edit           Buffer was empty (for this management domain).     someOtherError \- the apply failed for some other reason           (e.g., insufficient memory).     notPrimaryServer \- the apply failed because the local            device is not a VTP primary server for VLAN            database type when managementDomainVersionInUse           is version3(4)
            	**type**\: :py:class:`VtpVlanApplyStatus_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.VtpVlanApplyStatus_Enum>`
            
            .. attribute:: vtpvlaneditbufferowner
            
            	The management station which is currently using the Edit Buffer for this management domain.  When the Edit Buffer for a management domain is not currently in use, the value of this object is the zero\-length string.  Note that it is also the zero\-length string if a manager fails to set this object when invoking a copy operation
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: vtpvlaneditconfigrevnumber
            
            	The Configuration Revision Number to be used for the next apply operation.  This value is initialized (by the agent) on a copy operation to be one greater than the value of managementDomainConfigRevNumber. On an apply, if the  number is less or equal to the value of  managementDomainConfigRevNumber, then the apply fails. The value can be modified (increased) by network management before an apply to ensure that an apply does not fail for  this reason.  This object is used to allow management control over whether a configuration revision received via a VTP advertisement after a copy operation but before the succeeding apply operation is lost by being overwritten by the (local) edit operation.  By default, the apply operation will fail in this situation.  By increasing this object's value after the copy but before the apply, management can control whether the apply is to succeed (with the update via VTP advertisement being lost)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpvlaneditmodifiedvlan
            
            	The VLAN\-id of the modified VLAN in the Edit Buffer. If the object has the value of zero, any VLAN can  be edited. If the value of the object is not zero, only this VLAN can be edited.  The object's value is reset to zero after a successful 'apply' operation or a 'release' operation.   This object is only supported for devices which allow  only one VLAN editing for each 'apply' operation. For devices which allow multiple VLAN editing for each 'apply' operation, this object is not supported
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlaneditoperation
            
            	This object always has the value 'none' when read.  When written, each value causes the appropriate action\:   'copy' \- causes the creation of rows in the vtpVlanEditTable exactly corresponding to the current global VLAN information for this management domain.  If the Edit Buffer (for this management domain) is not currently empty, a copy operation fails.  A successful copy operation starts the deadman\-timer.   'apply' \- first performs a consistent check on the the modified information contained in the Edit Buffer, and if consistent, then tries to instanciate the modified information as the new global VLAN information.  Note that an empty Edit Buffer (for the management domain) would always result in an inconsistency since the default VLANs are required to be present.   'release' \- flushes the Edit Buffer (for this management domain), clears the Owner information, and aborts the deadman\-timer.  A release is generated automatically if the deadman\-timer ever expires.   'restartTimer' \- restarts the deadman\-timer.   'none' \- no operation is performed
            	**type**\: :py:class:`VtpVlanEditOperation_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.VtpVlanEditOperation_Enum>`
            
            

            """

            _prefix = 'cisco-vtp'
            _revision = '2013-10-14'

            def __init__(self):
                self.parent = None
                self.managementdomainindex = None
                self.managementdomainadminsrcif = None
                self.managementdomainconfigfile = None
                self.managementdomainconfigrevnumber = None
                self.managementdomaindeviceid = None
                self.managementdomainlastchange = None
                self.managementdomainlastupdater = None
                self.managementdomainlocalmode = None
                self.managementdomainlocalupdater = None
                self.managementdomainlocalupdatertype = None
                self.managementdomainname = None
                self.managementdomainopersrcif = None
                self.managementdomainpruningstate = None
                self.managementdomainpruningstateoper = None
                self.managementdomainrowstatus = None
                self.managementdomainsourceonlymode = None
                self.managementdomaintftppathname = None
                self.managementdomaintftpserver = None
                self.managementdomainversioninuse = None
                self.vtpconfigdigesterrors = None
                self.vtpconfigrevnumbererrors = None
                self.vtpinadvertrequests = None
                self.vtpinsubsetadverts = None
                self.vtpinsummaryadverts = None
                self.vtpoutadvertrequests = None
                self.vtpoutsubsetadverts = None
                self.vtpoutsummaryadverts = None
                self.vtpvlanapplystatus = None
                self.vtpvlaneditbufferowner = None
                self.vtpvlaneditconfigrevnumber = None
                self.vtpvlaneditmodifiedvlan = None
                self.vtpvlaneditoperation = None

            class ManagementDomainLocalMode_Enum(Enum):
                """
                ManagementDomainLocalMode_Enum

                The local VTP mode in this management domain when
                managementDomainVersionInUse is version1(1) or
                version2(2).
                
                If managementDomainVersionInUse is version3(4), this 
                object has the same value with vtpDatabaseLocalMode 
                of VLAN database type.
                
                \- 'client' indicates that the local system is acting
                  as a VTP client.
                
                \- 'server' indicates that the local system is acting
                  as a VTP server.
                
                \- 'transparent' indicates that the local system does
                  not generate or listen to VTP messages, but forwards
                  messages. This mode can also be set by the device
                  itself when the amount of VLAN information is too
                  large for it to hold in DRAM.
                
                \- 'off' indicates that the local system does not
                  generate, listen to or forward any VTP messages.

                """

                CLIENT = 1

                SERVER = 2

                TRANSPARENT = 3

                OFF = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.ManagementDomainLocalMode_Enum']


            class ManagementDomainPruningStateOper_Enum(Enum):
                """
                ManagementDomainPruningStateOper_Enum

                Indicates whether VTP pruning is operationally enabled or
                disabled in this managament domain.

                """

                ENABLED = 1

                DISABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.ManagementDomainPruningStateOper_Enum']


            class ManagementDomainPruningState_Enum(Enum):
                """
                ManagementDomainPruningState_Enum

                An indication of whether VTP pruning is enabled or disabled
                in this managament domain. 
                
                This object can only be modified, either when the 
                corresponding instance value of managementDomainVersionInUse 
                is 'version1' or 'version2' and the corresponding instance 
                value of managementDomainLocalMode is 'server', or when the 
                corresponding instance value of managementDomainVersionInUse 
                is 'version3' and the corresponding instance value of 
                managementDomainLocalMode is 'server' or 'client'.

                """

                ENABLED = 1

                DISABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.ManagementDomainPruningState_Enum']


            class ManagementDomainVersionInUse_Enum(Enum):
                """
                ManagementDomainVersionInUse_Enum

                The current version of the VTP that is in use by the
                designated management domain. 
                
                This object can be set to none(3) only when 
                vtpVersion is none(3).

                """

                VERSION1 = 1

                VERSION2 = 2

                NONE = 3

                VERSION3 = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.ManagementDomainVersionInUse_Enum']


            class VtpVlanApplyStatus_Enum(Enum):
                """
                VtpVlanApplyStatus_Enum

                The current status of an 'apply' operation to instanciate
                the Edit Buffer as the new global VLAN information (for this
                management domain).  If no apply is currently active, the
                status represented is that of the most recently completed
                apply.  The possible values are\:
                
                   inProgress \- 'apply' operation in progress;
                
                   succeeded \- the 'apply' was successful (this value is
                          also used when no apply has been invoked since the
                          last time the local system restarted);
                
                   configNumberError \- the apply failed because the value of
                          vtpVlanEditConfigRevNumber was less or equal to
                          the value of current value of 
                          managementDomainConfigRevNumber;
                
                   inconsistentEdit \- the apply failed because the modified
                          information was not self\-consistent;
                
                   tooBig \- the apply failed because the modified
                          information was too large to fit in this VTP
                          Server's non\-volatile storage location;
                
                   localNVStoreFail \- the apply failed in trying to store
                          the new information in a local non\-volatile
                          storage location;
                
                   remoteNVStoreFail \- the apply failed in trying to store
                          the new information in a remote non\-volatile
                          storage location;
                
                   editBufferEmpty \- the apply failed because the Edit
                          Buffer was empty (for this management domain).
                
                   someOtherError \- the apply failed for some other reason
                          (e.g., insufficient memory).
                
                   notPrimaryServer \- the apply failed because the local 
                          device is not a VTP primary server for VLAN 
                          database type when managementDomainVersionInUse
                          is version3(4).

                """

                INPROGRESS = 1

                SUCCEEDED = 2

                CONFIGNUMBERERROR = 3

                INCONSISTENTEDIT = 4

                TOOBIG = 5

                LOCALNVSTOREFAIL = 6

                REMOTENVSTOREFAIL = 7

                EDITBUFFEREMPTY = 8

                SOMEOTHERERROR = 9

                NOTPRIMARYSERVER = 10


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.VtpVlanApplyStatus_Enum']


            class VtpVlanEditOperation_Enum(Enum):
                """
                VtpVlanEditOperation_Enum

                This object always has the value 'none' when read.  When
                written, each value causes the appropriate action\:
                
                 'copy' \- causes the creation of rows in the
                vtpVlanEditTable exactly corresponding to the current global
                VLAN information for this management domain.  If the Edit
                Buffer (for this management domain) is not currently empty,
                a copy operation fails.  A successful copy operation starts
                the deadman\-timer.
                
                 'apply' \- first performs a consistent check on the the
                modified information contained in the Edit Buffer, and if
                consistent, then tries to instanciate the modified
                information as the new global VLAN information.  Note that
                an empty Edit Buffer (for the management domain) would
                always result in an inconsistency since the default VLANs
                are required to be present.
                
                 'release' \- flushes the Edit Buffer (for this management
                domain), clears the Owner information, and aborts the
                deadman\-timer.  A release is generated automatically if the
                deadman\-timer ever expires.
                
                 'restartTimer' \- restarts the deadman\-timer.
                
                 'none' \- no operation is performed.

                """

                NONE = 1

                COPY = 2

                APPLY = 3

                RELEASE = 4

                RESTARTTIMER = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry.VtpVlanEditOperation_Enum']


            @property
            def _common_path(self):
                if self.managementdomainindex is None:
                    raise YPYDataValidationError('Key property managementdomainindex is None')

                return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:managementDomainTable/CISCO-VTP-MIB:managementDomainEntry[CISCO-VTP-MIB:managementDomainIndex = ' + str(self.managementdomainindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.managementdomainindex is not None:
                    return True

                if self.managementdomainadminsrcif is not None:
                    return True

                if self.managementdomainconfigfile is not None:
                    return True

                if self.managementdomainconfigrevnumber is not None:
                    return True

                if self.managementdomaindeviceid is not None:
                    return True

                if self.managementdomainlastchange is not None:
                    return True

                if self.managementdomainlastupdater is not None:
                    return True

                if self.managementdomainlocalmode is not None:
                    return True

                if self.managementdomainlocalupdater is not None:
                    return True

                if self.managementdomainlocalupdatertype is not None:
                    return True

                if self.managementdomainname is not None:
                    return True

                if self.managementdomainopersrcif is not None:
                    return True

                if self.managementdomainpruningstate is not None:
                    return True

                if self.managementdomainpruningstateoper is not None:
                    return True

                if self.managementdomainrowstatus is not None:
                    return True

                if self.managementdomainsourceonlymode is not None:
                    return True

                if self.managementdomaintftppathname is not None:
                    return True

                if self.managementdomaintftpserver is not None:
                    return True

                if self.managementdomainversioninuse is not None:
                    return True

                if self.vtpconfigdigesterrors is not None:
                    return True

                if self.vtpconfigrevnumbererrors is not None:
                    return True

                if self.vtpinadvertrequests is not None:
                    return True

                if self.vtpinsubsetadverts is not None:
                    return True

                if self.vtpinsummaryadverts is not None:
                    return True

                if self.vtpoutadvertrequests is not None:
                    return True

                if self.vtpoutsubsetadverts is not None:
                    return True

                if self.vtpoutsummaryadverts is not None:
                    return True

                if self.vtpvlanapplystatus is not None:
                    return True

                if self.vtpvlaneditbufferowner is not None:
                    return True

                if self.vtpvlaneditconfigrevnumber is not None:
                    return True

                if self.vtpvlaneditmodifiedvlan is not None:
                    return True

                if self.vtpvlaneditoperation is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.ManagementDomainTable.ManagementDomainEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:managementDomainTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.managementdomainentry is not None:
                for child_ref in self.managementdomainentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.ManagementDomainTable']['meta_info']


    class VlanStatistics(object):
        """
        
        
        .. attribute:: vlanstatsextendedvlans
        
        	This object indicates the number of the existing manageable VLANs with VLAN indices greater than 1024 in the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vlanstatsfreevlans
        
        	This object indicates the number of the free or unused VLANs in the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vlanstatsinternalvlans
        
        	This object indicates the number of the internal VLANs existing in the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vlanstatsvlans
        
        	This object indicates the number of the existing manageable VLANs with VLAN indices from 1 to 1024 in the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vlanstatsextendedvlans = None
            self.vlanstatsfreevlans = None
            self.vlanstatsinternalvlans = None
            self.vlanstatsvlans = None

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vlanStatistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vlanstatsextendedvlans is not None:
                return True

            if self.vlanstatsfreevlans is not None:
                return True

            if self.vlanstatsinternalvlans is not None:
                return True

            if self.vlanstatsvlans is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VlanStatistics']['meta_info']


    class VlanTrunkPortTable(object):
        """
        The table containing information on the local system's VLAN
        trunk ports.
        
        .. attribute:: vlantrunkportentry
        
        	Information about one trunk port
        	**type**\: list of :py:class:`VlanTrunkPortEntry <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry>`
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vlantrunkportentry = YList()
            self.vlantrunkportentry.parent = self
            self.vlantrunkportentry.name = 'vlantrunkportentry'


        class VlanTrunkPortEntry(object):
            """
            Information about one trunk port.
            
            .. attribute:: vlantrunkportifindex
            
            	The value of ifIndex for the interface corresponding to this trunk port
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: stpxpreferredmistpinstancesmap
            
            	A string of octets containing one bit per MISTP instances  in the management domain on this trunk port. The first octet corresponds to MISTP instances with InstIndex values of 1  through 8; the second octet to MISTP instances 9 through 16; etc. The most significant bit of each octet corresponds to  the lowest value instanceIndex in that octet. The number of  bits for this mib object will be determined by the value of  stpxMISTPInstanceNumber.  For each instance, if it is preferred on this trunk port, then the bit corresponding to that instance is set to '1'.   To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single instance on the trunk port), any SNMP Set operation  accessing an instance of this object should also write the  value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: stpxpreferredmstinstancesmap
            
            	A string of octets containing one bit per MST instances  on this trunk port.  The first octet corresponds to MST  instances of 0 through 7; the second octet to MST instances  8 through 15; etc. The most significant bit of each octet  corresponds to the lowest MST instance value in that octet.  The number of bits for this mib object will be determined  by the value of stpxMSTMaxInstanceNumber.  For each instance, if it is preferred on this trunk port,  then the bit corresponding to that instance is set to '1'
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: stpxpreferredvlansmap
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is preferred on this trunk port, then the bit corresponding to that VLAN is set to '1'. The default value is 128 bytes of zeros.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 128
            
            .. attribute:: stpxpreferredvlansmap2k
            
            	A string of octets containing one bit per VLAN for VLANS  with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to  VLANs with VlanIndex values of 1024 through 1031;  the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the  lowest value VlanIndex in that octet.   For each VLAN, if it is preferred on this trunk port, then  the bit corresponding to that VLAN is set to '1'.  The default value is 128 bytes of zeros.   To avoid conflicts between overlapping partial updates by  multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of  vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: stpxpreferredvlansmap3k
            
            	A string of octets containing one bit per VLAN for VLANS  with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to  VLANs with VlanIndex values of 2048 through 2055;  the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the  lowest value VlanIndex in that octet.   For each VLAN, if it is preferred on this trunk port, then  the bit corresponding to that VLAN is set to '1'.  The default value is 128 bytes of zeros.   To avoid conflicts between overlapping partial updates by  multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of  vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: stpxpreferredvlansmap4k
            
            	A string of octets containing one bit per VLAN for VLANS  with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to  VLANs with VlanIndex values of 3072 through 3079;  the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the  lowest value VlanIndex in that octet.   For each VLAN, if it is preferred on this trunk port, then  the bit corresponding to that VLAN is set to '1'.  The default value is 128 bytes of zeros.   To avoid conflicts between overlapping partial updates by  multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of  vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vlantrunkportdot1qtunnel
            
            	Indicates dot1qtunnel mode of the port.  If the portDot1qTunnel  is set to 'trunk' mode, the port's vlanTrunkPortDynamicState will be changed to 'onNoNegotiate' and the vlanTrunkPortEncapsulationType will be set to 'dot1Q'. These values cannot be changed unless dot1q tunnel is disabled on this port.  If the portDot1qTunnel mode is set to 'access' mode, the port's vlanTrunkPortDynamicState will be set to 'off'.And the value of vlanTrunkPortDynamicState cannot be changed unless dot1q tunnel is disabled on this port. 1Q packets received on this access port will remain.  Setting the port to dot1q tunnel 'disabled' mode causes the dot1q tunnel feature to be disabled on this port.  This object can't be set to 'trunk' or 'access' mode, when vlanTrunkPortsDot1qTag  object is set to 'false'.  This object has been deprecated and is replaced by the object 'cltcDot1qTunnelMode' in the CISCO\-L2\-TUNNEL\-CONFIG\-MIB
            	**type**\: :py:class:`VlanTrunkPortDot1qTunnel_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry.VlanTrunkPortDot1qTunnel_Enum>`
            
            .. attribute:: vlantrunkportdynamicstate
            
            	For devices that allows dynamic determination of whether a link between two switches should be a trunk or not, this object allows the operator to mandate the behavior of that dynamic mechanism.  on(1) dictates that the interface will always be a trunk. This is the value for static entries (those that show no dynamic behavior). If the negotiation is supported on this port, negotiation will take place with the far end to attempt to bring the far end into trunking state.  off(2) allows an operator to specify that the specified interface is never to be trunk, regardless of any dynamic mechanisms to the contrary.  This value is useful for overriding the default behavior of some switches. If the negotiation is supported on this port, negotiation will take place with the far end to attempt on the link to bring the far end into non\-trunking state.  desirable(3) is used to indicate that it is desirable for the interface to become a trunk.  The device will initiate any negotiation necessary to become a trunk but will not become a trunk unless it receives confirmation from the far end on the link.  auto(4) is used to indicate that the interface is capable and willing to become a trunk but will not initiate trunking negotiations.  The far end on the link are required to either start negotiations or start sending encapsulated packets, on which event the specified interface will become a trunk.  onNoNegotiate(5) is used to indicate that the interface is permanently set to be a trunk, and no negotiation takes place with the far end on the link to ensure consistent operation. This is similar to on(1) except no negotiation takes place with the far end.  If the port does not support negotiation or its vlanTrunkPortEncapsulationType is set to negotiate(5), onNoNegotiate(5) is not allowed.  Devices that do no support dynamic determination (for just a particular interface, encapsulation or for the whole device) need only support the 'on', and 'off' values
            	**type**\: :py:class:`VlanTrunkPortDynamicState_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry.VlanTrunkPortDynamicState_Enum>`
            
            .. attribute:: vlantrunkportdynamicstatus
            
            	Indicates whether the specified interface is either acting as a trunk or not. This is a result of the vlanTrunkPortDynamicState and the ifOperStatus of the trunk port itself
            	**type**\: :py:class:`VlanTrunkPortDynamicStatus_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry.VlanTrunkPortDynamicStatus_Enum>`
            
            .. attribute:: vlantrunkportencapsulationopertype
            
            	The type of VLAN encapsulation in use on this trunk port. For intefaces with vlanTrunkPortDynamicStatus of notTrunking(2) the vlanTrunkPortEncapsulationOperType shall be notApplicable(6)
            	**type**\: :py:class:`VlanTrunkPortEncapsulationOperType_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry.VlanTrunkPortEncapsulationOperType_Enum>`
            
            .. attribute:: vlantrunkportencapsulationtype
            
            	The type of VLAN encapsulation desired to be used on this trunk port. It is either a particular type, or 'negotiate' meaning whatever type results from the negotiation. negotiate(5) is not allowed if the port does not support negotiation or if its vlanTrunkPortDynamicState is set to on(1) or onNoNegotiate(5). Whether writing to this object in order to modify the encapsulation is supported is both device and interface specific
            	**type**\: :py:class:`VlanTrunkPortEncapsulationType_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry.VlanTrunkPortEncapsulationType_Enum>`
            
            .. attribute:: vlantrunkportinjoins
            
            	The number of VTP Join messages received on this trunk port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vlantrunkportmanagementdomain
            
            	The value of managementDomainIndex for the management domain on this trunk port.  Devices which support only one management domain will support this object read\-only
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: vlantrunkportnativevlan
            
            	The VlanIndex of the VLAN which is represented by native frames on this trunk port.  For trunk ports not supporting the sending and receiving of native frames, this value should be set to zero
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vlantrunkportoldadverts
            
            	The number of VTP Advertisement messages which indicated the sender does not support VLAN\-pruning received on this trunk port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vlantrunkportoutjoins
            
            	The number of VTP Join messages sent on this trunk port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vlantrunkportrowstatus
            
            	The status of this row.  In some circumstances, the creation of a row in this table is needed to enable the appropriate trunking/tagging protocol on the port, to enable the use of VTP on the port, and to assign the port to the appropriate management domain.  In other circumstances, rows in this table will be created as a by\-product of other operations
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: vlantrunkportvlansactivefirst2k
            
            	A string of octets containing one bit per VLAN with VlanIndex values of 0 through 2047.  If the bit corresponding to a VLAN is set to 1, it indicates that vlan is allowed and active in management domain.  If the bit corresponding to a VLAN is set to 0, it indicates that vlan is not allowed or not active in management domain
            	**type**\: str
            
            	**range:** 0..256
            
            .. attribute:: vlantrunkportvlansactivesecond2k
            
            	A string of octets containing one bit per VLAN with VlanIndex values of 2048 through 4095.  If the bit corresponding to a VLAN is set to 1, it indicates that vlan is allowed and active in management domain.  If the bit corresponding to a VLAN is set to 0, it indicates that vlan is not allowed or not active in management domain
            	**type**\: str
            
            	**range:** 0..256
            
            .. attribute:: vlantrunkportvlansenabled
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 128
            
            .. attribute:: vlantrunkportvlansenabled2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet. If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vlantrunkportvlansenabled3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet. If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vlantrunkportvlansenabled4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet. If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vlantrunkportvlanspruningeligible
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 128
            
            .. attribute:: vlantrunkportvlansrcvjoined
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\: str
            
            	**range:** 128
            
            .. attribute:: vlantrunkportvlansrcvjoined2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vlantrunkportvlansrcvjoined3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vlantrunkportvlansrcvjoined4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vlantrunkportvlansxmitjoined
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\: str
            
            	**range:** 128
            
            .. attribute:: vlantrunkportvlansxmitjoined2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vlantrunkportvlansxmitjoined3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vlantrunkportvlansxmitjoined4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vlantrunkportvtpenabled
            
            	Some trunk interface modules allow VTP to be enabled/disabled seperately from that of the central device.  In such a case this object provides management a way to remotely enable VTP on that module.  If a module does not support a seperate VTP enabled state then this object shall always return 'true' and will accept no other value during a SET operation
            	**type**\: bool
            
            .. attribute:: vtpvlanspruningeligible2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vtpvlanspruningeligible3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: vtpvlanspruningeligible4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**range:** 0..128
            
            

            """

            _prefix = 'cisco-vtp'
            _revision = '2013-10-14'

            def __init__(self):
                self.parent = None
                self.vlantrunkportifindex = None
                self.stpxpreferredmistpinstancesmap = None
                self.stpxpreferredmstinstancesmap = None
                self.stpxpreferredvlansmap = None
                self.stpxpreferredvlansmap2k = None
                self.stpxpreferredvlansmap3k = None
                self.stpxpreferredvlansmap4k = None
                self.vlantrunkportdot1qtunnel = None
                self.vlantrunkportdynamicstate = None
                self.vlantrunkportdynamicstatus = None
                self.vlantrunkportencapsulationopertype = None
                self.vlantrunkportencapsulationtype = None
                self.vlantrunkportinjoins = None
                self.vlantrunkportmanagementdomain = None
                self.vlantrunkportnativevlan = None
                self.vlantrunkportoldadverts = None
                self.vlantrunkportoutjoins = None
                self.vlantrunkportrowstatus = None
                self.vlantrunkportvlansactivefirst2k = None
                self.vlantrunkportvlansactivesecond2k = None
                self.vlantrunkportvlansenabled = None
                self.vlantrunkportvlansenabled2k = None
                self.vlantrunkportvlansenabled3k = None
                self.vlantrunkportvlansenabled4k = None
                self.vlantrunkportvlanspruningeligible = None
                self.vlantrunkportvlansrcvjoined = None
                self.vlantrunkportvlansrcvjoined2k = None
                self.vlantrunkportvlansrcvjoined3k = None
                self.vlantrunkportvlansrcvjoined4k = None
                self.vlantrunkportvlansxmitjoined = None
                self.vlantrunkportvlansxmitjoined2k = None
                self.vlantrunkportvlansxmitjoined3k = None
                self.vlantrunkportvlansxmitjoined4k = None
                self.vlantrunkportvtpenabled = None
                self.vtpvlanspruningeligible2k = None
                self.vtpvlanspruningeligible3k = None
                self.vtpvlanspruningeligible4k = None

            class VlanTrunkPortDot1qTunnel_Enum(Enum):
                """
                VlanTrunkPortDot1qTunnel_Enum

                Indicates dot1qtunnel mode of the port.
                
                If the portDot1qTunnel  is set to 'trunk' mode, the port's
                vlanTrunkPortDynamicState will be changed to 'onNoNegotiate'
                and the vlanTrunkPortEncapsulationType will be set to
                'dot1Q'. These values cannot be changed unless dot1q tunnel
                is disabled on this port.
                
                If the portDot1qTunnel mode is set to 'access' mode, the
                port's vlanTrunkPortDynamicState will be set to 'off'.And
                the value of vlanTrunkPortDynamicState cannot be changed
                unless dot1q tunnel is disabled on this port. 1Q packets
                received on this access port will remain.
                
                Setting the port to dot1q tunnel 'disabled' mode causes the
                dot1q tunnel feature to be disabled on this port.  This
                object can't be set to 'trunk' or 'access' mode, when
                vlanTrunkPortsDot1qTag  object is set to 'false'.
                
                This object has been deprecated and is replaced by the
                object 'cltcDot1qTunnelMode' in the
                CISCO\-L2\-TUNNEL\-CONFIG\-MIB

                """

                TRUNK = 1

                ACCESS = 2

                DISABLED = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry.VlanTrunkPortDot1qTunnel_Enum']


            class VlanTrunkPortDynamicState_Enum(Enum):
                """
                VlanTrunkPortDynamicState_Enum

                For devices that allows dynamic determination of whether
                a link between two switches should be a trunk or not, this
                object allows the operator to mandate the behavior of that
                dynamic mechanism.
                
                on(1) dictates that the interface will always be a
                trunk. This is the value for static entries (those that
                show no dynamic behavior). If the negotiation is supported
                on this port, negotiation will take place with the far end
                to attempt to bring the far end into trunking state.
                
                off(2) allows an operator to specify that the specified
                interface is never to be trunk, regardless of any dynamic
                mechanisms to the contrary.  This value is useful for
                overriding the default behavior of some switches. If the
                negotiation is supported on this port, negotiation will take
                place with the far end to attempt on the link to bring the
                far end into non\-trunking state.
                
                desirable(3) is used to indicate that it is desirable for
                the interface to become a trunk.  The device will initiate
                any negotiation necessary to become a trunk but will not
                become a trunk unless it receives confirmation from the far
                end on the link.
                
                auto(4) is used to indicate that the interface is capable
                and willing to become a trunk but will not initiate
                trunking negotiations.  The far end on the link are
                required to either start negotiations or start sending
                encapsulated packets, on which event the specified
                interface will become a trunk.
                
                onNoNegotiate(5) is used to indicate that the interface is
                permanently set to be a trunk, and no negotiation takes
                place with the far end on the link to ensure consistent
                operation. This is similar to on(1) except no negotiation
                takes place with the far end.
                
                If the port does not support negotiation or its
                vlanTrunkPortEncapsulationType is set to negotiate(5),
                onNoNegotiate(5) is not allowed.
                
                Devices that do no support dynamic determination (for just
                a particular interface, encapsulation or for the whole
                device) need only support the 'on', and 'off' values.

                """

                ON = 1

                OFF = 2

                DESIRABLE = 3

                AUTO = 4

                ONNONEGOTIATE = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry.VlanTrunkPortDynamicState_Enum']


            class VlanTrunkPortDynamicStatus_Enum(Enum):
                """
                VlanTrunkPortDynamicStatus_Enum

                Indicates whether the specified interface is either
                acting as a trunk or not. This is a result of the
                vlanTrunkPortDynamicState and the ifOperStatus of the
                trunk port itself.

                """

                TRUNKING = 1

                NOTTRUNKING = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry.VlanTrunkPortDynamicStatus_Enum']


            class VlanTrunkPortEncapsulationOperType_Enum(Enum):
                """
                VlanTrunkPortEncapsulationOperType_Enum

                The type of VLAN encapsulation in use on this trunk port.
                For intefaces with vlanTrunkPortDynamicStatus of
                notTrunking(2) the vlanTrunkPortEncapsulationOperType shall
                be notApplicable(6).

                """

                ISL = 1

                DOT10 = 2

                LANE = 3

                DOT1Q = 4

                NEGOTIATING = 5

                NOTAPPLICABLE = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry.VlanTrunkPortEncapsulationOperType_Enum']


            class VlanTrunkPortEncapsulationType_Enum(Enum):
                """
                VlanTrunkPortEncapsulationType_Enum

                The type of VLAN encapsulation desired to be used on this
                trunk port. It is either a particular type, or 'negotiate'
                meaning whatever type results from the negotiation.
                negotiate(5) is not allowed if the port does not support
                negotiation or if its vlanTrunkPortDynamicState is set to
                on(1) or onNoNegotiate(5). Whether writing to this object
                in order to modify the encapsulation is supported is both
                device and interface specific.

                """

                ISL = 1

                DOT10 = 2

                LANE = 3

                DOT1Q = 4

                NEGOTIATE = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry.VlanTrunkPortEncapsulationType_Enum']


            @property
            def _common_path(self):
                if self.vlantrunkportifindex is None:
                    raise YPYDataValidationError('Key property vlantrunkportifindex is None')

                return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vlanTrunkPortTable/CISCO-VTP-MIB:vlanTrunkPortEntry[CISCO-VTP-MIB:vlanTrunkPortIfIndex = ' + str(self.vlantrunkportifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.vlantrunkportifindex is not None:
                    return True

                if self.stpxpreferredmistpinstancesmap is not None:
                    return True

                if self.stpxpreferredmstinstancesmap is not None:
                    return True

                if self.stpxpreferredvlansmap is not None:
                    return True

                if self.stpxpreferredvlansmap2k is not None:
                    return True

                if self.stpxpreferredvlansmap3k is not None:
                    return True

                if self.stpxpreferredvlansmap4k is not None:
                    return True

                if self.vlantrunkportdot1qtunnel is not None:
                    return True

                if self.vlantrunkportdynamicstate is not None:
                    return True

                if self.vlantrunkportdynamicstatus is not None:
                    return True

                if self.vlantrunkportencapsulationopertype is not None:
                    return True

                if self.vlantrunkportencapsulationtype is not None:
                    return True

                if self.vlantrunkportinjoins is not None:
                    return True

                if self.vlantrunkportmanagementdomain is not None:
                    return True

                if self.vlantrunkportnativevlan is not None:
                    return True

                if self.vlantrunkportoldadverts is not None:
                    return True

                if self.vlantrunkportoutjoins is not None:
                    return True

                if self.vlantrunkportrowstatus is not None:
                    return True

                if self.vlantrunkportvlansactivefirst2k is not None:
                    return True

                if self.vlantrunkportvlansactivesecond2k is not None:
                    return True

                if self.vlantrunkportvlansenabled is not None:
                    return True

                if self.vlantrunkportvlansenabled2k is not None:
                    return True

                if self.vlantrunkportvlansenabled3k is not None:
                    return True

                if self.vlantrunkportvlansenabled4k is not None:
                    return True

                if self.vlantrunkportvlanspruningeligible is not None:
                    return True

                if self.vlantrunkportvlansrcvjoined is not None:
                    return True

                if self.vlantrunkportvlansrcvjoined2k is not None:
                    return True

                if self.vlantrunkportvlansrcvjoined3k is not None:
                    return True

                if self.vlantrunkportvlansrcvjoined4k is not None:
                    return True

                if self.vlantrunkportvlansxmitjoined is not None:
                    return True

                if self.vlantrunkportvlansxmitjoined2k is not None:
                    return True

                if self.vlantrunkportvlansxmitjoined3k is not None:
                    return True

                if self.vlantrunkportvlansxmitjoined4k is not None:
                    return True

                if self.vlantrunkportvtpenabled is not None:
                    return True

                if self.vtpvlanspruningeligible2k is not None:
                    return True

                if self.vtpvlanspruningeligible3k is not None:
                    return True

                if self.vtpvlanspruningeligible4k is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.VlanTrunkPortTable.VlanTrunkPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vlanTrunkPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vlantrunkportentry is not None:
                for child_ref in self.vlantrunkportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VlanTrunkPortTable']['meta_info']


    class VlanTrunkPorts(object):
        """
        
        
        .. attribute:: vlantrunkportsdot1qtag
        
        	An indication of whether the tagging on all VLANs including native VLAN for all 802.1q trunks is enabled.  If this object has a value of true(1) then all VLANs including native VLAN are tagged.  If the value is false(2) then all VLANs excluding native VLAN are tagged.  This object has been deprecated and is replaced by the object 'cltcDot1qAllTaggedEnabled' in the CISCO\-L2\-TUNNEL\-CONFIG\-MIB
        	**type**\: bool
        
        .. attribute:: vlantrunkportsetserialno
        
        	An advisory lock used to allow several cooperating SNMPv2 managers to coordinate their use of the SNMPv2 set operation acting upon any instance of vlanTrunkPortVlansEnabled
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vlantrunkportsdot1qtag = None
            self.vlantrunkportsetserialno = None

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vlanTrunkPorts'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vlantrunkportsdot1qtag is not None:
                return True

            if self.vlantrunkportsetserialno is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VlanTrunkPorts']['meta_info']


    class VtpAuthenticationTable(object):
        """
        The table contains the authentication information of VTP
        in which the local system participates.
        
        The security mechanism of VTP relies on a secret key
        that is used to alter the MD5 digest of the packets
        transmitted on the wire.  The secret value is
        created from a password that may be saved in plain text
        in the configuration or hidden from the configuration.
        
        The device creating or modifying the VTP configuration
        signs it using the MD5 digest generated from the secret
        key before advertising it. Other devices in the domain
        receive this configuration use the same secret key
        to accept it if correctly signed or drop it otherwise.
        
        The user has the option to hide the password from the
        configuration. Once the password is hidden, the secret
        key generated from the password is shown in the 
        configuration instead, and there is no other way to 
        show the password in plain text again but clearing 
        it or resetting it. 
        
        In an un\-trusted area, the password on a device can 
        be configured without being unveiled. After that,
        it has to be provided again by setting the same 
        value to vtpDatabaseTakeOverPassword if the user 
        wants to take over the whole VTP management domain
        of the database type.
        
        When managementDomainVersionInUse is version3(4), the 
        authentication mechanism is common to all VTP
        database type.
        
        .. attribute:: vtpauthentry
        
        	Information about the status of the VTP authentication information in one domain
        	**type**\: list of :py:class:`VtpAuthEntry <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpAuthenticationTable.VtpAuthEntry>`
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vtpauthentry = YList()
            self.vtpauthentry.parent = self
            self.vtpauthentry.name = 'vtpauthentry'


        class VtpAuthEntry(object):
            """
            Information about the status of the VTP
            authentication information in one domain.
            
            .. attribute:: managementdomainindex
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: vtpauthpassword
            
            	By default, this object has a value of a zero\-length character string and is considered to be not configured.  The device uses the password to generate the  secret key. It can be stored in the configuration in  plain text or hidden from the configuration. If a VTP  server intends to modify the database's configuration in the domain but the password was hidden from the configuration, the same password (vtpDatabaseTakeOverPassword) as the hidden one has to be provided.  When this object is set alone, vtpAuthPasswordType is set to plaintext(1) automatically by the system. Setting this object to a zero length character string resets the password to its default value and the password is considered as not configured.  This object is not allowed to be set at the same time when  vtpAuthSecretKey is set.  When the vtpAuthPasswordType is hidden(2), this object  will return a zero\-length character string when read
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: vtpauthpasswordtype
            
            	By default this object has the value as plaintext(1) and the VTP password is stored in the configuration file in plain text.  Setting this object to hidden(2) will hide the password from the configuration.  Once this object is set to hidden(2), it cannot be set to plaintext(1) alone. However, it may be set to plaintext(1) at the same time the password is set
            	**type**\: :py:class:`VtpAuthPasswordType_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpAuthenticationTable.VtpAuthEntry.VtpAuthPasswordType_Enum>`
            
            .. attribute:: vtpauthsecretkey
            
            	The device creating or modifying the VTP configuration signs it using the MD5 digest generated from the secret key before advertising it. Other devices in the domain receiving this configuration use the same secret key to accept it if it was correctly signed or drop it  otherwise.  By default, the object has the value as a zero\-length string and this value is read only. It is set  to this value automatically when the password  (vtpAuthPassword) is set to a zero\-length octet string.  The secret key can be either generated using the password or configured by the user. Once the secret key is configured by the user, it is stored as a hexadecimal string in the device's configuration and the password is considered to be the secret key's matching password and hidden from the configuration automatically.  This object is not allowed to be set at the same time when vtpAuthPassword is set.  The secret key is overwritten by a newly generated secret key when the password is re\-configured
            	**type**\: str
            
            	**range:** 0 \| 16
            
            

            """

            _prefix = 'cisco-vtp'
            _revision = '2013-10-14'

            def __init__(self):
                self.parent = None
                self.managementdomainindex = None
                self.vtpauthpassword = None
                self.vtpauthpasswordtype = None
                self.vtpauthsecretkey = None

            class VtpAuthPasswordType_Enum(Enum):
                """
                VtpAuthPasswordType_Enum

                By default this object has the value as plaintext(1)
                and the VTP password is stored in the configuration
                file in plain text.
                
                Setting this object to hidden(2) will hide the
                password from the configuration.
                
                Once this object is set to hidden(2), it cannot
                be set to plaintext(1) alone. However, it may
                be set to plaintext(1) at the same time the
                password is set.

                """

                PLAINTEXT = 1

                HIDDEN = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VtpAuthenticationTable.VtpAuthEntry.VtpAuthPasswordType_Enum']


            @property
            def _common_path(self):
                if self.managementdomainindex is None:
                    raise YPYDataValidationError('Key property managementdomainindex is None')

                return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpAuthenticationTable/CISCO-VTP-MIB:vtpAuthEntry[CISCO-VTP-MIB:managementDomainIndex = ' + str(self.managementdomainindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.managementdomainindex is not None:
                    return True

                if self.vtpauthpassword is not None:
                    return True

                if self.vtpauthpasswordtype is not None:
                    return True

                if self.vtpauthsecretkey is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.VtpAuthenticationTable.VtpAuthEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpAuthenticationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vtpauthentry is not None:
                for child_ref in self.vtpauthentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VtpAuthenticationTable']['meta_info']


    class VtpDatabaseTable(object):
        """
        This table contains information of the VTP
        databases. It is not instantiated when
        managementDomainVersionInUse is version1(1), 
        version2(3) or none(3).
        
        .. attribute:: vtpdatabaseentry
        
        	Information about the status of the VTP database in the domain.  Each VTP database type known to the local device type has an entry in this table. An entry is also created for unknown database which is notified through VTP advertisements from other VTP servers
        	**type**\: list of :py:class:`VtpDatabaseEntry <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpDatabaseTable.VtpDatabaseEntry>`
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vtpdatabaseentry = YList()
            self.vtpdatabaseentry.parent = self
            self.vtpdatabaseentry.name = 'vtpdatabaseentry'


        class VtpDatabaseEntry(object):
            """
            Information about the status of the VTP database
            in the domain.  Each VTP database type known to the
            local device type has an entry in this table.
            An entry is also created for unknown database which is
            notified through VTP advertisements from other VTP
            servers.
            
            .. attribute:: managementdomainindex
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: vtpdatabaseindex
            
            	A value assigned by the system which uniquely identifies a VTP database in the local system
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdatabaselocalmode
            
            	The local VTP mode for a particular database type in this administrative domain.  \- 'client' indicates that the local system is acting   as a VTP client of the database type.  \- 'server' indicates that the local system is acting   as a VTP server of the database type.  \- 'transparent' indicates that the local system does   not generate or listen to VTP messages of this    database type, but forwards   messages. This mode can also be set by the device   itself when the size of database is too large for it   to hold in DRAM.  \- 'off' indicates that the local system does not   generate, listen to or forward any VTP messages   of this database type.  The default mode is 'client' for the database type  known to the local device and 'transparent' for the unknown database type
            	**type**\: :py:class:`VtpDatabaseLocalMode_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpDatabaseTable.VtpDatabaseEntry.VtpDatabaseLocalMode_Enum>`
            
            .. attribute:: vtpdatabasename
            
            	The name of the database
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: vtpdatabaseprimaryserver
            
            	There are two kinds of VTP version 3 servers for a certain database type \- the primary server and the secondary server. When a local device is configured as a server for a certain database type, it becomes secondary server by default. Primary server is an operational role under which a server can initiate or change the VTP configuration of the database type.  A true(1) value indicates that the local device is the  primary server of the database type in the management domain. A false(2) value indicates that the local device is not the primary server, or the database type is unknown to the local device
            	**type**\: bool
            
            .. attribute:: vtpdatabaseprimaryserverid
            
            	The unique identifier of the primary server in the management domain for the database type.   If no primary server is discovered for the database type, the object has a value of zero length string
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: vtpdatabaserevnumber
            
            	The current configuration revision number as known by the local device for this VTP 3 database type in the management domain.  This value is updated (if necessary) whenever a  VTP advertisement for the database type is received  or generated. When the database type is unknown to the  local device or no VTP advertisement for the database type is received or generated, its value is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdatabasetakeoverpassword
            
            	When read, this object always returns the value of a zero\-length octet string.  In the case that the VTP password is hidden from the  configuration and the local device intends to take over the whole domain, this object must be  set to the matching password with the secret key  (vtpAuthSecretKey) in the same data packet as which  the vtpDatabaseTakeOverPrimary is in. In all the  other situations, setting a valid value to this object  has no impact on the system
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: vtpdatabasetakeoverprimary
            
            	There are two kinds of VTP version 3 servers for a certain database type \- the primary server and the secondary server. When a local device is configured as a server for a certain database type, it becomes secondary server by default. Primary server is an operational role under which a server can initiate or change the VTP configuration of the database type.  Setting this object to a true(1) value will advertise the configuration of this database type to the whole domain.  In order to successfully setting this object to true(1), the value of vtpDatabaseLocalMode must be server(2). Besides that, when the VTP password is hidden from the configuration file, the password (vtpDatabaseTakeOverPassword) which  matches  the secret key (vtpAuthSecretKey) must be provided in the same data packet.   When read, the object always returns false(2)
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-vtp'
            _revision = '2013-10-14'

            def __init__(self):
                self.parent = None
                self.managementdomainindex = None
                self.vtpdatabaseindex = None
                self.vtpdatabaselocalmode = None
                self.vtpdatabasename = None
                self.vtpdatabaseprimaryserver = None
                self.vtpdatabaseprimaryserverid = None
                self.vtpdatabaserevnumber = None
                self.vtpdatabasetakeoverpassword = None
                self.vtpdatabasetakeoverprimary = None

            class VtpDatabaseLocalMode_Enum(Enum):
                """
                VtpDatabaseLocalMode_Enum

                The local VTP mode for a particular database type
                in this administrative domain.
                
                \- 'client' indicates that the local system is acting
                  as a VTP client of the database type.
                
                \- 'server' indicates that the local system is acting
                  as a VTP server of the database type.
                
                \- 'transparent' indicates that the local system does
                  not generate or listen to VTP messages of this 
                  database type, but forwards
                  messages. This mode can also be set by the device
                  itself when the size of database is too large for it
                  to hold in DRAM.
                
                \- 'off' indicates that the local system does not
                  generate, listen to or forward any VTP messages
                  of this database type.
                
                The default mode is 'client' for the database type 
                known to the local device and 'transparent' for the
                unknown database type.

                """

                CLIENT = 1

                SERVER = 2

                TRANSPARENT = 3

                OFF = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VtpDatabaseTable.VtpDatabaseEntry.VtpDatabaseLocalMode_Enum']


            @property
            def _common_path(self):
                if self.managementdomainindex is None:
                    raise YPYDataValidationError('Key property managementdomainindex is None')
                if self.vtpdatabaseindex is None:
                    raise YPYDataValidationError('Key property vtpdatabaseindex is None')

                return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpDatabaseTable/CISCO-VTP-MIB:vtpDatabaseEntry[CISCO-VTP-MIB:managementDomainIndex = ' + str(self.managementdomainindex) + '][CISCO-VTP-MIB:vtpDatabaseIndex = ' + str(self.vtpdatabaseindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.managementdomainindex is not None:
                    return True

                if self.vtpdatabaseindex is not None:
                    return True

                if self.vtpdatabaselocalmode is not None:
                    return True

                if self.vtpdatabasename is not None:
                    return True

                if self.vtpdatabaseprimaryserver is not None:
                    return True

                if self.vtpdatabaseprimaryserverid is not None:
                    return True

                if self.vtpdatabaserevnumber is not None:
                    return True

                if self.vtpdatabasetakeoverpassword is not None:
                    return True

                if self.vtpdatabasetakeoverprimary is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.VtpDatabaseTable.VtpDatabaseEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpDatabaseTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vtpdatabaseentry is not None:
                for child_ref in self.vtpdatabaseentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VtpDatabaseTable']['meta_info']


    class VtpDiscoverResultTable(object):
        """
        The table containing information of discovered VTP members
        in the management domain in which the local system is
        participating. This table is not instantiated when 
        managementDomainVersionInUse is version1(1), version2(2) or
        none(3).
        
        .. attribute:: vtpdiscoverresultentry
        
        	A conceptual row is created for each VTP member which is found through successful discovery
        	**type**\: list of :py:class:`VtpDiscoverResultEntry <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpDiscoverResultTable.VtpDiscoverResultEntry>`
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vtpdiscoverresultentry = YList()
            self.vtpdiscoverresultentry.parent = self
            self.vtpdiscoverresultentry.name = 'vtpdiscoverresultentry'


        class VtpDiscoverResultEntry(object):
            """
            A conceptual row is created for each VTP member which
            is found through successful discovery.
            
            .. attribute:: managementdomainindex
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: vtpdiscoverresultindex
            
            	A value assigned by the system which identifies a VTP member and the associated database in the  management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdiscoverresultconflicting
            
            	Indicates whether this VTP member contains conflicting information.  true(1) indicates that this member has conflicting  information of the database type in the management domain.  false(2) indicates that there is no conflicting information of the database type in the management domain
            	**type**\: bool
            
            .. attribute:: vtpdiscoverresultdatabasename
            
            	The database name associated with the discovered VTP member
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: vtpdiscoverresultdeviceid
            
            	The unique identifier of the device for this VTP member
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: vtpdiscoverresultprimaryserver
            
            	The unique identifier of the primary server for this VTP member and the associated database type.  There are two different VTP servers, the primary server and the secondary server.  When a local device is configured as a server for a certain database type, it becomes secondary server by default.  Primary server is an operational role under which a server can initiate or change the VTP configuration of the database type.  If this VTP member itself is the primary server, the    value of this object is the same as the value of  vtpDiscoverResultDeviceId of the instance
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: vtpdiscoverresultrevnumber
            
            	The current configuration revision number as known by the VTP member. When the database type is unknown for the VTP member, this value is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdiscoverresultsystemname
            
            	sysName of the VTP member
            	**type**\: str
            
            	**range:** 0..64
            
            

            """

            _prefix = 'cisco-vtp'
            _revision = '2013-10-14'

            def __init__(self):
                self.parent = None
                self.managementdomainindex = None
                self.vtpdiscoverresultindex = None
                self.vtpdiscoverresultconflicting = None
                self.vtpdiscoverresultdatabasename = None
                self.vtpdiscoverresultdeviceid = None
                self.vtpdiscoverresultprimaryserver = None
                self.vtpdiscoverresultrevnumber = None
                self.vtpdiscoverresultsystemname = None

            @property
            def _common_path(self):
                if self.managementdomainindex is None:
                    raise YPYDataValidationError('Key property managementdomainindex is None')
                if self.vtpdiscoverresultindex is None:
                    raise YPYDataValidationError('Key property vtpdiscoverresultindex is None')

                return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpDiscoverResultTable/CISCO-VTP-MIB:vtpDiscoverResultEntry[CISCO-VTP-MIB:managementDomainIndex = ' + str(self.managementdomainindex) + '][CISCO-VTP-MIB:vtpDiscoverResultIndex = ' + str(self.vtpdiscoverresultindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.managementdomainindex is not None:
                    return True

                if self.vtpdiscoverresultindex is not None:
                    return True

                if self.vtpdiscoverresultconflicting is not None:
                    return True

                if self.vtpdiscoverresultdatabasename is not None:
                    return True

                if self.vtpdiscoverresultdeviceid is not None:
                    return True

                if self.vtpdiscoverresultprimaryserver is not None:
                    return True

                if self.vtpdiscoverresultrevnumber is not None:
                    return True

                if self.vtpdiscoverresultsystemname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.VtpDiscoverResultTable.VtpDiscoverResultEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpDiscoverResultTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vtpdiscoverresultentry is not None:
                for child_ref in self.vtpdiscoverresultentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VtpDiscoverResultTable']['meta_info']


    class VtpDiscoverTable(object):
        """
        This table contains information related to the discovery
        of the VTP members in the designated management
        domain. This table is not instantiated when 
        managementDomainVersionInUse is version1(1), version2(3)
        or none(3).
        
        .. attribute:: vtpdiscoverentry
        
        	Information related to the discovery of the VTP members in one management domain
        	**type**\: list of :py:class:`VtpDiscoverEntry <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpDiscoverTable.VtpDiscoverEntry>`
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vtpdiscoverentry = YList()
            self.vtpdiscoverentry.parent = self
            self.vtpdiscoverentry.name = 'vtpdiscoverentry'


        class VtpDiscoverEntry(object):
            """
            Information related to the discovery of the
            VTP members in one management domain.
            
            .. attribute:: managementdomainindex
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: vtpdiscoveraction
            
            	When this object is set to discover(1), all the entries in vtpDiscoverResultTable for the corresponding management domain will be removed  and the local device will begin to discover all VTP members in the management domain. Upon the successful completion of discovery, the discovered result will be stored in the vtpDiscoverResultTable.  If vtpDiscoverStatus is inProgress(1), setting  vtpDiscoverAction to discover(1) will fail.   When this object is set to purgeResult(3),  all the entries of vtpDiscoverResultTable for  the corresponding management domain will be removed from vtpDiscoverResultTable.  When this object is set to noOperation(2), no action will be taken. When read, this object always returns noOperation(2)
            	**type**\: :py:class:`VtpDiscoverAction_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpDiscoverTable.VtpDiscoverEntry.VtpDiscoverAction_Enum>`
            
            .. attribute:: vtpdiscoverstatus
            
            	The current status of VTP discovery.  inProgress \- a discovery is in progress;  succeeded \- the discovery was completed successfully             (this value is also used when              no discover has been invoked since the             last time the local system restarted);  resourceUnavailable \- the discovery failed because             the required allocation of a resource is             presently unavailable.  someOtherError \- 'the discovery failed due to a             reason no listed
            	**type**\: :py:class:`VtpDiscoverStatus_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpDiscoverTable.VtpDiscoverEntry.VtpDiscoverStatus_Enum>`
            
            .. attribute:: vtplastdiscovertime
            
            	The value of sysUpTime at which the last discovery was completed.  A value of zero indicates that no discovery has been invoked since last time the local system restarted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-vtp'
            _revision = '2013-10-14'

            def __init__(self):
                self.parent = None
                self.managementdomainindex = None
                self.vtpdiscoveraction = None
                self.vtpdiscoverstatus = None
                self.vtplastdiscovertime = None

            class VtpDiscoverAction_Enum(Enum):
                """
                VtpDiscoverAction_Enum

                When this object is set to discover(1), all the
                entries in vtpDiscoverResultTable for the
                corresponding management domain will be removed 
                and the local device will begin to discover all
                VTP members in the management domain. Upon the
                successful completion of discovery, the discovered
                result will be stored in the vtpDiscoverResultTable.
                
                If vtpDiscoverStatus is inProgress(1), setting 
                vtpDiscoverAction to discover(1) will fail. 
                
                When this object is set to purgeResult(3), 
                all the entries of vtpDiscoverResultTable for 
                the corresponding management domain will be
                removed from vtpDiscoverResultTable.
                
                When this object is set to noOperation(2), no
                action will be taken. When read, this object
                always returns noOperation(2).

                """

                DISCOVER = 1

                NOOPERATION = 2

                PURGERESULT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VtpDiscoverTable.VtpDiscoverEntry.VtpDiscoverAction_Enum']


            class VtpDiscoverStatus_Enum(Enum):
                """
                VtpDiscoverStatus_Enum

                The current status of VTP discovery.
                
                inProgress \- a discovery is in progress;
                
                succeeded \- the discovery was completed successfully
                            (this value is also used when 
                            no discover has been invoked since the
                            last time the local system restarted);
                
                resourceUnavailable \- the discovery failed because
                            the required allocation of a resource is
                            presently unavailable.
                
                someOtherError \- 'the discovery failed due to a
                            reason no listed.

                """

                INPROGRESS = 1

                SUCCEEDED = 2

                RESOURCEUNAVAILABLE = 3

                SOMEOTHERERROR = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VtpDiscoverTable.VtpDiscoverEntry.VtpDiscoverStatus_Enum']


            @property
            def _common_path(self):
                if self.managementdomainindex is None:
                    raise YPYDataValidationError('Key property managementdomainindex is None')

                return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpDiscoverTable/CISCO-VTP-MIB:vtpDiscoverEntry[CISCO-VTP-MIB:managementDomainIndex = ' + str(self.managementdomainindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.managementdomainindex is not None:
                    return True

                if self.vtpdiscoveraction is not None:
                    return True

                if self.vtpdiscoverstatus is not None:
                    return True

                if self.vtplastdiscovertime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.VtpDiscoverTable.VtpDiscoverEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpDiscoverTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vtpdiscoverentry is not None:
                for child_ref in self.vtpdiscoverentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VtpDiscoverTable']['meta_info']


    class VtpInternalVlanTable(object):
        """
        A vtpInternalVlanTable entry contains
        information on an existing internal
        VLAN. It is internally created by the
        device for a specific application program 
        and hence owned by the application.  
        It cannot be modified or deleted by (local 
        or network) management.
        
        .. attribute:: vtpinternalvlanentry
        
        	Information about one current internal VLAN
        	**type**\: list of :py:class:`VtpInternalVlanEntry <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpInternalVlanTable.VtpInternalVlanEntry>`
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vtpinternalvlanentry = YList()
            self.vtpinternalvlanentry.parent = self
            self.vtpinternalvlanentry.name = 'vtpinternalvlanentry'


        class VtpInternalVlanEntry(object):
            """
            Information about one current internal
            VLAN.
            
            .. attribute:: managementdomainindex
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: vtpvlanindex
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpinternalvlanowner
            
            	The program name of the internal VLAN's owner application. This internal VLAN is allocated by the device specifically for this application and no one else could create, modify or delete this  VLAN
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-vtp'
            _revision = '2013-10-14'

            def __init__(self):
                self.parent = None
                self.managementdomainindex = None
                self.vtpvlanindex = None
                self.vtpinternalvlanowner = None

            @property
            def _common_path(self):
                if self.managementdomainindex is None:
                    raise YPYDataValidationError('Key property managementdomainindex is None')
                if self.vtpvlanindex is None:
                    raise YPYDataValidationError('Key property vtpvlanindex is None')

                return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpInternalVlanTable/CISCO-VTP-MIB:vtpInternalVlanEntry[CISCO-VTP-MIB:managementDomainIndex = ' + str(self.managementdomainindex) + '][CISCO-VTP-MIB:vtpVlanIndex = ' + str(self.vtpvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.managementdomainindex is not None:
                    return True

                if self.vtpvlanindex is not None:
                    return True

                if self.vtpinternalvlanowner is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.VtpInternalVlanTable.VtpInternalVlanEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpInternalVlanTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vtpinternalvlanentry is not None:
                for child_ref in self.vtpinternalvlanentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VtpInternalVlanTable']['meta_info']


    class VtpStatus(object):
        """
        
        
        .. attribute:: vtpmaxvlanstorage
        
        	An estimate of the maximum number of VLANs about which the local system can recover complete VTP information after a reboot.  If the number of defined VLANs is greater than this value, then the system can not act as a VTP Server. For a device which has no means to calculate the estimated number, this value is \-1
        	**type**\: int
        
        	**range:** \-1..1023
        
        .. attribute:: vtpnotificationsenabled
        
        	An indication of whether the notifications/traps defined by the vtpConfigNotificationsGroup, vtpConfigNotificationsGroup2, and vtpConfigNotificationsGroup8 are enabled
        	**type**\: bool
        
        .. attribute:: vtpversion
        
        	The version of VTP in use on the local system.  A device will report its version capability and not any particular version in use on the device. If the device does not support vtp, the version is none(3)
        	**type**\: :py:class:`VtpVersion_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpStatus.VtpVersion_Enum>`
        
        .. attribute:: vtpvlancreatednotifenabled
        
        	An indication of whether the notification should be generated when a VLAN is created.   If the value of this object is 'true' then the vtpVlanCreated notification will be generated.  If the value of this object is 'false' then the vtpVlanCreated notification will not be generated
        	**type**\: bool
        
        .. attribute:: vtpvlandeletednotifenabled
        
        	An indication of whether the notification should be generated when a VLAN is deleted.    If the value of this object is 'true' then the vtpVlanDeleted notification will be generated.  If the value of this object is 'false' then the vtpVlanDeleted notification will not be generated
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vtpmaxvlanstorage = None
            self.vtpnotificationsenabled = None
            self.vtpversion = None
            self.vtpvlancreatednotifenabled = None
            self.vtpvlandeletednotifenabled = None

        class VtpVersion_Enum(Enum):
            """
            VtpVersion_Enum

            The version of VTP in use on the local system.  A device
            will report its version capability and not any particular
            version in use on the device. If the device does not support
            vtp, the version is none(3).

            """

            ONE = 1

            TWO = 2

            NONE = 3

            THREE = 4


            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.VtpStatus.VtpVersion_Enum']


        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpStatus'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vtpmaxvlanstorage is not None:
                return True

            if self.vtpnotificationsenabled is not None:
                return True

            if self.vtpversion is not None:
                return True

            if self.vtpvlancreatednotifenabled is not None:
                return True

            if self.vtpvlandeletednotifenabled is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VtpStatus']['meta_info']


    class VtpVlanEditTable(object):
        """
        The table which contains the information in the Edit
        Buffers, one Edit Buffer per management domain.  The
        information for a particular management domain is
        initialized, by a 'copy' operation, to be the current global
        VLAN information for that management domain.  After
        initialization, editing can be performed to add VLANs,
        delete VLANs, or modify their global parameters.  The
        information as modified through editing is local to this
        Edit Buffer.  An apply operation using the
        vtpVlanEditOperation object is necessary to instanciate the
        modified information as the new global VLAN information for
        that management domain.
        
        To use the Edit Buffer, a manager acts as follows\:
        
        1. ensures the Edit Buffer for a management domain is empty,
        i.e., there are no rows in this table for this management
        domain.
        
        2. issues a SNMP set operation which sets
        vtpVlanEditOperation to 'copy', and vtpVlanEditBufferOwner
        to its own identifier (e.g., its own IP address).
        
        3. if this set operation is successful, proceeds to edit the
        information in the vtpVlanEditTable.
        
        4. if and when the edited information is to be instantiated,
        issues a SNMP set operation which sets vtpVlanEditOperation
        to 'apply'.
        
        5. issues retrieval requests to obtain the value of
        vtpVlanApplyStatus, until the result of the apply is
        determined.
        
        6. releases the Edit Buffer by issuing a SNMP set operation
        which sets vtpVlanEditOperation to 'release'.
        
        Note that the information contained in this table is not
        saved across agent reboots.
        
        .. attribute:: vtpvlaneditentry
        
        	Information about one VLAN in the Edit Buffer for a particular management domain
        	**type**\: list of :py:class:`VtpVlanEditEntry <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanEditTable.VtpVlanEditEntry>`
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vtpvlaneditentry = YList()
            self.vtpvlaneditentry.parent = self
            self.vtpvlaneditentry.name = 'vtpvlaneditentry'


        class VtpVlanEditEntry(object):
            """
            Information about one VLAN in the Edit Buffer for a
            particular management domain.
            
            .. attribute:: managementdomainindex
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: vtpvlaneditindex
            
            	The VLAN\-id which this VLAN would have on ISL or 802.1q trunks
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: stpxvlanmistpinstmapeditinstindex
            
            	The MISTP instance, to which the corresponding vlan would be  mapped. The value of this mib object is from 0 to the value of stpxMISTPInstanceNumber. If setting the value of this object to 0, the corresponding vlan will not be mapped to a MISTP  instance and all the ports under this VLAN will be moved into the blocking state
            	**type**\: int
            
            	**range:** 0..256
            
            .. attribute:: vtpvlaneditarehopcount
            
            	The maximum number of bridge hops allowed in All Routes Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\: int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlaneditbridgenumber
            
            	The bridge number of the VTP\-capable switches which would be used for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of fddiNet(4) or trNet(5)
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: vtpvlaneditbridgetype
            
            	The type of Source Route bridging mode which would be in use on this VLAN.  This object is only instantiated when  the value of  the corresponding instance of vtpVlanEditType has a value of fddi(2) or tokenRing(3) and Source Routing  is in use on this VLAN
            	**type**\: :py:class:`VtpVlanEditBridgeType_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanEditTable.VtpVlanEditEntry.VtpVlanEditBridgeType_Enum>`
            
            .. attribute:: vtpvlaneditdot10said
            
            	The value of the 802.10 SAID field which would be used for this VLAN.  An implementation may restrict access to this object
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: vtpvlaneditiscrfbackup
            
            	True if this VLAN is of type trCrf and also is acting as a backup trCrf for the ISL distributed BRF.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of tokenRing(3)
            	**type**\: bool
            
            .. attribute:: vtpvlaneditmtu
            
            	The MTU size which this VLAN would have, defined as the size of largest MAC\-layer (information field portion of the) data frame which can be transmitted on the VLAN.  An implementation may restrict access to this object
            	**type**\: int
            
            	**range:** 1500..18190
            
            .. attribute:: vtpvlaneditname
            
            	The name which this VLAN would have.  This name would be used as the ELAN\-name for an ATM LAN\-Emulation segment of this VLAN.  An implementation may restrict access to this object
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: vtpvlaneditparentvlan
            
            	The VLAN index of the VLAN which would be the parent for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on this VLAN.  The parent VLAN must have a vtpVlanEditType  value of fddiNet(4) or trNet(5), respectively
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlaneditringnumber
            
            	The ring number which would be used for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on  this VLAN
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlaneditrowstatus
            
            	The status of this row.  Any and all columnar objects in an existing row can be modified irrespective of the status of the row.  A row is not qualified for activation until instances of at least its vtpVlanEditType, vtpVlanEditName and vtpVlanEditDot10Said columns have appropriate values.  The management station should endeavor to make all rows consistent in the table before 'apply'ing the buffer.  An inconsistent entry in the table will cause the entire buffer to be rejected with the vtpVlanApplyStatus object set to the appropriate error value
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: vtpvlaneditstate
            
            	The state which this VLAN would have
            	**type**\: :py:class:`VtpVlanEditState_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanEditTable.VtpVlanEditEntry.VtpVlanEditState_Enum>`
            
            .. attribute:: vtpvlaneditstehopcount
            
            	The maximum number of bridge hops allowed in Spanning Tree Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\: int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlaneditstptype
            
            	The type of the Spanning Tree Protocol which would be running on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of fddiNet(4) or trNet(5).  If 'ieee' is selected, the STP that runs will be IEEE.  If 'ibm' is selected, the STP that runs will be IBM.  If 'auto' is selected, the STP that runs will be dependant on the values of vtpVlanEditBridgeType for all children tokenRing/fddi type VLANs.  This will result in a 'hybrid' STP (see vtpVlanStpType)
            	**type**\: :py:class:`VtpVlanEditStpType_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanEditTable.VtpVlanEditEntry.VtpVlanEditStpType_Enum>`
            
            .. attribute:: vtpvlanedittranslationalvlan1
            
            	A VLAN to which this VLAN would be translational\-bridged. If this value and the corresponding instance of vtpVlanTranslationalVlan2 are both zero, then this VLAN would not be translational\-bridged.  An implementation may restrict access to this object
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanedittranslationalvlan2
            
            	Another VLAN, i.e., other than that indicated by vtpVlanEditTranslationalVlan1, to which this VLAN would be translational\-bridged.  If this value and the corresponding instance of vtpVlanTranslationalVlan1 are both zero, then this VLAN would not be translational\-bridged.  An implementation may restrict access to this object
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanedittype
            
            	The type which this VLAN would have. An implementation may restrict access to this object
            	**type**\: :py:class:`VlanType_Enum <ydk.models.vtp.CISCO_VTP_MIB.VlanType_Enum>`
            
            .. attribute:: vtpvlanedittypeext
            
            	The additional type information of this VLAN. vtpVlanEditTypeExt object is superseded by vtpVlanEditTypeExt2
            	**type**\: :py:class:`VlanTypeExt_Bits <ydk.models.vtp.CISCO_VTP_MIB.VlanTypeExt_Bits>`
            
            .. attribute:: vtpvlanedittypeext2
            
            	The additional type information of this VLAN. The VlanTypeExt TC specifies which bits may be written by a management application. The agent should provide a default value
            	**type**\: :py:class:`VlanTypeExt_Bits <ydk.models.vtp.CISCO_VTP_MIB.VlanTypeExt_Bits>`
            
            

            """

            _prefix = 'cisco-vtp'
            _revision = '2013-10-14'

            def __init__(self):
                self.parent = None
                self.managementdomainindex = None
                self.vtpvlaneditindex = None
                self.stpxvlanmistpinstmapeditinstindex = None
                self.vtpvlaneditarehopcount = None
                self.vtpvlaneditbridgenumber = None
                self.vtpvlaneditbridgetype = None
                self.vtpvlaneditdot10said = None
                self.vtpvlaneditiscrfbackup = None
                self.vtpvlaneditmtu = None
                self.vtpvlaneditname = None
                self.vtpvlaneditparentvlan = None
                self.vtpvlaneditringnumber = None
                self.vtpvlaneditrowstatus = None
                self.vtpvlaneditstate = None
                self.vtpvlaneditstehopcount = None
                self.vtpvlaneditstptype = None
                self.vtpvlanedittranslationalvlan1 = None
                self.vtpvlanedittranslationalvlan2 = None
                self.vtpvlanedittype = None
                self.vtpvlanedittypeext = VlanTypeExt_Bits()
                self.vtpvlanedittypeext2 = VlanTypeExt_Bits()

            class VtpVlanEditBridgeType_Enum(Enum):
                """
                VtpVlanEditBridgeType_Enum

                The type of Source Route bridging mode which would be in
                use on this VLAN.  This object is only instantiated when 
                the value of  the corresponding instance of vtpVlanEditType
                has a value of fddi(2) or tokenRing(3) and Source Routing 
                is in use on this VLAN.

                """

                SRT = 1

                SRB = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VtpVlanEditTable.VtpVlanEditEntry.VtpVlanEditBridgeType_Enum']


            class VtpVlanEditState_Enum(Enum):
                """
                VtpVlanEditState_Enum

                The state which this VLAN would have.

                """

                OPERATIONAL = 1

                SUSPENDED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VtpVlanEditTable.VtpVlanEditEntry.VtpVlanEditState_Enum']


            class VtpVlanEditStpType_Enum(Enum):
                """
                VtpVlanEditStpType_Enum

                The type of the Spanning Tree Protocol which would be
                running on this VLAN.  This object is only instantiated
                when the value of the corresponding instance of
                vtpVlanEditType has a value of fddiNet(4) or trNet(5).
                
                If 'ieee' is selected, the STP that runs will be IEEE.
                
                If 'ibm' is selected, the STP that runs will be IBM.
                
                If 'auto' is selected, the STP that runs will be
                dependant on the values of vtpVlanEditBridgeType for all
                children tokenRing/fddi type VLANs.  This will result in
                a 'hybrid' STP (see vtpVlanStpType).

                """

                IEEE = 1

                IBM = 2

                AUTO = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VtpVlanEditTable.VtpVlanEditEntry.VtpVlanEditStpType_Enum']


            @property
            def _common_path(self):
                if self.managementdomainindex is None:
                    raise YPYDataValidationError('Key property managementdomainindex is None')
                if self.vtpvlaneditindex is None:
                    raise YPYDataValidationError('Key property vtpvlaneditindex is None')

                return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpVlanEditTable/CISCO-VTP-MIB:vtpVlanEditEntry[CISCO-VTP-MIB:managementDomainIndex = ' + str(self.managementdomainindex) + '][CISCO-VTP-MIB:vtpVlanEditIndex = ' + str(self.vtpvlaneditindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.managementdomainindex is not None:
                    return True

                if self.vtpvlaneditindex is not None:
                    return True

                if self.stpxvlanmistpinstmapeditinstindex is not None:
                    return True

                if self.vtpvlaneditarehopcount is not None:
                    return True

                if self.vtpvlaneditbridgenumber is not None:
                    return True

                if self.vtpvlaneditbridgetype is not None:
                    return True

                if self.vtpvlaneditdot10said is not None:
                    return True

                if self.vtpvlaneditiscrfbackup is not None:
                    return True

                if self.vtpvlaneditmtu is not None:
                    return True

                if self.vtpvlaneditname is not None:
                    return True

                if self.vtpvlaneditparentvlan is not None:
                    return True

                if self.vtpvlaneditringnumber is not None:
                    return True

                if self.vtpvlaneditrowstatus is not None:
                    return True

                if self.vtpvlaneditstate is not None:
                    return True

                if self.vtpvlaneditstehopcount is not None:
                    return True

                if self.vtpvlaneditstptype is not None:
                    return True

                if self.vtpvlanedittranslationalvlan1 is not None:
                    return True

                if self.vtpvlanedittranslationalvlan2 is not None:
                    return True

                if self.vtpvlanedittype is not None:
                    return True

                if self.vtpvlanedittypeext is not None:
                    if self.vtpvlanedittypeext._has_data():
                        return True

                if self.vtpvlanedittypeext2 is not None:
                    if self.vtpvlanedittypeext2._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.VtpVlanEditTable.VtpVlanEditEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpVlanEditTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vtpvlaneditentry is not None:
                for child_ref in self.vtpvlaneditentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VtpVlanEditTable']['meta_info']


    class VtpVlanLocalShutdownTable(object):
        """
        Ths table contains the VLAN local shutdown
        information within management domain.
        
        .. attribute:: vtpvlanlocalshutdownentry
        
        	An entry containing VLAN local shutdown information for a particular VLAN in the management domain.  An entry is created if a VLAN which supports local shutdown has been created.  An entry is deleted if a VLAN which supports local shutdown has been removed
        	**type**\: list of :py:class:`VtpVlanLocalShutdownEntry <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanLocalShutdownTable.VtpVlanLocalShutdownEntry>`
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vtpvlanlocalshutdownentry = YList()
            self.vtpvlanlocalshutdownentry.parent = self
            self.vtpvlanlocalshutdownentry.name = 'vtpvlanlocalshutdownentry'


        class VtpVlanLocalShutdownEntry(object):
            """
            An entry containing VLAN local shutdown information for a
            particular VLAN in the management domain.
            
            An entry is created if a VLAN which supports local shutdown
            has been created.
            
            An entry is deleted if a VLAN which supports local shutdown
            has been removed.
            
            .. attribute:: managementdomainindex
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: vtpvlanindex
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanlocalshutdown
            
            	The object specifies the VLAN local shutdown state
            	**type**\: :py:class:`VtpVlanLocalShutdown_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanLocalShutdownTable.VtpVlanLocalShutdownEntry.VtpVlanLocalShutdown_Enum>`
            
            

            """

            _prefix = 'cisco-vtp'
            _revision = '2013-10-14'

            def __init__(self):
                self.parent = None
                self.managementdomainindex = None
                self.vtpvlanindex = None
                self.vtpvlanlocalshutdown = None

            class VtpVlanLocalShutdown_Enum(Enum):
                """
                VtpVlanLocalShutdown_Enum

                The object specifies the VLAN local shutdown state.

                """

                UP = 1

                DOWN = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VtpVlanLocalShutdownTable.VtpVlanLocalShutdownEntry.VtpVlanLocalShutdown_Enum']


            @property
            def _common_path(self):
                if self.managementdomainindex is None:
                    raise YPYDataValidationError('Key property managementdomainindex is None')
                if self.vtpvlanindex is None:
                    raise YPYDataValidationError('Key property vtpvlanindex is None')

                return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpVlanLocalShutdownTable/CISCO-VTP-MIB:vtpVlanLocalShutdownEntry[CISCO-VTP-MIB:managementDomainIndex = ' + str(self.managementdomainindex) + '][CISCO-VTP-MIB:vtpVlanIndex = ' + str(self.vtpvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.managementdomainindex is not None:
                    return True

                if self.vtpvlanindex is not None:
                    return True

                if self.vtpvlanlocalshutdown is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.VtpVlanLocalShutdownTable.VtpVlanLocalShutdownEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpVlanLocalShutdownTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vtpvlanlocalshutdownentry is not None:
                for child_ref in self.vtpvlanlocalshutdownentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VtpVlanLocalShutdownTable']['meta_info']


    class VtpVlanTable(object):
        """
        This table contains information on the VLANs which
        currently exist.
        
        .. attribute:: vtpvlanentry
        
        	Information about one current VLAN.  The managementDomainIndex value in the INDEX clause indicates which management domain the VLAN is in
        	**type**\: list of :py:class:`VtpVlanEntry <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanTable.VtpVlanEntry>`
        
        

        """

        _prefix = 'cisco-vtp'
        _revision = '2013-10-14'

        def __init__(self):
            self.parent = None
            self.vtpvlanentry = YList()
            self.vtpvlanentry.parent = self
            self.vtpvlanentry.name = 'vtpvlanentry'


        class VtpVlanEntry(object):
            """
            Information about one current VLAN.  The
            managementDomainIndex value in the INDEX clause indicates
            which management domain the VLAN is in.
            
            .. attribute:: managementdomainindex
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: vtpvlanindex
            
            	The VLAN\-id of this VLAN on ISL or 802.1q trunks
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: stpxvlanmistpinstmapinstindex
            
            	The MISTP instance, to which the corresponding vlan is mapped. If this value of this mib object is 0,  the corresponding vlan  is not configured to be mapped to any MISTP instance and all the ports under this VLAN remain in blocking state
            	**type**\: int
            
            	**range:** 0..256
            
            .. attribute:: vtpvlanarehopcount
            
            	The maximum number of bridge hops allowed in All Routes Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\: int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlanbridgenumber
            
            	The bridge number of the VTP\-capable switches for this VLAN.  This object is only instantiated for VLANs that are involved with emulating token ring segments
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: vtpvlanbridgetype
            
            	The type of the Source Route bridging mode in use on this VLAN.  This object is only instantiated when the value of  the corresponding instance of vtpVlanType has a value of  fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\: :py:class:`VtpVlanBridgeType_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanTable.VtpVlanEntry.VtpVlanBridgeType_Enum>`
            
            .. attribute:: vtpvlandot10said
            
            	The value of the 802.10 SAID field for this VLAN
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: vtpvlanifindex
            
            	The value of the ifIndex corresponding to this VLAN ID. If the VLAN ID does not have its corresponding interface,  this object has the value of zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: vtpvlaniscrfbackup
            
            	True if this VLAN is of type trCrf and also is acting as a backup trCrf for the ISL distributed BRF
            	**type**\: bool
            
            .. attribute:: vtpvlanmtu
            
            	The MTU size on this VLAN, defined as the size of largest MAC\-layer (information field portion of the) data frame which can be transmitted on the VLAN
            	**type**\: int
            
            	**range:** 1500..18190
            
            .. attribute:: vtpvlanname
            
            	The name of this VLAN.  This name is used as the ELAN\-name for an ATM LAN\-Emulation segment of this VLAN
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: vtpvlanparentvlan
            
            	The parent VLAN for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on this VLAN.  The parent VLAN must have  a vtpVlanType value of fddiNet(4) or trNet(5),  respectively
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanringnumber
            
            	The ring number of this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on this VLAN
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanstate
            
            	The state of this VLAN.  The state 'mtuTooBigForDevice' indicates that this device cannot participate in this VLAN because the VLAN's MTU is larger than the device can support.  The state 'mtuTooBigForTrunk' indicates that while this VLAN's MTU is supported by this device, it is too large for one or more of the device's trunk ports
            	**type**\: :py:class:`VtpVlanState_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanTable.VtpVlanEntry.VtpVlanState_Enum>`
            
            .. attribute:: vtpvlanstehopcount
            
            	The maximum number of bridge hops allowed in Spanning Tree Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\: int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlanstptype
            
            	The type of the Spanning Tree Protocol (STP) running on this VLAN.  This object is only instanciated when the value of the corresponding instance of vtpVlanType has a value of 'fddiNet' or 'trNet'.  The value returned by this object depends upon the value of the corresponding instance of vtpVlanEditStpType.  \- 'ieee' indicates IEEE STP is running exclusively.  \- 'ibm' indicates IBM STP is running exclusively.  \- 'hybrid' indicates a STP that allows a combination of   IEEE and IBM is running.  The 'hybrid' STP type results from tokenRing/fddi VLANs that are children of this trNet/fddiNet parent VLAN being configured in a combination of SRT and SRB vtpVlanBridgeTypes while the instance of vtpVlanEditStpType that corresponds to this object is set to 'auto'
            	**type**\: :py:class:`VtpVlanStpType_Enum <ydk.models.vtp.CISCO_VTP_MIB.CISCOVTPMIB.VtpVlanTable.VtpVlanEntry.VtpVlanStpType_Enum>`
            
            .. attribute:: vtpvlantranslationalvlan1
            
            	A VLAN to which this VLAN is being translational\-bridged. If this value and the corresponding instance of vtpVlanTranslationalVlan2 are both zero, then this VLAN is not being translational\-bridged
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlantranslationalvlan2
            
            	Another VLAN, i.e., other than that indicated by vtpVlanTranslationalVlan1, to which this VLAN is being translational\-bridged.  If this value and the corresponding instance of vtpVlanTranslationalVlan1 are both zero, then this VLAN is not being translational\-bridged
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlantype
            
            	The type of this VLAN
            	**type**\: :py:class:`VlanType_Enum <ydk.models.vtp.CISCO_VTP_MIB.VlanType_Enum>`
            
            .. attribute:: vtpvlantypeext
            
            	The additional type information of this VLAN
            	**type**\: :py:class:`VlanTypeExt_Bits <ydk.models.vtp.CISCO_VTP_MIB.VlanTypeExt_Bits>`
            
            

            """

            _prefix = 'cisco-vtp'
            _revision = '2013-10-14'

            def __init__(self):
                self.parent = None
                self.managementdomainindex = None
                self.vtpvlanindex = None
                self.stpxvlanmistpinstmapinstindex = None
                self.vtpvlanarehopcount = None
                self.vtpvlanbridgenumber = None
                self.vtpvlanbridgetype = None
                self.vtpvlandot10said = None
                self.vtpvlanifindex = None
                self.vtpvlaniscrfbackup = None
                self.vtpvlanmtu = None
                self.vtpvlanname = None
                self.vtpvlanparentvlan = None
                self.vtpvlanringnumber = None
                self.vtpvlanstate = None
                self.vtpvlanstehopcount = None
                self.vtpvlanstptype = None
                self.vtpvlantranslationalvlan1 = None
                self.vtpvlantranslationalvlan2 = None
                self.vtpvlantype = None
                self.vtpvlantypeext = VlanTypeExt_Bits()

            class VtpVlanBridgeType_Enum(Enum):
                """
                VtpVlanBridgeType_Enum

                The type of the Source Route bridging mode in use on this
                VLAN.  This object is only instantiated when the value of 
                the corresponding instance of vtpVlanType has a value of 
                fddi(2) or tokenRing(3) and Source Routing is in use on
                this VLAN.

                """

                SRT = 1

                SRB = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VtpVlanTable.VtpVlanEntry.VtpVlanBridgeType_Enum']


            class VtpVlanState_Enum(Enum):
                """
                VtpVlanState_Enum

                The state of this VLAN.
                
                The state 'mtuTooBigForDevice' indicates that this device
                cannot participate in this VLAN because the VLAN's MTU is
                larger than the device can support.
                
                The state 'mtuTooBigForTrunk' indicates that while this
                VLAN's MTU is supported by this device, it is too large for
                one or more of the device's trunk ports.

                """

                OPERATIONAL = 1

                SUSPENDED = 2

                MTUTOOBIGFORDEVICE = 3

                MTUTOOBIGFORTRUNK = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VtpVlanTable.VtpVlanEntry.VtpVlanState_Enum']


            class VtpVlanStpType_Enum(Enum):
                """
                VtpVlanStpType_Enum

                The type of the Spanning Tree Protocol (STP) running on
                this VLAN.  This object is only instanciated when the
                value of the corresponding instance of vtpVlanType has a
                value of 'fddiNet' or 'trNet'.
                
                The value returned by this object depends upon the value
                of the corresponding instance of vtpVlanEditStpType.
                
                \- 'ieee' indicates IEEE STP is running exclusively.
                
                \- 'ibm' indicates IBM STP is running exclusively.
                
                \- 'hybrid' indicates a STP that allows a combination of
                  IEEE and IBM is running.
                
                The 'hybrid' STP type results from tokenRing/fddi VLANs
                that are children of this trNet/fddiNet parent VLAN being
                configured in a combination of SRT and SRB
                vtpVlanBridgeTypes while the instance of
                vtpVlanEditStpType that corresponds to this object is set
                to 'auto'.

                """

                IEEE = 1

                IBM = 2

                HYBRID = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                    return meta._meta_table['CISCOVTPMIB.VtpVlanTable.VtpVlanEntry.VtpVlanStpType_Enum']


            @property
            def _common_path(self):
                if self.managementdomainindex is None:
                    raise YPYDataValidationError('Key property managementdomainindex is None')
                if self.vtpvlanindex is None:
                    raise YPYDataValidationError('Key property vtpvlanindex is None')

                return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpVlanTable/CISCO-VTP-MIB:vtpVlanEntry[CISCO-VTP-MIB:managementDomainIndex = ' + str(self.managementdomainindex) + '][CISCO-VTP-MIB:vtpVlanIndex = ' + str(self.vtpvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.managementdomainindex is not None:
                    return True

                if self.vtpvlanindex is not None:
                    return True

                if self.stpxvlanmistpinstmapinstindex is not None:
                    return True

                if self.vtpvlanarehopcount is not None:
                    return True

                if self.vtpvlanbridgenumber is not None:
                    return True

                if self.vtpvlanbridgetype is not None:
                    return True

                if self.vtpvlandot10said is not None:
                    return True

                if self.vtpvlanifindex is not None:
                    return True

                if self.vtpvlaniscrfbackup is not None:
                    return True

                if self.vtpvlanmtu is not None:
                    return True

                if self.vtpvlanname is not None:
                    return True

                if self.vtpvlanparentvlan is not None:
                    return True

                if self.vtpvlanringnumber is not None:
                    return True

                if self.vtpvlanstate is not None:
                    return True

                if self.vtpvlanstehopcount is not None:
                    return True

                if self.vtpvlanstptype is not None:
                    return True

                if self.vtpvlantranslationalvlan1 is not None:
                    return True

                if self.vtpvlantranslationalvlan2 is not None:
                    return True

                if self.vtpvlantype is not None:
                    return True

                if self.vtpvlantypeext is not None:
                    if self.vtpvlantypeext._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
                return meta._meta_table['CISCOVTPMIB.VtpVlanTable.VtpVlanEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VTP-MIB:CISCO-VTP-MIB/CISCO-VTP-MIB:vtpVlanTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vtpvlanentry is not None:
                for child_ref in self.vtpvlanentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
            return meta._meta_table['CISCOVTPMIB.VtpVlanTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-VTP-MIB:CISCO-VTP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.internalvlaninfo is not None and self.internalvlaninfo._has_data():
            return True

        if self.internalvlaninfo is not None and self.internalvlaninfo.is_presence():
            return True

        if self.managementdomaintable is not None and self.managementdomaintable._has_data():
            return True

        if self.managementdomaintable is not None and self.managementdomaintable.is_presence():
            return True

        if self.vlanstatistics is not None and self.vlanstatistics._has_data():
            return True

        if self.vlanstatistics is not None and self.vlanstatistics.is_presence():
            return True

        if self.vlantrunkports is not None and self.vlantrunkports._has_data():
            return True

        if self.vlantrunkports is not None and self.vlantrunkports.is_presence():
            return True

        if self.vlantrunkporttable is not None and self.vlantrunkporttable._has_data():
            return True

        if self.vlantrunkporttable is not None and self.vlantrunkporttable.is_presence():
            return True

        if self.vtpauthenticationtable is not None and self.vtpauthenticationtable._has_data():
            return True

        if self.vtpauthenticationtable is not None and self.vtpauthenticationtable.is_presence():
            return True

        if self.vtpdatabasetable is not None and self.vtpdatabasetable._has_data():
            return True

        if self.vtpdatabasetable is not None and self.vtpdatabasetable.is_presence():
            return True

        if self.vtpdiscoverresulttable is not None and self.vtpdiscoverresulttable._has_data():
            return True

        if self.vtpdiscoverresulttable is not None and self.vtpdiscoverresulttable.is_presence():
            return True

        if self.vtpdiscovertable is not None and self.vtpdiscovertable._has_data():
            return True

        if self.vtpdiscovertable is not None and self.vtpdiscovertable.is_presence():
            return True

        if self.vtpinternalvlantable is not None and self.vtpinternalvlantable._has_data():
            return True

        if self.vtpinternalvlantable is not None and self.vtpinternalvlantable.is_presence():
            return True

        if self.vtpstatus is not None and self.vtpstatus._has_data():
            return True

        if self.vtpstatus is not None and self.vtpstatus.is_presence():
            return True

        if self.vtpvlanedittable is not None and self.vtpvlanedittable._has_data():
            return True

        if self.vtpvlanedittable is not None and self.vtpvlanedittable.is_presence():
            return True

        if self.vtpvlanlocalshutdowntable is not None and self.vtpvlanlocalshutdowntable._has_data():
            return True

        if self.vtpvlanlocalshutdowntable is not None and self.vtpvlanlocalshutdowntable.is_presence():
            return True

        if self.vtpvlantable is not None and self.vtpvlantable._has_data():
            return True

        if self.vtpvlantable is not None and self.vtpvlantable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.vtp._meta import _CISCO_VTP_MIB as meta
        return meta._meta_table['CISCOVTPMIB']['meta_info']


