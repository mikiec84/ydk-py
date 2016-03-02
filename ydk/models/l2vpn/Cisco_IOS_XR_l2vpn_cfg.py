""" Cisco_IOS_XR_l2vpn_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR l2vpn package configuration.

This module contains definitions
for the following management objects\:
  l2vpn\: L2VPN configuration
  generic\-interface\-lists\: generic interface lists
  evpn\: evpn

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
modules with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class BackupDisable_Enum(Enum):
    """
    BackupDisable_Enum

    Backup disable

    """

    """

    Never

    """
    NEVER = 0

    """

    Delay seconds

    """
    DELAY = 1


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BackupDisable_Enum']


class BgpRouteDistinguisher_Enum(Enum):
    """
    BgpRouteDistinguisher_Enum

    Bgp route distinguisher

    """

    """

    RD automatically assigned

    """
    AUTO = 1

    """

    RD in 2 byte AS\:nn format

    """
    TWO_BYTE_AS = 2

    """

    RD in 4 byte AS\:nn format

    """
    FOUR_BYTE_AS = 3

    """

    RD in IpV4address

    """
    IPV4_ADDRESS = 4


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BgpRouteDistinguisher_Enum']


class BgpRouteTargetFormat_Enum(Enum):
    """
    BgpRouteTargetFormat_Enum

    Bgp route target format

    """

    """

    No route target

    """
    NONE = 0

    """

    2 Byte AS\:nn format

    """
    TWO_BYTE_AS = 1

    """

    4 byte AS\:nn format

    """
    FOUR_BYTE_AS = 2

    """

    IP\:nn format

    """
    IPV4_ADDRESS = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BgpRouteTargetFormat_Enum']


class BgpRouteTargetRole_Enum(Enum):
    """
    BgpRouteTargetRole_Enum

    Bgp route target role

    """

    """

    Both Import and export roles

    """
    BOTH = 0

    """

    Import role

    """
    IMPORT = 1

    """

    Export role

    """
    EXPORT = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BgpRouteTargetRole_Enum']


class BridgeDomainTransportMode_Enum(Enum):
    """
    BridgeDomainTransportMode_Enum

    Bridge domain transport mode

    """

    """

    Vlan tagged passthrough mode

    """
    VLAN_PASSTHROUGH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['BridgeDomainTransportMode_Enum']


class ControlWord_Enum(Enum):
    """
    ControlWord_Enum

    Control word

    """

    """

    Enable control word

    """
    ENABLE = 1

    """

    Disable control word

    """
    DISABLE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['ControlWord_Enum']


class ErpPort1_Enum(Enum):
    """
    ErpPort1_Enum

    Erp port1

    """

    """

    ERP main port 0

    """
    PORT0 = 0

    """

    ERP main port 1

    """
    PORT1 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['ErpPort1_Enum']


class ErpPort_Enum(Enum):
    """
    ErpPort_Enum

    Erp port

    """

    """

    ERP port type none

    """
    NONE = 1

    """

    ERP port type virtual

    """
    VIRTUAL = 2

    """

    ERP port type interface

    """
    INTERFACE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['ErpPort_Enum']


class Erpaps_Enum(Enum):
    """
    Erpaps_Enum

    Erpaps

    """

    """

    ERP APS type interface

    """
    INTERFACE = 1

    """

    ERP APS type bridge domain

    """
    BRIDGE_DOMAIN = 2

    """

    ERP APS type xconnect

    """
    XCONNECT = 3

    """

    ERP APS type none

    """
    NONE = 4


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['Erpaps_Enum']


class FlowLabelLoadBalance_Enum(Enum):
    """
    FlowLabelLoadBalance_Enum

    Flow label load balance

    """

    """

    Flow Label load balance is off

    """
    OFF = 0

    """

    Delete Flow Label on receive side

    """
    RECEIVE = 1

    """

    Insert Flow Label on transmit side

    """
    TRANSMIT = 2

    """

    Insert/Delete  Flow Label on transmit/receive
    side

    """
    BOTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['FlowLabelLoadBalance_Enum']


class FlowLabelTlvCode_Enum(Enum):
    """
    FlowLabelTlvCode_Enum

    Flow label tlv code

    """

    """

    Set Flow Label Legacy TLV code (DEPRECATED)

    """
    Y_17 = 4

    """

    Disable Sending Flow Label Legacy TLV

    """
    DISABLE = 8


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['FlowLabelTlvCode_Enum']


class InterfaceProfile_Enum(Enum):
    """
    InterfaceProfile_Enum

    Interface profile

    """

    """

    Set the snooping

    """
    SNOOP = 1

    """

    disable DHCP protocol

    """
    DHCP_PROTOCOL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['InterfaceProfile_Enum']


class InterfaceTrafficFlood_Enum(Enum):
    """
    InterfaceTrafficFlood_Enum

    Interface traffic flood

    """

    """

    Traffic flooding

    """
    TRAFFIC_FLOODING = 0

    """

    Enable Flooding

    """
    ENABLE_FLOODING = 1

    """

    Disable flooding

    """
    DISABLE_FLOODING = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['InterfaceTrafficFlood_Enum']


class Interworking_Enum(Enum):
    """
    Interworking_Enum

    Interworking

    """

    """

    Ethernet interworking

    """
    ETHERNET = 1

    """

    IPv4 interworking

    """
    IPV4 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['Interworking_Enum']


class L2Encapsulation_Enum(Enum):
    """
    L2Encapsulation_Enum

    L2 encapsulation

    """

    """

    Vlan tagged mode

    """
    VLAN = 4

    """

    Ethernet port mode

    """
    ETHERNET = 5


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2Encapsulation_Enum']


class L2tpCookieSize_Enum(Enum):
    """
    L2tpCookieSize_Enum

    L2tp cookie size

    """

    """

    Cookie size is zero bytes

    """
    ZERO = 0

    """

    Cookie size is four bytes

    """
    FOUR = 4

    """

    Cookie size is eight bytes

    """
    EIGHT = 8


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2tpCookieSize_Enum']


class L2tpSignalingProtocol_Enum(Enum):
    """
    L2tpSignalingProtocol_Enum

    L2tp signaling protocol

    """

    """

    No signaling

    """
    NONE = 1

    """

    L2TPv3

    """
    L2TPV3 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2tpSignalingProtocol_Enum']


class L2tpv3Sequencing_Enum(Enum):
    """
    L2tpv3Sequencing_Enum

    L2tpv3 sequencing

    """

    """

    Sequencing is off

    """
    OFF = 0

    """

    Sequencing on both transmit and receive side

    """
    BOTH = 4


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2tpv3Sequencing_Enum']


class L2vpnCapabilityMode_Enum(Enum):
    """
    L2vpnCapabilityMode_Enum

    L2vpn capability mode

    """

    """

    Compute global capability as the highest node
    capability

    """
    HIGH_MODE = 1

    """

    Disable global capability re\-computation

    """
    SINGLE_MODE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2vpnCapabilityMode_Enum']


class L2vpnLogging_Enum(Enum):
    """
    L2vpnLogging_Enum

    L2vpn logging

    """

    """

    enable logging

    """
    ENABLE = 1

    """

    disable logging

    """
    DISABLE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2vpnLogging_Enum']


class L2vpnVerification_Enum(Enum):
    """
    L2vpnVerification_Enum

    L2vpn verification

    """

    """

    enable verification

    """
    ENABLE = 1

    """

    disable verification

    """
    DISABLE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2vpnVerification_Enum']


class LdpVplsId_Enum(Enum):
    """
    LdpVplsId_Enum

    Ldp vpls id

    """

    """

    VPLS\-ID in 2 byte AS\:nn format

    """
    TWO_BYTE_AS = 10

    """

    VPLS\-ID in IPv4 IP\:nn format

    """
    IPV4_ADDRESS = 266


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['LdpVplsId_Enum']


class LoadBalance_Enum(Enum):
    """
    LoadBalance_Enum

    Load balance

    """

    """

    Source and Destination MAC hashing

    """
    SOURCE_DEST_MAC = 1

    """

    Source and Destination IP hashing

    """
    SOURCE_DEST_IP = 2

    """

    PW Label hashing

    """
    PSEUDOWIRE_LABEL = 4


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['LoadBalance_Enum']


class MacAging_Enum(Enum):
    """
    MacAging_Enum

    Mac aging

    """

    """

    Absolute aging type

    """
    ABSOLUTE = 1

    """

    Inactivity aging type

    """
    INACTIVITY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacAging_Enum']


class MacLearn_Enum(Enum):
    """
    MacLearn_Enum

    Mac learn

    """

    """

    Mac Learning

    """
    DEFAULT_LEARNING = 0

    """

    Enable Learning

    """
    ENABLE_LEARNING = 1

    """

    Disable Learning

    """
    DISABLE_LEARNING = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacLearn_Enum']


class MacLimitAction_Enum(Enum):
    """
    MacLimitAction_Enum

    Mac limit action

    """

    """

    No action

    """
    NONE = 0

    """

    Flood Mac Limit Action

    """
    FLOOD = 1

    """

    NoFlood Mac Limit Action

    """
    NO_FLOOD = 2

    """

    Shutdown Mac Limit Action

    """
    SHUTDOWN = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacLimitAction_Enum']


class MacNotification_Enum(Enum):
    """
    MacNotification_Enum

    Mac notification

    """

    """

    No\_Notification Trap

    """
    NO_NOTIF = 0

    """

    syslog message

    """
    SYSLOG = 1

    """

    Snmp Trap

    """
    TRAP = 2

    """

    Syslog\_snmp Trap

    """
    SYSLOG_SNMP = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacNotification_Enum']


class MacSecureAction_Enum(Enum):
    """
    MacSecureAction_Enum

    Mac secure action

    """

    """

    MAC Secure Action Restrict

    """
    RESTRICT = 1

    """

    No Action

    """
    NONE = 2

    """

    MAC Secure Action Shutdown

    """
    SHUTDOWN = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacSecureAction_Enum']


class MacWithdrawBehavior_Enum(Enum):
    """
    MacWithdrawBehavior_Enum

    Mac withdraw behavior

    """

    """

    MAC Withdrawal sent on state\-down (legacy)

    """
    LEGACY = 1

    """

    Optimized MAC Withdrawal

    """
    OPTIMIZED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MacWithdrawBehavior_Enum']


class MplsSequencing_Enum(Enum):
    """
    MplsSequencing_Enum

    Mpls sequencing

    """

    """

    Sequencing is off

    """
    OFF = 0

    """

    Sequencing on transmit side

    """
    TRANSMIT = 1

    """

    Sequencing on receive side

    """
    RECEIVE = 2

    """

    Sequencing on both transmit and receive side

    """
    BOTH = 4


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MplsSequencing_Enum']


class MplsSignalingProtocol_Enum(Enum):
    """
    MplsSignalingProtocol_Enum

    Mpls signaling protocol

    """

    """

    No signaling

    """
    NONE = 1

    """

    LDP

    """
    LDP = 4


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['MplsSignalingProtocol_Enum']


class PortDownFlush_Enum(Enum):
    """
    PortDownFlush_Enum

    Port down flush

    """

    """

    MAC Port Down Flush

    """
    PORT_DOWN_FLUSH = 0

    """

    Enable Port Down Flush

    """
    ENABLE_PORT_DOWN_FLUSH = 1

    """

    Disable Port Down Flush

    """
    DISABLE_PORT_DOWN_FLUSH = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['PortDownFlush_Enum']


class PreferredPath_Enum(Enum):
    """
    PreferredPath_Enum

    Preferred path

    """

    """

    TE Tunnel

    """
    TE_TUNNEL = 2

    """

    IP Tunnel

    """
    IP_TUNNEL = 3

    """

    TP Tunnel

    """
    TP_TUNNEL = 4


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['PreferredPath_Enum']


class PwSwitchingPointTlv_Enum(Enum):
    """
    PwSwitchingPointTlv_Enum

    Pw switching point tlv

    """

    """

    Hide TLV

    """
    HIDE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['PwSwitchingPointTlv_Enum']


class RplRole_Enum(Enum):
    """
    RplRole_Enum

    Rpl role

    """

    """

    ERP RPL owner

    """
    OWNER = 1

    """

    ERP RPL neighbor

    """
    NEIGHBOR = 2

    """

    ERP RPL next neighbor

    """
    NEXT_NEIGHBOR = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['RplRole_Enum']


class StormControl_Enum(Enum):
    """
    StormControl_Enum

    Storm control

    """

    """

    Unknown\-unicast Storm Control

    """
    UNICAST = 1

    """

    Multicast Storm Control

    """
    MULTICAST = 2

    """

    Broadcast Storm Control

    """
    BROADCAST = 4


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['StormControl_Enum']


class TransportMode_Enum(Enum):
    """
    TransportMode_Enum

    Transport mode

    """

    """

    Ethernet port mode

    """
    ETHERNET = 1

    """

    Vlan tagged mode

    """
    VLAN = 2

    """

    Vlan tagged passthrough mode

    """
    VLAN_PASSTHROUGH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['TransportMode_Enum']


class TypeOfServiceMode_Enum(Enum):
    """
    TypeOfServiceMode_Enum

    Type of service mode

    """

    """

    Do not reflect the type of service

    """
    NONE = 0

    """

    Reflect the type of service

    """
    REFLECT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['TypeOfServiceMode_Enum']


class VccvVerification_Enum(Enum):
    """
    VccvVerification_Enum

    Vccv verification

    """

    """

    No connectivity verification over VCCV

    """
    NONE = 0

    """

    LSP Ping over VCCV

    """
    LSP_PING = 2


    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['VccvVerification_Enum']



class Evpn(object):
    """
    evpn
    
    .. attribute:: enable
    
    	Enable EVPN feature
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: evpn_tables
    
    	EVPN submodes
    	**type**\: :py:class:`EvpnTables <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables>`
    
    .. attribute:: standard_version
    
    	Set Standard EVPN Version
    	**type**\: :py:class:`StandardVersion <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.StandardVersion>`
    
    

    """

    _prefix = 'l2vpn-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.enable = None
        self.evpn_tables = Evpn.EvpnTables()
        self.evpn_tables.parent = self
        self.standard_version = Evpn.StandardVersion()
        self.standard_version.parent = self


    class EvpnTables(object):
        """
        EVPN submodes
        
        .. attribute:: evpn_interfaces
        
        	Attachment Circuit interfaces
        	**type**\: :py:class:`EvpnInterfaces <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces>`
        
        .. attribute:: evpn_load_balancing
        
        	Enter EVPN Loadbalancing configuration submode
        	**type**\: :py:class:`EvpnLoadBalancing <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnLoadBalancing>`
        
        .. attribute:: evpn_timers
        
        	Enter EVPN timers configuration submode
        	**type**\: :py:class:`EvpnTimers <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnTimers>`
        
        .. attribute:: evpnbgp_auto_discovery
        
        	Enable Autodiscovery BGP in EVPN
        	**type**\: :py:class:`EvpnbgpAutoDiscovery <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnbgpAutoDiscovery>`
        
        .. attribute:: evpnevis
        
        	Enter EVPN EVI configuration submode
        	**type**\: :py:class:`Evpnevis <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.evpn_interfaces = Evpn.EvpnTables.EvpnInterfaces()
            self.evpn_interfaces.parent = self
            self.evpn_load_balancing = Evpn.EvpnTables.EvpnLoadBalancing()
            self.evpn_load_balancing.parent = self
            self.evpn_timers = Evpn.EvpnTables.EvpnTimers()
            self.evpn_timers.parent = self
            self.evpnbgp_auto_discovery = Evpn.EvpnTables.EvpnbgpAutoDiscovery()
            self.evpnbgp_auto_discovery.parent = self
            self.evpnevis = Evpn.EvpnTables.Evpnevis()
            self.evpnevis.parent = self


        class EvpnInterfaces(object):
            """
            Attachment Circuit interfaces
            
            .. attribute:: evpn_interface
            
            	Attachment circuit interface
            	**type**\: list of :py:class:`EvpnInterface <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.evpn_interface = YList()
                self.evpn_interface.parent = self
                self.evpn_interface.name = 'evpn_interface'


            class EvpnInterface(object):
                """
                Attachment circuit interface
                
                .. attribute:: interface_name
                
                	Name of the attachment circuit interface
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: ethernet_segment
                
                	Enter Ethernet Segment configuration submode
                	**type**\: :py:class:`EthernetSegment <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment>`
                
                .. attribute:: evpnac_timers
                
                	Enter Interface\-specific timers configuration submode
                	**type**\: :py:class:`EvpnacTimers <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers>`
                
                .. attribute:: mac_flush
                
                	Enable MVRP MAC Flush mode
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.ethernet_segment = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment()
                    self.ethernet_segment.parent = self
                    self.evpnac_timers = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers()
                    self.evpnac_timers.parent = self
                    self.mac_flush = None


                class EthernetSegment(object):
                    """
                    Enter Ethernet Segment configuration submode
                    
                    .. attribute:: backbone_source_mac
                    
                    	Backbone Source MAC
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: enable
                    
                    	Enable Ethernet Segment
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: es_import_route_target
                    
                    	ES\-Import Route Target
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: force_single_homed
                    
                    	Force ethernet segment to remain single\-homed
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: identifier_type0
                    
                    	Ethernet segment identifier (Type 0)
                    	**type**\: :py:class:`IdentifierType0 <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.IdentifierType0>`
                    
                    .. attribute:: load_balancing_per_service
                    
                    	Enable per service load balancing mode
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: manual_service_carving
                    
                    	Enter Manual service carving configuration submode
                    	**type**\: :py:class:`ManualServiceCarving <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.backbone_source_mac = None
                        self.enable = None
                        self.es_import_route_target = None
                        self.force_single_homed = None
                        self.identifier_type0 = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.IdentifierType0()
                        self.identifier_type0.parent = self
                        self.load_balancing_per_service = None
                        self.manual_service_carving = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving()
                        self.manual_service_carving.parent = self


                    class IdentifierType0(object):
                        """
                        Ethernet segment identifier (Type 0)
                        
                        .. attribute:: bytes1
                        
                        	Type 0's 1st Byte
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: bytes23
                        
                        	Type 0's 2nd and 3rd Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: bytes45
                        
                        	Type 0's 4th and 5th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: bytes67
                        
                        	Type 0's 6th and 7th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: bytes89
                        
                        	Type 0's 8th and 9th Bytes
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bytes1 = None
                            self.bytes23 = None
                            self.bytes45 = None
                            self.bytes67 = None
                            self.bytes89 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:identifier-type0'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.bytes1 is not None:
                                return True

                            if self.bytes23 is not None:
                                return True

                            if self.bytes45 is not None:
                                return True

                            if self.bytes67 is not None:
                                return True

                            if self.bytes89 is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.IdentifierType0']['meta_info']


                    class ManualServiceCarving(object):
                        """
                        Enter Manual service carving configuration
                        submode
                        
                        .. attribute:: enable
                        
                        	Enable Manual service carving
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: service_list
                        
                        	Manual service carving primary,secondary lists
                        	**type**\: :py:class:`ServiceList <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving.ServiceList>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.enable = None
                            self.service_list = Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving.ServiceList()
                            self.service_list.parent = self


                        class ServiceList(object):
                            """
                            Manual service carving primary,secondary
                            lists
                            
                            .. attribute:: primary
                            
                            	Primary services list
                            	**type**\: str
                            
                            	**range:** 0..150
                            
                            .. attribute:: secondary
                            
                            	Secondary services list
                            	**type**\: str
                            
                            	**range:** 0..150
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.primary = None
                                self.secondary = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:service-list'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.primary is not None:
                                    return True

                                if self.secondary is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving.ServiceList']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:manual-service-carving'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.enable is not None:
                                return True

                            if self.service_list is not None and self.service_list._has_data():
                                return True

                            if self.service_list is not None and self.service_list.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment.ManualServiceCarving']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ethernet-segment'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.backbone_source_mac is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.es_import_route_target is not None:
                            return True

                        if self.force_single_homed is not None:
                            return True

                        if self.identifier_type0 is not None and self.identifier_type0._has_data():
                            return True

                        if self.identifier_type0 is not None and self.identifier_type0.is_presence():
                            return True

                        if self.load_balancing_per_service is not None:
                            return True

                        if self.manual_service_carving is not None and self.manual_service_carving._has_data():
                            return True

                        if self.manual_service_carving is not None and self.manual_service_carving.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EthernetSegment']['meta_info']


                class EvpnacTimers(object):
                    """
                    Enter Interface\-specific timers configuration
                    submode
                    
                    .. attribute:: enable
                    
                    	Enable Interface\-specific timers
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: evpnac_flush_again
                    
                    	Interface\-specific MAC Flush again timer
                    	**type**\: int
                    
                    	**range:** 0..120
                    
                    .. attribute:: evpnac_recovery
                    
                    	Interface\-specific Recovery timer
                    	**type**\: int
                    
                    	**range:** 20..3600
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.evpnac_flush_again = None
                        self.evpnac_recovery = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpnac-timers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.enable is not None:
                            return True

                        if self.evpnac_flush_again is not None:
                            return True

                        if self.evpnac_recovery is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface.EvpnacTimers']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYDataValidationError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-interfaces/Cisco-IOS-XR-l2vpn-cfg:evpn-interface[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.interface_name is not None:
                        return True

                    if self.ethernet_segment is not None and self.ethernet_segment._has_data():
                        return True

                    if self.ethernet_segment is not None and self.ethernet_segment.is_presence():
                        return True

                    if self.evpnac_timers is not None and self.evpnac_timers._has_data():
                        return True

                    if self.evpnac_timers is not None and self.evpnac_timers.is_presence():
                        return True

                    if self.mac_flush is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces.EvpnInterface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.evpn_interface is not None:
                    for child_ref in self.evpn_interface:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.EvpnInterfaces']['meta_info']


        class EvpnLoadBalancing(object):
            """
            Enter EVPN Loadbalancing configuration submode
            
            .. attribute:: enable
            
            	Enable EVPN Loadbalancing
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: evpn_flow_label
            
            	Enable Flow Label based load balancing
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.evpn_flow_label = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-load-balancing'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.enable is not None:
                    return True

                if self.evpn_flow_label is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.EvpnLoadBalancing']['meta_info']


        class EvpnTimers(object):
            """
            Enter EVPN timers configuration submode
            
            .. attribute:: enable
            
            	Enable EVPN timers
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: evpn_flush_again
            
            	Global MAC Flush again timer
            	**type**\: int
            
            	**range:** 0..120
            
            .. attribute:: evpn_peering
            
            	Global Peering timer
            	**type**\: int
            
            	**range:** 0..300
            
            .. attribute:: evpn_programming
            
            	Global Programming timer
            	**type**\: int
            
            	**range:** 0..100000
            
            .. attribute:: evpn_recovery
            
            	Global Recovery timer
            	**type**\: int
            
            	**range:** 20..3600
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.evpn_flush_again = None
                self.evpn_peering = None
                self.evpn_programming = None
                self.evpn_recovery = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpn-timers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.enable is not None:
                    return True

                if self.evpn_flush_again is not None:
                    return True

                if self.evpn_peering is not None:
                    return True

                if self.evpn_programming is not None:
                    return True

                if self.evpn_recovery is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.EvpnTimers']['meta_info']


        class EvpnbgpAutoDiscovery(object):
            """
            Enable Autodiscovery BGP in EVPN
            
            .. attribute:: enable
            
            	Enable Autodiscovery BGP
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: evpn_route_distinguisher
            
            	Route Distinguisher
            	**type**\: :py:class:`EvpnRouteDistinguisher <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.EvpnbgpAutoDiscovery.EvpnRouteDistinguisher>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.evpn_route_distinguisher = Evpn.EvpnTables.EvpnbgpAutoDiscovery.EvpnRouteDistinguisher()
                self.evpn_route_distinguisher.parent = self


            class EvpnRouteDistinguisher(object):
                """
                Route Distinguisher
                
                .. attribute:: addr_index
                
                	Addr index
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: address
                
                	IPV4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: as_
                
                	Two byte or 4 byte AS number
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: as_index
                
                	AS\:nn (hex or decimal format)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Router Distinguisher Type
                	**type**\: :py:class:`BgpRouteDistinguisher_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher_Enum>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.addr_index = None
                    self.address = None
                    self.as_ = None
                    self.as_index = None
                    self.type = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpnbgp-auto-discovery/Cisco-IOS-XR-l2vpn-cfg:evpn-route-distinguisher'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.addr_index is not None:
                        return True

                    if self.address is not None:
                        return True

                    if self.as_ is not None:
                        return True

                    if self.as_index is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['Evpn.EvpnTables.EvpnbgpAutoDiscovery.EvpnRouteDistinguisher']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpnbgp-auto-discovery'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.enable is not None:
                    return True

                if self.evpn_route_distinguisher is not None and self.evpn_route_distinguisher._has_data():
                    return True

                if self.evpn_route_distinguisher is not None and self.evpn_route_distinguisher.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.EvpnbgpAutoDiscovery']['meta_info']


        class Evpnevis(object):
            """
            Enter EVPN EVI configuration submode
            
            .. attribute:: evpnevi
            
            	Enter EVPN EVI configuration submode
            	**type**\: list of :py:class:`Evpnevi <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.evpnevi = YList()
                self.evpnevi.parent = self
                self.evpnevi.name = 'evpnevi'


            class Evpnevi(object):
                """
                Enter EVPN EVI configuration submode
                
                .. attribute:: eviid
                
                	EVI ID
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: evi_load_balancing
                
                	Enter EVI Loadbalancing configuration submode
                	**type**\: :py:class:`EviLoadBalancing <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing>`
                
                .. attribute:: evpnevibgp_auto_discovery
                
                	Enable Autodiscovery BGP in EVPN EVI
                	**type**\: :py:class:`EvpnevibgpAutoDiscovery <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.eviid = None
                    self.evi_load_balancing = Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing()
                    self.evi_load_balancing.parent = self
                    self.evpnevibgp_auto_discovery = Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery()
                    self.evpnevibgp_auto_discovery.parent = self


                class EviLoadBalancing(object):
                    """
                    Enter EVI Loadbalancing configuration submode
                    
                    .. attribute:: enable
                    
                    	Enable EVI Loadbalancing
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: evi_flow_label
                    
                    	Enable Flow Label based load balancing
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.evi_flow_label = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evi-load-balancing'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.enable is not None:
                            return True

                        if self.evi_flow_label is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EviLoadBalancing']['meta_info']


                class EvpnevibgpAutoDiscovery(object):
                    """
                    Enable Autodiscovery BGP in EVPN EVI
                    
                    .. attribute:: enable
                    
                    	Enable Autodiscovery BGP
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: evpn_route_distinguisher
                    
                    	Route Distinguisher
                    	**type**\: :py:class:`EvpnRouteDistinguisher <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteDistinguisher>`
                    
                    .. attribute:: evpn_route_targets
                    
                    	Route Target
                    	**type**\: :py:class:`EvpnRouteTargets <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.evpn_route_distinguisher = Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteDistinguisher()
                        self.evpn_route_distinguisher.parent = self
                        self.evpn_route_targets = Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets()
                        self.evpn_route_targets.parent = self


                    class EvpnRouteDistinguisher(object):
                        """
                        Route Distinguisher
                        
                        .. attribute:: addr_index
                        
                        	Addr index
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: address
                        
                        	IPV4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: as_
                        
                        	Two byte or 4 byte AS number
                        	**type**\: int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: as_index
                        
                        	AS\:nn (hex or decimal format)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Router Distinguisher Type
                        	**type**\: :py:class:`BgpRouteDistinguisher_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher_Enum>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.addr_index = None
                            self.address = None
                            self.as_ = None
                            self.as_index = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-route-distinguisher'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.addr_index is not None:
                                return True

                            if self.address is not None:
                                return True

                            if self.as_ is not None:
                                return True

                            if self.as_index is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteDistinguisher']['meta_info']


                    class EvpnRouteTargets(object):
                        """
                        Route Target
                        
                        .. attribute:: evpn_route_target
                        
                        	Name of the Route Target
                        	**type**\: list of :py:class:`EvpnRouteTarget <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTarget>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.evpn_route_target = YList()
                            self.evpn_route_target.parent = self
                            self.evpn_route_target.name = 'evpn_route_target'


                        class EvpnRouteTarget(object):
                            """
                            Name of the Route Target
                            
                            .. attribute:: format
                            
                            	Format of the route target
                            	**type**\: :py:class:`BgpRouteTargetFormat_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat_Enum>`
                            
                            .. attribute:: role
                            
                            	Role of the router target type
                            	**type**\: :py:class:`BgpRouteTargetRole_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole_Enum>`
                            
                            .. attribute:: ipv4_address
                            
                            	ipv4 address
                            	**type**\: list of :py:class:`Ipv4Address <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTarget.Ipv4Address>`
                            
                            .. attribute:: two_byte_as_or_four_byte_as
                            
                            	two byte as or four byte as
                            	**type**\: list of :py:class:`TwoByteAsOrFourByteAs <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTarget.TwoByteAsOrFourByteAs>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.format = None
                                self.role = None
                                self.ipv4_address = YList()
                                self.ipv4_address.parent = self
                                self.ipv4_address.name = 'ipv4_address'
                                self.two_byte_as_or_four_byte_as = YList()
                                self.two_byte_as_or_four_byte_as.parent = self
                                self.two_byte_as_or_four_byte_as.name = 'two_byte_as_or_four_byte_as'


                            class Ipv4Address(object):
                                """
                                ipv4 address
                                
                                .. attribute:: addr_index
                                
                                	Addr index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: address
                                
                                	IPV4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.addr_index = None
                                    self.address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.addr_index is None:
                                        raise YPYDataValidationError('Key property addr_index is None')
                                    if self.address is None:
                                        raise YPYDataValidationError('Key property address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ipv4-address[Cisco-IOS-XR-l2vpn-cfg:addr-index = ' + str(self.addr_index) + '][Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.addr_index is not None:
                                        return True

                                    if self.address is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTarget.Ipv4Address']['meta_info']


                            class TwoByteAsOrFourByteAs(object):
                                """
                                two byte as or four byte as
                                
                                .. attribute:: as_
                                
                                	Two byte or 4 byte AS number
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: as_index
                                
                                	AS\:nn (hex or decimal format)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.as_ = None
                                    self.as_index = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.as_ is None:
                                        raise YPYDataValidationError('Key property as_ is None')
                                    if self.as_index is None:
                                        raise YPYDataValidationError('Key property as_index is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:two-byte-as-or-four-byte-as[Cisco-IOS-XR-l2vpn-cfg:as = ' + str(self.as_) + '][Cisco-IOS-XR-l2vpn-cfg:as-index = ' + str(self.as_index) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.as_ is not None:
                                        return True

                                    if self.as_index is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTarget.TwoByteAsOrFourByteAs']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.format is None:
                                    raise YPYDataValidationError('Key property format is None')
                                if self.role is None:
                                    raise YPYDataValidationError('Key property role is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-route-target[Cisco-IOS-XR-l2vpn-cfg:format = ' + str(self.format) + '][Cisco-IOS-XR-l2vpn-cfg:role = ' + str(self.role) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.format is not None:
                                    return True

                                if self.role is not None:
                                    return True

                                if self.ipv4_address is not None:
                                    for child_ref in self.ipv4_address:
                                        if child_ref._has_data():
                                            return True

                                if self.two_byte_as_or_four_byte_as is not None:
                                    for child_ref in self.two_byte_as_or_four_byte_as:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets.EvpnRouteTarget']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpn-route-targets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.evpn_route_target is not None:
                                for child_ref in self.evpn_route_target:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery.EvpnRouteTargets']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:evpnevibgp-auto-discovery'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.enable is not None:
                            return True

                        if self.evpn_route_distinguisher is not None and self.evpn_route_distinguisher._has_data():
                            return True

                        if self.evpn_route_distinguisher is not None and self.evpn_route_distinguisher.is_presence():
                            return True

                        if self.evpn_route_targets is not None and self.evpn_route_targets._has_data():
                            return True

                        if self.evpn_route_targets is not None and self.evpn_route_targets.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi.EvpnevibgpAutoDiscovery']['meta_info']

                @property
                def _common_path(self):
                    if self.eviid is None:
                        raise YPYDataValidationError('Key property eviid is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpnevis/Cisco-IOS-XR-l2vpn-cfg:evpnevi[Cisco-IOS-XR-l2vpn-cfg:eviid = ' + str(self.eviid) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.eviid is not None:
                        return True

                    if self.evi_load_balancing is not None and self.evi_load_balancing._has_data():
                        return True

                    if self.evi_load_balancing is not None and self.evi_load_balancing.is_presence():
                        return True

                    if self.evpnevibgp_auto_discovery is not None and self.evpnevibgp_auto_discovery._has_data():
                        return True

                    if self.evpnevibgp_auto_discovery is not None and self.evpnevibgp_auto_discovery.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['Evpn.EvpnTables.Evpnevis.Evpnevi']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables/Cisco-IOS-XR-l2vpn-cfg:evpnevis'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.evpnevi is not None:
                    for child_ref in self.evpnevi:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['Evpn.EvpnTables.Evpnevis']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:evpn-tables'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.evpn_interfaces is not None and self.evpn_interfaces._has_data():
                return True

            if self.evpn_interfaces is not None and self.evpn_interfaces.is_presence():
                return True

            if self.evpn_load_balancing is not None and self.evpn_load_balancing._has_data():
                return True

            if self.evpn_load_balancing is not None and self.evpn_load_balancing.is_presence():
                return True

            if self.evpn_timers is not None and self.evpn_timers._has_data():
                return True

            if self.evpn_timers is not None and self.evpn_timers.is_presence():
                return True

            if self.evpnbgp_auto_discovery is not None and self.evpnbgp_auto_discovery._has_data():
                return True

            if self.evpnbgp_auto_discovery is not None and self.evpnbgp_auto_discovery.is_presence():
                return True

            if self.evpnevis is not None and self.evpnevis._has_data():
                return True

            if self.evpnevis is not None and self.evpnevis.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['Evpn.EvpnTables']['meta_info']


    class StandardVersion(object):
        """
        Set Standard EVPN Version
        
        .. attribute:: draft_04
        
        	Set IETF Draft version to 04
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.draft_04 = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:evpn/Cisco-IOS-XR-l2vpn-cfg:standard-version'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.draft_04 is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['Evpn.StandardVersion']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-l2vpn-cfg:evpn'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.enable is not None:
            return True

        if self.evpn_tables is not None and self.evpn_tables._has_data():
            return True

        if self.evpn_tables is not None and self.evpn_tables.is_presence():
            return True

        if self.standard_version is not None and self.standard_version._has_data():
            return True

        if self.standard_version is not None and self.standard_version.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['Evpn']['meta_info']


class GenericInterfaceLists(object):
    """
    generic interface lists
    
    .. attribute:: generic_interface
    
    	Bridge group
    	**type**\: list of :py:class:`GenericInterface <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.GenericInterfaceLists.GenericInterface>`
    
    

    """

    _prefix = 'l2vpn-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.generic_interface = YList()
        self.generic_interface.parent = self
        self.generic_interface.name = 'generic_interface'


    class GenericInterface(object):
        """
        Bridge group
        
        .. attribute:: generic_interface_list_name
        
        	Name of the interface list
        	**type**\: str
        
        	**range:** 0..32
        
        .. attribute:: enable
        
        	Enable interface list
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: interfaces
        
        	Interface table
        	**type**\: :py:class:`Interfaces <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.GenericInterfaceLists.GenericInterface.Interfaces>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.generic_interface_list_name = None
            self.enable = None
            self.interfaces = GenericInterfaceLists.GenericInterface.Interfaces()
            self.interfaces.parent = self


        class Interfaces(object):
            """
            Interface table
            
            .. attribute:: interface
            
            	Interface
            	**type**\: list of :py:class:`Interface <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.GenericInterfaceLists.GenericInterface.Interfaces.Interface>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                Interface
                
                .. attribute:: interface_name
                
                	Name of the interface
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: enable
                
                	Enable interface
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.enable = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                    if self.interface_name is None:
                        raise YPYDataValidationError('Key property interface_name is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.interface_name is not None:
                        return True

                    if self.enable is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['GenericInterfaceLists.GenericInterface.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['GenericInterfaceLists.GenericInterface.Interfaces']['meta_info']

        @property
        def _common_path(self):
            if self.generic_interface_list_name is None:
                raise YPYDataValidationError('Key property generic_interface_list_name is None')

            return '/Cisco-IOS-XR-l2vpn-cfg:generic-interface-lists/Cisco-IOS-XR-l2vpn-cfg:generic-interface[Cisco-IOS-XR-l2vpn-cfg:generic-interface-list-name = ' + str(self.generic_interface_list_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.generic_interface_list_name is not None:
                return True

            if self.enable is not None:
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.interfaces is not None and self.interfaces.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['GenericInterfaceLists.GenericInterface']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-l2vpn-cfg:generic-interface-lists'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.generic_interface is not None:
            for child_ref in self.generic_interface:
                if child_ref._has_data():
                    return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['GenericInterfaceLists']['meta_info']


class L2vpn(object):
    """
    L2VPN configuration
    
    .. attribute:: auto_discovery
    
    	Global auto\-discovery attributes
    	**type**\: :py:class:`AutoDiscovery <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.AutoDiscovery>`
    
    .. attribute:: capability
    
    	L2VPN Capability Mode
    	**type**\: :py:class:`L2vpnCapabilityMode_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnCapabilityMode_Enum>`
    
    .. attribute:: database
    
    	L2VPN databases
    	**type**\: :py:class:`Database <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database>`
    
    .. attribute:: enable
    
    	Enable L2VPN feature
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: l2vpn_router_id
    
    	Global L2VPN Router ID
    	**type**\: str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    .. attribute:: load_balance
    
    	Enable flow load balancing on l2vpn bridges
    	**type**\: :py:class:`LoadBalance_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.LoadBalance_Enum>`
    
    .. attribute:: mspw_description
    
    	MS\-PW global description
    	**type**\: str
    
    	**range:** 0..64
    
    .. attribute:: mtu_mismatch_ignore
    
    	Ignore MTU Mismatch for XCs
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: neighbor
    
    	L2VPN neighbor submode
    	**type**\: :py:class:`Neighbor <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Neighbor>`
    
    .. attribute:: nsr
    
    	Enable Non\-Stop Routing
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: pbb
    
    	L2VPN PBB Global
    	**type**\: :py:class:`Pbb <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Pbb>`
    
    .. attribute:: pw_grouping
    
    	Enable PW grouping
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: pw_routing
    
    	Pseudowire\-routing attributes
    	**type**\: :py:class:`PwRouting <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.PwRouting>`
    
    .. attribute:: pw_status_disable
    
    	Disable PW status
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: pwoam_refresh
    
    	Configure PW OAM refresh interval
    	**type**\: int
    
    	**range:** 1..4095
    
    .. attribute:: snmp
    
    	SNMP related configuration
    	**type**\: :py:class:`Snmp <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Snmp>`
    
    .. attribute:: tcn_propagation
    
    	Topology change notification propagation
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: utility
    
    	L2VPN utilities
    	**type**\: :py:class:`Utility <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Utility>`
    
    

    """

    _prefix = 'l2vpn-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.auto_discovery = L2vpn.AutoDiscovery()
        self.auto_discovery.parent = self
        self.capability = None
        self.database = L2vpn.Database()
        self.database.parent = self
        self.enable = None
        self.l2vpn_router_id = None
        self.load_balance = None
        self.mspw_description = None
        self.mtu_mismatch_ignore = None
        self.neighbor = L2vpn.Neighbor()
        self.neighbor.parent = self
        self.nsr = None
        self.pbb = L2vpn.Pbb()
        self.pbb.parent = self
        self.pw_grouping = None
        self.pw_routing = L2vpn.PwRouting()
        self.pw_routing.parent = self
        self.pw_status_disable = None
        self.pwoam_refresh = None
        self.snmp = L2vpn.Snmp()
        self.snmp.parent = self
        self.tcn_propagation = None
        self.utility = L2vpn.Utility()
        self.utility.parent = self


    class AutoDiscovery(object):
        """
        Global auto\-discovery attributes
        
        .. attribute:: bgp_signaling
        
        	Global bgp signaling attributes
        	**type**\: :py:class:`BgpSignaling <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.AutoDiscovery.BgpSignaling>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.bgp_signaling = L2vpn.AutoDiscovery.BgpSignaling()
            self.bgp_signaling.parent = self


        class BgpSignaling(object):
            """
            Global bgp signaling attributes
            
            .. attribute:: mtu_mismatch_ignore
            
            	Ignore MTU mismatch for auto\-discovered pseudowires
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.mtu_mismatch_ignore = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:auto-discovery/Cisco-IOS-XR-l2vpn-cfg:bgp-signaling'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mtu_mismatch_ignore is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2vpn.AutoDiscovery.BgpSignaling']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:auto-discovery'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.bgp_signaling is not None and self.bgp_signaling._has_data():
                return True

            if self.bgp_signaling is not None and self.bgp_signaling.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2vpn.AutoDiscovery']['meta_info']


    class Database(object):
        """
        L2VPN databases
        
        .. attribute:: bridge_domain_groups
        
        	List of bridge  groups
        	**type**\: :py:class:`BridgeDomainGroups <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups>`
        
        .. attribute:: g8032_rings
        
        	List of G8032 Ring
        	**type**\: :py:class:`G8032Rings <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings>`
        
        .. attribute:: pseudowire_classes
        
        	List of pseudowire classes
        	**type**\: :py:class:`PseudowireClasses <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses>`
        
        .. attribute:: redundancy
        
        	Redundancy groups
        	**type**\: :py:class:`Redundancy <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.Redundancy>`
        
        .. attribute:: xconnect_groups
        
        	List of xconnect groups
        	**type**\: :py:class:`XconnectGroups <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.bridge_domain_groups = L2vpn.Database.BridgeDomainGroups()
            self.bridge_domain_groups.parent = self
            self.g8032_rings = L2vpn.Database.G8032Rings()
            self.g8032_rings.parent = self
            self.pseudowire_classes = L2vpn.Database.PseudowireClasses()
            self.pseudowire_classes.parent = self
            self.redundancy = L2vpn.Database.Redundancy()
            self.redundancy.parent = self
            self.xconnect_groups = L2vpn.Database.XconnectGroups()
            self.xconnect_groups.parent = self


        class BridgeDomainGroups(object):
            """
            List of bridge  groups
            
            .. attribute:: bridge_domain_group
            
            	Bridge group
            	**type**\: list of :py:class:`BridgeDomainGroup <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bridge_domain_group = YList()
                self.bridge_domain_group.parent = self
                self.bridge_domain_group.name = 'bridge_domain_group'


            class BridgeDomainGroup(object):
                """
                Bridge group
                
                .. attribute:: name
                
                	Name of the Bridge group
                	**type**\: str
                
                	**range:** 0..32
                
                .. attribute:: bridge_domains
                
                	List of Bridge Domain
                	**type**\: :py:class:`BridgeDomains <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.bridge_domains = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains()
                    self.bridge_domains.parent = self


                class BridgeDomains(object):
                    """
                    List of Bridge Domain
                    
                    .. attribute:: bridge_domain
                    
                    	bridge domain
                    	**type**\: list of :py:class:`BridgeDomain <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bridge_domain = YList()
                        self.bridge_domain.parent = self
                        self.bridge_domain.name = 'bridge_domain'


                    class BridgeDomain(object):
                        """
                        bridge domain
                        
                        .. attribute:: name
                        
                        	Name of the bridge domain
                        	**type**\: str
                        
                        	**range:** 0..27
                        
                        .. attribute:: bd_attachment_circuits
                        
                        	Attachment Circuit table
                        	**type**\: :py:class:`BdAttachmentCircuits <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits>`
                        
                        .. attribute:: bd_pseudowires
                        
                        	List of pseudowires
                        	**type**\: :py:class:`BdPseudowires <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires>`
                        
                        .. attribute:: bd_storm_controls
                        
                        	Storm Control
                        	**type**\: :py:class:`BdStormControls <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls>`
                        
                        .. attribute:: bridge_domain_mac
                        
                        	MAC configuration commands
                        	**type**\: :py:class:`BridgeDomainMac <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac>`
                        
                        .. attribute:: bridge_domain_mtu
                        
                        	Maximum transmission unit for this Bridge Domain
                        	**type**\: int
                        
                        	**range:** 46..65535
                        
                        .. attribute:: bridge_domain_pbb
                        
                        	Bridge Domain PBB
                        	**type**\: :py:class:`BridgeDomainPbb <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb>`
                        
                        .. attribute:: coupled_mode
                        
                        	Coupled\-mode configuration
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: dai
                        
                        	Dynamic ARP Inspection
                        	**type**\: :py:class:`Dai <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai>`
                        
                        .. attribute:: dhcp
                        
                        	DHCPv4 Snooping profile name
                        	**type**\: str
                        
                        	**range:** 0..32
                        
                        .. attribute:: flooding
                        
                        	Disable flooding
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: flooding_unknown_unicast
                        
                        	Disable Unknown Unicast flooding
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: igmp_snooping
                        
                        	Attach IGMP Snooping Profile Name
                        	**type**\: str
                        
                        	**range:** 0..32
                        
                        .. attribute:: igmp_snooping_disable
                        
                        	Disable IGMP Snooping
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: ip_source_guard
                        
                        	IP Source Guard
                        	**type**\: :py:class:`IpSourceGuard <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard>`
                        
                        .. attribute:: member_vnis
                        
                        	Bridge Domain VxLAN Network Identifier Table
                        	**type**\: :py:class:`MemberVnis <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis>`
                        
                        .. attribute:: mld_snooping
                        
                        	Attach MLD Snooping Profile Name
                        	**type**\: str
                        
                        	**range:** 0..32
                        
                        .. attribute:: nv_satellite
                        
                        	nV Satellite
                        	**type**\: :py:class:`NvSatellite <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite>`
                        
                        .. attribute:: routed_interfaces
                        
                        	Bridge Domain Routed Interface Table
                        	**type**\: :py:class:`RoutedInterfaces <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces>`
                        
                        .. attribute:: shutdown
                        
                        	shutdown the Bridge Domain
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: transport_mode
                        
                        	Bridge Domain Transport mode
                        	**type**\: :py:class:`BridgeDomainTransportMode_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BridgeDomainTransportMode_Enum>`
                        
                        .. attribute:: vfis
                        
                        	Specify the virtual forwarding interface name
                        	**type**\: :py:class:`Vfis <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.bd_attachment_circuits = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits()
                            self.bd_attachment_circuits.parent = self
                            self.bd_pseudowires = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires()
                            self.bd_pseudowires.parent = self
                            self.bd_storm_controls = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls()
                            self.bd_storm_controls.parent = self
                            self.bridge_domain_mac = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac()
                            self.bridge_domain_mac.parent = self
                            self.bridge_domain_mtu = None
                            self.bridge_domain_pbb = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb()
                            self.bridge_domain_pbb.parent = self
                            self.coupled_mode = None
                            self.dai = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai()
                            self.dai.parent = self
                            self.dhcp = None
                            self.flooding = None
                            self.flooding_unknown_unicast = None
                            self.igmp_snooping = None
                            self.igmp_snooping_disable = None
                            self.ip_source_guard = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard()
                            self.ip_source_guard.parent = self
                            self.member_vnis = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis()
                            self.member_vnis.parent = self
                            self.mld_snooping = None
                            self.nv_satellite = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite()
                            self.nv_satellite.parent = self
                            self.routed_interfaces = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces()
                            self.routed_interfaces.parent = self
                            self.shutdown = None
                            self.transport_mode = None
                            self.vfis = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis()
                            self.vfis.parent = self


                        class BdAttachmentCircuits(object):
                            """
                            Attachment Circuit table
                            
                            .. attribute:: bd_attachment_circuit
                            
                            	Name of the Attachment Circuit
                            	**type**\: list of :py:class:`BdAttachmentCircuit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bd_attachment_circuit = YList()
                                self.bd_attachment_circuit.parent = self
                                self.bd_attachment_circuit.name = 'bd_attachment_circuit'


                            class BdAttachmentCircuit(object):
                                """
                                Name of the Attachment Circuit
                                
                                .. attribute:: name
                                
                                	The name of the Attachment Circuit
                                	**type**\: str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: bdac_storm_control_types
                                
                                	Storm Control
                                	**type**\: :py:class:`BdacStormControlTypes <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes>`
                                
                                .. attribute:: interface_dai
                                
                                	L2 Interface Dynamic ARP Inspection
                                	**type**\: :py:class:`InterfaceDai <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai>`
                                
                                .. attribute:: interface_flooding
                                
                                	Enable or Disable Flooding
                                	**type**\: :py:class:`InterfaceTrafficFlood_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood_Enum>`
                                
                                .. attribute:: interface_flooding_unknown_unicast
                                
                                	Enable or Disable Unknown Unicast Flooding
                                	**type**\: :py:class:`InterfaceTrafficFlood_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood_Enum>`
                                
                                .. attribute:: interface_igmp_snoop
                                
                                	Attach a IGMP Snooping profile
                                	**type**\: str
                                
                                	**range:** 0..32
                                
                                .. attribute:: interface_ip_source_guard
                                
                                	IP Source Guard
                                	**type**\: :py:class:`InterfaceIpSourceGuard <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard>`
                                
                                .. attribute:: interface_mac
                                
                                	MAC configuration commands
                                	**type**\: :py:class:`InterfaceMac <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac>`
                                
                                .. attribute:: interface_mld_snoop
                                
                                	Attach a MLD Snooping profile
                                	**type**\: str
                                
                                	**range:** 0..32
                                
                                .. attribute:: interface_profile
                                
                                	Attach a DHCP profile
                                	**type**\: :py:class:`InterfaceProfile <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile>`
                                
                                .. attribute:: split_horizon
                                
                                	Split Horizon
                                	**type**\: :py:class:`SplitHorizon <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon>`
                                
                                .. attribute:: static_mac_addresses
                                
                                	Static Mac Address Table
                                	**type**\: :py:class:`StaticMacAddresses <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.name = None
                                    self.bdac_storm_control_types = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes()
                                    self.bdac_storm_control_types.parent = self
                                    self.interface_dai = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai()
                                    self.interface_dai.parent = self
                                    self.interface_flooding = None
                                    self.interface_flooding_unknown_unicast = None
                                    self.interface_igmp_snoop = None
                                    self.interface_ip_source_guard = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard()
                                    self.interface_ip_source_guard.parent = self
                                    self.interface_mac = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac()
                                    self.interface_mac.parent = self
                                    self.interface_mld_snoop = None
                                    self.interface_profile = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile()
                                    self.interface_profile.parent = self
                                    self.split_horizon = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon()
                                    self.split_horizon.parent = self
                                    self.static_mac_addresses = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses()
                                    self.static_mac_addresses.parent = self


                                class BdacStormControlTypes(object):
                                    """
                                    Storm Control
                                    
                                    .. attribute:: bdac_storm_control_type
                                    
                                    	Storm Control Type
                                    	**type**\: list of :py:class:`BdacStormControlType <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bdac_storm_control_type = YList()
                                        self.bdac_storm_control_type.parent = self
                                        self.bdac_storm_control_type.name = 'bdac_storm_control_type'


                                    class BdacStormControlType(object):
                                        """
                                        Storm Control Type
                                        
                                        .. attribute:: sctype
                                        
                                        	Storm Control Type
                                        	**type**\: :py:class:`StormControl_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.StormControl_Enum>`
                                        
                                        .. attribute:: storm_control_unit
                                        
                                        	Specify units for Storm Control Configuration
                                        	**type**\: :py:class:`StormControlUnit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.sctype = None
                                            self.storm_control_unit = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit()
                                            self.storm_control_unit.parent = self


                                        class StormControlUnit(object):
                                            """
                                            Specify units for Storm Control Configuration
                                            
                                            .. attribute:: kbits_per_sec
                                            
                                            	Kilobits Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\: int
                                            
                                            	**range:** 64..1280000
                                            
                                            .. attribute:: pkts_per_sec
                                            
                                            	Packets Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\: int
                                            
                                            	**range:** 1..160000
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.kbits_per_sec = None
                                                self.pkts_per_sec = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:storm-control-unit'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.kbits_per_sec is not None:
                                                    return True

                                                if self.pkts_per_sec is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType.StormControlUnit']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.sctype is None:
                                                raise YPYDataValidationError('Key property sctype is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bdac-storm-control-type[Cisco-IOS-XR-l2vpn-cfg:sctype = ' + str(self.sctype) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.sctype is not None:
                                                return True

                                            if self.storm_control_unit is not None and self.storm_control_unit._has_data():
                                                return True

                                            if self.storm_control_unit is not None and self.storm_control_unit.is_presence():
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes.BdacStormControlType']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bdac-storm-control-types'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.bdac_storm_control_type is not None:
                                            for child_ref in self.bdac_storm_control_type:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.BdacStormControlTypes']['meta_info']


                                class InterfaceDai(object):
                                    """
                                    L2 Interface Dynamic ARP Inspection
                                    
                                    .. attribute:: disable
                                    
                                    	Disable L2 Interface Dynamic ARP Inspection
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable L2 Interface Dynamic ARP Inspection
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: interface_dai_address_validation
                                    
                                    	Address Validation
                                    	**type**\: :py:class:`InterfaceDaiAddressValidation <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation>`
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\: :py:class:`L2vpnLogging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.disable = None
                                        self.enable = None
                                        self.interface_dai_address_validation = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation()
                                        self.interface_dai_address_validation.parent = self
                                        self.logging = None


                                    class InterfaceDaiAddressValidation(object):
                                        """
                                        Address Validation
                                        
                                        .. attribute:: destination_mac_verification
                                        
                                        	Destination MAC Verification
                                        	**type**\: :py:class:`L2vpnVerification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification_Enum>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable Address Validation
                                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                        
                                        .. attribute:: ipv4_verification
                                        
                                        	IPv4 Verification
                                        	**type**\: :py:class:`L2vpnVerification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification_Enum>`
                                        
                                        .. attribute:: source_mac_verification
                                        
                                        	Source MAC Verification
                                        	**type**\: :py:class:`L2vpnVerification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.destination_mac_verification = None
                                            self.enable = None
                                            self.ipv4_verification = None
                                            self.source_mac_verification = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-dai-address-validation'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.destination_mac_verification is not None:
                                                return True

                                            if self.enable is not None:
                                                return True

                                            if self.ipv4_verification is not None:
                                                return True

                                            if self.source_mac_verification is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai.InterfaceDaiAddressValidation']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-dai'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.disable is not None:
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.interface_dai_address_validation is not None and self.interface_dai_address_validation._has_data():
                                            return True

                                        if self.interface_dai_address_validation is not None and self.interface_dai_address_validation.is_presence():
                                            return True

                                        if self.logging is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceDai']['meta_info']


                                class InterfaceIpSourceGuard(object):
                                    """
                                    IP Source Guard
                                    
                                    .. attribute:: disable
                                    
                                    	Disable L2 Interface Dynamic IP source guard
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable IP Source Guard
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\: :py:class:`L2vpnLogging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.disable = None
                                        self.enable = None
                                        self.logging = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-ip-source-guard'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.disable is not None:
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.logging is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceIpSourceGuard']['meta_info']


                                class InterfaceMac(object):
                                    """
                                    MAC configuration commands
                                    
                                    .. attribute:: interface_mac_aging
                                    
                                    	MAC\-Aging configuration commands
                                    	**type**\: :py:class:`InterfaceMacAging <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging>`
                                    
                                    .. attribute:: interface_mac_learning
                                    
                                    	Enable Mac Learning
                                    	**type**\: :py:class:`MacLearn_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacLearn_Enum>`
                                    
                                    .. attribute:: interface_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\: :py:class:`InterfaceMacLimit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit>`
                                    
                                    .. attribute:: interface_mac_port_down_flush
                                    
                                    	Enable/Disable MAC Flush When Port goes down
                                    	**type**\: :py:class:`PortDownFlush_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.PortDownFlush_Enum>`
                                    
                                    .. attribute:: interface_mac_secure
                                    
                                    	MAC Secure
                                    	**type**\: :py:class:`InterfaceMacSecure <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.interface_mac_aging = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging()
                                        self.interface_mac_aging.parent = self
                                        self.interface_mac_learning = None
                                        self.interface_mac_limit = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit()
                                        self.interface_mac_limit.parent = self
                                        self.interface_mac_port_down_flush = None
                                        self.interface_mac_secure = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure()
                                        self.interface_mac_secure.parent = self


                                    class InterfaceMacAging(object):
                                        """
                                        MAC\-Aging configuration commands
                                        
                                        .. attribute:: interface_mac_aging_time
                                        
                                        	Mac Aging Time
                                        	**type**\: int
                                        
                                        	**range:** 300..30000
                                        
                                        .. attribute:: interface_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\: :py:class:`MacAging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacAging_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.interface_mac_aging_time = None
                                            self.interface_mac_aging_type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-mac-aging'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.interface_mac_aging_time is not None:
                                                return True

                                            if self.interface_mac_aging_type is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacAging']['meta_info']


                                    class InterfaceMacLimit(object):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: interface_mac_limit_action
                                        
                                        	Interface MAC address limit enforcement action
                                        	**type**\: :py:class:`MacLimitAction_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction_Enum>`
                                        
                                        .. attribute:: interface_mac_limit_max
                                        
                                        	Number of MAC addresses on an Interface after which MAC limit action is taken
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: interface_mac_limit_notif
                                        
                                        	MAC address limit notification action in a Interface
                                        	**type**\: :py:class:`MacNotification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacNotification_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.interface_mac_limit_action = None
                                            self.interface_mac_limit_max = None
                                            self.interface_mac_limit_notif = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-mac-limit'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.interface_mac_limit_action is not None:
                                                return True

                                            if self.interface_mac_limit_max is not None:
                                                return True

                                            if self.interface_mac_limit_notif is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacLimit']['meta_info']


                                    class InterfaceMacSecure(object):
                                        """
                                        MAC Secure
                                        
                                        .. attribute:: action
                                        
                                        	MAC secure enforcement action
                                        	**type**\: :py:class:`MacSecureAction_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction_Enum>`
                                        
                                        .. attribute:: disable
                                        
                                        	Disable L2 Interface MAC Secure
                                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable MAC Secure
                                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                        
                                        .. attribute:: logging
                                        
                                        	MAC Secure Logging
                                        	**type**\: :py:class:`L2vpnLogging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.action = None
                                            self.disable = None
                                            self.enable = None
                                            self.logging = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-mac-secure'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.action is not None:
                                                return True

                                            if self.disable is not None:
                                                return True

                                            if self.enable is not None:
                                                return True

                                            if self.logging is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac.InterfaceMacSecure']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-mac'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.interface_mac_aging is not None and self.interface_mac_aging._has_data():
                                            return True

                                        if self.interface_mac_aging is not None and self.interface_mac_aging.is_presence():
                                            return True

                                        if self.interface_mac_learning is not None:
                                            return True

                                        if self.interface_mac_limit is not None and self.interface_mac_limit._has_data():
                                            return True

                                        if self.interface_mac_limit is not None and self.interface_mac_limit.is_presence():
                                            return True

                                        if self.interface_mac_port_down_flush is not None:
                                            return True

                                        if self.interface_mac_secure is not None and self.interface_mac_secure._has_data():
                                            return True

                                        if self.interface_mac_secure is not None and self.interface_mac_secure.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceMac']['meta_info']


                                class InterfaceProfile(object):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\: str
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\: :py:class:`InterfaceProfile_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.dhcp_snooping_id = None
                                        self.profile_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:interface-profile'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.dhcp_snooping_id is not None:
                                            return True

                                        if self.profile_id is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.InterfaceProfile']['meta_info']


                                class SplitHorizon(object):
                                    """
                                    Split Horizon
                                    
                                    .. attribute:: split_horizon_group_id
                                    
                                    	Split Horizon Group ID
                                    	**type**\: :py:class:`SplitHorizonGroupId <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.split_horizon_group_id = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId()
                                        self.split_horizon_group_id.parent = self


                                    class SplitHorizonGroupId(object):
                                        """
                                        Split Horizon Group ID
                                        
                                        .. attribute:: enable
                                        
                                        	Enable split horizon group
                                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:split-horizon-group-id'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.enable is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon.SplitHorizonGroupId']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:split-horizon'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.split_horizon_group_id is not None and self.split_horizon_group_id._has_data():
                                            return True

                                        if self.split_horizon_group_id is not None and self.split_horizon_group_id.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.SplitHorizon']['meta_info']


                                class StaticMacAddresses(object):
                                    """
                                    Static Mac Address Table
                                    
                                    .. attribute:: static_mac_address
                                    
                                    	Static Mac Address Configuration
                                    	**type**\: list of :py:class:`StaticMacAddress <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.static_mac_address = YList()
                                        self.static_mac_address.parent = self
                                        self.static_mac_address.name = 'static_mac_address'


                                    class StaticMacAddress(object):
                                        """
                                        Static Mac Address Configuration
                                        
                                        .. attribute:: address
                                        
                                        	Static MAC address
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.address = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.address is None:
                                                raise YPYDataValidationError('Key property address is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:static-mac-address[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.address is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses.StaticMacAddress']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:static-mac-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.static_mac_address is not None:
                                            for child_ref in self.static_mac_address:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit.StaticMacAddresses']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.name is None:
                                        raise YPYDataValidationError('Key property name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-attachment-circuit[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.name is not None:
                                        return True

                                    if self.bdac_storm_control_types is not None and self.bdac_storm_control_types._has_data():
                                        return True

                                    if self.bdac_storm_control_types is not None and self.bdac_storm_control_types.is_presence():
                                        return True

                                    if self.interface_dai is not None and self.interface_dai._has_data():
                                        return True

                                    if self.interface_dai is not None and self.interface_dai.is_presence():
                                        return True

                                    if self.interface_flooding is not None:
                                        return True

                                    if self.interface_flooding_unknown_unicast is not None:
                                        return True

                                    if self.interface_igmp_snoop is not None:
                                        return True

                                    if self.interface_ip_source_guard is not None and self.interface_ip_source_guard._has_data():
                                        return True

                                    if self.interface_ip_source_guard is not None and self.interface_ip_source_guard.is_presence():
                                        return True

                                    if self.interface_mac is not None and self.interface_mac._has_data():
                                        return True

                                    if self.interface_mac is not None and self.interface_mac.is_presence():
                                        return True

                                    if self.interface_mld_snoop is not None:
                                        return True

                                    if self.interface_profile is not None and self.interface_profile._has_data():
                                        return True

                                    if self.interface_profile is not None and self.interface_profile.is_presence():
                                        return True

                                    if self.split_horizon is not None and self.split_horizon._has_data():
                                        return True

                                    if self.split_horizon is not None and self.split_horizon.is_presence():
                                        return True

                                    if self.static_mac_addresses is not None and self.static_mac_addresses._has_data():
                                        return True

                                    if self.static_mac_addresses is not None and self.static_mac_addresses.is_presence():
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits.BdAttachmentCircuit']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-attachment-circuits'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.bd_attachment_circuit is not None:
                                    for child_ref in self.bd_attachment_circuit:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdAttachmentCircuits']['meta_info']


                        class BdPseudowires(object):
                            """
                            List of pseudowires
                            
                            .. attribute:: bd_pseudowire
                            
                            	Pseudowire configuration
                            	**type**\: list of :py:class:`BdPseudowire <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bd_pseudowire = YList()
                                self.bd_pseudowire.parent = self
                                self.bd_pseudowire.name = 'bd_pseudowire'


                            class BdPseudowire(object):
                                """
                                Pseudowire configuration
                                
                                .. attribute:: neighbor
                                
                                	Neighbor IP address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: pseudowire_id
                                
                                	Pseudowire ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: bd_pw_class
                                
                                	PW class template name to use for this pseudowire
                                	**type**\: str
                                
                                	**range:** 0..32
                                
                                .. attribute:: bd_pw_mpls_static_labels
                                
                                	MPLS static labels
                                	**type**\: :py:class:`BdPwMplsStaticLabels <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels>`
                                
                                .. attribute:: bd_pw_split_horizon
                                
                                	Split Horizon
                                	**type**\: :py:class:`BdPwSplitHorizon <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon>`
                                
                                .. attribute:: bd_pw_static_mac_addresses
                                
                                	Static Mac Address Table
                                	**type**\: :py:class:`BdPwStaticMacAddresses <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses>`
                                
                                .. attribute:: bdpw_storm_control_types
                                
                                	Storm Control
                                	**type**\: :py:class:`BdpwStormControlTypes <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes>`
                                
                                .. attribute:: bridge_domain_backup_pseudowires
                                
                                	List of pseudowires
                                	**type**\: :py:class:`BridgeDomainBackupPseudowires <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires>`
                                
                                .. attribute:: pseudowire_dai
                                
                                	Access Pseudowire Dynamic ARP Inspection
                                	**type**\: :py:class:`PseudowireDai <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai>`
                                
                                .. attribute:: pseudowire_flooding
                                
                                	Bridge\-domain Pseudowire flooding
                                	**type**\: :py:class:`InterfaceTrafficFlood_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood_Enum>`
                                
                                .. attribute:: pseudowire_flooding_unknown_unicast
                                
                                	Bridge\-domain Pseudowire flooding Unknown Unicast
                                	**type**\: :py:class:`InterfaceTrafficFlood_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.InterfaceTrafficFlood_Enum>`
                                
                                .. attribute:: pseudowire_igmp_snoop
                                
                                	Attach a IGMP Snooping profile
                                	**type**\: str
                                
                                	**range:** 0..32
                                
                                .. attribute:: pseudowire_ip_source_guard
                                
                                	IP Source Guard
                                	**type**\: :py:class:`PseudowireIpSourceGuard <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard>`
                                
                                .. attribute:: pseudowire_mac
                                
                                	Bridge\-domain Pseudowire MAC configuration commands
                                	**type**\: :py:class:`PseudowireMac <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac>`
                                
                                .. attribute:: pseudowire_mld_snoop
                                
                                	Attach a MLD Snooping profile
                                	**type**\: str
                                
                                	**range:** 0..32
                                
                                .. attribute:: pseudowire_profile
                                
                                	Attach a DHCP profile
                                	**type**\: :py:class:`PseudowireProfile <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.neighbor = None
                                    self.pseudowire_id = None
                                    self.bd_pw_class = None
                                    self.bd_pw_mpls_static_labels = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels()
                                    self.bd_pw_mpls_static_labels.parent = self
                                    self.bd_pw_split_horizon = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon()
                                    self.bd_pw_split_horizon.parent = self
                                    self.bd_pw_static_mac_addresses = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses()
                                    self.bd_pw_static_mac_addresses.parent = self
                                    self.bdpw_storm_control_types = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes()
                                    self.bdpw_storm_control_types.parent = self
                                    self.bridge_domain_backup_pseudowires = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires()
                                    self.bridge_domain_backup_pseudowires.parent = self
                                    self.pseudowire_dai = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai()
                                    self.pseudowire_dai.parent = self
                                    self.pseudowire_flooding = None
                                    self.pseudowire_flooding_unknown_unicast = None
                                    self.pseudowire_igmp_snoop = None
                                    self.pseudowire_ip_source_guard = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard()
                                    self.pseudowire_ip_source_guard.parent = self
                                    self.pseudowire_mac = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac()
                                    self.pseudowire_mac.parent = self
                                    self.pseudowire_mld_snoop = None
                                    self.pseudowire_profile = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile()
                                    self.pseudowire_profile.parent = self


                                class BdPwMplsStaticLabels(object):
                                    """
                                    MPLS static labels
                                    
                                    .. attribute:: local_static_label
                                    
                                    	Pseudowire local static label
                                    	**type**\: int
                                    
                                    	**range:** 16..1048575
                                    
                                    .. attribute:: remote_static_label
                                    
                                    	Pseudowire remote static label
                                    	**type**\: int
                                    
                                    	**range:** 16..1048575
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.local_static_label = None
                                        self.remote_static_label = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pw-mpls-static-labels'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.local_static_label is not None:
                                            return True

                                        if self.remote_static_label is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwMplsStaticLabels']['meta_info']


                                class BdPwSplitHorizon(object):
                                    """
                                    Split Horizon
                                    
                                    .. attribute:: bd_pw_split_horizon_group
                                    
                                    	Split Horizon Group
                                    	**type**\: :py:class:`BdPwSplitHorizonGroup <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bd_pw_split_horizon_group = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup()
                                        self.bd_pw_split_horizon_group.parent = self


                                    class BdPwSplitHorizonGroup(object):
                                        """
                                        Split Horizon Group
                                        
                                        .. attribute:: enable
                                        
                                        	Enable split horizon group
                                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pw-split-horizon-group'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.enable is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon.BdPwSplitHorizonGroup']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pw-split-horizon'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.bd_pw_split_horizon_group is not None and self.bd_pw_split_horizon_group._has_data():
                                            return True

                                        if self.bd_pw_split_horizon_group is not None and self.bd_pw_split_horizon_group.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwSplitHorizon']['meta_info']


                                class BdPwStaticMacAddresses(object):
                                    """
                                    Static Mac Address Table
                                    
                                    .. attribute:: bd_pw_static_mac_address
                                    
                                    	Static Mac Address Configuration
                                    	**type**\: list of :py:class:`BdPwStaticMacAddress <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bd_pw_static_mac_address = YList()
                                        self.bd_pw_static_mac_address.parent = self
                                        self.bd_pw_static_mac_address.name = 'bd_pw_static_mac_address'


                                    class BdPwStaticMacAddress(object):
                                        """
                                        Static Mac Address Configuration
                                        
                                        .. attribute:: address
                                        
                                        	Static MAC address
                                        	**type**\: str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.address = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.address is None:
                                                raise YPYDataValidationError('Key property address is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pw-static-mac-address[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.address is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses.BdPwStaticMacAddress']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pw-static-mac-addresses'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.bd_pw_static_mac_address is not None:
                                            for child_ref in self.bd_pw_static_mac_address:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdPwStaticMacAddresses']['meta_info']


                                class BdpwStormControlTypes(object):
                                    """
                                    Storm Control
                                    
                                    .. attribute:: bdpw_storm_control_type
                                    
                                    	Storm Control Type
                                    	**type**\: list of :py:class:`BdpwStormControlType <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bdpw_storm_control_type = YList()
                                        self.bdpw_storm_control_type.parent = self
                                        self.bdpw_storm_control_type.name = 'bdpw_storm_control_type'


                                    class BdpwStormControlType(object):
                                        """
                                        Storm Control Type
                                        
                                        .. attribute:: sctype
                                        
                                        	Storm Control Type
                                        	**type**\: :py:class:`StormControl_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.StormControl_Enum>`
                                        
                                        .. attribute:: storm_control_unit
                                        
                                        	Specify units for Storm Control Configuration
                                        	**type**\: :py:class:`StormControlUnit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.sctype = None
                                            self.storm_control_unit = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit()
                                            self.storm_control_unit.parent = self


                                        class StormControlUnit(object):
                                            """
                                            Specify units for Storm Control Configuration
                                            
                                            .. attribute:: kbits_per_sec
                                            
                                            	Kilobits Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\: int
                                            
                                            	**range:** 64..1280000
                                            
                                            .. attribute:: pkts_per_sec
                                            
                                            	Packets Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                            	**type**\: int
                                            
                                            	**range:** 1..160000
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.kbits_per_sec = None
                                                self.pkts_per_sec = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:storm-control-unit'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.kbits_per_sec is not None:
                                                    return True

                                                if self.pkts_per_sec is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType.StormControlUnit']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.sctype is None:
                                                raise YPYDataValidationError('Key property sctype is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bdpw-storm-control-type[Cisco-IOS-XR-l2vpn-cfg:sctype = ' + str(self.sctype) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.sctype is not None:
                                                return True

                                            if self.storm_control_unit is not None and self.storm_control_unit._has_data():
                                                return True

                                            if self.storm_control_unit is not None and self.storm_control_unit.is_presence():
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes.BdpwStormControlType']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bdpw-storm-control-types'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.bdpw_storm_control_type is not None:
                                            for child_ref in self.bdpw_storm_control_type:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BdpwStormControlTypes']['meta_info']


                                class BridgeDomainBackupPseudowires(object):
                                    """
                                    List of pseudowires
                                    
                                    .. attribute:: bridge_domain_backup_pseudowire
                                    
                                    	Backup pseudowire configuration
                                    	**type**\: list of :py:class:`BridgeDomainBackupPseudowire <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bridge_domain_backup_pseudowire = YList()
                                        self.bridge_domain_backup_pseudowire.parent = self
                                        self.bridge_domain_backup_pseudowire.name = 'bridge_domain_backup_pseudowire'


                                    class BridgeDomainBackupPseudowire(object):
                                        """
                                        Backup pseudowire configuration
                                        
                                        .. attribute:: neighbor
                                        
                                        	Neighbor IP address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: pseudowire_id
                                        
                                        	Pseudowire ID
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: bridge_domain_backup_pw_class
                                        
                                        	PW class template name to use for this pseudowire
                                        	**type**\: str
                                        
                                        	**range:** 0..32
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.neighbor = None
                                            self.pseudowire_id = None
                                            self.bridge_domain_backup_pw_class = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.neighbor is None:
                                                raise YPYDataValidationError('Key property neighbor is None')
                                            if self.pseudowire_id is None:
                                                raise YPYDataValidationError('Key property pseudowire_id is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-backup-pseudowire[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.neighbor is not None:
                                                return True

                                            if self.pseudowire_id is not None:
                                                return True

                                            if self.bridge_domain_backup_pw_class is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires.BridgeDomainBackupPseudowire']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-backup-pseudowires'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.bridge_domain_backup_pseudowire is not None:
                                            for child_ref in self.bridge_domain_backup_pseudowire:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.BridgeDomainBackupPseudowires']['meta_info']


                                class PseudowireDai(object):
                                    """
                                    Access Pseudowire Dynamic ARP Inspection
                                    
                                    .. attribute:: disable
                                    
                                    	Disable Dynamic ARP Inspection
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable Access Pseudowire Dynamic ARP Inspection
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\: :py:class:`L2vpnLogging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging_Enum>`
                                    
                                    .. attribute:: pseudowire_dai_address_validation
                                    
                                    	Address Validation
                                    	**type**\: :py:class:`PseudowireDaiAddressValidation <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.disable = None
                                        self.enable = None
                                        self.logging = None
                                        self.pseudowire_dai_address_validation = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation()
                                        self.pseudowire_dai_address_validation.parent = self


                                    class PseudowireDaiAddressValidation(object):
                                        """
                                        Address Validation
                                        
                                        .. attribute:: destination_mac_verification
                                        
                                        	Destination MAC Verification
                                        	**type**\: :py:class:`L2vpnVerification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification_Enum>`
                                        
                                        .. attribute:: ipv4_verification
                                        
                                        	IPv4 Verification
                                        	**type**\: :py:class:`L2vpnVerification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification_Enum>`
                                        
                                        .. attribute:: source_mac_verification
                                        
                                        	Source MAC Verification
                                        	**type**\: :py:class:`L2vpnVerification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnVerification_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.destination_mac_verification = None
                                            self.ipv4_verification = None
                                            self.source_mac_verification = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-dai-address-validation'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.destination_mac_verification is not None:
                                                return True

                                            if self.ipv4_verification is not None:
                                                return True

                                            if self.source_mac_verification is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai.PseudowireDaiAddressValidation']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-dai'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.disable is not None:
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.logging is not None:
                                            return True

                                        if self.pseudowire_dai_address_validation is not None and self.pseudowire_dai_address_validation._has_data():
                                            return True

                                        if self.pseudowire_dai_address_validation is not None and self.pseudowire_dai_address_validation.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireDai']['meta_info']


                                class PseudowireIpSourceGuard(object):
                                    """
                                    IP Source Guard
                                    
                                    .. attribute:: disable
                                    
                                    	Disable Dynamic IP source guard
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable IP Source Guard
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: logging
                                    
                                    	Logging Type
                                    	**type**\: :py:class:`L2vpnLogging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.disable = None
                                        self.enable = None
                                        self.logging = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-ip-source-guard'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.disable is not None:
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.logging is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireIpSourceGuard']['meta_info']


                                class PseudowireMac(object):
                                    """
                                    Bridge\-domain Pseudowire MAC
                                    configuration commands
                                    
                                    .. attribute:: enable
                                    
                                    	Bridge\-domain Pseudowire MAC configuration mode
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: pseudowire_mac_aging
                                    
                                    	MAC\-Aging configuration commands
                                    	**type**\: :py:class:`PseudowireMacAging <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging>`
                                    
                                    .. attribute:: pseudowire_mac_learning
                                    
                                    	Enable MAC Learning
                                    	**type**\: :py:class:`MacLearn_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacLearn_Enum>`
                                    
                                    .. attribute:: pseudowire_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\: :py:class:`PseudowireMacLimit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit>`
                                    
                                    .. attribute:: pseudowire_mac_port_down_flush
                                    
                                    	Enable/Disable MAC Flush When Port goes down
                                    	**type**\: :py:class:`PortDownFlush_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.PortDownFlush_Enum>`
                                    
                                    .. attribute:: pseudowire_mac_secure
                                    
                                    	MAC Secure
                                    	**type**\: :py:class:`PseudowireMacSecure <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.enable = None
                                        self.pseudowire_mac_aging = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging()
                                        self.pseudowire_mac_aging.parent = self
                                        self.pseudowire_mac_learning = None
                                        self.pseudowire_mac_limit = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit()
                                        self.pseudowire_mac_limit.parent = self
                                        self.pseudowire_mac_port_down_flush = None
                                        self.pseudowire_mac_secure = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure()
                                        self.pseudowire_mac_secure.parent = self


                                    class PseudowireMacAging(object):
                                        """
                                        MAC\-Aging configuration commands
                                        
                                        .. attribute:: pseudowire_mac_aging_time
                                        
                                        	MAC Aging Time
                                        	**type**\: int
                                        
                                        	**range:** 300..30000
                                        
                                        .. attribute:: pseudowire_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\: :py:class:`MacAging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacAging_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pseudowire_mac_aging_time = None
                                            self.pseudowire_mac_aging_type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-mac-aging'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.pseudowire_mac_aging_time is not None:
                                                return True

                                            if self.pseudowire_mac_aging_type is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacAging']['meta_info']


                                    class PseudowireMacLimit(object):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: pseudowire_mac_limit_action
                                        
                                        	Bridge Access Pseudowire MAC address limit enforcement action
                                        	**type**\: :py:class:`MacLimitAction_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction_Enum>`
                                        
                                        .. attribute:: pseudowire_mac_limit_max
                                        
                                        	Number of MAC addresses on a Bridge Access Pseudowire after which MAC limit action is taken
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pseudowire_mac_limit_notif
                                        
                                        	MAC address limit notification action in a Bridge Access Pseudowire
                                        	**type**\: :py:class:`MacNotification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacNotification_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pseudowire_mac_limit_action = None
                                            self.pseudowire_mac_limit_max = None
                                            self.pseudowire_mac_limit_notif = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-mac-limit'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.pseudowire_mac_limit_action is not None:
                                                return True

                                            if self.pseudowire_mac_limit_max is not None:
                                                return True

                                            if self.pseudowire_mac_limit_notif is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacLimit']['meta_info']


                                    class PseudowireMacSecure(object):
                                        """
                                        MAC Secure
                                        
                                        .. attribute:: action
                                        
                                        	MAC secure enforcement action
                                        	**type**\: :py:class:`MacSecureAction_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction_Enum>`
                                        
                                        .. attribute:: disable
                                        
                                        	Disable L2 Pseudowire MAC Secure
                                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                        
                                        .. attribute:: enable
                                        
                                        	Enable MAC Secure
                                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                        
                                        .. attribute:: logging
                                        
                                        	MAC Secure Logging
                                        	**type**\: :py:class:`L2vpnLogging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.action = None
                                            self.disable = None
                                            self.enable = None
                                            self.logging = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-mac-secure'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.action is not None:
                                                return True

                                            if self.disable is not None:
                                                return True

                                            if self.enable is not None:
                                                return True

                                            if self.logging is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac.PseudowireMacSecure']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-mac'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.enable is not None:
                                            return True

                                        if self.pseudowire_mac_aging is not None and self.pseudowire_mac_aging._has_data():
                                            return True

                                        if self.pseudowire_mac_aging is not None and self.pseudowire_mac_aging.is_presence():
                                            return True

                                        if self.pseudowire_mac_learning is not None:
                                            return True

                                        if self.pseudowire_mac_limit is not None and self.pseudowire_mac_limit._has_data():
                                            return True

                                        if self.pseudowire_mac_limit is not None and self.pseudowire_mac_limit.is_presence():
                                            return True

                                        if self.pseudowire_mac_port_down_flush is not None:
                                            return True

                                        if self.pseudowire_mac_secure is not None and self.pseudowire_mac_secure._has_data():
                                            return True

                                        if self.pseudowire_mac_secure is not None and self.pseudowire_mac_secure.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireMac']['meta_info']


                                class PseudowireProfile(object):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\: str
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\: :py:class:`InterfaceProfile_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.dhcp_snooping_id = None
                                        self.profile_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-profile'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.dhcp_snooping_id is not None:
                                            return True

                                        if self.profile_id is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire.PseudowireProfile']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.neighbor is None:
                                        raise YPYDataValidationError('Key property neighbor is None')
                                    if self.pseudowire_id is None:
                                        raise YPYDataValidationError('Key property pseudowire_id is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pseudowire[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.neighbor is not None:
                                        return True

                                    if self.pseudowire_id is not None:
                                        return True

                                    if self.bd_pw_class is not None:
                                        return True

                                    if self.bd_pw_mpls_static_labels is not None and self.bd_pw_mpls_static_labels._has_data():
                                        return True

                                    if self.bd_pw_mpls_static_labels is not None and self.bd_pw_mpls_static_labels.is_presence():
                                        return True

                                    if self.bd_pw_split_horizon is not None and self.bd_pw_split_horizon._has_data():
                                        return True

                                    if self.bd_pw_split_horizon is not None and self.bd_pw_split_horizon.is_presence():
                                        return True

                                    if self.bd_pw_static_mac_addresses is not None and self.bd_pw_static_mac_addresses._has_data():
                                        return True

                                    if self.bd_pw_static_mac_addresses is not None and self.bd_pw_static_mac_addresses.is_presence():
                                        return True

                                    if self.bdpw_storm_control_types is not None and self.bdpw_storm_control_types._has_data():
                                        return True

                                    if self.bdpw_storm_control_types is not None and self.bdpw_storm_control_types.is_presence():
                                        return True

                                    if self.bridge_domain_backup_pseudowires is not None and self.bridge_domain_backup_pseudowires._has_data():
                                        return True

                                    if self.bridge_domain_backup_pseudowires is not None and self.bridge_domain_backup_pseudowires.is_presence():
                                        return True

                                    if self.pseudowire_dai is not None and self.pseudowire_dai._has_data():
                                        return True

                                    if self.pseudowire_dai is not None and self.pseudowire_dai.is_presence():
                                        return True

                                    if self.pseudowire_flooding is not None:
                                        return True

                                    if self.pseudowire_flooding_unknown_unicast is not None:
                                        return True

                                    if self.pseudowire_igmp_snoop is not None:
                                        return True

                                    if self.pseudowire_ip_source_guard is not None and self.pseudowire_ip_source_guard._has_data():
                                        return True

                                    if self.pseudowire_ip_source_guard is not None and self.pseudowire_ip_source_guard.is_presence():
                                        return True

                                    if self.pseudowire_mac is not None and self.pseudowire_mac._has_data():
                                        return True

                                    if self.pseudowire_mac is not None and self.pseudowire_mac.is_presence():
                                        return True

                                    if self.pseudowire_mld_snoop is not None:
                                        return True

                                    if self.pseudowire_profile is not None and self.pseudowire_profile._has_data():
                                        return True

                                    if self.pseudowire_profile is not None and self.pseudowire_profile.is_presence():
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires.BdPseudowire']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-pseudowires'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.bd_pseudowire is not None:
                                    for child_ref in self.bd_pseudowire:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdPseudowires']['meta_info']


                        class BdStormControls(object):
                            """
                            Storm Control
                            
                            .. attribute:: bd_storm_control
                            
                            	Storm Control Type
                            	**type**\: list of :py:class:`BdStormControl <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bd_storm_control = YList()
                                self.bd_storm_control.parent = self
                                self.bd_storm_control.name = 'bd_storm_control'


                            class BdStormControl(object):
                                """
                                Storm Control Type
                                
                                .. attribute:: sctype
                                
                                	Storm Control Type
                                	**type**\: :py:class:`StormControl_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.StormControl_Enum>`
                                
                                .. attribute:: storm_control_unit
                                
                                	Specify units for Storm Control Configuration
                                	**type**\: :py:class:`StormControlUnit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.sctype = None
                                    self.storm_control_unit = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit()
                                    self.storm_control_unit.parent = self


                                class StormControlUnit(object):
                                    """
                                    Specify units for Storm Control Configuration
                                    
                                    .. attribute:: kbits_per_sec
                                    
                                    	Kilobits Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                    	**type**\: int
                                    
                                    	**range:** 64..1280000
                                    
                                    .. attribute:: pkts_per_sec
                                    
                                    	Packets Per Second, PktsPerSec and KbitsPerSec cannot be configured together
                                    	**type**\: int
                                    
                                    	**range:** 1..160000
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.kbits_per_sec = None
                                        self.pkts_per_sec = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:storm-control-unit'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.kbits_per_sec is not None:
                                            return True

                                        if self.pkts_per_sec is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl.StormControlUnit']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.sctype is None:
                                        raise YPYDataValidationError('Key property sctype is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-storm-control[Cisco-IOS-XR-l2vpn-cfg:sctype = ' + str(self.sctype) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.sctype is not None:
                                        return True

                                    if self.storm_control_unit is not None and self.storm_control_unit._has_data():
                                        return True

                                    if self.storm_control_unit is not None and self.storm_control_unit.is_presence():
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls.BdStormControl']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-storm-controls'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.bd_storm_control is not None:
                                    for child_ref in self.bd_storm_control:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BdStormControls']['meta_info']


                        class BridgeDomainMac(object):
                            """
                            MAC configuration commands
                            
                            .. attribute:: bd_mac_aging
                            
                            	MAC\-Aging configuration commands
                            	**type**\: :py:class:`BdMacAging <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging>`
                            
                            .. attribute:: bd_mac_filters
                            
                            	Filter Mac Address
                            	**type**\: :py:class:`BdMacFilters <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters>`
                            
                            .. attribute:: bd_mac_learn
                            
                            	Enable Mac Learning
                            	**type**\: :py:class:`MacLearn_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacLearn_Enum>`
                            
                            .. attribute:: bd_mac_limit
                            
                            	MAC\-Limit configuration commands
                            	**type**\: :py:class:`BdMacLimit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit>`
                            
                            .. attribute:: bd_mac_port_down_flush
                            
                            	Disable MAC Flush when Port goes Down
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: bd_mac_withdraw
                            
                            	Disable Mac Withdraw
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: bd_mac_withdraw_access_pw_disable
                            
                            	MAC withdraw on Access PW
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: bd_mac_withdraw_behavior
                            
                            	MAC withdraw sent on bridge port down
                            	**type**\: :py:class:`MacWithdrawBehavior_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacWithdrawBehavior_Enum>`
                            
                            .. attribute:: bd_mac_withdraw_relay
                            
                            	Mac withdraw sent from access PW to access PW
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: mac_secure
                            
                            	MAC Secure
                            	**type**\: :py:class:`MacSecure <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bd_mac_aging = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging()
                                self.bd_mac_aging.parent = self
                                self.bd_mac_filters = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters()
                                self.bd_mac_filters.parent = self
                                self.bd_mac_learn = None
                                self.bd_mac_limit = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit()
                                self.bd_mac_limit.parent = self
                                self.bd_mac_port_down_flush = None
                                self.bd_mac_withdraw = None
                                self.bd_mac_withdraw_access_pw_disable = None
                                self.bd_mac_withdraw_behavior = None
                                self.bd_mac_withdraw_relay = None
                                self.mac_secure = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure()
                                self.mac_secure.parent = self


                            class BdMacAging(object):
                                """
                                MAC\-Aging configuration commands
                                
                                .. attribute:: bd_mac_aging_time
                                
                                	Mac Aging Time
                                	**type**\: int
                                
                                	**range:** 300..30000
                                
                                .. attribute:: bd_mac_aging_type
                                
                                	MAC address aging type
                                	**type**\: :py:class:`MacAging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacAging_Enum>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bd_mac_aging_time = None
                                    self.bd_mac_aging_type = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-mac-aging'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.bd_mac_aging_time is not None:
                                        return True

                                    if self.bd_mac_aging_type is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacAging']['meta_info']


                            class BdMacFilters(object):
                                """
                                Filter Mac Address
                                
                                .. attribute:: bd_mac_filter
                                
                                	Static MAC address
                                	**type**\: list of :py:class:`BdMacFilter <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bd_mac_filter = YList()
                                    self.bd_mac_filter.parent = self
                                    self.bd_mac_filter.name = 'bd_mac_filter'


                                class BdMacFilter(object):
                                    """
                                    Static MAC address
                                    
                                    .. attribute:: address
                                    
                                    	Static MAC address
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    .. attribute:: drop
                                    
                                    	MAC address for filtering
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.drop = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.address is None:
                                            raise YPYDataValidationError('Key property address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-mac-filter[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.address is not None:
                                            return True

                                        if self.drop is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters.BdMacFilter']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-mac-filters'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.bd_mac_filter is not None:
                                        for child_ref in self.bd_mac_filter:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacFilters']['meta_info']


                            class BdMacLimit(object):
                                """
                                MAC\-Limit configuration commands
                                
                                .. attribute:: bd_mac_limit_action
                                
                                	MAC address limit enforcement action
                                	**type**\: :py:class:`MacLimitAction_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction_Enum>`
                                
                                .. attribute:: bd_mac_limit_max
                                
                                	Number of MAC addresses after which MAC limit action is taken
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: bd_mac_limit_notif
                                
                                	Mac Address Limit Notification
                                	**type**\: :py:class:`MacNotification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacNotification_Enum>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.bd_mac_limit_action = None
                                    self.bd_mac_limit_max = None
                                    self.bd_mac_limit_notif = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bd-mac-limit'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.bd_mac_limit_action is not None:
                                        return True

                                    if self.bd_mac_limit_max is not None:
                                        return True

                                    if self.bd_mac_limit_notif is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.BdMacLimit']['meta_info']


                            class MacSecure(object):
                                """
                                MAC Secure
                                
                                .. attribute:: action
                                
                                	MAC secure enforcement action
                                	**type**\: :py:class:`MacSecureAction_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction_Enum>`
                                
                                .. attribute:: enable
                                
                                	Enable MAC Secure
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: logging
                                
                                	MAC Secure Logging
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.action = None
                                    self.enable = None
                                    self.logging = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mac-secure'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.action is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.logging is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac.MacSecure']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-mac'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.bd_mac_aging is not None and self.bd_mac_aging._has_data():
                                    return True

                                if self.bd_mac_aging is not None and self.bd_mac_aging.is_presence():
                                    return True

                                if self.bd_mac_filters is not None and self.bd_mac_filters._has_data():
                                    return True

                                if self.bd_mac_filters is not None and self.bd_mac_filters.is_presence():
                                    return True

                                if self.bd_mac_learn is not None:
                                    return True

                                if self.bd_mac_limit is not None and self.bd_mac_limit._has_data():
                                    return True

                                if self.bd_mac_limit is not None and self.bd_mac_limit.is_presence():
                                    return True

                                if self.bd_mac_port_down_flush is not None:
                                    return True

                                if self.bd_mac_withdraw is not None:
                                    return True

                                if self.bd_mac_withdraw_access_pw_disable is not None:
                                    return True

                                if self.bd_mac_withdraw_behavior is not None:
                                    return True

                                if self.bd_mac_withdraw_relay is not None:
                                    return True

                                if self.mac_secure is not None and self.mac_secure._has_data():
                                    return True

                                if self.mac_secure is not None and self.mac_secure.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainMac']['meta_info']


                        class BridgeDomainPbb(object):
                            """
                            Bridge Domain PBB
                            
                            .. attribute:: pbb_core
                            
                            	PBB Core
                            	**type**\: :py:class:`PbbCore <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore>`
                            
                            .. attribute:: pbb_edges
                            
                            	PBB Edge
                            	**type**\: :py:class:`PbbEdges <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pbb_core = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore()
                                self.pbb_core.parent = self
                                self.pbb_edges = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges()
                                self.pbb_edges.parent = self


                            class PbbCore(object):
                                """
                                PBB Core
                                
                                .. attribute:: enable
                                
                                	Enable Bridge Domain PBB Core Configuration
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: evpn_attribute
                                
                                	Configure EVPN EVI
                                	**type**\: int
                                
                                	**range:** 1..65534
                                
                                .. attribute:: pbb_core_dhcp_profile
                                
                                	Attach a DHCP profile
                                	**type**\: :py:class:`PbbCoreDhcpProfile <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile>`
                                
                                .. attribute:: pbb_core_igmp_profile
                                
                                	Attach a IGMP Snooping profile
                                	**type**\: str
                                
                                	**range:** 0..32
                                
                                .. attribute:: pbb_core_mac
                                
                                	MAC configuration commands
                                	**type**\: :py:class:`PbbCoreMac <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac>`
                                
                                .. attribute:: pbb_core_mmrp_flood_optimization
                                
                                	Enabling MMRP PBB\-VPLS Flood Optimization
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN ID to push
                                	**type**\: int
                                
                                	**range:** 1..4094
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.enable = None
                                    self.evpn_attribute = None
                                    self.pbb_core_dhcp_profile = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile()
                                    self.pbb_core_dhcp_profile.parent = self
                                    self.pbb_core_igmp_profile = None
                                    self.pbb_core_mac = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac()
                                    self.pbb_core_mac.parent = self
                                    self.pbb_core_mmrp_flood_optimization = None
                                    self.vlan_id = None


                                class PbbCoreDhcpProfile(object):
                                    """
                                    Attach a DHCP profile
                                    
                                    .. attribute:: dhcp_snooping_id
                                    
                                    	Disable DHCP snooping
                                    	**type**\: str
                                    
                                    .. attribute:: profile_id
                                    
                                    	Set the snooping profile
                                    	**type**\: :py:class:`InterfaceProfile_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.dhcp_snooping_id = None
                                        self.profile_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core-dhcp-profile'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.dhcp_snooping_id is not None:
                                            return True

                                        if self.profile_id is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreDhcpProfile']['meta_info']


                                class PbbCoreMac(object):
                                    """
                                    MAC configuration commands
                                    
                                    .. attribute:: pbb_core_mac_aging
                                    
                                    	MAC\-Aging configuration commands
                                    	**type**\: :py:class:`PbbCoreMacAging <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging>`
                                    
                                    .. attribute:: pbb_core_mac_learning
                                    
                                    	Enable Mac Learning
                                    	**type**\: :py:class:`MacLearn_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacLearn_Enum>`
                                    
                                    .. attribute:: pbb_core_mac_limit
                                    
                                    	MAC\-Limit configuration commands
                                    	**type**\: :py:class:`PbbCoreMacLimit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.pbb_core_mac_aging = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging()
                                        self.pbb_core_mac_aging.parent = self
                                        self.pbb_core_mac_learning = None
                                        self.pbb_core_mac_limit = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit()
                                        self.pbb_core_mac_limit.parent = self


                                    class PbbCoreMacAging(object):
                                        """
                                        MAC\-Aging configuration commands
                                        
                                        .. attribute:: pbb_core_mac_aging_time
                                        
                                        	Mac Aging Time
                                        	**type**\: int
                                        
                                        	**range:** 300..30000
                                        
                                        .. attribute:: pbb_core_mac_aging_type
                                        
                                        	MAC address aging type
                                        	**type**\: :py:class:`MacAging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacAging_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pbb_core_mac_aging_time = None
                                            self.pbb_core_mac_aging_type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core-mac-aging'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.pbb_core_mac_aging_time is not None:
                                                return True

                                            if self.pbb_core_mac_aging_type is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacAging']['meta_info']


                                    class PbbCoreMacLimit(object):
                                        """
                                        MAC\-Limit configuration commands
                                        
                                        .. attribute:: pbb_core_mac_limit_action
                                        
                                        	MAC address limit enforcement action
                                        	**type**\: :py:class:`MacLimitAction_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction_Enum>`
                                        
                                        .. attribute:: pbb_core_mac_limit_max
                                        
                                        	Number of MAC addresses after which MAC limit action is taken
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: pbb_core_mac_limit_notif
                                        
                                        	MAC address limit notification action
                                        	**type**\: :py:class:`MacNotification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacNotification_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pbb_core_mac_limit_action = None
                                            self.pbb_core_mac_limit_max = None
                                            self.pbb_core_mac_limit_notif = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core-mac-limit'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.pbb_core_mac_limit_action is not None:
                                                return True

                                            if self.pbb_core_mac_limit_max is not None:
                                                return True

                                            if self.pbb_core_mac_limit_notif is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac.PbbCoreMacLimit']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core-mac'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.pbb_core_mac_aging is not None and self.pbb_core_mac_aging._has_data():
                                            return True

                                        if self.pbb_core_mac_aging is not None and self.pbb_core_mac_aging.is_presence():
                                            return True

                                        if self.pbb_core_mac_learning is not None:
                                            return True

                                        if self.pbb_core_mac_limit is not None and self.pbb_core_mac_limit._has_data():
                                            return True

                                        if self.pbb_core_mac_limit is not None and self.pbb_core_mac_limit.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore.PbbCoreMac']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-core'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.enable is not None:
                                        return True

                                    if self.evpn_attribute is not None:
                                        return True

                                    if self.pbb_core_dhcp_profile is not None and self.pbb_core_dhcp_profile._has_data():
                                        return True

                                    if self.pbb_core_dhcp_profile is not None and self.pbb_core_dhcp_profile.is_presence():
                                        return True

                                    if self.pbb_core_igmp_profile is not None:
                                        return True

                                    if self.pbb_core_mac is not None and self.pbb_core_mac._has_data():
                                        return True

                                    if self.pbb_core_mac is not None and self.pbb_core_mac.is_presence():
                                        return True

                                    if self.pbb_core_mmrp_flood_optimization is not None:
                                        return True

                                    if self.vlan_id is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbCore']['meta_info']


                            class PbbEdges(object):
                                """
                                PBB Edge
                                
                                .. attribute:: pbb_edge
                                
                                	Configure BD as PBB Edge with ISID and associated PBB Core BD
                                	**type**\: list of :py:class:`PbbEdge <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.pbb_edge = YList()
                                    self.pbb_edge.parent = self
                                    self.pbb_edge.name = 'pbb_edge'


                                class PbbEdge(object):
                                    """
                                    Configure BD as PBB Edge with ISID and
                                    associated PBB Core BD
                                    
                                    .. attribute:: core_bd_name
                                    
                                    	Core BD Name
                                    	**type**\: str
                                    
                                    	**range:** 0..27
                                    
                                    .. attribute:: isid
                                    
                                    	ISID
                                    	**type**\: int
                                    
                                    	**range:** 256..16777214
                                    
                                    .. attribute:: pbb_edge_dhcp_profile
                                    
                                    	Attach a DHCP profile
                                    	**type**\: :py:class:`PbbEdgeDhcpProfile <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile>`
                                    
                                    .. attribute:: pbb_edge_igmp_profile
                                    
                                    	Attach a IGMP Snooping profile
                                    	**type**\: str
                                    
                                    	**range:** 0..32
                                    
                                    .. attribute:: pbb_edge_mac
                                    
                                    	MAC configuration commands
                                    	**type**\: :py:class:`PbbEdgeMac <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac>`
                                    
                                    .. attribute:: pbb_static_mac_mappings
                                    
                                    	PBB Static Mac Address Mapping Table
                                    	**type**\: :py:class:`PbbStaticMacMappings <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings>`
                                    
                                    .. attribute:: unknown_unicast_bmac
                                    
                                    	Configure Unknown Unicast BMAC address for PBB Edge Port
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.core_bd_name = None
                                        self.isid = None
                                        self.pbb_edge_dhcp_profile = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile()
                                        self.pbb_edge_dhcp_profile.parent = self
                                        self.pbb_edge_igmp_profile = None
                                        self.pbb_edge_mac = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac()
                                        self.pbb_edge_mac.parent = self
                                        self.pbb_static_mac_mappings = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings()
                                        self.pbb_static_mac_mappings.parent = self
                                        self.unknown_unicast_bmac = None


                                    class PbbEdgeDhcpProfile(object):
                                        """
                                        Attach a DHCP profile
                                        
                                        .. attribute:: dhcp_snooping_id
                                        
                                        	Disable DHCP snooping
                                        	**type**\: str
                                        
                                        .. attribute:: profile_id
                                        
                                        	Set the snooping profile
                                        	**type**\: :py:class:`InterfaceProfile_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.dhcp_snooping_id = None
                                            self.profile_id = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge-dhcp-profile'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.dhcp_snooping_id is not None:
                                                return True

                                            if self.profile_id is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeDhcpProfile']['meta_info']


                                    class PbbEdgeMac(object):
                                        """
                                        MAC configuration commands
                                        
                                        .. attribute:: pbb_edge_mac_aging
                                        
                                        	MAC\-Aging configuration commands
                                        	**type**\: :py:class:`PbbEdgeMacAging <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging>`
                                        
                                        .. attribute:: pbb_edge_mac_learning
                                        
                                        	Enable Mac Learning
                                        	**type**\: :py:class:`MacLearn_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacLearn_Enum>`
                                        
                                        .. attribute:: pbb_edge_mac_limit
                                        
                                        	MAC\-Limit configuration commands
                                        	**type**\: :py:class:`PbbEdgeMacLimit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit>`
                                        
                                        .. attribute:: pbb_edge_mac_secure
                                        
                                        	MAC Secure
                                        	**type**\: :py:class:`PbbEdgeMacSecure <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pbb_edge_mac_aging = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging()
                                            self.pbb_edge_mac_aging.parent = self
                                            self.pbb_edge_mac_learning = None
                                            self.pbb_edge_mac_limit = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit()
                                            self.pbb_edge_mac_limit.parent = self
                                            self.pbb_edge_mac_secure = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure()
                                            self.pbb_edge_mac_secure.parent = self


                                        class PbbEdgeMacAging(object):
                                            """
                                            MAC\-Aging configuration commands
                                            
                                            .. attribute:: pbb_edge_mac_aging_time
                                            
                                            	Mac Aging Time
                                            	**type**\: int
                                            
                                            	**range:** 300..30000
                                            
                                            .. attribute:: pbb_edge_mac_aging_type
                                            
                                            	MAC address aging type
                                            	**type**\: :py:class:`MacAging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacAging_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.pbb_edge_mac_aging_time = None
                                                self.pbb_edge_mac_aging_type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge-mac-aging'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.pbb_edge_mac_aging_time is not None:
                                                    return True

                                                if self.pbb_edge_mac_aging_type is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacAging']['meta_info']


                                        class PbbEdgeMacLimit(object):
                                            """
                                            MAC\-Limit configuration commands
                                            
                                            .. attribute:: pbb_edge_mac_limit_action
                                            
                                            	MAC address limit enforcement action
                                            	**type**\: :py:class:`MacLimitAction_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacLimitAction_Enum>`
                                            
                                            .. attribute:: pbb_edge_mac_limit_max
                                            
                                            	Number of MAC addresses after which MAC limit action is taken
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: pbb_edge_mac_limit_notif
                                            
                                            	MAC address limit notification action
                                            	**type**\: :py:class:`MacNotification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacNotification_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.pbb_edge_mac_limit_action = None
                                                self.pbb_edge_mac_limit_max = None
                                                self.pbb_edge_mac_limit_notif = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge-mac-limit'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.pbb_edge_mac_limit_action is not None:
                                                    return True

                                                if self.pbb_edge_mac_limit_max is not None:
                                                    return True

                                                if self.pbb_edge_mac_limit_notif is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacLimit']['meta_info']


                                        class PbbEdgeMacSecure(object):
                                            """
                                            MAC Secure
                                            
                                            .. attribute:: accept_shutdown
                                            
                                            	Accept Virtual instance port to be shutdown on mac violation
                                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                            
                                            .. attribute:: action
                                            
                                            	MAC secure enforcement action
                                            	**type**\: :py:class:`MacSecureAction_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MacSecureAction_Enum>`
                                            
                                            .. attribute:: disable
                                            
                                            	Disable Virtual instance port MAC Secure
                                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                            
                                            .. attribute:: enable
                                            
                                            	Enable MAC Secure
                                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                            
                                            .. attribute:: logging
                                            
                                            	MAC Secure Logging
                                            	**type**\: :py:class:`L2vpnLogging_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpnLogging_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.accept_shutdown = None
                                                self.action = None
                                                self.disable = None
                                                self.enable = None
                                                self.logging = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge-mac-secure'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.accept_shutdown is not None:
                                                    return True

                                                if self.action is not None:
                                                    return True

                                                if self.disable is not None:
                                                    return True

                                                if self.enable is not None:
                                                    return True

                                                if self.logging is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac.PbbEdgeMacSecure']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge-mac'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.pbb_edge_mac_aging is not None and self.pbb_edge_mac_aging._has_data():
                                                return True

                                            if self.pbb_edge_mac_aging is not None and self.pbb_edge_mac_aging.is_presence():
                                                return True

                                            if self.pbb_edge_mac_learning is not None:
                                                return True

                                            if self.pbb_edge_mac_limit is not None and self.pbb_edge_mac_limit._has_data():
                                                return True

                                            if self.pbb_edge_mac_limit is not None and self.pbb_edge_mac_limit.is_presence():
                                                return True

                                            if self.pbb_edge_mac_secure is not None and self.pbb_edge_mac_secure._has_data():
                                                return True

                                            if self.pbb_edge_mac_secure is not None and self.pbb_edge_mac_secure.is_presence():
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbEdgeMac']['meta_info']


                                    class PbbStaticMacMappings(object):
                                        """
                                        PBB Static Mac Address Mapping Table
                                        
                                        .. attribute:: pbb_static_mac_mapping
                                        
                                        	PBB Static Mac Address Mapping Configuration
                                        	**type**\: list of :py:class:`PbbStaticMacMapping <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.pbb_static_mac_mapping = YList()
                                            self.pbb_static_mac_mapping.parent = self
                                            self.pbb_static_mac_mapping.name = 'pbb_static_mac_mapping'


                                        class PbbStaticMacMapping(object):
                                            """
                                            PBB Static Mac Address Mapping
                                            Configuration
                                            
                                            .. attribute:: address
                                            
                                            	Static MAC address
                                            	**type**\: str
                                            
                                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                            
                                            .. attribute:: bmac
                                            
                                            	Backbone MAC address
                                            	**type**\: str
                                            
                                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.bmac = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.address is None:
                                                    raise YPYDataValidationError('Key property address is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-static-mac-mapping[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.address is not None:
                                                    return True

                                                if self.bmac is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings.PbbStaticMacMapping']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-static-mac-mappings'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.pbb_static_mac_mapping is not None:
                                                for child_ref in self.pbb_static_mac_mapping:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge.PbbStaticMacMappings']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.core_bd_name is None:
                                            raise YPYDataValidationError('Key property core_bd_name is None')
                                        if self.isid is None:
                                            raise YPYDataValidationError('Key property isid is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edge[Cisco-IOS-XR-l2vpn-cfg:core-bd-name = ' + str(self.core_bd_name) + '][Cisco-IOS-XR-l2vpn-cfg:isid = ' + str(self.isid) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.core_bd_name is not None:
                                            return True

                                        if self.isid is not None:
                                            return True

                                        if self.pbb_edge_dhcp_profile is not None and self.pbb_edge_dhcp_profile._has_data():
                                            return True

                                        if self.pbb_edge_dhcp_profile is not None and self.pbb_edge_dhcp_profile.is_presence():
                                            return True

                                        if self.pbb_edge_igmp_profile is not None:
                                            return True

                                        if self.pbb_edge_mac is not None and self.pbb_edge_mac._has_data():
                                            return True

                                        if self.pbb_edge_mac is not None and self.pbb_edge_mac.is_presence():
                                            return True

                                        if self.pbb_static_mac_mappings is not None and self.pbb_static_mac_mappings._has_data():
                                            return True

                                        if self.pbb_static_mac_mappings is not None and self.pbb_static_mac_mappings.is_presence():
                                            return True

                                        if self.unknown_unicast_bmac is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges.PbbEdge']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pbb-edges'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.pbb_edge is not None:
                                        for child_ref in self.pbb_edge:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb.PbbEdges']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-pbb'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.pbb_core is not None and self.pbb_core._has_data():
                                    return True

                                if self.pbb_core is not None and self.pbb_core.is_presence():
                                    return True

                                if self.pbb_edges is not None and self.pbb_edges._has_data():
                                    return True

                                if self.pbb_edges is not None and self.pbb_edges.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.BridgeDomainPbb']['meta_info']


                        class Dai(object):
                            """
                            Dynamic ARP Inspection
                            
                            .. attribute:: dai_address_validation
                            
                            	Address Validation
                            	**type**\: :py:class:`DaiAddressValidation <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation>`
                            
                            .. attribute:: enable
                            
                            	Enable Dynamic ARP Inspection
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: logging
                            
                            	Enable Logging
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dai_address_validation = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation()
                                self.dai_address_validation.parent = self
                                self.enable = None
                                self.logging = None


                            class DaiAddressValidation(object):
                                """
                                Address Validation
                                
                                .. attribute:: destination_mac_verification
                                
                                	Enable Destination MAC Verification
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: enable
                                
                                	Enable Address Validation
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: ipv4_verification
                                
                                	Enable IPv4 Verification
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: source_mac_verification
                                
                                	Enable Source MAC Verification
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.destination_mac_verification = None
                                    self.enable = None
                                    self.ipv4_verification = None
                                    self.source_mac_verification = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:dai-address-validation'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.destination_mac_verification is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.ipv4_verification is not None:
                                        return True

                                    if self.source_mac_verification is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai.DaiAddressValidation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:dai'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.dai_address_validation is not None and self.dai_address_validation._has_data():
                                    return True

                                if self.dai_address_validation is not None and self.dai_address_validation.is_presence():
                                    return True

                                if self.enable is not None:
                                    return True

                                if self.logging is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Dai']['meta_info']


                        class IpSourceGuard(object):
                            """
                            IP Source Guard
                            
                            .. attribute:: enable
                            
                            	Enable IP Source Guard
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: logging
                            
                            	Enable Logging
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.logging = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ip-source-guard'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.enable is not None:
                                    return True

                                if self.logging is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.IpSourceGuard']['meta_info']


                        class MemberVnis(object):
                            """
                            Bridge Domain VxLAN Network Identifier
                            Table
                            
                            .. attribute:: member_vni
                            
                            	Bridge Domain Member VxLAN Network Identifier 
                            	**type**\: list of :py:class:`MemberVni <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.member_vni = YList()
                                self.member_vni.parent = self
                                self.member_vni.name = 'member_vni'


                            class MemberVni(object):
                                """
                                Bridge Domain Member VxLAN Network
                                Identifier 
                                
                                .. attribute:: vni
                                
                                	VxLAN Network Identifier number
                                	**type**\: int
                                
                                	**range:** 1..16777215
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.vni = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.vni is None:
                                        raise YPYDataValidationError('Key property vni is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:member-vni[Cisco-IOS-XR-l2vpn-cfg:vni = ' + str(self.vni) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.vni is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis.MemberVni']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:member-vnis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.member_vni is not None:
                                    for child_ref in self.member_vni:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.MemberVnis']['meta_info']


                        class NvSatellite(object):
                            """
                            nV Satellite
                            
                            .. attribute:: enable
                            
                            	Enable nV Satellite Settings
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: offload_ipv4_multicast_enable
                            
                            	Enable IPv4 Multicast Offload to Satellite Nodes
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.offload_ipv4_multicast_enable = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:nv-satellite'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.enable is not None:
                                    return True

                                if self.offload_ipv4_multicast_enable is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.NvSatellite']['meta_info']


                        class RoutedInterfaces(object):
                            """
                            Bridge Domain Routed Interface Table
                            
                            .. attribute:: routed_interface
                            
                            	Bridge Domain Routed Interface
                            	**type**\: list of :py:class:`RoutedInterface <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.routed_interface = YList()
                                self.routed_interface.parent = self
                                self.routed_interface.name = 'routed_interface'


                            class RoutedInterface(object):
                                """
                                Bridge Domain Routed Interface
                                
                                .. attribute:: interface_name
                                
                                	The name of the Routed Interface
                                	**type**\: str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYDataValidationError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:routed-interface[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.interface_name is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces.RoutedInterface']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:routed-interfaces'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.routed_interface is not None:
                                    for child_ref in self.routed_interface:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.RoutedInterfaces']['meta_info']


                        class Vfis(object):
                            """
                            Specify the virtual forwarding interface
                            name
                            
                            .. attribute:: vfi
                            
                            	Name of the Virtual Forwarding Interface
                            	**type**\: list of :py:class:`Vfi <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.vfi = YList()
                                self.vfi.parent = self
                                self.vfi.name = 'vfi'


                            class Vfi(object):
                                """
                                Name of the Virtual Forwarding Interface
                                
                                .. attribute:: name
                                
                                	Name of the Virtual Forwarding Interface
                                	**type**\: str
                                
                                	**range:** 0..32
                                
                                .. attribute:: bgp_auto_discovery
                                
                                	Enable Autodiscovery BGP in this VFI
                                	**type**\: :py:class:`BgpAutoDiscovery <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery>`
                                
                                .. attribute:: multicast_p2mp
                                
                                	Enable Multicast P2MP in this VFI
                                	**type**\: :py:class:`MulticastP2mp <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp>`
                                
                                .. attribute:: vfi_pseudowires
                                
                                	List of pseudowires
                                	**type**\: :py:class:`VfiPseudowires <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires>`
                                
                                .. attribute:: vfi_shutdown
                                
                                	Enabling Shutdown
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: vpnid
                                
                                	VPN Identifier
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.name = None
                                    self.bgp_auto_discovery = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery()
                                    self.bgp_auto_discovery.parent = self
                                    self.multicast_p2mp = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp()
                                    self.multicast_p2mp.parent = self
                                    self.vfi_pseudowires = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires()
                                    self.vfi_pseudowires.parent = self
                                    self.vfi_shutdown = None
                                    self.vpnid = None


                                class BgpAutoDiscovery(object):
                                    """
                                    Enable Autodiscovery BGP in this VFI
                                    
                                    .. attribute:: ad_control_word
                                    
                                    	Enable control\-word for this VFI
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: bgp_signaling_protocol
                                    
                                    	Enable Signaling Protocol BGP in this VFI
                                    	**type**\: :py:class:`BgpSignalingProtocol <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable Autodiscovery BGP
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: ldp_signaling_protocol
                                    
                                    	Signaling Protocol LDP in this VFI configuration
                                    	**type**\: :py:class:`LdpSignalingProtocol <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol>`
                                    
                                    .. attribute:: route_distinguisher
                                    
                                    	Route Distinguisher
                                    	**type**\: :py:class:`RouteDistinguisher <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher>`
                                    
                                    .. attribute:: route_targets
                                    
                                    	Route Target
                                    	**type**\: :py:class:`RouteTargets <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.ad_control_word = None
                                        self.bgp_signaling_protocol = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol()
                                        self.bgp_signaling_protocol.parent = self
                                        self.enable = None
                                        self.ldp_signaling_protocol = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol()
                                        self.ldp_signaling_protocol.parent = self
                                        self.route_distinguisher = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher()
                                        self.route_distinguisher.parent = self
                                        self.route_targets = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets()
                                        self.route_targets.parent = self


                                    class BgpSignalingProtocol(object):
                                        """
                                        Enable Signaling Protocol BGP in this
                                        VFI
                                        
                                        .. attribute:: enable
                                        
                                        	Enable BGP as Signaling Protocol
                                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                        
                                        .. attribute:: flow_label_load_balance
                                        
                                        	Enable Flow Label based load balancing
                                        	**type**\: :py:class:`FlowLabelLoadBalance <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance>`
                                        
                                        .. attribute:: ve_range
                                        
                                        	Local Virtual Edge Block Configurable Range
                                        	**type**\: int
                                        
                                        	**range:** 11..100
                                        
                                        .. attribute:: veid
                                        
                                        	Local Virtual Edge Identifier
                                        	**type**\: int
                                        
                                        	**range:** 1..16384
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None
                                            self.flow_label_load_balance = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance()
                                            self.flow_label_load_balance.parent = self
                                            self.ve_range = None
                                            self.veid = None


                                        class FlowLabelLoadBalance(object):
                                            """
                                            Enable Flow Label based load balancing
                                            
                                            .. attribute:: flow_label
                                            
                                            	Flow Label load balance type
                                            	**type**\: :py:class:`FlowLabelLoadBalance_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance_Enum>`
                                            
                                            .. attribute:: static
                                            
                                            	Static Flow Label
                                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.flow_label = None
                                                self.static = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:flow-label-load-balance'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.flow_label is not None:
                                                    return True

                                                if self.static is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol.FlowLabelLoadBalance']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bgp-signaling-protocol'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.enable is not None:
                                                return True

                                            if self.flow_label_load_balance is not None and self.flow_label_load_balance._has_data():
                                                return True

                                            if self.flow_label_load_balance is not None and self.flow_label_load_balance.is_presence():
                                                return True

                                            if self.ve_range is not None:
                                                return True

                                            if self.veid is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.BgpSignalingProtocol']['meta_info']


                                    class LdpSignalingProtocol(object):
                                        """
                                        Signaling Protocol LDP in this VFI
                                        configuration
                                        
                                        .. attribute:: enable
                                        
                                        	Enable LDP as Signaling Protocol .Deletion of this object also causes deletion of all objects under LDPSignalingProtocol
                                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                        
                                        .. attribute:: flow_label_load_balance
                                        
                                        	Enable Flow Label based load balancing
                                        	**type**\: :py:class:`FlowLabelLoadBalance <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance>`
                                        
                                        .. attribute:: vplsid
                                        
                                        	VPLS ID
                                        	**type**\: :py:class:`Vplsid <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.Vplsid>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None
                                            self.flow_label_load_balance = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance()
                                            self.flow_label_load_balance.parent = self
                                            self.vplsid = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.Vplsid()
                                            self.vplsid.parent = self


                                        class FlowLabelLoadBalance(object):
                                            """
                                            Enable Flow Label based load balancing
                                            
                                            .. attribute:: flow_label
                                            
                                            	Flow Label load balance type
                                            	**type**\: :py:class:`FlowLabelLoadBalance_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance_Enum>`
                                            
                                            .. attribute:: static
                                            
                                            	Static Flow Label
                                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.flow_label = None
                                                self.static = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:flow-label-load-balance'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.flow_label is not None:
                                                    return True

                                                if self.static is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.FlowLabelLoadBalance']['meta_info']


                                        class Vplsid(object):
                                            """
                                            VPLS ID
                                            
                                            .. attribute:: address
                                            
                                            	IPV4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: address_index
                                            
                                            	Address index
                                            	**type**\: int
                                            
                                            	**range:** 0..32767
                                            
                                            .. attribute:: as_
                                            
                                            	Two byte AS number
                                            	**type**\: int
                                            
                                            	**range:** 1..65535
                                            
                                            .. attribute:: as_index
                                            
                                            	AS index
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: type
                                            
                                            	VPLS\-ID Type
                                            	**type**\: :py:class:`LdpVplsId_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.LdpVplsId_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.address_index = None
                                                self.as_ = None
                                                self.as_index = None
                                                self.type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vplsid'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.address is not None:
                                                    return True

                                                if self.address_index is not None:
                                                    return True

                                                if self.as_ is not None:
                                                    return True

                                                if self.as_index is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol.Vplsid']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ldp-signaling-protocol'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.enable is not None:
                                                return True

                                            if self.flow_label_load_balance is not None and self.flow_label_load_balance._has_data():
                                                return True

                                            if self.flow_label_load_balance is not None and self.flow_label_load_balance.is_presence():
                                                return True

                                            if self.vplsid is not None and self.vplsid._has_data():
                                                return True

                                            if self.vplsid is not None and self.vplsid.is_presence():
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.LdpSignalingProtocol']['meta_info']


                                    class RouteDistinguisher(object):
                                        """
                                        Route Distinguisher
                                        
                                        .. attribute:: addr_index
                                        
                                        	Addr index
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: address
                                        
                                        	IPV4 address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: as_
                                        
                                        	Two byte or 4 byte AS number
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: as_index
                                        
                                        	AS\:nn (hex or decimal format)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: type
                                        
                                        	Router Distinguisher Type
                                        	**type**\: :py:class:`BgpRouteDistinguisher_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.addr_index = None
                                            self.address = None
                                            self.as_ = None
                                            self.as_index = None
                                            self.type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:route-distinguisher'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.addr_index is not None:
                                                return True

                                            if self.address is not None:
                                                return True

                                            if self.as_ is not None:
                                                return True

                                            if self.as_index is not None:
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteDistinguisher']['meta_info']


                                    class RouteTargets(object):
                                        """
                                        Route Target
                                        
                                        .. attribute:: route_target
                                        
                                        	Name of the Route Target
                                        	**type**\: list of :py:class:`RouteTarget <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.route_target = YList()
                                            self.route_target.parent = self
                                            self.route_target.name = 'route_target'


                                        class RouteTarget(object):
                                            """
                                            Name of the Route Target
                                            
                                            .. attribute:: format
                                            
                                            	Format of the route target
                                            	**type**\: :py:class:`BgpRouteTargetFormat_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat_Enum>`
                                            
                                            .. attribute:: role
                                            
                                            	Role of the router target type
                                            	**type**\: :py:class:`BgpRouteTargetRole_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole_Enum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	ipv4 address
                                            	**type**\: list of :py:class:`Ipv4Address <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address>`
                                            
                                            .. attribute:: two_byte_as_or_four_byte_as
                                            
                                            	two byte as or four byte as
                                            	**type**\: list of :py:class:`TwoByteAsOrFourByteAs <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.format = None
                                                self.role = None
                                                self.ipv4_address = YList()
                                                self.ipv4_address.parent = self
                                                self.ipv4_address.name = 'ipv4_address'
                                                self.two_byte_as_or_four_byte_as = YList()
                                                self.two_byte_as_or_four_byte_as.parent = self
                                                self.two_byte_as_or_four_byte_as.name = 'two_byte_as_or_four_byte_as'


                                            class Ipv4Address(object):
                                                """
                                                ipv4 address
                                                
                                                .. attribute:: addr_index
                                                
                                                	Addr index
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: address
                                                
                                                	IPV4 address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.addr_index = None
                                                    self.address = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                    if self.addr_index is None:
                                                        raise YPYDataValidationError('Key property addr_index is None')
                                                    if self.address is None:
                                                        raise YPYDataValidationError('Key property address is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ipv4-address[Cisco-IOS-XR-l2vpn-cfg:addr-index = ' + str(self.addr_index) + '][Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.is_presence():
                                                        return True
                                                    if self.addr_index is not None:
                                                        return True

                                                    if self.address is not None:
                                                        return True

                                                    return False

                                                def is_presence(self):
                                                    ''' Returns True if this instance represents presence container else returns False '''
                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.Ipv4Address']['meta_info']


                                            class TwoByteAsOrFourByteAs(object):
                                                """
                                                two byte as or four byte as
                                                
                                                .. attribute:: as_
                                                
                                                	Two byte or 4 byte AS number
                                                	**type**\: int
                                                
                                                	**range:** 1..4294967295
                                                
                                                .. attribute:: as_index
                                                
                                                	AS\:nn (hex or decimal format)
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.as_ = None
                                                    self.as_index = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                    if self.as_ is None:
                                                        raise YPYDataValidationError('Key property as_ is None')
                                                    if self.as_index is None:
                                                        raise YPYDataValidationError('Key property as_index is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:two-byte-as-or-four-byte-as[Cisco-IOS-XR-l2vpn-cfg:as = ' + str(self.as_) + '][Cisco-IOS-XR-l2vpn-cfg:as-index = ' + str(self.as_index) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.is_presence():
                                                        return True
                                                    if self.as_ is not None:
                                                        return True

                                                    if self.as_index is not None:
                                                        return True

                                                    return False

                                                def is_presence(self):
                                                    ''' Returns True if this instance represents presence container else returns False '''
                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget.TwoByteAsOrFourByteAs']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.format is None:
                                                    raise YPYDataValidationError('Key property format is None')
                                                if self.role is None:
                                                    raise YPYDataValidationError('Key property role is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:route-target[Cisco-IOS-XR-l2vpn-cfg:format = ' + str(self.format) + '][Cisco-IOS-XR-l2vpn-cfg:role = ' + str(self.role) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.format is not None:
                                                    return True

                                                if self.role is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    for child_ref in self.ipv4_address:
                                                        if child_ref._has_data():
                                                            return True

                                                if self.two_byte_as_or_four_byte_as is not None:
                                                    for child_ref in self.two_byte_as_or_four_byte_as:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets.RouteTarget']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:route-targets'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.route_target is not None:
                                                for child_ref in self.route_target:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery.RouteTargets']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bgp-auto-discovery'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.ad_control_word is not None:
                                            return True

                                        if self.bgp_signaling_protocol is not None and self.bgp_signaling_protocol._has_data():
                                            return True

                                        if self.bgp_signaling_protocol is not None and self.bgp_signaling_protocol.is_presence():
                                            return True

                                        if self.enable is not None:
                                            return True

                                        if self.ldp_signaling_protocol is not None and self.ldp_signaling_protocol._has_data():
                                            return True

                                        if self.ldp_signaling_protocol is not None and self.ldp_signaling_protocol.is_presence():
                                            return True

                                        if self.route_distinguisher is not None and self.route_distinguisher._has_data():
                                            return True

                                        if self.route_distinguisher is not None and self.route_distinguisher.is_presence():
                                            return True

                                        if self.route_targets is not None and self.route_targets._has_data():
                                            return True

                                        if self.route_targets is not None and self.route_targets.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.BgpAutoDiscovery']['meta_info']


                                class MulticastP2mp(object):
                                    """
                                    Enable Multicast P2MP in this VFI
                                    
                                    .. attribute:: enable
                                    
                                    	Enable Autodiscovery P2MP
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    .. attribute:: signalings
                                    
                                    	Multicast P2MP Signaling Type
                                    	**type**\: :py:class:`Signalings <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp.Signalings>`
                                    
                                    .. attribute:: transports
                                    
                                    	Multicast P2MP Transport
                                    	**type**\: :py:class:`Transports <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp.Transports>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.enable = None
                                        self.signalings = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp.Signalings()
                                        self.signalings.parent = self
                                        self.transports = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp.Transports()
                                        self.transports.parent = self


                                    class Signalings(object):
                                        """
                                        Multicast P2MP Signaling Type
                                        
                                        .. attribute:: signaling
                                        
                                        	Multicast P2MP Signaling Type
                                        	**type**\: list of :py:class:`Signaling <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp.Signalings.Signaling>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.signaling = YList()
                                            self.signaling.parent = self
                                            self.signaling.name = 'signaling'


                                        class Signaling(object):
                                            """
                                            Multicast P2MP Signaling Type
                                            
                                            .. attribute:: signaling_name
                                            
                                            	Signaling Type
                                            	**type**\: str
                                            
                                            	**pattern:** (BGP)
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.signaling_name = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.signaling_name is None:
                                                    raise YPYDataValidationError('Key property signaling_name is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:signaling[Cisco-IOS-XR-l2vpn-cfg:signaling-name = ' + str(self.signaling_name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.signaling_name is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp.Signalings.Signaling']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:signalings'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.signaling is not None:
                                                for child_ref in self.signaling:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp.Signalings']['meta_info']


                                    class Transports(object):
                                        """
                                        Multicast P2MP Transport
                                        
                                        .. attribute:: transport
                                        
                                        	Multicast P2MP Transport Type
                                        	**type**\: list of :py:class:`Transport <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp.Transports.Transport>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.transport = YList()
                                            self.transport.parent = self
                                            self.transport.name = 'transport'


                                        class Transport(object):
                                            """
                                            Multicast P2MP Transport Type
                                            
                                            .. attribute:: transport_name
                                            
                                            	Transport Type
                                            	**type**\: str
                                            
                                            	**pattern:** (RSVP\_TE)
                                            
                                            .. attribute:: attribute_set_name
                                            
                                            	Multicast P2MP TE Attribute Set Name
                                            	**type**\: str
                                            
                                            	**range:** 0..64
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.transport_name = None
                                                self.attribute_set_name = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.transport_name is None:
                                                    raise YPYDataValidationError('Key property transport_name is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:transport[Cisco-IOS-XR-l2vpn-cfg:transport-name = ' + str(self.transport_name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.transport_name is not None:
                                                    return True

                                                if self.attribute_set_name is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp.Transports.Transport']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:transports'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.transport is not None:
                                                for child_ref in self.transport:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp.Transports']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:multicast-p2mp'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.enable is not None:
                                            return True

                                        if self.signalings is not None and self.signalings._has_data():
                                            return True

                                        if self.signalings is not None and self.signalings.is_presence():
                                            return True

                                        if self.transports is not None and self.transports._has_data():
                                            return True

                                        if self.transports is not None and self.transports.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.MulticastP2mp']['meta_info']


                                class VfiPseudowires(object):
                                    """
                                    List of pseudowires
                                    
                                    .. attribute:: vfi_pseudowire
                                    
                                    	Pseudowire configuration
                                    	**type**\: list of :py:class:`VfiPseudowire <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.vfi_pseudowire = YList()
                                        self.vfi_pseudowire.parent = self
                                        self.vfi_pseudowire.name = 'vfi_pseudowire'


                                    class VfiPseudowire(object):
                                        """
                                        Pseudowire configuration
                                        
                                        .. attribute:: neighbor
                                        
                                        	Neighbor IP address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: pseudowire_id
                                        
                                        	Pseudowire ID
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: pseudowire_static_mac_addresses
                                        
                                        	Static Mac Address Table
                                        	**type**\: :py:class:`PseudowireStaticMacAddresses <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses>`
                                        
                                        .. attribute:: vfi_pw_class
                                        
                                        	PW class template name to use for this pseudowire
                                        	**type**\: str
                                        
                                        	**range:** 0..32
                                        
                                        .. attribute:: vfi_pw_dhcp_snoop
                                        
                                        	Attach a DHCP Snooping profile
                                        	**type**\: :py:class:`VfiPwDhcpSnoop <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop>`
                                        
                                        .. attribute:: vfi_pw_igmp_snoop
                                        
                                        	Attach a IGMP Snooping profile
                                        	**type**\: str
                                        
                                        	**range:** 0..32
                                        
                                        .. attribute:: vfi_pw_mld_snoop
                                        
                                        	Attach a MLD Snooping profile
                                        	**type**\: str
                                        
                                        	**range:** 0..32
                                        
                                        .. attribute:: vfi_pw_mpls_static_labels
                                        
                                        	MPLS static labels
                                        	**type**\: :py:class:`VfiPwMplsStaticLabels <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.neighbor = None
                                            self.pseudowire_id = None
                                            self.pseudowire_static_mac_addresses = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses()
                                            self.pseudowire_static_mac_addresses.parent = self
                                            self.vfi_pw_class = None
                                            self.vfi_pw_dhcp_snoop = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop()
                                            self.vfi_pw_dhcp_snoop.parent = self
                                            self.vfi_pw_igmp_snoop = None
                                            self.vfi_pw_mld_snoop = None
                                            self.vfi_pw_mpls_static_labels = L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels()
                                            self.vfi_pw_mpls_static_labels.parent = self


                                        class PseudowireStaticMacAddresses(object):
                                            """
                                            Static Mac Address Table
                                            
                                            .. attribute:: pseudowire_static_mac_address
                                            
                                            	Static Mac Address Configuration
                                            	**type**\: list of :py:class:`PseudowireStaticMacAddress <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.pseudowire_static_mac_address = YList()
                                                self.pseudowire_static_mac_address.parent = self
                                                self.pseudowire_static_mac_address.name = 'pseudowire_static_mac_address'


                                            class PseudowireStaticMacAddress(object):
                                                """
                                                Static Mac Address Configuration
                                                
                                                .. attribute:: address
                                                
                                                	Static MAC address
                                                	**type**\: str
                                                
                                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.address = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                    if self.address is None:
                                                        raise YPYDataValidationError('Key property address is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-static-mac-address[Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.is_presence():
                                                        return True
                                                    if self.address is not None:
                                                        return True

                                                    return False

                                                def is_presence(self):
                                                    ''' Returns True if this instance represents presence container else returns False '''
                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses.PseudowireStaticMacAddress']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-static-mac-addresses'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.pseudowire_static_mac_address is not None:
                                                    for child_ref in self.pseudowire_static_mac_address:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.PseudowireStaticMacAddresses']['meta_info']


                                        class VfiPwDhcpSnoop(object):
                                            """
                                            Attach a DHCP Snooping profile
                                            
                                            .. attribute:: dhcp_snooping_id
                                            
                                            	Disable DHCP snooping
                                            	**type**\: str
                                            
                                            .. attribute:: profile_id
                                            
                                            	Set the snooping profile
                                            	**type**\: :py:class:`InterfaceProfile_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.InterfaceProfile_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.dhcp_snooping_id = None
                                                self.profile_id = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfi-pw-dhcp-snoop'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.dhcp_snooping_id is not None:
                                                    return True

                                                if self.profile_id is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwDhcpSnoop']['meta_info']


                                        class VfiPwMplsStaticLabels(object):
                                            """
                                            MPLS static labels
                                            
                                            .. attribute:: local_static_label
                                            
                                            	Pseudowire local static label
                                            	**type**\: int
                                            
                                            	**range:** 16..1048575
                                            
                                            .. attribute:: remote_static_label
                                            
                                            	Pseudowire remote static label
                                            	**type**\: int
                                            
                                            	**range:** 16..1048575
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.local_static_label = None
                                                self.remote_static_label = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfi-pw-mpls-static-labels'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.local_static_label is not None:
                                                    return True

                                                if self.remote_static_label is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire.VfiPwMplsStaticLabels']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.neighbor is None:
                                                raise YPYDataValidationError('Key property neighbor is None')
                                            if self.pseudowire_id is None:
                                                raise YPYDataValidationError('Key property pseudowire_id is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfi-pseudowire[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.neighbor is not None:
                                                return True

                                            if self.pseudowire_id is not None:
                                                return True

                                            if self.pseudowire_static_mac_addresses is not None and self.pseudowire_static_mac_addresses._has_data():
                                                return True

                                            if self.pseudowire_static_mac_addresses is not None and self.pseudowire_static_mac_addresses.is_presence():
                                                return True

                                            if self.vfi_pw_class is not None:
                                                return True

                                            if self.vfi_pw_dhcp_snoop is not None and self.vfi_pw_dhcp_snoop._has_data():
                                                return True

                                            if self.vfi_pw_dhcp_snoop is not None and self.vfi_pw_dhcp_snoop.is_presence():
                                                return True

                                            if self.vfi_pw_igmp_snoop is not None:
                                                return True

                                            if self.vfi_pw_mld_snoop is not None:
                                                return True

                                            if self.vfi_pw_mpls_static_labels is not None and self.vfi_pw_mpls_static_labels._has_data():
                                                return True

                                            if self.vfi_pw_mpls_static_labels is not None and self.vfi_pw_mpls_static_labels.is_presence():
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires.VfiPseudowire']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfi-pseudowires'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.vfi_pseudowire is not None:
                                            for child_ref in self.vfi_pseudowire:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi.VfiPseudowires']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.name is None:
                                        raise YPYDataValidationError('Key property name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfi[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.name is not None:
                                        return True

                                    if self.bgp_auto_discovery is not None and self.bgp_auto_discovery._has_data():
                                        return True

                                    if self.bgp_auto_discovery is not None and self.bgp_auto_discovery.is_presence():
                                        return True

                                    if self.multicast_p2mp is not None and self.multicast_p2mp._has_data():
                                        return True

                                    if self.multicast_p2mp is not None and self.multicast_p2mp.is_presence():
                                        return True

                                    if self.vfi_pseudowires is not None and self.vfi_pseudowires._has_data():
                                        return True

                                    if self.vfi_pseudowires is not None and self.vfi_pseudowires.is_presence():
                                        return True

                                    if self.vfi_shutdown is not None:
                                        return True

                                    if self.vpnid is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis.Vfi']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:vfis'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.vfi is not None:
                                    for child_ref in self.vfi:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain.Vfis']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYDataValidationError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domain[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.name is not None:
                                return True

                            if self.bd_attachment_circuits is not None and self.bd_attachment_circuits._has_data():
                                return True

                            if self.bd_attachment_circuits is not None and self.bd_attachment_circuits.is_presence():
                                return True

                            if self.bd_pseudowires is not None and self.bd_pseudowires._has_data():
                                return True

                            if self.bd_pseudowires is not None and self.bd_pseudowires.is_presence():
                                return True

                            if self.bd_storm_controls is not None and self.bd_storm_controls._has_data():
                                return True

                            if self.bd_storm_controls is not None and self.bd_storm_controls.is_presence():
                                return True

                            if self.bridge_domain_mac is not None and self.bridge_domain_mac._has_data():
                                return True

                            if self.bridge_domain_mac is not None and self.bridge_domain_mac.is_presence():
                                return True

                            if self.bridge_domain_mtu is not None:
                                return True

                            if self.bridge_domain_pbb is not None and self.bridge_domain_pbb._has_data():
                                return True

                            if self.bridge_domain_pbb is not None and self.bridge_domain_pbb.is_presence():
                                return True

                            if self.coupled_mode is not None:
                                return True

                            if self.dai is not None and self.dai._has_data():
                                return True

                            if self.dai is not None and self.dai.is_presence():
                                return True

                            if self.dhcp is not None:
                                return True

                            if self.flooding is not None:
                                return True

                            if self.flooding_unknown_unicast is not None:
                                return True

                            if self.igmp_snooping is not None:
                                return True

                            if self.igmp_snooping_disable is not None:
                                return True

                            if self.ip_source_guard is not None and self.ip_source_guard._has_data():
                                return True

                            if self.ip_source_guard is not None and self.ip_source_guard.is_presence():
                                return True

                            if self.member_vnis is not None and self.member_vnis._has_data():
                                return True

                            if self.member_vnis is not None and self.member_vnis.is_presence():
                                return True

                            if self.mld_snooping is not None:
                                return True

                            if self.nv_satellite is not None and self.nv_satellite._has_data():
                                return True

                            if self.nv_satellite is not None and self.nv_satellite.is_presence():
                                return True

                            if self.routed_interfaces is not None and self.routed_interfaces._has_data():
                                return True

                            if self.routed_interfaces is not None and self.routed_interfaces.is_presence():
                                return True

                            if self.shutdown is not None:
                                return True

                            if self.transport_mode is not None:
                                return True

                            if self.vfis is not None and self.vfis._has_data():
                                return True

                            if self.vfis is not None and self.vfis.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains.BridgeDomain']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:bridge-domains'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.bridge_domain is not None:
                            for child_ref in self.bridge_domain:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup.BridgeDomains']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-groups/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-group[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.name is not None:
                        return True

                    if self.bridge_domains is not None and self.bridge_domains._has_data():
                        return True

                    if self.bridge_domains is not None and self.bridge_domains.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2vpn.Database.BridgeDomainGroups.BridgeDomainGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:bridge-domain-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.bridge_domain_group is not None:
                    for child_ref in self.bridge_domain_group:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2vpn.Database.BridgeDomainGroups']['meta_info']


        class G8032Rings(object):
            """
            List of G8032 Ring
            
            .. attribute:: g8032_ring
            
            	G8032 Ring
            	**type**\: list of :py:class:`G8032Ring <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.g8032_ring = YList()
                self.g8032_ring.parent = self
                self.g8032_ring.name = 'g8032_ring'


            class G8032Ring(object):
                """
                G8032 Ring
                
                .. attribute:: g8032_ring_name
                
                	Name of the G8032 ring
                	**type**\: str
                
                	**range:** 0..32
                
                .. attribute:: erp_instances
                
                	List of ethernet ring protection instance
                	**type**\: :py:class:`ErpInstances <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring.ErpInstances>`
                
                .. attribute:: erp_port0s
                
                	Ethernet ring protection port0
                	**type**\: :py:class:`ErpPort0s <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring.ErpPort0s>`
                
                .. attribute:: erp_port1s
                
                	Ethernet ring protection port0
                	**type**\: :py:class:`ErpPort1s <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring.ErpPort1s>`
                
                .. attribute:: erp_provider_bridge
                
                	Ethernet ring protection provider bridge
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: exclusion_list
                
                	Vlan IDs in the format of a\-b,c,d,e\-f,g ,untagged
                	**type**\: str
                
                .. attribute:: open_ring
                
                	Specify the G.8032 instance as open ring
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.g8032_ring_name = None
                    self.erp_instances = L2vpn.Database.G8032Rings.G8032Ring.ErpInstances()
                    self.erp_instances.parent = self
                    self.erp_port0s = L2vpn.Database.G8032Rings.G8032Ring.ErpPort0s()
                    self.erp_port0s.parent = self
                    self.erp_port1s = L2vpn.Database.G8032Rings.G8032Ring.ErpPort1s()
                    self.erp_port1s.parent = self
                    self.erp_provider_bridge = None
                    self.exclusion_list = None
                    self.open_ring = None


                class ErpInstances(object):
                    """
                    List of ethernet ring protection instance
                    
                    .. attribute:: erp_instance
                    
                    	Ethernet ring protection instance
                    	**type**\: list of :py:class:`ErpInstance <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.erp_instance = YList()
                        self.erp_instance.parent = self
                        self.erp_instance.name = 'erp_instance'


                    class ErpInstance(object):
                        """
                        Ethernet ring protection instance
                        
                        .. attribute:: erp_instance_id
                        
                        	ERP instance number
                        	**type**\: int
                        
                        	**range:** 1..2
                        
                        .. attribute:: aps
                        
                        	Automatic protection switching
                        	**type**\: :py:class:`Aps <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps>`
                        
                        .. attribute:: description
                        
                        	Ethernet ring protection instance description
                        	**type**\: str
                        
                        	**range:** 0..32
                        
                        .. attribute:: inclusion_list
                        
                        	Associates a set of VLAN IDs with the G .8032 instance
                        	**type**\: str
                        
                        .. attribute:: profile
                        
                        	Ethernet ring protection instance profile
                        	**type**\: str
                        
                        	**range:** 0..32
                        
                        .. attribute:: rpl
                        
                        	Ring protection link
                        	**type**\: :py:class:`Rpl <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.erp_instance_id = None
                            self.aps = L2vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps()
                            self.aps.parent = self
                            self.description = None
                            self.inclusion_list = None
                            self.profile = None
                            self.rpl = L2vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl()
                            self.rpl.parent = self


                        class Aps(object):
                            """
                            Automatic protection switching
                            
                            .. attribute:: enable
                            
                            	Enable automatic protection switching
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: level
                            
                            	Automatic protection switching level
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: port0
                            
                            	Port0 APS channel in the format of InterfaceName
                            	**type**\: str
                            
                            .. attribute:: port1
                            
                            	APS channel for ERP port1
                            	**type**\: :py:class:`Port1 <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.level = None
                                self.port0 = None
                                self.port1 = L2vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1()
                                self.port1.parent = self


                            class Port1(object):
                                """
                                APS channel for ERP port1
                                
                                .. attribute:: aps_channel
                                
                                	Port1 APS channel in the format of InterfaceName, BDName or XconnectName
                                	**type**\: str
                                
                                .. attribute:: aps_type
                                
                                	Port1 APS type
                                	**type**\: :py:class:`Erpaps_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Erpaps_Enum>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aps_channel = None
                                    self.aps_type = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:port1'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.aps_channel is not None:
                                        return True

                                    if self.aps_type is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps.Port1']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:aps'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.enable is not None:
                                    return True

                                if self.level is not None:
                                    return True

                                if self.port0 is not None:
                                    return True

                                if self.port1 is not None and self.port1._has_data():
                                    return True

                                if self.port1 is not None and self.port1.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Aps']['meta_info']


                        class Rpl(object):
                            """
                            Ring protection link
                            
                            .. attribute:: port
                            
                            	ERP main port number
                            	**type**\: :py:class:`ErpPort1_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.ErpPort1_Enum>`
                            
                            .. attribute:: role
                            
                            	RPL role
                            	**type**\: :py:class:`RplRole_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.RplRole_Enum>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.port = None
                                self.role = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:rpl'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.port is not None:
                                    return True

                                if self.role is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance.Rpl']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.erp_instance_id is None:
                                raise YPYDataValidationError('Key property erp_instance_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-instance[Cisco-IOS-XR-l2vpn-cfg:erp-instance-id = ' + str(self.erp_instance_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.erp_instance_id is not None:
                                return True

                            if self.aps is not None and self.aps._has_data():
                                return True

                            if self.aps is not None and self.aps.is_presence():
                                return True

                            if self.description is not None:
                                return True

                            if self.inclusion_list is not None:
                                return True

                            if self.profile is not None:
                                return True

                            if self.rpl is not None and self.rpl._has_data():
                                return True

                            if self.rpl is not None and self.rpl.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring.ErpInstances.ErpInstance']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-instances'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.erp_instance is not None:
                            for child_ref in self.erp_instance:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring.ErpInstances']['meta_info']


                class ErpPort0s(object):
                    """
                    Ethernet ring protection port0
                    
                    .. attribute:: erp_port0
                    
                    	Configure ERP main port0
                    	**type**\: list of :py:class:`ErpPort0 <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring.ErpPort0s.ErpPort0>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.erp_port0 = YList()
                        self.erp_port0.parent = self
                        self.erp_port0.name = 'erp_port0'


                    class ErpPort0(object):
                        """
                        Configure ERP main port0
                        
                        .. attribute:: interface_name
                        
                        	Port0 interface
                        	**type**\: str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: monitor
                        
                        	Ethernet ring protection port0 monitor
                        	**type**\: str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.monitor = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYDataValidationError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-port0[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.interface_name is not None:
                                return True

                            if self.monitor is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring.ErpPort0s.ErpPort0']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-port0s'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.erp_port0 is not None:
                            for child_ref in self.erp_port0:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring.ErpPort0s']['meta_info']


                class ErpPort1s(object):
                    """
                    Ethernet ring protection port0
                    
                    .. attribute:: erp_port1
                    
                    	Ethernet ring protection port1
                    	**type**\: list of :py:class:`ErpPort1 <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring.ErpPort1s.ErpPort1>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.erp_port1 = YList()
                        self.erp_port1.parent = self
                        self.erp_port1.name = 'erp_port1'


                    class ErpPort1(object):
                        """
                        Ethernet ring protection port1
                        
                        .. attribute:: erp_port_type
                        
                        	Port1 type
                        	**type**\: :py:class:`ErpPort_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.ErpPort_Enum>`
                        
                        .. attribute:: none
                        
                        	none
                        	**type**\: :py:class:`None_ <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring.ErpPort1s.ErpPort1.None_>`
                        
                        .. attribute:: virtual_or_interface
                        
                        	virtual or interface
                        	**type**\: list of :py:class:`VirtualOrInterface <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.G8032Rings.G8032Ring.ErpPort1s.ErpPort1.VirtualOrInterface>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.erp_port_type = None
                            self.none = None
                            self.virtual_or_interface = YList()
                            self.virtual_or_interface.parent = self
                            self.virtual_or_interface.name = 'virtual_or_interface'


                        class None_(object):
                            """
                            none
                            
                            .. attribute:: monitor
                            
                            	Ethernet ring protection port1 monitor
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.monitor = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:none'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.monitor is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return True

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring.ErpPort1s.ErpPort1.None_']['meta_info']


                        class VirtualOrInterface(object):
                            """
                            virtual or interface
                            
                            .. attribute:: interface_name
                            
                            	Port1 interface
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: monitor
                            
                            	Ethernet ring protection port1 monitor
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.monitor = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYDataValidationError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:virtual-or-interface[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.interface_name is not None:
                                    return True

                                if self.monitor is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring.ErpPort1s.ErpPort1.VirtualOrInterface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.erp_port_type is None:
                                raise YPYDataValidationError('Key property erp_port_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-port1[Cisco-IOS-XR-l2vpn-cfg:erp-port-type = ' + str(self.erp_port_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.erp_port_type is not None:
                                return True

                            if self.none is not None and self.none._has_data():
                                return True

                            if self.none is not None and self.none.is_presence():
                                return True

                            if self.virtual_or_interface is not None:
                                for child_ref in self.virtual_or_interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring.ErpPort1s.ErpPort1']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:erp-port1s'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.erp_port1 is not None:
                            for child_ref in self.erp_port1:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring.ErpPort1s']['meta_info']

                @property
                def _common_path(self):
                    if self.g8032_ring_name is None:
                        raise YPYDataValidationError('Key property g8032_ring_name is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:g8032-rings/Cisco-IOS-XR-l2vpn-cfg:g8032-ring[Cisco-IOS-XR-l2vpn-cfg:g8032-ring-name = ' + str(self.g8032_ring_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.g8032_ring_name is not None:
                        return True

                    if self.erp_instances is not None and self.erp_instances._has_data():
                        return True

                    if self.erp_instances is not None and self.erp_instances.is_presence():
                        return True

                    if self.erp_port0s is not None and self.erp_port0s._has_data():
                        return True

                    if self.erp_port0s is not None and self.erp_port0s.is_presence():
                        return True

                    if self.erp_port1s is not None and self.erp_port1s._has_data():
                        return True

                    if self.erp_port1s is not None and self.erp_port1s.is_presence():
                        return True

                    if self.erp_provider_bridge is not None:
                        return True

                    if self.exclusion_list is not None:
                        return True

                    if self.open_ring is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2vpn.Database.G8032Rings.G8032Ring']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:g8032-rings'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.g8032_ring is not None:
                    for child_ref in self.g8032_ring:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2vpn.Database.G8032Rings']['meta_info']


        class PseudowireClasses(object):
            """
            List of pseudowire classes
            
            .. attribute:: pseudowire_class
            
            	Pseudowire class
            	**type**\: list of :py:class:`PseudowireClass <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.pseudowire_class = YList()
                self.pseudowire_class.parent = self
                self.pseudowire_class.name = 'pseudowire_class'


            class PseudowireClass(object):
                """
                Pseudowire class
                
                .. attribute:: name
                
                	Name of the pseudowire class
                	**type**\: str
                
                	**range:** 0..32
                
                .. attribute:: backup_disable_delay
                
                	Back Up Pseudowire class
                	**type**\: :py:class:`BackupDisableDelay <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay>`
                
                .. attribute:: enable
                
                	Enable pseudowire class
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: l2tpv3_encapsulation
                
                	L2TPv3 encapsulation
                	**type**\: :py:class:`L2tpv3Encapsulation <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation>`
                
                .. attribute:: mac_withdraw
                
                	Enable backup MAC withdraw
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: mpls_encapsulation
                
                	MPLS encapsulation
                	**type**\: :py:class:`MplsEncapsulation <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.backup_disable_delay = L2vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay()
                    self.backup_disable_delay.parent = self
                    self.enable = None
                    self.l2tpv3_encapsulation = L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation()
                    self.l2tpv3_encapsulation.parent = self
                    self.mac_withdraw = None
                    self.mpls_encapsulation = L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation()
                    self.mpls_encapsulation.parent = self


                class BackupDisableDelay(object):
                    """
                    Back Up Pseudowire class
                    
                    .. attribute:: disable_backup
                    
                    	Disable backup delay
                    	**type**\: int
                    
                    	**range:** 0..180
                    
                    .. attribute:: type
                    
                    	Delay or Never
                    	**type**\: :py:class:`BackupDisable_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BackupDisable_Enum>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.disable_backup = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-disable-delay'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.disable_backup is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.BackupDisableDelay']['meta_info']


                class L2tpv3Encapsulation(object):
                    """
                    L2TPv3 encapsulation
                    
                    .. attribute:: cookie_size
                    
                    	Cookie size
                    	**type**\: :py:class:`L2tpCookieSize_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize_Enum>`
                    
                    .. attribute:: df_bit_set
                    
                    	Set the do not fragment bit to 1
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	Enable L2TPv3 encapsulation
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: path_mtu
                    
                    	Path maximum transmission unit
                    	**type**\: :py:class:`PathMtu <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.PathMtu>`
                    
                    .. attribute:: sequencing
                    
                    	Sequencing
                    	**type**\: :py:class:`Sequencing <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.Sequencing>`
                    
                    .. attribute:: signaling_protocol
                    
                    	L2TPv3 signaling protocol
                    	**type**\: :py:class:`SignalingProtocol <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.SignalingProtocol>`
                    
                    .. attribute:: source_address
                    
                    	Source IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: time_to_live
                    
                    	Time to live
                    	**type**\: int
                    
                    	**range:** 1..255
                    
                    .. attribute:: transport_mode
                    
                    	Transport mode
                    	**type**\: :py:class:`TransportMode_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.TransportMode_Enum>`
                    
                    .. attribute:: type_of_service
                    
                    	Type of service
                    	**type**\: :py:class:`TypeOfService <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.TypeOfService>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.cookie_size = None
                        self.df_bit_set = None
                        self.enable = None
                        self.path_mtu = L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.PathMtu()
                        self.path_mtu.parent = self
                        self.sequencing = L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.Sequencing()
                        self.sequencing.parent = self
                        self.signaling_protocol = L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.SignalingProtocol()
                        self.signaling_protocol.parent = self
                        self.source_address = None
                        self.time_to_live = None
                        self.transport_mode = None
                        self.type_of_service = L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.TypeOfService()
                        self.type_of_service.parent = self


                    class PathMtu(object):
                        """
                        Path maximum transmission unit
                        
                        .. attribute:: enable
                        
                        	Enable path MTU
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: max_path_mtu
                        
                        	Maximum path maximum transmission unit
                        	**type**\: int
                        
                        	**range:** 68..65535
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.enable = None
                            self.max_path_mtu = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:path-mtu'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.enable is not None:
                                return True

                            if self.max_path_mtu is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.PathMtu']['meta_info']


                    class Sequencing(object):
                        """
                        Sequencing
                        
                        .. attribute:: resync_threshold
                        
                        	Out of sequence threshold
                        	**type**\: int
                        
                        	**range:** 5..65535
                        
                        .. attribute:: sequencing
                        
                        	Sequencing
                        	**type**\: :py:class:`L2tpv3Sequencing_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2tpv3Sequencing_Enum>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.resync_threshold = None
                            self.sequencing = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:sequencing'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.resync_threshold is not None:
                                return True

                            if self.sequencing is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.Sequencing']['meta_info']


                    class SignalingProtocol(object):
                        """
                        L2TPv3 signaling protocol
                        
                        .. attribute:: l2tpv3_class_name
                        
                        	Name of the L2TPv3 class name
                        	**type**\: str
                        
                        	**range:** 0..32
                        
                        .. attribute:: protocol
                        
                        	L2TPv3 signaling protocol
                        	**type**\: :py:class:`L2tpSignalingProtocol_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2tpSignalingProtocol_Enum>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.l2tpv3_class_name = None
                            self.protocol = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:signaling-protocol'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.l2tpv3_class_name is not None:
                                return True

                            if self.protocol is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.SignalingProtocol']['meta_info']


                    class TypeOfService(object):
                        """
                        Type of service
                        
                        .. attribute:: type_of_service_mode
                        
                        	Type of service mode
                        	**type**\: :py:class:`TypeOfServiceMode_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.TypeOfServiceMode_Enum>`
                        
                        .. attribute:: type_of_service_value
                        
                        	Type of service value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.type_of_service_mode = None
                            self.type_of_service_value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:type-of-service'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.type_of_service_mode is not None:
                                return True

                            if self.type_of_service_value is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation.TypeOfService']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tpv3-encapsulation'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.cookie_size is not None:
                            return True

                        if self.df_bit_set is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.path_mtu is not None and self.path_mtu._has_data():
                            return True

                        if self.path_mtu is not None and self.path_mtu.is_presence():
                            return True

                        if self.sequencing is not None and self.sequencing._has_data():
                            return True

                        if self.sequencing is not None and self.sequencing.is_presence():
                            return True

                        if self.signaling_protocol is not None and self.signaling_protocol._has_data():
                            return True

                        if self.signaling_protocol is not None and self.signaling_protocol.is_presence():
                            return True

                        if self.source_address is not None:
                            return True

                        if self.time_to_live is not None:
                            return True

                        if self.transport_mode is not None:
                            return True

                        if self.type_of_service is not None and self.type_of_service._has_data():
                            return True

                        if self.type_of_service is not None and self.type_of_service.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.L2tpv3Encapsulation']['meta_info']


                class MplsEncapsulation(object):
                    """
                    MPLS encapsulation
                    
                    .. attribute:: control_word
                    
                    	Enable control word
                    	**type**\: :py:class:`ControlWord_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.ControlWord_Enum>`
                    
                    .. attribute:: enable
                    
                    	Enable MPLS encapsulation
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: load_balance_group
                    
                    	Load Balancing
                    	**type**\: :py:class:`LoadBalanceGroup <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup>`
                    
                    .. attribute:: mpls_redundancy
                    
                    	Redundancy options for MPLS encapsulation
                    	**type**\: :py:class:`MplsRedundancy <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy>`
                    
                    .. attribute:: preferred_path
                    
                    	Preferred path
                    	**type**\: :py:class:`PreferredPath <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath>`
                    
                    .. attribute:: pw_switching_tlv
                    
                    	Pseudowire Switching Point Tlv
                    	**type**\: :py:class:`PwSwitchingPointTlv_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.PwSwitchingPointTlv_Enum>`
                    
                    .. attribute:: sequencing
                    
                    	Sequencing
                    	**type**\: :py:class:`Sequencing <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing>`
                    
                    .. attribute:: signaling_protocol
                    
                    	MPLS signaling protocol
                    	**type**\: :py:class:`MplsSignalingProtocol_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MplsSignalingProtocol_Enum>`
                    
                    .. attribute:: source_address
                    
                    	Source IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: static_tag_rewrite
                    
                    	Static Tag rewrite
                    	**type**\: int
                    
                    	**range:** 1..4094
                    
                    .. attribute:: transport_mode
                    
                    	Transport mode
                    	**type**\: :py:class:`TransportMode_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.TransportMode_Enum>`
                    
                    .. attribute:: vccv_type
                    
                    	VCCV verification type
                    	**type**\: :py:class:`VccvVerification_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.VccvVerification_Enum>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.control_word = None
                        self.enable = None
                        self.load_balance_group = L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup()
                        self.load_balance_group.parent = self
                        self.mpls_redundancy = L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy()
                        self.mpls_redundancy.parent = self
                        self.preferred_path = L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath()
                        self.preferred_path.parent = self
                        self.pw_switching_tlv = None
                        self.sequencing = L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing()
                        self.sequencing.parent = self
                        self.signaling_protocol = None
                        self.source_address = None
                        self.static_tag_rewrite = None
                        self.transport_mode = None
                        self.vccv_type = None


                    class LoadBalanceGroup(object):
                        """
                        Load Balancing
                        
                        .. attribute:: flow_label_load_balance
                        
                        	Enable Flow Label based load balancing
                        	**type**\: :py:class:`FlowLabelLoadBalance <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance>`
                        
                        .. attribute:: flow_label_load_balance_code
                        
                        	Enable Legacy Flow Label TLV code
                        	**type**\: :py:class:`FlowLabelTlvCode_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.FlowLabelTlvCode_Enum>`
                        
                        .. attribute:: pw_label_load_balance
                        
                        	Enable PW Label based Load Balancing
                        	**type**\: :py:class:`LoadBalance_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.LoadBalance_Enum>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.flow_label_load_balance = L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance()
                            self.flow_label_load_balance.parent = self
                            self.flow_label_load_balance_code = None
                            self.pw_label_load_balance = None


                        class FlowLabelLoadBalance(object):
                            """
                            Enable Flow Label based load balancing
                            
                            .. attribute:: flow_label
                            
                            	Flow Label load balance type
                            	**type**\: :py:class:`FlowLabelLoadBalance_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance_Enum>`
                            
                            .. attribute:: static
                            
                            	Static Flow Label
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.flow_label = None
                                self.static = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:flow-label-load-balance'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.flow_label is not None:
                                    return True

                                if self.static is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup.FlowLabelLoadBalance']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:load-balance-group'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.flow_label_load_balance is not None and self.flow_label_load_balance._has_data():
                                return True

                            if self.flow_label_load_balance is not None and self.flow_label_load_balance.is_presence():
                                return True

                            if self.flow_label_load_balance_code is not None:
                                return True

                            if self.pw_label_load_balance is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.LoadBalanceGroup']['meta_info']


                    class MplsRedundancy(object):
                        """
                        Redundancy options for MPLS encapsulation
                        
                        .. attribute:: redundancy_initial_delay
                        
                        	Initial delay before activating the redundant PW, in seconds
                        	**type**\: int
                        
                        	**range:** 0..120
                        
                        .. attribute:: redundancy_one_way
                        
                        	Force one\-way PW redundancy behavior in Redundancy Group
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.redundancy_initial_delay = None
                            self.redundancy_one_way = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mpls-redundancy'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.redundancy_initial_delay is not None:
                                return True

                            if self.redundancy_one_way is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.MplsRedundancy']['meta_info']


                    class PreferredPath(object):
                        """
                        Preferred path
                        
                        .. attribute:: fallback_disable
                        
                        	Fallback disable
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: interface_tunnel_number
                        
                        	Interface Tunnel number for preferred path
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: type
                        
                        	Preferred Path Type
                        	**type**\: :py:class:`PreferredPath_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.PreferredPath_Enum>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.fallback_disable = None
                            self.interface_tunnel_number = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:preferred-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.fallback_disable is not None:
                                return True

                            if self.interface_tunnel_number is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.PreferredPath']['meta_info']


                    class Sequencing(object):
                        """
                        Sequencing
                        
                        .. attribute:: resync_threshold
                        
                        	Out of sequence threshold
                        	**type**\: int
                        
                        	**range:** 5..65535
                        
                        .. attribute:: sequencing
                        
                        	Sequencing
                        	**type**\: :py:class:`MplsSequencing_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.MplsSequencing_Enum>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.resync_threshold = None
                            self.sequencing = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:sequencing'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.resync_threshold is not None:
                                return True

                            if self.sequencing is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation.Sequencing']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mpls-encapsulation'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.control_word is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.load_balance_group is not None and self.load_balance_group._has_data():
                            return True

                        if self.load_balance_group is not None and self.load_balance_group.is_presence():
                            return True

                        if self.mpls_redundancy is not None and self.mpls_redundancy._has_data():
                            return True

                        if self.mpls_redundancy is not None and self.mpls_redundancy.is_presence():
                            return True

                        if self.preferred_path is not None and self.preferred_path._has_data():
                            return True

                        if self.preferred_path is not None and self.preferred_path.is_presence():
                            return True

                        if self.pw_switching_tlv is not None:
                            return True

                        if self.sequencing is not None and self.sequencing._has_data():
                            return True

                        if self.sequencing is not None and self.sequencing.is_presence():
                            return True

                        if self.signaling_protocol is not None:
                            return True

                        if self.source_address is not None:
                            return True

                        if self.static_tag_rewrite is not None:
                            return True

                        if self.transport_mode is not None:
                            return True

                        if self.vccv_type is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass.MplsEncapsulation']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:pseudowire-classes/Cisco-IOS-XR-l2vpn-cfg:pseudowire-class[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.name is not None:
                        return True

                    if self.backup_disable_delay is not None and self.backup_disable_delay._has_data():
                        return True

                    if self.backup_disable_delay is not None and self.backup_disable_delay.is_presence():
                        return True

                    if self.enable is not None:
                        return True

                    if self.l2tpv3_encapsulation is not None and self.l2tpv3_encapsulation._has_data():
                        return True

                    if self.l2tpv3_encapsulation is not None and self.l2tpv3_encapsulation.is_presence():
                        return True

                    if self.mac_withdraw is not None:
                        return True

                    if self.mpls_encapsulation is not None and self.mpls_encapsulation._has_data():
                        return True

                    if self.mpls_encapsulation is not None and self.mpls_encapsulation.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2vpn.Database.PseudowireClasses.PseudowireClass']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:pseudowire-classes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.pseudowire_class is not None:
                    for child_ref in self.pseudowire_class:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2vpn.Database.PseudowireClasses']['meta_info']


        class Redundancy(object):
            """
            Redundancy groups
            
            .. attribute:: enable
            
            	Enable redundancy groups
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: iccp_redundancy_groups
            
            	List of Inter\-Chassis Communication Protocol redundancy groups
            	**type**\: :py:class:`IccpRedundancyGroups <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.Redundancy.IccpRedundancyGroups>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.iccp_redundancy_groups = L2vpn.Database.Redundancy.IccpRedundancyGroups()
                self.iccp_redundancy_groups.parent = self


            class IccpRedundancyGroups(object):
                """
                List of Inter\-Chassis Communication Protocol
                redundancy groups
                
                .. attribute:: iccp_redundancy_group
                
                	ICCP Redundancy group
                	**type**\: list of :py:class:`IccpRedundancyGroup <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.iccp_redundancy_group = YList()
                    self.iccp_redundancy_group.parent = self
                    self.iccp_redundancy_group.name = 'iccp_redundancy_group'


                class IccpRedundancyGroup(object):
                    """
                    ICCP Redundancy group
                    
                    .. attribute:: group_id
                    
                    	Group ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: iccp_interfaces
                    
                    	List of interfaces
                    	**type**\: :py:class:`IccpInterfaces <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces>`
                    
                    .. attribute:: multi_homing_node_id
                    
                    	ICCP\-based service multi\-homing node ID
                    	**type**\: int
                    
                    	**range:** 0..254
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.group_id = None
                        self.iccp_interfaces = L2vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces()
                        self.iccp_interfaces.parent = self
                        self.multi_homing_node_id = None


                    class IccpInterfaces(object):
                        """
                        List of interfaces
                        
                        .. attribute:: iccp_interface
                        
                        	Interface name
                        	**type**\: list of :py:class:`IccpInterface <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.iccp_interface = YList()
                            self.iccp_interface.parent = self
                            self.iccp_interface.name = 'iccp_interface'


                        class IccpInterface(object):
                            """
                            Interface name
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: mac_flush_tcn
                            
                            	Enable STP\-TCN MAC flushing
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: primary_vlan_range
                            
                            	Primary VLAN range, in the form of 1\-3,5 ,8\-11
                            	**type**\: str
                            
                            .. attribute:: recovery_delay
                            
                            	Failure clear recovery delay
                            	**type**\: int
                            
                            	**range:** 30..3600
                            
                            .. attribute:: secondary_vlan_range
                            
                            	Secondary VLAN range, in the form of 1\-3,5 ,8\-11
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None
                                self.mac_flush_tcn = None
                                self.primary_vlan_range = None
                                self.recovery_delay = None
                                self.secondary_vlan_range = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.interface_name is None:
                                    raise YPYDataValidationError('Key property interface_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:iccp-interface[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.interface_name is not None:
                                    return True

                                if self.mac_flush_tcn is not None:
                                    return True

                                if self.primary_vlan_range is not None:
                                    return True

                                if self.recovery_delay is not None:
                                    return True

                                if self.secondary_vlan_range is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces.IccpInterface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:iccp-interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.iccp_interface is not None:
                                for child_ref in self.iccp_interface:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup.IccpInterfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.group_id is None:
                            raise YPYDataValidationError('Key property group_id is None')

                        return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:redundancy/Cisco-IOS-XR-l2vpn-cfg:iccp-redundancy-groups/Cisco-IOS-XR-l2vpn-cfg:iccp-redundancy-group[Cisco-IOS-XR-l2vpn-cfg:group-id = ' + str(self.group_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.group_id is not None:
                            return True

                        if self.iccp_interfaces is not None and self.iccp_interfaces._has_data():
                            return True

                        if self.iccp_interfaces is not None and self.iccp_interfaces.is_presence():
                            return True

                        if self.multi_homing_node_id is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2vpn.Database.Redundancy.IccpRedundancyGroups.IccpRedundancyGroup']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:redundancy/Cisco-IOS-XR-l2vpn-cfg:iccp-redundancy-groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.iccp_redundancy_group is not None:
                        for child_ref in self.iccp_redundancy_group:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2vpn.Database.Redundancy.IccpRedundancyGroups']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:redundancy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.enable is not None:
                    return True

                if self.iccp_redundancy_groups is not None and self.iccp_redundancy_groups._has_data():
                    return True

                if self.iccp_redundancy_groups is not None and self.iccp_redundancy_groups.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2vpn.Database.Redundancy']['meta_info']


        class XconnectGroups(object):
            """
            List of xconnect groups
            
            .. attribute:: xconnect_group
            
            	Xconnect group
            	**type**\: list of :py:class:`XconnectGroup <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.xconnect_group = YList()
                self.xconnect_group.parent = self
                self.xconnect_group.name = 'xconnect_group'


            class XconnectGroup(object):
                """
                Xconnect group
                
                .. attribute:: name
                
                	Name of the xconnect group
                	**type**\: str
                
                	**range:** 0..32
                
                .. attribute:: mp2mp_xconnects
                
                	List of multi point to multi point xconnects
                	**type**\: :py:class:`Mp2mpXconnects <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects>`
                
                .. attribute:: p2p_xconnects
                
                	List of point to point xconnects
                	**type**\: :py:class:`P2pXconnects <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.mp2mp_xconnects = L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects()
                    self.mp2mp_xconnects.parent = self
                    self.p2p_xconnects = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects()
                    self.p2p_xconnects.parent = self


                class Mp2mpXconnects(object):
                    """
                    List of multi point to multi point xconnects
                    
                    .. attribute:: mp2mp_xconnect
                    
                    	Multi point to multi point xconnect
                    	**type**\: list of :py:class:`Mp2mpXconnect <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mp2mp_xconnect = YList()
                        self.mp2mp_xconnect.parent = self
                        self.mp2mp_xconnect.name = 'mp2mp_xconnect'


                    class Mp2mpXconnect(object):
                        """
                        Multi point to multi point xconnect
                        
                        .. attribute:: name
                        
                        	Name of the multi point to multi point xconnect
                        	**type**\: str
                        
                        	**range:** 0..26
                        
                        .. attribute:: mp2mp_auto_discovery
                        
                        	auto\-discovery in this MP2MP
                        	**type**\: :py:class:`Mp2mpAutoDiscovery <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery>`
                        
                        .. attribute:: mp2mp_control_word
                        
                        	Disable control word
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: mp2mp_interworking
                        
                        	Interworking
                        	**type**\: :py:class:`Interworking_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Interworking_Enum>`
                        
                        .. attribute:: mp2mp_shutdown
                        
                        	shutdown this MP2MP VPWS instance
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: mp2mpl2_encapsulation
                        
                        	Configure Layer 2 Encapsulation
                        	**type**\: :py:class:`L2Encapsulation_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2Encapsulation_Enum>`
                        
                        .. attribute:: mp2mpmtu
                        
                        	Maximum transmission unit for this MP2MP VPWS instance
                        	**type**\: int
                        
                        	**range:** 64..65535
                        
                        .. attribute:: mp2mpvpn_id
                        
                        	VPN Identifier
                        	**type**\: int
                        
                        	**range:** 1..4294967295
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.mp2mp_auto_discovery = L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery()
                            self.mp2mp_auto_discovery.parent = self
                            self.mp2mp_control_word = None
                            self.mp2mp_interworking = None
                            self.mp2mp_shutdown = None
                            self.mp2mpl2_encapsulation = None
                            self.mp2mpmtu = None
                            self.mp2mpvpn_id = None


                        class Mp2mpAutoDiscovery(object):
                            """
                            auto\-discovery in this MP2MP
                            
                            .. attribute:: enable
                            
                            	Enable auto\-discovery
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: mp2mp_route_targets
                            
                            	Route Target
                            	**type**\: :py:class:`Mp2mpRouteTargets <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpRouteTargets>`
                            
                            .. attribute:: mp2mp_signaling_protocol
                            
                            	signaling protocol in this MP2MP
                            	**type**\: :py:class:`Mp2mpSignalingProtocol <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol>`
                            
                            .. attribute:: route_distinguisher
                            
                            	Route Distinguisher
                            	**type**\: :py:class:`RouteDistinguisher <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.RouteDistinguisher>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.mp2mp_route_targets = L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpRouteTargets()
                                self.mp2mp_route_targets.parent = self
                                self.mp2mp_signaling_protocol = L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol()
                                self.mp2mp_signaling_protocol.parent = self
                                self.route_distinguisher = L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.RouteDistinguisher()
                                self.route_distinguisher.parent = self


                            class Mp2mpRouteTargets(object):
                                """
                                Route Target
                                
                                .. attribute:: mp2mp_route_target
                                
                                	Name of the Route Target
                                	**type**\: list of :py:class:`Mp2mpRouteTarget <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpRouteTargets.Mp2mpRouteTarget>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.mp2mp_route_target = YList()
                                    self.mp2mp_route_target.parent = self
                                    self.mp2mp_route_target.name = 'mp2mp_route_target'


                                class Mp2mpRouteTarget(object):
                                    """
                                    Name of the Route Target
                                    
                                    .. attribute:: format
                                    
                                    	Format of the route target
                                    	**type**\: :py:class:`BgpRouteTargetFormat_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetFormat_Enum>`
                                    
                                    .. attribute:: role
                                    
                                    	Role of the router target type
                                    	**type**\: :py:class:`BgpRouteTargetRole_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BgpRouteTargetRole_Enum>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	ipv4 address
                                    	**type**\: list of :py:class:`Ipv4Address <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpRouteTargets.Mp2mpRouteTarget.Ipv4Address>`
                                    
                                    .. attribute:: two_byte_as_or_four_byte_as
                                    
                                    	two byte as or four byte as
                                    	**type**\: list of :py:class:`TwoByteAsOrFourByteAs <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpRouteTargets.Mp2mpRouteTarget.TwoByteAsOrFourByteAs>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.format = None
                                        self.role = None
                                        self.ipv4_address = YList()
                                        self.ipv4_address.parent = self
                                        self.ipv4_address.name = 'ipv4_address'
                                        self.two_byte_as_or_four_byte_as = YList()
                                        self.two_byte_as_or_four_byte_as.parent = self
                                        self.two_byte_as_or_four_byte_as.name = 'two_byte_as_or_four_byte_as'


                                    class Ipv4Address(object):
                                        """
                                        ipv4 address
                                        
                                        .. attribute:: addr_index
                                        
                                        	Addr index
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: address
                                        
                                        	IPV4 address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.addr_index = None
                                            self.address = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.addr_index is None:
                                                raise YPYDataValidationError('Key property addr_index is None')
                                            if self.address is None:
                                                raise YPYDataValidationError('Key property address is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ipv4-address[Cisco-IOS-XR-l2vpn-cfg:addr-index = ' + str(self.addr_index) + '][Cisco-IOS-XR-l2vpn-cfg:address = ' + str(self.address) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.addr_index is not None:
                                                return True

                                            if self.address is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpRouteTargets.Mp2mpRouteTarget.Ipv4Address']['meta_info']


                                    class TwoByteAsOrFourByteAs(object):
                                        """
                                        two byte as or four byte as
                                        
                                        .. attribute:: as_
                                        
                                        	Two byte or 4 byte AS number
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: as_index
                                        
                                        	AS\:nn (hex or decimal format)
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.as_ = None
                                            self.as_index = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.as_ is None:
                                                raise YPYDataValidationError('Key property as_ is None')
                                            if self.as_index is None:
                                                raise YPYDataValidationError('Key property as_index is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:two-byte-as-or-four-byte-as[Cisco-IOS-XR-l2vpn-cfg:as = ' + str(self.as_) + '][Cisco-IOS-XR-l2vpn-cfg:as-index = ' + str(self.as_index) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.as_ is not None:
                                                return True

                                            if self.as_index is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpRouteTargets.Mp2mpRouteTarget.TwoByteAsOrFourByteAs']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.format is None:
                                            raise YPYDataValidationError('Key property format is None')
                                        if self.role is None:
                                            raise YPYDataValidationError('Key property role is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-route-target[Cisco-IOS-XR-l2vpn-cfg:format = ' + str(self.format) + '][Cisco-IOS-XR-l2vpn-cfg:role = ' + str(self.role) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.format is not None:
                                            return True

                                        if self.role is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            for child_ref in self.ipv4_address:
                                                if child_ref._has_data():
                                                    return True

                                        if self.two_byte_as_or_four_byte_as is not None:
                                            for child_ref in self.two_byte_as_or_four_byte_as:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpRouteTargets.Mp2mpRouteTarget']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-route-targets'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.mp2mp_route_target is not None:
                                        for child_ref in self.mp2mp_route_target:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpRouteTargets']['meta_info']


                            class Mp2mpSignalingProtocol(object):
                                """
                                signaling protocol in this MP2MP
                                
                                .. attribute:: ce_range
                                
                                	Local Customer Edge Identifier
                                	**type**\: int
                                
                                	**range:** 11..100
                                
                                .. attribute:: ceids
                                
                                	Local Customer Edge Identifier Table
                                	**type**\: :py:class:`Ceids <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.Ceids>`
                                
                                .. attribute:: enable
                                
                                	Enable signaling protocol
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: flow_label_load_balance
                                
                                	Enable Flow Label based load balancing
                                	**type**\: :py:class:`FlowLabelLoadBalance <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.FlowLabelLoadBalance>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ce_range = None
                                    self.ceids = L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.Ceids()
                                    self.ceids.parent = self
                                    self.enable = None
                                    self.flow_label_load_balance = L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.FlowLabelLoadBalance()
                                    self.flow_label_load_balance.parent = self


                                class Ceids(object):
                                    """
                                    Local Customer Edge Identifier Table
                                    
                                    .. attribute:: ceid
                                    
                                    	Local Customer Edge Identifier 
                                    	**type**\: list of :py:class:`Ceid <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.Ceids.Ceid>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.ceid = YList()
                                        self.ceid.parent = self
                                        self.ceid.name = 'ceid'


                                    class Ceid(object):
                                        """
                                        Local Customer Edge Identifier 
                                        
                                        .. attribute:: ce_id
                                        
                                        	Local Customer Edge Identifier
                                        	**type**\: int
                                        
                                        	**range:** 1..16384
                                        
                                        .. attribute:: remote_ceid_attachment_circuits
                                        
                                        	AC And Remote Customer Edge Identifier Table
                                        	**type**\: :py:class:`RemoteCeidAttachmentCircuits <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.ce_id = None
                                            self.remote_ceid_attachment_circuits = L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits()
                                            self.remote_ceid_attachment_circuits.parent = self


                                        class RemoteCeidAttachmentCircuits(object):
                                            """
                                            AC And Remote Customer Edge Identifier
                                            Table
                                            
                                            .. attribute:: remote_ceid_attachment_circuit
                                            
                                            	AC And Remote Customer Edge Identifier
                                            	**type**\: list of :py:class:`RemoteCeidAttachmentCircuit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.remote_ceid_attachment_circuit = YList()
                                                self.remote_ceid_attachment_circuit.parent = self
                                                self.remote_ceid_attachment_circuit.name = 'remote_ceid_attachment_circuit'


                                            class RemoteCeidAttachmentCircuit(object):
                                                """
                                                AC And Remote Customer Edge Identifier
                                                
                                                .. attribute:: name
                                                
                                                	The name of the Attachment Circuit
                                                	**type**\: str
                                                
                                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                                
                                                .. attribute:: remote_ce_id
                                                
                                                	Remote Customer Edge Identifier
                                                	**type**\: int
                                                
                                                	**range:** 1..16384
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.name = None
                                                    self.remote_ce_id = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                    if self.name is None:
                                                        raise YPYDataValidationError('Key property name is None')
                                                    if self.remote_ce_id is None:
                                                        raise YPYDataValidationError('Key property remote_ce_id is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:remote-ceid-attachment-circuit[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + '][Cisco-IOS-XR-l2vpn-cfg:remote-ce-id = ' + str(self.remote_ce_id) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.is_presence():
                                                        return True
                                                    if self.name is not None:
                                                        return True

                                                    if self.remote_ce_id is not None:
                                                        return True

                                                    return False

                                                def is_presence(self):
                                                    ''' Returns True if this instance represents presence container else returns False '''
                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits.RemoteCeidAttachmentCircuit']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:remote-ceid-attachment-circuits'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.remote_ceid_attachment_circuit is not None:
                                                    for child_ref in self.remote_ceid_attachment_circuit:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.Ceids.Ceid.RemoteCeidAttachmentCircuits']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.ce_id is None:
                                                raise YPYDataValidationError('Key property ce_id is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ceid[Cisco-IOS-XR-l2vpn-cfg:ce-id = ' + str(self.ce_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.ce_id is not None:
                                                return True

                                            if self.remote_ceid_attachment_circuits is not None and self.remote_ceid_attachment_circuits._has_data():
                                                return True

                                            if self.remote_ceid_attachment_circuits is not None and self.remote_ceid_attachment_circuits.is_presence():
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.Ceids.Ceid']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:ceids'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.ceid is not None:
                                            for child_ref in self.ceid:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.Ceids']['meta_info']


                                class FlowLabelLoadBalance(object):
                                    """
                                    Enable Flow Label based load balancing
                                    
                                    .. attribute:: flow_label
                                    
                                    	Flow Label load balance type
                                    	**type**\: :py:class:`FlowLabelLoadBalance_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.FlowLabelLoadBalance_Enum>`
                                    
                                    .. attribute:: static
                                    
                                    	Static Flow Label
                                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.flow_label = None
                                        self.static = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:flow-label-load-balance'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.flow_label is not None:
                                            return True

                                        if self.static is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol.FlowLabelLoadBalance']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-signaling-protocol'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.ce_range is not None:
                                        return True

                                    if self.ceids is not None and self.ceids._has_data():
                                        return True

                                    if self.ceids is not None and self.ceids.is_presence():
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.flow_label_load_balance is not None and self.flow_label_load_balance._has_data():
                                        return True

                                    if self.flow_label_load_balance is not None and self.flow_label_load_balance.is_presence():
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.Mp2mpSignalingProtocol']['meta_info']


                            class RouteDistinguisher(object):
                                """
                                Route Distinguisher
                                
                                .. attribute:: addr_index
                                
                                	Addr index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: address
                                
                                	IPV4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: as_
                                
                                	Two byte or 4 byte AS number
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: as_index
                                
                                	AS\:nn (hex or decimal format)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: type
                                
                                	Router distinguisher type
                                	**type**\: :py:class:`BgpRouteDistinguisher_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher_Enum>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.addr_index = None
                                    self.address = None
                                    self.as_ = None
                                    self.as_index = None
                                    self.type = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:route-distinguisher'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.addr_index is not None:
                                        return True

                                    if self.address is not None:
                                        return True

                                    if self.as_ is not None:
                                        return True

                                    if self.as_index is not None:
                                        return True

                                    if self.type is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery.RouteDistinguisher']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-auto-discovery'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.enable is not None:
                                    return True

                                if self.mp2mp_route_targets is not None and self.mp2mp_route_targets._has_data():
                                    return True

                                if self.mp2mp_route_targets is not None and self.mp2mp_route_targets.is_presence():
                                    return True

                                if self.mp2mp_signaling_protocol is not None and self.mp2mp_signaling_protocol._has_data():
                                    return True

                                if self.mp2mp_signaling_protocol is not None and self.mp2mp_signaling_protocol.is_presence():
                                    return True

                                if self.route_distinguisher is not None and self.route_distinguisher._has_data():
                                    return True

                                if self.route_distinguisher is not None and self.route_distinguisher.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect.Mp2mpAutoDiscovery']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYDataValidationError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-xconnect[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.name is not None:
                                return True

                            if self.mp2mp_auto_discovery is not None and self.mp2mp_auto_discovery._has_data():
                                return True

                            if self.mp2mp_auto_discovery is not None and self.mp2mp_auto_discovery.is_presence():
                                return True

                            if self.mp2mp_control_word is not None:
                                return True

                            if self.mp2mp_interworking is not None:
                                return True

                            if self.mp2mp_shutdown is not None:
                                return True

                            if self.mp2mpl2_encapsulation is not None:
                                return True

                            if self.mp2mpmtu is not None:
                                return True

                            if self.mp2mpvpn_id is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects.Mp2mpXconnect']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mp2mp-xconnects'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.mp2mp_xconnect is not None:
                            for child_ref in self.mp2mp_xconnect:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.Mp2mpXconnects']['meta_info']


                class P2pXconnects(object):
                    """
                    List of point to point xconnects
                    
                    .. attribute:: p2p_xconnect
                    
                    	Point to point xconnect
                    	**type**\: list of :py:class:`P2pXconnect <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.p2p_xconnect = YList()
                        self.p2p_xconnect.parent = self
                        self.p2p_xconnect.name = 'p2p_xconnect'


                    class P2pXconnect(object):
                        """
                        Point to point xconnect
                        
                        .. attribute:: name
                        
                        	Name of the point to point xconnect
                        	**type**\: str
                        
                        	**range:** 0..38
                        
                        .. attribute:: attachment_circuits
                        
                        	List of attachment circuits
                        	**type**\: :py:class:`AttachmentCircuits <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.AttachmentCircuits>`
                        
                        .. attribute:: backup_attachment_circuits
                        
                        	List of backup attachment circuits
                        	**type**\: :py:class:`BackupAttachmentCircuits <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.BackupAttachmentCircuits>`
                        
                        .. attribute:: interworking
                        
                        	Interworking
                        	**type**\: :py:class:`Interworking_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.Interworking_Enum>`
                        
                        .. attribute:: monitor_sessions
                        
                        	List of Monitor session segments
                        	**type**\: :py:class:`MonitorSessions <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.MonitorSessions>`
                        
                        .. attribute:: p2p_description
                        
                        	cross connect description Name
                        	**type**\: str
                        
                        	**range:** 0..64
                        
                        .. attribute:: pseudowire_evpns
                        
                        	List of EVPN Services
                        	**type**\: :py:class:`PseudowireEvpns <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.PseudowireEvpns>`
                        
                        .. attribute:: pseudowire_routeds
                        
                        	List of pseudowire\-routed
                        	**type**\: :py:class:`PseudowireRouteds <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.PseudowireRouteds>`
                        
                        .. attribute:: pseudowires
                        
                        	List of pseudowires
                        	**type**\: :py:class:`Pseudowires <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires>`
                        
                        

                        """

                        _prefix = 'l2vpn-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.attachment_circuits = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.AttachmentCircuits()
                            self.attachment_circuits.parent = self
                            self.backup_attachment_circuits = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.BackupAttachmentCircuits()
                            self.backup_attachment_circuits.parent = self
                            self.interworking = None
                            self.monitor_sessions = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.MonitorSessions()
                            self.monitor_sessions.parent = self
                            self.p2p_description = None
                            self.pseudowire_evpns = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.PseudowireEvpns()
                            self.pseudowire_evpns.parent = self
                            self.pseudowire_routeds = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.PseudowireRouteds()
                            self.pseudowire_routeds.parent = self
                            self.pseudowires = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires()
                            self.pseudowires.parent = self


                        class AttachmentCircuits(object):
                            """
                            List of attachment circuits
                            
                            .. attribute:: attachment_circuit
                            
                            	Attachment circuit interface
                            	**type**\: list of :py:class:`AttachmentCircuit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.AttachmentCircuits.AttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.attachment_circuit = YList()
                                self.attachment_circuit.parent = self
                                self.attachment_circuit.name = 'attachment_circuit'


                            class AttachmentCircuit(object):
                                """
                                Attachment circuit interface
                                
                                .. attribute:: name
                                
                                	Name of the attachment circuit interface
                                	**type**\: str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: enable
                                
                                	Enable attachment circuit interface
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.name = None
                                    self.enable = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.name is None:
                                        raise YPYDataValidationError('Key property name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:attachment-circuit[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.name is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.AttachmentCircuits.AttachmentCircuit']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:attachment-circuits'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.attachment_circuit is not None:
                                    for child_ref in self.attachment_circuit:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.AttachmentCircuits']['meta_info']


                        class BackupAttachmentCircuits(object):
                            """
                            List of backup attachment circuits
                            
                            .. attribute:: backup_attachment_circuit
                            
                            	Backup attachment circuit
                            	**type**\: list of :py:class:`BackupAttachmentCircuit <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.backup_attachment_circuit = YList()
                                self.backup_attachment_circuit.parent = self
                                self.backup_attachment_circuit.name = 'backup_attachment_circuit'


                            class BackupAttachmentCircuit(object):
                                """
                                Backup attachment circuit
                                
                                .. attribute:: interface_name
                                
                                	Name of the attachment circuit interface
                                	**type**\: str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.interface_name is None:
                                        raise YPYDataValidationError('Key property interface_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-attachment-circuit[Cisco-IOS-XR-l2vpn-cfg:interface-name = ' + str(self.interface_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.interface_name is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.BackupAttachmentCircuits.BackupAttachmentCircuit']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-attachment-circuits'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.backup_attachment_circuit is not None:
                                    for child_ref in self.backup_attachment_circuit:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.BackupAttachmentCircuits']['meta_info']


                        class MonitorSessions(object):
                            """
                            List of Monitor session segments
                            
                            .. attribute:: monitor_session
                            
                            	Monitor session segment
                            	**type**\: list of :py:class:`MonitorSession <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.MonitorSessions.MonitorSession>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.monitor_session = YList()
                                self.monitor_session.parent = self
                                self.monitor_session.name = 'monitor_session'


                            class MonitorSession(object):
                                """
                                Monitor session segment
                                
                                .. attribute:: name
                                
                                	Name of the monitor session
                                	**type**\: str
                                
                                	**range:** 0..64
                                
                                .. attribute:: enable
                                
                                	Enable monitor session segment 
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.name = None
                                    self.enable = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.name is None:
                                        raise YPYDataValidationError('Key property name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:monitor-session[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.name is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.MonitorSessions.MonitorSession']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:monitor-sessions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.monitor_session is not None:
                                    for child_ref in self.monitor_session:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.MonitorSessions']['meta_info']


                        class PseudowireEvpns(object):
                            """
                            List of EVPN Services
                            
                            .. attribute:: pseudowire_evpn
                            
                            	EVPN P2P Service Configuration
                            	**type**\: list of :py:class:`PseudowireEvpn <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.PseudowireEvpns.PseudowireEvpn>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pseudowire_evpn = YList()
                                self.pseudowire_evpn.parent = self
                                self.pseudowire_evpn.name = 'pseudowire_evpn'


                            class PseudowireEvpn(object):
                                """
                                EVPN P2P Service Configuration
                                
                                .. attribute:: eviid
                                
                                	Ethernet VPN ID
                                	**type**\: int
                                
                                	**range:** 1..65534
                                
                                .. attribute:: remote_acid
                                
                                	Remote AC ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: source_acid
                                
                                	Source AC ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.eviid = None
                                    self.remote_acid = None
                                    self.source_acid = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.eviid is None:
                                        raise YPYDataValidationError('Key property eviid is None')
                                    if self.remote_acid is None:
                                        raise YPYDataValidationError('Key property remote_acid is None')
                                    if self.source_acid is None:
                                        raise YPYDataValidationError('Key property source_acid is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-evpn[Cisco-IOS-XR-l2vpn-cfg:eviid = ' + str(self.eviid) + '][Cisco-IOS-XR-l2vpn-cfg:remote-acid = ' + str(self.remote_acid) + '][Cisco-IOS-XR-l2vpn-cfg:source-acid = ' + str(self.source_acid) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.eviid is not None:
                                        return True

                                    if self.remote_acid is not None:
                                        return True

                                    if self.source_acid is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.PseudowireEvpns.PseudowireEvpn']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-evpns'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.pseudowire_evpn is not None:
                                    for child_ref in self.pseudowire_evpn:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.PseudowireEvpns']['meta_info']


                        class PseudowireRouteds(object):
                            """
                            List of pseudowire\-routed
                            
                            .. attribute:: pseudowire_routed
                            
                            	Pseudowire configuration
                            	**type**\: list of :py:class:`PseudowireRouted <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.PseudowireRouteds.PseudowireRouted>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pseudowire_routed = YList()
                                self.pseudowire_routed.parent = self
                                self.pseudowire_routed.name = 'pseudowire_routed'


                            class PseudowireRouted(object):
                                """
                                Pseudowire configuration
                                
                                .. attribute:: acid
                                
                                	Target AC ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: global_id
                                
                                	Target Global ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: prefix
                                
                                	Target Prefix
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: sacid
                                
                                	Source AC ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: class_
                                
                                	Name of the pseudowire class
                                	**type**\: str
                                
                                	**range:** 0..32
                                
                                .. attribute:: tag_impose
                                
                                	Tag Impose vlan tagged mode
                                	**type**\: int
                                
                                	**range:** 1..4094
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acid = None
                                    self.global_id = None
                                    self.prefix = None
                                    self.sacid = None
                                    self.class_ = None
                                    self.tag_impose = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.acid is None:
                                        raise YPYDataValidationError('Key property acid is None')
                                    if self.global_id is None:
                                        raise YPYDataValidationError('Key property global_id is None')
                                    if self.prefix is None:
                                        raise YPYDataValidationError('Key property prefix is None')
                                    if self.sacid is None:
                                        raise YPYDataValidationError('Key property sacid is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-routed[Cisco-IOS-XR-l2vpn-cfg:acid = ' + str(self.acid) + '][Cisco-IOS-XR-l2vpn-cfg:global-id = ' + str(self.global_id) + '][Cisco-IOS-XR-l2vpn-cfg:prefix = ' + str(self.prefix) + '][Cisco-IOS-XR-l2vpn-cfg:sacid = ' + str(self.sacid) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.acid is not None:
                                        return True

                                    if self.global_id is not None:
                                        return True

                                    if self.prefix is not None:
                                        return True

                                    if self.sacid is not None:
                                        return True

                                    if self.class_ is not None:
                                        return True

                                    if self.tag_impose is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.PseudowireRouteds.PseudowireRouted']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-routeds'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.pseudowire_routed is not None:
                                    for child_ref in self.pseudowire_routed:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.PseudowireRouteds']['meta_info']


                        class Pseudowires(object):
                            """
                            List of pseudowires
                            
                            .. attribute:: pseudowire
                            
                            	Pseudowire configuration
                            	**type**\: list of :py:class:`Pseudowire <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire>`
                            
                            

                            """

                            _prefix = 'l2vpn-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pseudowire = YList()
                                self.pseudowire.parent = self
                                self.pseudowire.name = 'pseudowire'


                            class Pseudowire(object):
                                """
                                Pseudowire configuration
                                
                                .. attribute:: pseudowire_id
                                
                                	Pseudowire ID
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: neighbor
                                
                                	keys\: neighbor
                                	**type**\: list of :py:class:`Neighbor <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor>`
                                
                                .. attribute:: pseudowire_address
                                
                                	keys\: pseudowire\-address
                                	**type**\: list of :py:class:`PseudowireAddress <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress>`
                                
                                

                                """

                                _prefix = 'l2vpn-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.pseudowire_id = None
                                    self.neighbor = YList()
                                    self.neighbor.parent = self
                                    self.neighbor.name = 'neighbor'
                                    self.pseudowire_address = YList()
                                    self.pseudowire_address.parent = self
                                    self.pseudowire_address.name = 'pseudowire_address'


                                class Neighbor(object):
                                    """
                                    keys\: neighbor
                                    
                                    .. attribute:: neighbor
                                    
                                    	Pseudowire IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: backup_pseudowires
                                    
                                    	List of pseudowires
                                    	**type**\: :py:class:`BackupPseudowires <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires>`
                                    
                                    .. attribute:: bandwidth
                                    
                                    	Pseudowire Bandwidth
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: class_
                                    
                                    	Name of the pseudowire class
                                    	**type**\: str
                                    
                                    	**range:** 0..32
                                    
                                    .. attribute:: l2tp_static
                                    
                                    	Pseudowire L2TPv3 static configuration
                                    	**type**\: :py:class:`L2tpStatic <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStatic>`
                                    
                                    .. attribute:: l2tp_static_attributes
                                    
                                    	L2TP Static Attributes
                                    	**type**\: :py:class:`L2tpStaticAttributes <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes>`
                                    
                                    .. attribute:: mpls_static_labels
                                    
                                    	MPLS static labels
                                    	**type**\: :py:class:`MplsStaticLabels <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels>`
                                    
                                    .. attribute:: source_address
                                    
                                    	Value of the Pseudowire source address. Must be IPv6 only
                                    	**type**\: one of { str | str }
                                    
                                    .. attribute:: tag_impose
                                    
                                    	Tag Impose vlan tagged mode
                                    	**type**\: int
                                    
                                    	**range:** 1..4094
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.neighbor = None
                                        self.backup_pseudowires = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires()
                                        self.backup_pseudowires.parent = self
                                        self.bandwidth = None
                                        self.class_ = None
                                        self.l2tp_static = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStatic()
                                        self.l2tp_static.parent = self
                                        self.l2tp_static_attributes = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes()
                                        self.l2tp_static_attributes.parent = self
                                        self.mpls_static_labels = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels()
                                        self.mpls_static_labels.parent = self
                                        self.source_address = None
                                        self.tag_impose = None


                                    class BackupPseudowires(object):
                                        """
                                        List of pseudowires
                                        
                                        .. attribute:: backup_pseudowire
                                        
                                        	Backup pseudowire for the cross connect
                                        	**type**\: list of :py:class:`BackupPseudowire <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.backup_pseudowire = YList()
                                            self.backup_pseudowire.parent = self
                                            self.backup_pseudowire.name = 'backup_pseudowire'


                                        class BackupPseudowire(object):
                                            """
                                            Backup pseudowire for the cross connect
                                            
                                            .. attribute:: neighbor
                                            
                                            	Neighbor IP address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: pseudowire_id
                                            
                                            	Pseudowire ID
                                            	**type**\: int
                                            
                                            	**range:** 1..4294967295
                                            
                                            .. attribute:: backup_mpls_static_labels
                                            
                                            	MPLS static labels
                                            	**type**\: :py:class:`BackupMplsStaticLabels <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels>`
                                            
                                            .. attribute:: backup_pw_class
                                            
                                            	PW class template name to use for the backup PW
                                            	**type**\: str
                                            
                                            	**range:** 0..32
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.neighbor = None
                                                self.pseudowire_id = None
                                                self.backup_mpls_static_labels = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels()
                                                self.backup_mpls_static_labels.parent = self
                                                self.backup_pw_class = None


                                            class BackupMplsStaticLabels(object):
                                                """
                                                MPLS static labels
                                                
                                                .. attribute:: local_static_label
                                                
                                                	Pseudowire local static label
                                                	**type**\: int
                                                
                                                	**range:** 16..1048575
                                                
                                                .. attribute:: remote_static_label
                                                
                                                	Pseudowire remote static label
                                                	**type**\: int
                                                
                                                	**range:** 16..1048575
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.local_static_label = None
                                                    self.remote_static_label = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-mpls-static-labels'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.is_presence():
                                                        return True
                                                    if self.local_static_label is not None:
                                                        return True

                                                    if self.remote_static_label is not None:
                                                        return True

                                                    return False

                                                def is_presence(self):
                                                    ''' Returns True if this instance represents presence container else returns False '''
                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.neighbor is None:
                                                    raise YPYDataValidationError('Key property neighbor is None')
                                                if self.pseudowire_id is None:
                                                    raise YPYDataValidationError('Key property pseudowire_id is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-pseudowire[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.neighbor is not None:
                                                    return True

                                                if self.pseudowire_id is not None:
                                                    return True

                                                if self.backup_mpls_static_labels is not None and self.backup_mpls_static_labels._has_data():
                                                    return True

                                                if self.backup_mpls_static_labels is not None and self.backup_mpls_static_labels.is_presence():
                                                    return True

                                                if self.backup_pw_class is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires.BackupPseudowire']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-pseudowires'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.backup_pseudowire is not None:
                                                for child_ref in self.backup_pseudowire:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.BackupPseudowires']['meta_info']


                                    class L2tpStatic(object):
                                        """
                                        Pseudowire L2TPv3 static configuration
                                        
                                        .. attribute:: enable
                                        
                                        	Enable pseudowire L2TPv3 static configuration
                                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-static'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.enable is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStatic']['meta_info']


                                    class L2tpStaticAttributes(object):
                                        """
                                        L2TP Static Attributes
                                        
                                        .. attribute:: l2tp_local_cookie
                                        
                                        	L2TP local cookie
                                        	**type**\: :py:class:`L2tpLocalCookie <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes.L2tpLocalCookie>`
                                        
                                        .. attribute:: l2tp_local_session_id
                                        
                                        	L2TP local session ID
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: l2tp_remote_cookie
                                        
                                        	L2TP remote cookie
                                        	**type**\: :py:class:`L2tpRemoteCookie <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes.L2tpRemoteCookie>`
                                        
                                        .. attribute:: l2tp_remote_session_id
                                        
                                        	L2TP remote session ID
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: l2tp_secondary_local_cookie
                                        
                                        	L2TP secondary local cookie
                                        	**type**\: :py:class:`L2tpSecondaryLocalCookie <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes.L2tpSecondaryLocalCookie>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.l2tp_local_cookie = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes.L2tpLocalCookie()
                                            self.l2tp_local_cookie.parent = self
                                            self.l2tp_local_session_id = None
                                            self.l2tp_remote_cookie = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes.L2tpRemoteCookie()
                                            self.l2tp_remote_cookie.parent = self
                                            self.l2tp_remote_session_id = None
                                            self.l2tp_secondary_local_cookie = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes.L2tpSecondaryLocalCookie()
                                            self.l2tp_secondary_local_cookie.parent = self


                                        class L2tpLocalCookie(object):
                                            """
                                            L2TP local cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\: :py:class:`L2tpCookieSize_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-local-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes.L2tpLocalCookie']['meta_info']


                                        class L2tpRemoteCookie(object):
                                            """
                                            L2TP remote cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher remote cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower remote cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Remote cookie size
                                            	**type**\: :py:class:`L2tpCookieSize_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-remote-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes.L2tpRemoteCookie']['meta_info']


                                        class L2tpSecondaryLocalCookie(object):
                                            """
                                            L2TP secondary local cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\: :py:class:`L2tpCookieSize_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-secondary-local-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes.L2tpSecondaryLocalCookie']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-static-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.l2tp_local_cookie is not None and self.l2tp_local_cookie._has_data():
                                                return True

                                            if self.l2tp_local_cookie is not None and self.l2tp_local_cookie.is_presence():
                                                return True

                                            if self.l2tp_local_session_id is not None:
                                                return True

                                            if self.l2tp_remote_cookie is not None and self.l2tp_remote_cookie._has_data():
                                                return True

                                            if self.l2tp_remote_cookie is not None and self.l2tp_remote_cookie.is_presence():
                                                return True

                                            if self.l2tp_remote_session_id is not None:
                                                return True

                                            if self.l2tp_secondary_local_cookie is not None and self.l2tp_secondary_local_cookie._has_data():
                                                return True

                                            if self.l2tp_secondary_local_cookie is not None and self.l2tp_secondary_local_cookie.is_presence():
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.L2tpStaticAttributes']['meta_info']


                                    class MplsStaticLabels(object):
                                        """
                                        MPLS static labels
                                        
                                        .. attribute:: local_static_label
                                        
                                        	Pseudowire local static label
                                        	**type**\: int
                                        
                                        	**range:** 16..1048575
                                        
                                        .. attribute:: remote_static_label
                                        
                                        	Pseudowire remote static label
                                        	**type**\: int
                                        
                                        	**range:** 16..1048575
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.local_static_label = None
                                            self.remote_static_label = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mpls-static-labels'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.local_static_label is not None:
                                                return True

                                            if self.remote_static_label is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor.MplsStaticLabels']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.neighbor is None:
                                            raise YPYDataValidationError('Key property neighbor is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:neighbor[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.neighbor is not None:
                                            return True

                                        if self.backup_pseudowires is not None and self.backup_pseudowires._has_data():
                                            return True

                                        if self.backup_pseudowires is not None and self.backup_pseudowires.is_presence():
                                            return True

                                        if self.bandwidth is not None:
                                            return True

                                        if self.class_ is not None:
                                            return True

                                        if self.l2tp_static is not None and self.l2tp_static._has_data():
                                            return True

                                        if self.l2tp_static is not None and self.l2tp_static.is_presence():
                                            return True

                                        if self.l2tp_static_attributes is not None and self.l2tp_static_attributes._has_data():
                                            return True

                                        if self.l2tp_static_attributes is not None and self.l2tp_static_attributes.is_presence():
                                            return True

                                        if self.mpls_static_labels is not None and self.mpls_static_labels._has_data():
                                            return True

                                        if self.mpls_static_labels is not None and self.mpls_static_labels.is_presence():
                                            return True

                                        if self.source_address is not None:
                                            return True

                                        if self.tag_impose is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.Neighbor']['meta_info']


                                class PseudowireAddress(object):
                                    """
                                    keys\: pseudowire\-address
                                    
                                    .. attribute:: pseudowire_address
                                    
                                    	Pseudowire IPv6 address. A pseudowire can have only one address\: IPv4 or IPv6
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: backup_pseudowires
                                    
                                    	List of pseudowires
                                    	**type**\: :py:class:`BackupPseudowires <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires>`
                                    
                                    .. attribute:: bandwidth
                                    
                                    	Pseudowire Bandwidth
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: class_
                                    
                                    	Name of the pseudowire class
                                    	**type**\: str
                                    
                                    	**range:** 0..32
                                    
                                    .. attribute:: l2tp_static
                                    
                                    	Pseudowire L2TPv3 static configuration
                                    	**type**\: :py:class:`L2tpStatic <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStatic>`
                                    
                                    .. attribute:: l2tp_static_attributes
                                    
                                    	L2TP Static Attributes
                                    	**type**\: :py:class:`L2tpStaticAttributes <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes>`
                                    
                                    .. attribute:: mpls_static_labels
                                    
                                    	MPLS static labels
                                    	**type**\: :py:class:`MplsStaticLabels <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels>`
                                    
                                    .. attribute:: source_address
                                    
                                    	Value of the Pseudowire source address. Must be IPv6 only
                                    	**type**\: one of { str | str }
                                    
                                    .. attribute:: tag_impose
                                    
                                    	Tag Impose vlan tagged mode
                                    	**type**\: int
                                    
                                    	**range:** 1..4094
                                    
                                    

                                    """

                                    _prefix = 'l2vpn-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.pseudowire_address = None
                                        self.backup_pseudowires = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires()
                                        self.backup_pseudowires.parent = self
                                        self.bandwidth = None
                                        self.class_ = None
                                        self.l2tp_static = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStatic()
                                        self.l2tp_static.parent = self
                                        self.l2tp_static_attributes = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes()
                                        self.l2tp_static_attributes.parent = self
                                        self.mpls_static_labels = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels()
                                        self.mpls_static_labels.parent = self
                                        self.source_address = None
                                        self.tag_impose = None


                                    class BackupPseudowires(object):
                                        """
                                        List of pseudowires
                                        
                                        .. attribute:: backup_pseudowire
                                        
                                        	Backup pseudowire for the cross connect
                                        	**type**\: list of :py:class:`BackupPseudowire <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.backup_pseudowire = YList()
                                            self.backup_pseudowire.parent = self
                                            self.backup_pseudowire.name = 'backup_pseudowire'


                                        class BackupPseudowire(object):
                                            """
                                            Backup pseudowire for the cross connect
                                            
                                            .. attribute:: neighbor
                                            
                                            	Neighbor IP address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: pseudowire_id
                                            
                                            	Pseudowire ID
                                            	**type**\: int
                                            
                                            	**range:** 1..4294967295
                                            
                                            .. attribute:: backup_mpls_static_labels
                                            
                                            	MPLS static labels
                                            	**type**\: :py:class:`BackupMplsStaticLabels <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels>`
                                            
                                            .. attribute:: backup_pw_class
                                            
                                            	PW class template name to use for the backup PW
                                            	**type**\: str
                                            
                                            	**range:** 0..32
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.neighbor = None
                                                self.pseudowire_id = None
                                                self.backup_mpls_static_labels = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels()
                                                self.backup_mpls_static_labels.parent = self
                                                self.backup_pw_class = None


                                            class BackupMplsStaticLabels(object):
                                                """
                                                MPLS static labels
                                                
                                                .. attribute:: local_static_label
                                                
                                                	Pseudowire local static label
                                                	**type**\: int
                                                
                                                	**range:** 16..1048575
                                                
                                                .. attribute:: remote_static_label
                                                
                                                	Pseudowire remote static label
                                                	**type**\: int
                                                
                                                	**range:** 16..1048575
                                                
                                                

                                                """

                                                _prefix = 'l2vpn-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.local_static_label = None
                                                    self.remote_static_label = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-mpls-static-labels'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.is_presence():
                                                        return True
                                                    if self.local_static_label is not None:
                                                        return True

                                                    if self.remote_static_label is not None:
                                                        return True

                                                    return False

                                                def is_presence(self):
                                                    ''' Returns True if this instance represents presence container else returns False '''
                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire.BackupMplsStaticLabels']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.neighbor is None:
                                                    raise YPYDataValidationError('Key property neighbor is None')
                                                if self.pseudowire_id is None:
                                                    raise YPYDataValidationError('Key property pseudowire_id is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-pseudowire[Cisco-IOS-XR-l2vpn-cfg:neighbor = ' + str(self.neighbor) + '][Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.neighbor is not None:
                                                    return True

                                                if self.pseudowire_id is not None:
                                                    return True

                                                if self.backup_mpls_static_labels is not None and self.backup_mpls_static_labels._has_data():
                                                    return True

                                                if self.backup_mpls_static_labels is not None and self.backup_mpls_static_labels.is_presence():
                                                    return True

                                                if self.backup_pw_class is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires.BackupPseudowire']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:backup-pseudowires'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.backup_pseudowire is not None:
                                                for child_ref in self.backup_pseudowire:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.BackupPseudowires']['meta_info']


                                    class L2tpStatic(object):
                                        """
                                        Pseudowire L2TPv3 static configuration
                                        
                                        .. attribute:: enable
                                        
                                        	Enable pseudowire L2TPv3 static configuration
                                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.enable = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-static'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.enable is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStatic']['meta_info']


                                    class L2tpStaticAttributes(object):
                                        """
                                        L2TP Static Attributes
                                        
                                        .. attribute:: l2tp_local_cookie
                                        
                                        	L2TP local cookie
                                        	**type**\: :py:class:`L2tpLocalCookie <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes.L2tpLocalCookie>`
                                        
                                        .. attribute:: l2tp_local_session_id
                                        
                                        	L2TP local session ID
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: l2tp_remote_cookie
                                        
                                        	L2TP remote cookie
                                        	**type**\: :py:class:`L2tpRemoteCookie <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes.L2tpRemoteCookie>`
                                        
                                        .. attribute:: l2tp_remote_session_id
                                        
                                        	L2TP remote session ID
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: l2tp_secondary_local_cookie
                                        
                                        	L2TP secondary local cookie
                                        	**type**\: :py:class:`L2tpSecondaryLocalCookie <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes.L2tpSecondaryLocalCookie>`
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.l2tp_local_cookie = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes.L2tpLocalCookie()
                                            self.l2tp_local_cookie.parent = self
                                            self.l2tp_local_session_id = None
                                            self.l2tp_remote_cookie = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes.L2tpRemoteCookie()
                                            self.l2tp_remote_cookie.parent = self
                                            self.l2tp_remote_session_id = None
                                            self.l2tp_secondary_local_cookie = L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes.L2tpSecondaryLocalCookie()
                                            self.l2tp_secondary_local_cookie.parent = self


                                        class L2tpLocalCookie(object):
                                            """
                                            L2TP local cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\: :py:class:`L2tpCookieSize_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-local-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes.L2tpLocalCookie']['meta_info']


                                        class L2tpRemoteCookie(object):
                                            """
                                            L2TP remote cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher remote cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower remote cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Remote cookie size
                                            	**type**\: :py:class:`L2tpCookieSize_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-remote-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes.L2tpRemoteCookie']['meta_info']


                                        class L2tpSecondaryLocalCookie(object):
                                            """
                                            L2TP secondary local cookie
                                            
                                            .. attribute:: higher_value
                                            
                                            	Higher local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: lower_value
                                            
                                            	Lower local cookie value
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: size
                                            
                                            	Local cookie size
                                            	**type**\: :py:class:`L2tpCookieSize_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2tpCookieSize_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'l2vpn-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.higher_value = None
                                                self.lower_value = None
                                                self.size = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-secondary-local-cookie'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.higher_value is not None:
                                                    return True

                                                if self.lower_value is not None:
                                                    return True

                                                if self.size is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes.L2tpSecondaryLocalCookie']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:l2tp-static-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.l2tp_local_cookie is not None and self.l2tp_local_cookie._has_data():
                                                return True

                                            if self.l2tp_local_cookie is not None and self.l2tp_local_cookie.is_presence():
                                                return True

                                            if self.l2tp_local_session_id is not None:
                                                return True

                                            if self.l2tp_remote_cookie is not None and self.l2tp_remote_cookie._has_data():
                                                return True

                                            if self.l2tp_remote_cookie is not None and self.l2tp_remote_cookie.is_presence():
                                                return True

                                            if self.l2tp_remote_session_id is not None:
                                                return True

                                            if self.l2tp_secondary_local_cookie is not None and self.l2tp_secondary_local_cookie._has_data():
                                                return True

                                            if self.l2tp_secondary_local_cookie is not None and self.l2tp_secondary_local_cookie.is_presence():
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.L2tpStaticAttributes']['meta_info']


                                    class MplsStaticLabels(object):
                                        """
                                        MPLS static labels
                                        
                                        .. attribute:: local_static_label
                                        
                                        	Pseudowire local static label
                                        	**type**\: int
                                        
                                        	**range:** 16..1048575
                                        
                                        .. attribute:: remote_static_label
                                        
                                        	Pseudowire remote static label
                                        	**type**\: int
                                        
                                        	**range:** 16..1048575
                                        
                                        

                                        """

                                        _prefix = 'l2vpn-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.local_static_label = None
                                            self.remote_static_label = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:mpls-static-labels'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.local_static_label is not None:
                                                return True

                                            if self.remote_static_label is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress.MplsStaticLabels']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.pseudowire_address is None:
                                            raise YPYDataValidationError('Key property pseudowire_address is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire-address[Cisco-IOS-XR-l2vpn-cfg:pseudowire-address = ' + str(self.pseudowire_address) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.pseudowire_address is not None:
                                            return True

                                        if self.backup_pseudowires is not None and self.backup_pseudowires._has_data():
                                            return True

                                        if self.backup_pseudowires is not None and self.backup_pseudowires.is_presence():
                                            return True

                                        if self.bandwidth is not None:
                                            return True

                                        if self.class_ is not None:
                                            return True

                                        if self.l2tp_static is not None and self.l2tp_static._has_data():
                                            return True

                                        if self.l2tp_static is not None and self.l2tp_static.is_presence():
                                            return True

                                        if self.l2tp_static_attributes is not None and self.l2tp_static_attributes._has_data():
                                            return True

                                        if self.l2tp_static_attributes is not None and self.l2tp_static_attributes.is_presence():
                                            return True

                                        if self.mpls_static_labels is not None and self.mpls_static_labels._has_data():
                                            return True

                                        if self.mpls_static_labels is not None and self.mpls_static_labels.is_presence():
                                            return True

                                        if self.source_address is not None:
                                            return True

                                        if self.tag_impose is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                        return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire.PseudowireAddress']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.pseudowire_id is None:
                                        raise YPYDataValidationError('Key property pseudowire_id is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowire[Cisco-IOS-XR-l2vpn-cfg:pseudowire-id = ' + str(self.pseudowire_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.pseudowire_id is not None:
                                        return True

                                    if self.neighbor is not None:
                                        for child_ref in self.neighbor:
                                            if child_ref._has_data():
                                                return True

                                    if self.pseudowire_address is not None:
                                        for child_ref in self.pseudowire_address:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires.Pseudowire']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:pseudowires'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.pseudowire is not None:
                                    for child_ref in self.pseudowire:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                                return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect.Pseudowires']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYDataValidationError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:p2p-xconnect[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.name is not None:
                                return True

                            if self.attachment_circuits is not None and self.attachment_circuits._has_data():
                                return True

                            if self.attachment_circuits is not None and self.attachment_circuits.is_presence():
                                return True

                            if self.backup_attachment_circuits is not None and self.backup_attachment_circuits._has_data():
                                return True

                            if self.backup_attachment_circuits is not None and self.backup_attachment_circuits.is_presence():
                                return True

                            if self.interworking is not None:
                                return True

                            if self.monitor_sessions is not None and self.monitor_sessions._has_data():
                                return True

                            if self.monitor_sessions is not None and self.monitor_sessions.is_presence():
                                return True

                            if self.p2p_description is not None:
                                return True

                            if self.pseudowire_evpns is not None and self.pseudowire_evpns._has_data():
                                return True

                            if self.pseudowire_evpns is not None and self.pseudowire_evpns.is_presence():
                                return True

                            if self.pseudowire_routeds is not None and self.pseudowire_routeds._has_data():
                                return True

                            if self.pseudowire_routeds is not None and self.pseudowire_routeds.is_presence():
                                return True

                            if self.pseudowires is not None and self.pseudowires._has_data():
                                return True

                            if self.pseudowires is not None and self.pseudowires.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                            return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects.P2pXconnect']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-l2vpn-cfg:p2p-xconnects'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.p2p_xconnect is not None:
                            for child_ref in self.p2p_xconnect:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup.P2pXconnects']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:xconnect-groups/Cisco-IOS-XR-l2vpn-cfg:xconnect-group[Cisco-IOS-XR-l2vpn-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.name is not None:
                        return True

                    if self.mp2mp_xconnects is not None and self.mp2mp_xconnects._has_data():
                        return True

                    if self.mp2mp_xconnects is not None and self.mp2mp_xconnects.is_presence():
                        return True

                    if self.p2p_xconnects is not None and self.p2p_xconnects._has_data():
                        return True

                    if self.p2p_xconnects is not None and self.p2p_xconnects.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2vpn.Database.XconnectGroups.XconnectGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database/Cisco-IOS-XR-l2vpn-cfg:xconnect-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.xconnect_group is not None:
                    for child_ref in self.xconnect_group:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2vpn.Database.XconnectGroups']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:database'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.bridge_domain_groups is not None and self.bridge_domain_groups._has_data():
                return True

            if self.bridge_domain_groups is not None and self.bridge_domain_groups.is_presence():
                return True

            if self.g8032_rings is not None and self.g8032_rings._has_data():
                return True

            if self.g8032_rings is not None and self.g8032_rings.is_presence():
                return True

            if self.pseudowire_classes is not None and self.pseudowire_classes._has_data():
                return True

            if self.pseudowire_classes is not None and self.pseudowire_classes.is_presence():
                return True

            if self.redundancy is not None and self.redundancy._has_data():
                return True

            if self.redundancy is not None and self.redundancy.is_presence():
                return True

            if self.xconnect_groups is not None and self.xconnect_groups._has_data():
                return True

            if self.xconnect_groups is not None and self.xconnect_groups.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2vpn.Database']['meta_info']


    class Neighbor(object):
        """
        L2VPN neighbor submode
        
        .. attribute:: ldp_flap
        
        	Enable targetted LDP session flap action
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.ldp_flap = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:neighbor'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ldp_flap is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2vpn.Neighbor']['meta_info']


    class Pbb(object):
        """
        L2VPN PBB Global
        
        .. attribute:: backbone_source_mac
        
        	Backbone Source MAC
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.backbone_source_mac = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:pbb'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.backbone_source_mac is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2vpn.Pbb']['meta_info']


    class PwRouting(object):
        """
        Pseudowire\-routing attributes
        
        .. attribute:: pw_routing_bgp
        
        	Enable Autodiscovery BGP Pseudowire\-routing BGP
        	**type**\: :py:class:`PwRoutingBgp <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.PwRouting.PwRoutingBgp>`
        
        .. attribute:: pw_routing_global_id
        
        	Pseudowire\-routing Global ID
        	**type**\: int
        
        	**range:** 1..4294967295
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.pw_routing_bgp = L2vpn.PwRouting.PwRoutingBgp()
            self.pw_routing_bgp.parent = self
            self.pw_routing_global_id = None


        class PwRoutingBgp(object):
            """
            Enable Autodiscovery BGP Pseudowire\-routing BGP
            
            .. attribute:: enable
            
            	Enable Autodiscovery BGP
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: evpn_route_distinguisher
            
            	Route Distinguisher
            	**type**\: :py:class:`EvpnRouteDistinguisher <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.evpn_route_distinguisher = L2vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher()
                self.evpn_route_distinguisher.parent = self


            class EvpnRouteDistinguisher(object):
                """
                Route Distinguisher
                
                .. attribute:: addr_index
                
                	Addr index
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: address
                
                	IPV4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: as_
                
                	Two byte or 4 byte AS number
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: as_index
                
                	AS\:nn (hex or decimal format)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Router Distinguisher Type
                	**type**\: :py:class:`BgpRouteDistinguisher_Enum <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.BgpRouteDistinguisher_Enum>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.addr_index = None
                    self.address = None
                    self.as_ = None
                    self.as_index = None
                    self.type = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:pw-routing/Cisco-IOS-XR-l2vpn-cfg:pw-routing-bgp/Cisco-IOS-XR-l2vpn-cfg:evpn-route-distinguisher'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.addr_index is not None:
                        return True

                    if self.address is not None:
                        return True

                    if self.as_ is not None:
                        return True

                    if self.as_index is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2vpn.PwRouting.PwRoutingBgp.EvpnRouteDistinguisher']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:pw-routing/Cisco-IOS-XR-l2vpn-cfg:pw-routing-bgp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.enable is not None:
                    return True

                if self.evpn_route_distinguisher is not None and self.evpn_route_distinguisher._has_data():
                    return True

                if self.evpn_route_distinguisher is not None and self.evpn_route_distinguisher.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2vpn.PwRouting.PwRoutingBgp']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:pw-routing'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.pw_routing_bgp is not None and self.pw_routing_bgp._has_data():
                return True

            if self.pw_routing_bgp is not None and self.pw_routing_bgp.is_presence():
                return True

            if self.pw_routing_global_id is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2vpn.PwRouting']['meta_info']


    class Snmp(object):
        """
        SNMP related configuration
        
        .. attribute:: mib
        
        	MIB related configuration
        	**type**\: :py:class:`Mib <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Snmp.Mib>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.mib = L2vpn.Snmp.Mib()
            self.mib.parent = self


        class Mib(object):
            """
            MIB related configuration
            
            .. attribute:: mib_interface
            
            	Interface related configuration for MIB
            	**type**\: :py:class:`MibInterface <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Snmp.Mib.MibInterface>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.mib_interface = L2vpn.Snmp.Mib.MibInterface()
                self.mib_interface.parent = self


            class MibInterface(object):
                """
                Interface related configuration for MIB
                
                .. attribute:: format
                
                	MIB interface name output format
                	**type**\: :py:class:`Format <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Snmp.Mib.MibInterface.Format>`
                
                

                """

                _prefix = 'l2vpn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.format = L2vpn.Snmp.Mib.MibInterface.Format()
                    self.format.parent = self


                class Format(object):
                    """
                    MIB interface name output format
                    
                    .. attribute:: external_interface_format
                    
                    	Set MIB interface name output in slash format (/)
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'l2vpn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.external_interface_format = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:snmp/Cisco-IOS-XR-l2vpn-cfg:mib/Cisco-IOS-XR-l2vpn-cfg:mib-interface/Cisco-IOS-XR-l2vpn-cfg:format'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.external_interface_format is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                        return meta._meta_table['L2vpn.Snmp.Mib.MibInterface.Format']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:snmp/Cisco-IOS-XR-l2vpn-cfg:mib/Cisco-IOS-XR-l2vpn-cfg:mib-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.format is not None and self.format._has_data():
                        return True

                    if self.format is not None and self.format.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                    return meta._meta_table['L2vpn.Snmp.Mib.MibInterface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:snmp/Cisco-IOS-XR-l2vpn-cfg:mib'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.mib_interface is not None and self.mib_interface._has_data():
                    return True

                if self.mib_interface is not None and self.mib_interface.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2vpn.Snmp.Mib']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:snmp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.mib is not None and self.mib._has_data():
                return True

            if self.mib is not None and self.mib.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2vpn.Snmp']['meta_info']


    class Utility(object):
        """
        L2VPN utilities
        
        .. attribute:: logging
        
        	L2VPN logging utility
        	**type**\: :py:class:`Logging <ydk.models.l2vpn.Cisco_IOS_XR_l2vpn_cfg.L2vpn.Utility.Logging>`
        
        

        """

        _prefix = 'l2vpn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.logging = L2vpn.Utility.Logging()
            self.logging.parent = self


        class Logging(object):
            """
            L2VPN logging utility
            
            .. attribute:: bridge_domain_state_change
            
            	Enable Bridge Domain state change logging
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: nsr_state_change
            
            	Enable Non Stop Routing state change logging
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: pseudowire_state_change
            
            	Enable pseudowire state change logging
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: pwhe_replication_state_change
            
            	Enable PW\-HE Replication state change logging
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: vfi
            
            	Enable VFI state change logging
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'l2vpn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bridge_domain_state_change = None
                self.nsr_state_change = None
                self.pseudowire_state_change = None
                self.pwhe_replication_state_change = None
                self.vfi = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:utility/Cisco-IOS-XR-l2vpn-cfg:logging'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.bridge_domain_state_change is not None:
                    return True

                if self.nsr_state_change is not None:
                    return True

                if self.pseudowire_state_change is not None:
                    return True

                if self.pwhe_replication_state_change is not None:
                    return True

                if self.vfi is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
                return meta._meta_table['L2vpn.Utility.Logging']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn/Cisco-IOS-XR-l2vpn-cfg:utility'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.logging is not None and self.logging._has_data():
                return True

            if self.logging is not None and self.logging.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
            return meta._meta_table['L2vpn.Utility']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-l2vpn-cfg:l2vpn'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.auto_discovery is not None and self.auto_discovery._has_data():
            return True

        if self.auto_discovery is not None and self.auto_discovery.is_presence():
            return True

        if self.capability is not None:
            return True

        if self.database is not None and self.database._has_data():
            return True

        if self.database is not None and self.database.is_presence():
            return True

        if self.enable is not None:
            return True

        if self.l2vpn_router_id is not None:
            return True

        if self.load_balance is not None:
            return True

        if self.mspw_description is not None:
            return True

        if self.mtu_mismatch_ignore is not None:
            return True

        if self.neighbor is not None and self.neighbor._has_data():
            return True

        if self.neighbor is not None and self.neighbor.is_presence():
            return True

        if self.nsr is not None:
            return True

        if self.pbb is not None and self.pbb._has_data():
            return True

        if self.pbb is not None and self.pbb.is_presence():
            return True

        if self.pw_grouping is not None:
            return True

        if self.pw_routing is not None and self.pw_routing._has_data():
            return True

        if self.pw_routing is not None and self.pw_routing.is_presence():
            return True

        if self.pw_status_disable is not None:
            return True

        if self.pwoam_refresh is not None:
            return True

        if self.snmp is not None and self.snmp._has_data():
            return True

        if self.snmp is not None and self.snmp.is_presence():
            return True

        if self.tcn_propagation is not None:
            return True

        if self.utility is not None and self.utility._has_data():
            return True

        if self.utility is not None and self.utility.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.l2vpn._meta import _Cisco_IOS_XR_l2vpn_cfg as meta
        return meta._meta_table['L2vpn']['meta_info']


