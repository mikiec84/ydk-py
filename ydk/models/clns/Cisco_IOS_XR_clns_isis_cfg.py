""" Cisco_IOS_XR_clns_isis_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR clns\-isis package configuration.

This module contains definitions
for the following management objects\:
  isis\: IS\-IS configuration for all instances

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes import IsisAddressFamily_Enum
from ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes import IsisInternalLevel_Enum
from ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes import IsisSubAddressFamily_Enum

class IsisAdjCheck_Enum(Enum):
    """
    IsisAdjCheck_Enum

    Isis adj check

    """

    """

    Disabled

    """
    DISABLED = 0


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAdjCheck_Enum']


class IsisAdvTypeExternal_Enum(Enum):
    """
    IsisAdvTypeExternal_Enum

    Isis adv type external

    """

    """

    External

    """
    EXTERNAL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAdvTypeExternal_Enum']


class IsisAdvTypeInterLevel_Enum(Enum):
    """
    IsisAdvTypeInterLevel_Enum

    Isis adv type inter level

    """

    """

    InterLevel

    """
    INTER_LEVEL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAdvTypeInterLevel_Enum']


class IsisApplyWeight_Enum(Enum):
    """
    IsisApplyWeight_Enum

    Isis apply weight

    """

    """

    Apply weight to ECMP prefixes

    """
    ECMP_ONLY = 1

    """

    Apply weight to UCMP prefixes

    """
    UCMP_ONLY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisApplyWeight_Enum']


class IsisAttachedBit_Enum(Enum):
    """
    IsisAttachedBit_Enum

    Isis attached bit

    """

    """

    Computed from the attached areas

    """
    AREA = 0

    """

    Forced ON

    """
    ON = 1

    """

    Forced OFF

    """
    OFF = 2


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAttachedBit_Enum']


class IsisAuthenticationAlgorithm_Enum(Enum):
    """
    IsisAuthenticationAlgorithm_Enum

    Isis authentication algorithm

    """

    """

    Cleartext password

    """
    CLEARTEXT = 1

    """

    HMAC\-MD5 checksum

    """
    HMAC_MD5 = 2

    """

    Key Chain authentication

    """
    KEYCHAIN = 3


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAuthenticationAlgorithm_Enum']


class IsisAuthenticationFailureMode_Enum(Enum):
    """
    IsisAuthenticationFailureMode_Enum

    Isis authentication failure mode

    """

    """

    Drop non\-authenticating PDUs

    """
    DROP = 0

    """

    Accept non\-authenticating PDUs

    """
    SEND_ONLY = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisAuthenticationFailureMode_Enum']


class IsisConfigurableLevels_Enum(Enum):
    """
    IsisConfigurableLevels_Enum

    Isis configurable levels

    """

    """

    Level1

    """
    LEVEL1 = 1

    """

    Level2

    """
    LEVEL2 = 2

    """

    Both Levels

    """
    LEVEL1_AND2 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisConfigurableLevels_Enum']


class IsisHelloPadding_Enum(Enum):
    """
    IsisHelloPadding_Enum

    Isis hello padding

    """

    """

    Never pad Hellos

    """
    NEVER = 0

    """

    Pad Hellos during adjacency formation only

    """
    SOMETIMES = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisHelloPadding_Enum']


class IsisInterfaceAfState_Enum(Enum):
    """
    IsisInterfaceAfState_Enum

    Isis interface af state

    """

    """

    Disable

    """
    DISABLE = 0


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisInterfaceAfState_Enum']


class IsisInterfaceState_Enum(Enum):
    """
    IsisInterfaceState_Enum

    Isis interface state

    """

    """

    Shutdown

    """
    SHUTDOWN = 0

    """

    Suppressed

    """
    SUPPRESSED = 1

    """

    Passive

    """
    PASSIVE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisInterfaceState_Enum']


class IsisLabelPreference_Enum(Enum):
    """
    IsisLabelPreference_Enum

    Isis label preference

    """

    """

    Label Distribution Protocol

    """
    LDP = 0

    """

    Segment Routing

    """
    SEGMENT_ROUTING = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisLabelPreference_Enum']


class IsisMetricStyleTransition_Enum(Enum):
    """
    IsisMetricStyleTransition_Enum

    Isis metric style transition

    """

    """

    Disabled

    """
    DISABLED = 0

    """

    Enabled

    """
    ENABLED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMetricStyleTransition_Enum']


class IsisMetricStyle_Enum(Enum):
    """
    IsisMetricStyle_Enum

    Isis metric style

    """

    """

    ISO 10589 metric style (old\-style)

    """
    OLD_METRIC_STYLE = 0

    """

    32\-bit metric style (new\-style)

    """
    NEW_METRIC_STYLE = 1

    """

    Both forms of metric style

    """
    BOTH_METRIC_STYLE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMetricStyle_Enum']


class IsisMetric_Enum(Enum):
    """
    IsisMetric_Enum

    Isis metric

    """

    """

    Internal metric

    """
    INTERNAL = 0

    """

    External metric

    """
    EXTERNAL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMetric_Enum']


class IsisMibAdjacencyChangeBoolean_Enum(Enum):
    """
    IsisMibAdjacencyChangeBoolean_Enum

    Isis mib adjacency change boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 17


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAdjacencyChangeBoolean_Enum']


class IsisMibAllBoolean_Enum(Enum):
    """
    IsisMibAllBoolean_Enum

    Isis mib all boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 19


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAllBoolean_Enum']


class IsisMibAreaMismatchBoolean_Enum(Enum):
    """
    IsisMibAreaMismatchBoolean_Enum

    Isis mib area mismatch boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 12


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAreaMismatchBoolean_Enum']


class IsisMibAttemptToExceedMaxSequenceBoolean_Enum(Enum):
    """
    IsisMibAttemptToExceedMaxSequenceBoolean_Enum

    Isis mib attempt to exceed max sequence boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 4


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAttemptToExceedMaxSequenceBoolean_Enum']


class IsisMibAuthenticationFailureBoolean_Enum(Enum):
    """
    IsisMibAuthenticationFailureBoolean_Enum

    Isis mib authentication failure boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 10


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAuthenticationFailureBoolean_Enum']


class IsisMibAuthenticationTypeFailureBoolean_Enum(Enum):
    """
    IsisMibAuthenticationTypeFailureBoolean_Enum

    Isis mib authentication type failure boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 9


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibAuthenticationTypeFailureBoolean_Enum']


class IsisMibCorruptedLspDetectedBoolean_Enum(Enum):
    """
    IsisMibCorruptedLspDetectedBoolean_Enum

    Isis mib corrupted lsp detected boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibCorruptedLspDetectedBoolean_Enum']


class IsisMibDatabaseOverFlowBoolean_Enum(Enum):
    """
    IsisMibDatabaseOverFlowBoolean_Enum

    Isis mib database over flow boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibDatabaseOverFlowBoolean_Enum']


class IsisMibIdLengthMismatchBoolean_Enum(Enum):
    """
    IsisMibIdLengthMismatchBoolean_Enum

    Isis mib id length mismatch boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 5


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibIdLengthMismatchBoolean_Enum']


class IsisMibLspErrorDetectedBoolean_Enum(Enum):
    """
    IsisMibLspErrorDetectedBoolean_Enum

    Isis mib lsp error detected boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 18


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibLspErrorDetectedBoolean_Enum']


class IsisMibLspTooLargeToPropagateBoolean_Enum(Enum):
    """
    IsisMibLspTooLargeToPropagateBoolean_Enum

    Isis mib lsp too large to propagate boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 14


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibLspTooLargeToPropagateBoolean_Enum']


class IsisMibManualAddressDropsBoolean_Enum(Enum):
    """
    IsisMibManualAddressDropsBoolean_Enum

    Isis mib manual address drops boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibManualAddressDropsBoolean_Enum']


class IsisMibMaxAreaAddressMismatchBoolean_Enum(Enum):
    """
    IsisMibMaxAreaAddressMismatchBoolean_Enum

    Isis mib max area address mismatch boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 6


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibMaxAreaAddressMismatchBoolean_Enum']


class IsisMibOriginatedLspBufferSizeMismatchBoolean_Enum(Enum):
    """
    IsisMibOriginatedLspBufferSizeMismatchBoolean_Enum

    Isis mib originated lsp buffer size mismatch
    boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 15


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibOriginatedLspBufferSizeMismatchBoolean_Enum']


class IsisMibOwnLspPurgeBoolean_Enum(Enum):
    """
    IsisMibOwnLspPurgeBoolean_Enum

    Isis mib own lsp purge boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 7


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibOwnLspPurgeBoolean_Enum']


class IsisMibProtocolsSupportedMismatchBoolean_Enum(Enum):
    """
    IsisMibProtocolsSupportedMismatchBoolean_Enum

    Isis mib protocols supported mismatch boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 16


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibProtocolsSupportedMismatchBoolean_Enum']


class IsisMibRejectedAdjacencyBoolean_Enum(Enum):
    """
    IsisMibRejectedAdjacencyBoolean_Enum

    Isis mib rejected adjacency boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 13


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibRejectedAdjacencyBoolean_Enum']


class IsisMibSequenceNumberSkipBoolean_Enum(Enum):
    """
    IsisMibSequenceNumberSkipBoolean_Enum

    Isis mib sequence number skip boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 8


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibSequenceNumberSkipBoolean_Enum']


class IsisMibVersionSkewBoolean_Enum(Enum):
    """
    IsisMibVersionSkewBoolean_Enum

    Isis mib version skew boolean

    """

    """

    Disable

    """
    FALSE = 0

    """

    Enable

    """
    TRUE = 11


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMibVersionSkewBoolean_Enum']


class IsisMicroLoopAvoidance_Enum(Enum):
    """
    IsisMicroLoopAvoidance_Enum

    Isis micro loop avoidance

    """

    """

    No Avoidance type set

    """
    NOT_SET = 0

    """

    Provide mirco loop avoidance for all prefixes

    """
    MICRO_LOOP_AVOIDANCE_ALL = 1

    """

    Provide mirco loop avoidance only for protected
    prefixes

    """
    MICRO_LOOP_AVOIDANCE_PROTECTED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisMicroLoopAvoidance_Enum']


class IsisNsfFlavor_Enum(Enum):
    """
    IsisNsfFlavor_Enum

    Isis nsf flavor

    """

    """

    Cisco proprietary NSF

    """
    CISCO_PROPRIETARY_NSF = 1

    """

    IETF standard NSF

    """
    IETF_STANDARD_NSF = 2


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisNsfFlavor_Enum']


class IsisOverloadBitMode_Enum(Enum):
    """
    IsisOverloadBitMode_Enum

    Isis overload bit mode

    """

    """

    Set always

    """
    PERMANENTLY_SET = 1

    """

    Set during the startup period

    """
    STARTUP_PERIOD = 2

    """

    Set until BGP comverges

    """
    WAIT_FOR_BGP = 3


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisOverloadBitMode_Enum']


class IsisPrefixPriority_Enum(Enum):
    """
    IsisPrefixPriority_Enum

    Isis prefix priority

    """

    """

    Critical prefix priority

    """
    CRITICAL_PRIORITY = 0

    """

    High prefix priority

    """
    HIGH_PRIORITY = 1

    """

    Medium prefix priority

    """
    MEDIUM_PRIORITY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisPrefixPriority_Enum']


class IsisRedistProto_Enum(Enum):
    """
    IsisRedistProto_Enum

    Isis redist proto

    """

    """

    Connected

    """
    CONNECTED = 0

    """

    Static

    """
    STATIC = 1

    """

    OSPF

    """
    OSPF = 2

    """

    BGP

    """
    BGP = 3

    """

    ISIS

    """
    ISIS = 4

    """

    OSPFv3

    """
    OSPFV3 = 5

    """

    RIP

    """
    RIP = 6

    """

    EIGRP

    """
    EIGRP = 7

    """

    Subscriber

    """
    SUBSCRIBER = 8

    """

    Application

    """
    APPLICATION = 9

    """

    Mobile

    """
    MOBILE = 10


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisRedistProto_Enum']


class IsisRemoteLfa_Enum(Enum):
    """
    IsisRemoteLfa_Enum

    Isis remote lfa

    """

    """

    No remote LFA option set

    """
    REMOTE_LFA_NONE = 0

    """

    Construct remote LFA tunnel using MPLS LDP

    """
    REMOTE_LFA_TUNNEL_LDP = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisRemoteLfa_Enum']


class IsisSnpAuth_Enum(Enum):
    """
    IsisSnpAuth_Enum

    Isis snp auth

    """

    """

    Authenticate SNP send only

    """
    SEND_ONLY = 0

    """

    Authenticate SNP send and recv

    """
    FULL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisSnpAuth_Enum']


class IsisexplicitNullFlag_Enum(Enum):
    """
    IsisexplicitNullFlag_Enum

    Isisexplicit null flag

    """

    """

    Disable EXPLICITNULL

    """
    DISABLE = 0

    """

    Enable EXPLICITNULL

    """
    ENABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisexplicitNullFlag_Enum']


class IsisfrrLoadSharing_Enum(Enum):
    """
    IsisfrrLoadSharing_Enum

    Isisfrr load sharing

    """

    """

    Disable load sharing of prefixes across
    multiple backups

    """
    DISABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisfrrLoadSharing_Enum']


class IsisfrrTiebreaker_Enum(Enum):
    """
    IsisfrrTiebreaker_Enum

    Isisfrr tiebreaker

    """

    """

    Prefer backup path via downstream node

    """
    DOWNSTREAM = 0

    """

    Prefer line card disjoint backup path

    """
    LC_DISJOINT = 1

    """

    Prefer backup path with lowest total metric

    """
    LOWEST_BACKUP_METRIC = 2

    """

    Prefer node protecting backup path

    """
    NODE_PROTECTING = 3

    """

    Prefer backup path from ECMP set

    """
    PRIMARY_PATH = 4

    """

    Prefer non\-ECMP backup path

    """
    SECONDARY_PATH = 5

    """

    Prefer SRLG disjoint backup path

    """
    SRLG_DISJOINT = 6


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisfrrTiebreaker_Enum']


class Isisfrr_Enum(Enum):
    """
    Isisfrr_Enum

    Isisfrr

    """

    """

    Prefix independent per\-link computation

    """
    PER_LINK = 1

    """

    Prefix dependent computation

    """
    PER_PREFIX = 2


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['Isisfrr_Enum']


class IsisispfState_Enum(Enum):
    """
    IsisispfState_Enum

    Isisispf state

    """

    """

    Enabled

    """
    ENABLED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisispfState_Enum']


class IsisphpFlag_Enum(Enum):
    """
    IsisphpFlag_Enum

    Isisphp flag

    """

    """

    Enable PHP

    """
    ENABLE = 0

    """

    Disable PHP

    """
    DISABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['IsisphpFlag_Enum']


class Isissid_Enum(Enum):
    """
    Isissid_Enum

    Isissid

    """

    """

    SID as an index

    """
    INDEX = 1

    """

    SID as an absolute label

    """
    ABSOLUTE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['Isissid_Enum']


class NflagClear_Enum(Enum):
    """
    NflagClear_Enum

    Nflag clear

    """

    """

    Disable N\-flag\-clear

    """
    DISABLE = 0

    """

    Enable N\-flag\-clear

    """
    ENABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['NflagClear_Enum']



class Isis(object):
    """
    IS\-IS configuration for all instances
    
    .. attribute:: instances
    
    	IS\-IS instance configuration
    	**type**\: :py:class:`Instances <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances>`
    
    

    """

    _prefix = 'clns-isis-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.instances = Isis.Instances()
        self.instances.parent = self


    class Instances(object):
        """
        IS\-IS instance configuration
        
        .. attribute:: instance
        
        	Configuration for a single IS\-IS instance
        	**type**\: list of :py:class:`Instance <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance>`
        
        

        """

        _prefix = 'clns-isis-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.instance = YList()
            self.instance.parent = self
            self.instance.name = 'instance'


        class Instance(object):
            """
            Configuration for a single IS\-IS instance
            
            .. attribute:: instance_name
            
            	Instance identifier
            	**type**\: str
            
            	**range:** 0..40
            
            .. attribute:: afs
            
            	Per\-address\-family configuration
            	**type**\: :py:class:`Afs <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs>`
            
            .. attribute:: distribute
            
            	IS\-IS Distribute BGP\-LS configuration
            	**type**\: :py:class:`Distribute <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Distribute>`
            
            .. attribute:: dynamic_host_name
            
            	If TRUE, dynamic hostname resolution is disabled, and system IDs will always be displayed by show and debug output
            	**type**\: bool
            
            .. attribute:: ignore_lsp_errors
            
            	If TRUE, LSPs recieved with bad checksums will result in the purging of that LSP from the LSP DB. If FALSE or not set, the received LSP will just be ignored
            	**type**\: bool
            
            .. attribute:: interfaces
            
            	Per\-interface configuration
            	**type**\: :py:class:`Interfaces <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces>`
            
            .. attribute:: is_type
            
            	IS type of the IS\-IS process
            	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
            
            .. attribute:: link_groups
            
            	Link Group
            	**type**\: :py:class:`LinkGroups <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LinkGroups>`
            
            .. attribute:: log_adjacency_changes
            
            	Log changes in adjacency state
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: log_pdu_drops
            
            	Log PDU drops
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: lsp_accept_passwords
            
            	LSP/SNP accept password configuration
            	**type**\: :py:class:`LspAcceptPasswords <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspAcceptPasswords>`
            
            .. attribute:: lsp_arrival_times
            
            	LSP arrival time configuration
            	**type**\: :py:class:`LspArrivalTimes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspArrivalTimes>`
            
            .. attribute:: lsp_check_intervals
            
            	LSP checksum check interval configuration
            	**type**\: :py:class:`LspCheckIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspCheckIntervals>`
            
            .. attribute:: lsp_generation_intervals
            
            	LSP generation\-interval configuration
            	**type**\: :py:class:`LspGenerationIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspGenerationIntervals>`
            
            .. attribute:: lsp_lifetimes
            
            	LSP lifetime configuration
            	**type**\: :py:class:`LspLifetimes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspLifetimes>`
            
            .. attribute:: lsp_mtus
            
            	LSP MTU configuration
            	**type**\: :py:class:`LspMtus <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspMtus>`
            
            .. attribute:: lsp_passwords
            
            	LSP/SNP password configuration
            	**type**\: :py:class:`LspPasswords <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspPasswords>`
            
            .. attribute:: lsp_refresh_intervals
            
            	LSP refresh\-interval configuration
            	**type**\: :py:class:`LspRefreshIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspRefreshIntervals>`
            
            .. attribute:: max_link_metrics
            
            	Max Link Metric configuration
            	**type**\: :py:class:`MaxLinkMetrics <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.MaxLinkMetrics>`
            
            .. attribute:: nets
            
            	NET configuration
            	**type**\: :py:class:`Nets <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nets>`
            
            .. attribute:: nsf
            
            	IS\-IS NSF configuration
            	**type**\: :py:class:`Nsf <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nsf>`
            
            .. attribute:: nsr
            
            	IS\-IS NSR configuration
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: overload_bits
            
            	LSP overload\-bit configuration
            	**type**\: :py:class:`OverloadBits <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.OverloadBits>`
            
            .. attribute:: running
            
            	Flag to indicate that instance should be running.  This must be the first object created when an IS\-IS instance is configured, and the last object deleted when it is deconfigured.  When this object is deleted, the IS\-IS instance will exit
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: srgb
            
            	Segment Routing Global Block configuration
            	**type**\: :py:class:`Srgb <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Srgb>`
            
            .. attribute:: trace_buffer_size
            
            	Trace buffer size configuration
            	**type**\: :py:class:`TraceBufferSize <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.TraceBufferSize>`
            
            

            """

            _prefix = 'clns-isis-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.instance_name = None
                self.afs = Isis.Instances.Instance.Afs()
                self.afs.parent = self
                self.distribute = None
                self.dynamic_host_name = None
                self.ignore_lsp_errors = None
                self.interfaces = Isis.Instances.Instance.Interfaces()
                self.interfaces.parent = self
                self.is_type = None
                self.link_groups = Isis.Instances.Instance.LinkGroups()
                self.link_groups.parent = self
                self.log_adjacency_changes = None
                self.log_pdu_drops = None
                self.lsp_accept_passwords = Isis.Instances.Instance.LspAcceptPasswords()
                self.lsp_accept_passwords.parent = self
                self.lsp_arrival_times = Isis.Instances.Instance.LspArrivalTimes()
                self.lsp_arrival_times.parent = self
                self.lsp_check_intervals = Isis.Instances.Instance.LspCheckIntervals()
                self.lsp_check_intervals.parent = self
                self.lsp_generation_intervals = Isis.Instances.Instance.LspGenerationIntervals()
                self.lsp_generation_intervals.parent = self
                self.lsp_lifetimes = Isis.Instances.Instance.LspLifetimes()
                self.lsp_lifetimes.parent = self
                self.lsp_mtus = Isis.Instances.Instance.LspMtus()
                self.lsp_mtus.parent = self
                self.lsp_passwords = Isis.Instances.Instance.LspPasswords()
                self.lsp_passwords.parent = self
                self.lsp_refresh_intervals = Isis.Instances.Instance.LspRefreshIntervals()
                self.lsp_refresh_intervals.parent = self
                self.max_link_metrics = Isis.Instances.Instance.MaxLinkMetrics()
                self.max_link_metrics.parent = self
                self.nets = Isis.Instances.Instance.Nets()
                self.nets.parent = self
                self.nsf = Isis.Instances.Instance.Nsf()
                self.nsf.parent = self
                self.nsr = None
                self.overload_bits = Isis.Instances.Instance.OverloadBits()
                self.overload_bits.parent = self
                self.running = None
                self.srgb = None
                self.trace_buffer_size = Isis.Instances.Instance.TraceBufferSize()
                self.trace_buffer_size.parent = self


            class Afs(object):
                """
                Per\-address\-family configuration
                
                .. attribute:: af
                
                	Configuration for an IS\-IS address\-family. If a named (non\-default) topology is being created it must be multicast
                	**type**\: list of :py:class:`Af <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.af = YList()
                    self.af.parent = self
                    self.af.name = 'af'


                class Af(object):
                    """
                    Configuration for an IS\-IS address\-family. If
                    a named (non\-default) topology is being
                    created it must be multicast.
                    
                    .. attribute:: af_name
                    
                    	Address family
                    	**type**\: :py:class:`IsisAddressFamily_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisAddressFamily_Enum>`
                    
                    .. attribute:: saf_name
                    
                    	Sub address family
                    	**type**\: :py:class:`IsisSubAddressFamily_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisSubAddressFamily_Enum>`
                    
                    .. attribute:: af_data
                    
                    	Data container
                    	**type**\: :py:class:`AfData <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData>`
                    
                    .. attribute:: topology_name
                    
                    	keys\: topology\-name
                    	**type**\: list of :py:class:`TopologyName <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.af_name = None
                        self.saf_name = None
                        self.af_data = None
                        self.topology_name = YList()
                        self.topology_name.parent = self
                        self.topology_name.name = 'topology_name'


                    class AfData(object):
                        """
                        Data container.
                        
                        .. attribute:: adjacency_check
                        
                        	Suppress check for consistent AF support on received IIHs
                        	**type**\: :py:class:`IsisAdjCheck_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisAdjCheck_Enum>`
                        
                        .. attribute:: admin_distances
                        
                        	Per\-route administrative distanceconfiguration
                        	**type**\: :py:class:`AdminDistances <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.AdminDistances>`
                        
                        .. attribute:: advertise_passive_only
                        
                        	If enabled, advertise prefixes of passive interfaces only
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: apply_weight
                        
                        	Apply weights to UCMP or ECMP only
                        	**type**\: :py:class:`IsisApplyWeight_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisApplyWeight_Enum>`
                        
                        .. attribute:: attached_bit
                        
                        	Set the attached bit in this router's level 1 System LSP
                        	**type**\: :py:class:`IsisAttachedBit_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisAttachedBit_Enum>`
                        
                        .. attribute:: default_admin_distance
                        
                        	Default IS\-IS administrative distance configuration
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        .. attribute:: default_information
                        
                        	Control origination of a default route with the option of using a policy.  If no policy is specified the default route is advertised with zero cost in level 2 only
                        	**type**\: :py:class:`DefaultInformation <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation>`
                        
                        .. attribute:: frr_table
                        
                        	Fast\-ReRoute configuration
                        	**type**\: :py:class:`FrrTable <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable>`
                        
                        .. attribute:: ignore_attached_bit
                        
                        	If TRUE, Ignore other routers attached bit
                        	**type**\: bool
                        
                        .. attribute:: ispf
                        
                        	ISPF configuration
                        	**type**\: :py:class:`Ispf <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf>`
                        
                        .. attribute:: max_redist_prefixes
                        
                        	Maximum number of redistributed prefixesconfiguration
                        	**type**\: :py:class:`MaxRedistPrefixes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes>`
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of active parallel paths per route
                        	**type**\: int
                        
                        	**range:** 1..64
                        
                        .. attribute:: metric_styles
                        
                        	Metric\-style configuration
                        	**type**\: :py:class:`MetricStyles <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MetricStyles>`
                        
                        .. attribute:: metrics
                        
                        	Metric configuration
                        	**type**\: :py:class:`Metrics <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Metrics>`
                        
                        .. attribute:: micro_loop_avoidance
                        
                        	Micro Loop Avoidance configuration
                        	**type**\: :py:class:`MicroLoopAvoidance <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance>`
                        
                        .. attribute:: monitor_convergence
                        
                        	Enable convergence monitoring
                        	**type**\: :py:class:`MonitorConvergence <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence>`
                        
                        .. attribute:: mpls
                        
                        	MPLS configuration. MPLS configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\: :py:class:`Mpls <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Mpls>`
                        
                        .. attribute:: mpls_ldp_global
                        
                        	MPLS LDP configuration. MPLS LDP configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\: :py:class:`MplsLdpGlobal <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal>`
                        
                        .. attribute:: propagations
                        
                        	Route propagation configuration
                        	**type**\: :py:class:`Propagations <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Propagations>`
                        
                        .. attribute:: redistributions
                        
                        	Protocol redistribution configuration
                        	**type**\: :py:class:`Redistributions <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions>`
                        
                        .. attribute:: route_source_first_hop
                        
                        	If TRUE, routes will be installed with the IP address of the first\-hop node as the source instead of the originating node
                        	**type**\: bool
                        
                        .. attribute:: segment_routing
                        
                        	Enable Segment Routing configuration
                        	**type**\: :py:class:`SegmentRouting <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting>`
                        
                        .. attribute:: single_topology
                        
                        	Run IPv6 Unicast using the standard (IPv4 Unicast) topology
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: spf_intervals
                        
                        	SPF\-interval configuration
                        	**type**\: :py:class:`SpfIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals>`
                        
                        .. attribute:: spf_periodic_intervals
                        
                        	Peoridic SPF configuration
                        	**type**\: :py:class:`SpfPeriodicIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals>`
                        
                        .. attribute:: spf_prefix_priorities
                        
                        	SPF Prefix Priority configuration
                        	**type**\: :py:class:`SpfPrefixPriorities <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities>`
                        
                        .. attribute:: summary_prefixes
                        
                        	Summary\-prefix configuration
                        	**type**\: :py:class:`SummaryPrefixes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes>`
                        
                        .. attribute:: topology_id
                        
                        	Set the topology ID for a named (non\-default) topology. This object must be set before any other configuration is supplied for a named (non\-default) topology , and must be the last configuration object to be removed. This item should not be supplied for the non\-named default topologies
                        	**type**\: int
                        
                        	**range:** 6..4095
                        
                        .. attribute:: ucmp
                        
                        	UCMP (UnEqual Cost MultiPath) configuration
                        	**type**\: :py:class:`Ucmp <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp>`
                        
                        .. attribute:: weights
                        
                        	Weight configuration
                        	**type**\: :py:class:`Weights <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Weights>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.adjacency_check = None
                            self.admin_distances = Isis.Instances.Instance.Afs.Af.AfData.AdminDistances()
                            self.admin_distances.parent = self
                            self.advertise_passive_only = None
                            self.apply_weight = None
                            self.attached_bit = None
                            self.default_admin_distance = None
                            self.default_information = Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation()
                            self.default_information.parent = self
                            self.frr_table = Isis.Instances.Instance.Afs.Af.AfData.FrrTable()
                            self.frr_table.parent = self
                            self.ignore_attached_bit = None
                            self.ispf = Isis.Instances.Instance.Afs.Af.AfData.Ispf()
                            self.ispf.parent = self
                            self.max_redist_prefixes = Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes()
                            self.max_redist_prefixes.parent = self
                            self.maximum_paths = None
                            self.metric_styles = Isis.Instances.Instance.Afs.Af.AfData.MetricStyles()
                            self.metric_styles.parent = self
                            self.metrics = Isis.Instances.Instance.Afs.Af.AfData.Metrics()
                            self.metrics.parent = self
                            self.micro_loop_avoidance = Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance()
                            self.micro_loop_avoidance.parent = self
                            self.monitor_convergence = Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence()
                            self.monitor_convergence.parent = self
                            self.mpls = Isis.Instances.Instance.Afs.Af.AfData.Mpls()
                            self.mpls.parent = self
                            self.mpls_ldp_global = Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal()
                            self.mpls_ldp_global.parent = self
                            self.propagations = Isis.Instances.Instance.Afs.Af.AfData.Propagations()
                            self.propagations.parent = self
                            self.redistributions = Isis.Instances.Instance.Afs.Af.AfData.Redistributions()
                            self.redistributions.parent = self
                            self.route_source_first_hop = None
                            self.segment_routing = Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting()
                            self.segment_routing.parent = self
                            self.single_topology = None
                            self.spf_intervals = Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals()
                            self.spf_intervals.parent = self
                            self.spf_periodic_intervals = Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals()
                            self.spf_periodic_intervals.parent = self
                            self.spf_prefix_priorities = Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities()
                            self.spf_prefix_priorities.parent = self
                            self.summary_prefixes = Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes()
                            self.summary_prefixes.parent = self
                            self.topology_id = None
                            self.ucmp = Isis.Instances.Instance.Afs.Af.AfData.Ucmp()
                            self.ucmp.parent = self
                            self.weights = Isis.Instances.Instance.Afs.Af.AfData.Weights()
                            self.weights.parent = self


                        class AdminDistances(object):
                            """
                            Per\-route administrative
                            distanceconfiguration
                            
                            .. attribute:: admin_distance
                            
                            	Administrative distance configuration. The supplied distance is applied to all routes discovered from the specified source, or only those that match the supplied prefix list if this is specified
                            	**type**\: list of :py:class:`AdminDistance <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_distance = YList()
                                self.admin_distance.parent = self
                                self.admin_distance.name = 'admin_distance'


                            class AdminDistance(object):
                                """
                                Administrative distance configuration. The
                                supplied distance is applied to all routes
                                discovered from the specified source, or
                                only those that match the supplied prefix
                                list if this is specified
                                
                                .. attribute:: address_prefix
                                
                                	IP route source prefix
                                	**type**\: one of { str | str }
                                
                                .. attribute:: distance
                                
                                	Administrative distance
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                .. attribute:: prefix_list
                                
                                	List of prefixes to which this distance applies
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address_prefix = None
                                    self.distance = None
                                    self.prefix_list = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.address_prefix is None:
                                        raise YPYDataValidationError('Key property address_prefix is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-distance[Cisco-IOS-XR-clns-isis-cfg:address-prefix = ' + str(self.address_prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.address_prefix is not None:
                                        return True

                                    if self.distance is not None:
                                        return True

                                    if self.prefix_list is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-distances'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.admin_distance is not None:
                                    for child_ref in self.admin_distance:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.AdminDistances']['meta_info']


                        class DefaultInformation(object):
                            """
                            Control origination of a default route with
                            the option of using a policy.  If no policy
                            is specified the default route is
                            advertised with zero cost in level 2 only.
                            
                            .. attribute:: external
                            
                            	Flag to indicate that the default prefix should be originated as an external route
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\: str
                            
                            .. attribute:: use_policy
                            
                            	Flag to indicate whether default origination is controlled using a policy
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.external = None
                                self.policy_name = None
                                self.use_policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:default-information'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.external is not None:
                                    return True

                                if self.policy_name is not None:
                                    return True

                                if self.use_policy is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation']['meta_info']


                        class FrrTable(object):
                            """
                            Fast\-ReRoute configuration
                            
                            .. attribute:: frr_load_sharings
                            
                            	Load share prefixes across multiple backups
                            	**type**\: :py:class:`FrrLoadSharings <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings>`
                            
                            .. attribute:: frr_remote_lfa_prefixes
                            
                            	FRR remote LFA prefix list filter configuration
                            	**type**\: :py:class:`FrrRemoteLfaPrefixes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes>`
                            
                            .. attribute:: frr_tiebreakers
                            
                            	FRR tiebreakers configuration
                            	**type**\: :py:class:`FrrTiebreakers <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers>`
                            
                            .. attribute:: frr_use_cand_onlies
                            
                            	FRR use candidate only configuration
                            	**type**\: :py:class:`FrrUseCandOnlies <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies>`
                            
                            .. attribute:: priority_limits
                            
                            	FRR prefix\-limit configuration
                            	**type**\: :py:class:`PriorityLimits <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.frr_load_sharings = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings()
                                self.frr_load_sharings.parent = self
                                self.frr_remote_lfa_prefixes = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes()
                                self.frr_remote_lfa_prefixes.parent = self
                                self.frr_tiebreakers = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers()
                                self.frr_tiebreakers.parent = self
                                self.frr_use_cand_onlies = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies()
                                self.frr_use_cand_onlies.parent = self
                                self.priority_limits = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits()
                                self.priority_limits.parent = self


                            class FrrLoadSharings(object):
                                """
                                Load share prefixes across multiple
                                backups
                                
                                .. attribute:: frr_load_sharing
                                
                                	Disable load sharing
                                	**type**\: list of :py:class:`FrrLoadSharing <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_load_sharing = YList()
                                    self.frr_load_sharing.parent = self
                                    self.frr_load_sharing.name = 'frr_load_sharing'


                                class FrrLoadSharing(object):
                                    """
                                    Disable load sharing
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    .. attribute:: load_sharing
                                    
                                    	Load sharing
                                    	**type**\: :py:class:`IsisfrrLoadSharing_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisfrrLoadSharing_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.load_sharing = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-load-sharing[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.load_sharing is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-load-sharings'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.frr_load_sharing is not None:
                                        for child_ref in self.frr_load_sharing:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings']['meta_info']


                            class FrrRemoteLfaPrefixes(object):
                                """
                                FRR remote LFA prefix list filter
                                configuration
                                
                                .. attribute:: frr_remote_lfa_prefix
                                
                                	Filter remote LFA router IDs using prefix\-list
                                	**type**\: list of :py:class:`FrrRemoteLfaPrefix <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_remote_lfa_prefix = YList()
                                    self.frr_remote_lfa_prefix.parent = self
                                    self.frr_remote_lfa_prefix.name = 'frr_remote_lfa_prefix'


                                class FrrRemoteLfaPrefix(object):
                                    """
                                    Filter remote LFA router IDs using
                                    prefix\-list
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    .. attribute:: prefix_list_name
                                    
                                    	Name of the prefix list
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.prefix_list_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-prefix[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.prefix_list_name is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-prefixes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.frr_remote_lfa_prefix is not None:
                                        for child_ref in self.frr_remote_lfa_prefix:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes']['meta_info']


                            class FrrTiebreakers(object):
                                """
                                FRR tiebreakers configuration
                                
                                .. attribute:: frr_tiebreaker
                                
                                	Configure tiebreaker for multiple backups
                                	**type**\: list of :py:class:`FrrTiebreaker <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_tiebreaker = YList()
                                    self.frr_tiebreaker.parent = self
                                    self.frr_tiebreaker.name = 'frr_tiebreaker'


                                class FrrTiebreaker(object):
                                    """
                                    Configure tiebreaker for multiple backups
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    .. attribute:: tiebreaker
                                    
                                    	Tiebreaker for which configuration applies
                                    	**type**\: :py:class:`IsisfrrTiebreaker_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisfrrTiebreaker_Enum>`
                                    
                                    .. attribute:: index
                                    
                                    	Preference order among tiebreakers
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.tiebreaker = None
                                        self.index = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')
                                        if self.tiebreaker is None:
                                            raise YPYDataValidationError('Key property tiebreaker is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-tiebreaker[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:tiebreaker = ' + str(self.tiebreaker) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.tiebreaker is not None:
                                            return True

                                        if self.index is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-tiebreakers'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.frr_tiebreaker is not None:
                                        for child_ref in self.frr_tiebreaker:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers']['meta_info']


                            class FrrUseCandOnlies(object):
                                """
                                FRR use candidate only configuration
                                
                                .. attribute:: frr_use_cand_only
                                
                                	Configure use candidate only to exclude interfaces as backup
                                	**type**\: list of :py:class:`FrrUseCandOnly <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_use_cand_only = YList()
                                    self.frr_use_cand_only.parent = self
                                    self.frr_use_cand_only.name = 'frr_use_cand_only'


                                class FrrUseCandOnly(object):
                                    """
                                    Configure use candidate only to exclude
                                    interfaces as backup
                                    
                                    .. attribute:: frr_type
                                    
                                    	Computation Type
                                    	**type**\: :py:class:`Isisfrr_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isisfrr_Enum>`
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.frr_type = None
                                        self.level = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.frr_type is None:
                                            raise YPYDataValidationError('Key property frr_type is None')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-use-cand-only[Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + '][Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.frr_type is not None:
                                            return True

                                        if self.level is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-use-cand-onlies'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.frr_use_cand_only is not None:
                                        for child_ref in self.frr_use_cand_only:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies']['meta_info']


                            class PriorityLimits(object):
                                """
                                FRR prefix\-limit configuration
                                
                                .. attribute:: priority_limit
                                
                                	Limit backup computation upto the prefix priority
                                	**type**\: list of :py:class:`PriorityLimit <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.priority_limit = YList()
                                    self.priority_limit.parent = self
                                    self.priority_limit.name = 'priority_limit'


                                class PriorityLimit(object):
                                    """
                                    Limit backup computation upto the prefix
                                    priority
                                    
                                    .. attribute:: frr_type
                                    
                                    	Computation Type
                                    	**type**\: :py:class:`Isisfrr_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isisfrr_Enum>`
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    .. attribute:: priority
                                    
                                    	Compute for all prefixes upto the specified priority
                                    	**type**\: :py:class:`IsisPrefixPriority_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.frr_type = None
                                        self.level = None
                                        self.priority = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.frr_type is None:
                                            raise YPYDataValidationError('Key property frr_type is None')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priority-limit[Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + '][Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.frr_type is not None:
                                            return True

                                        if self.level is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priority-limits'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.priority_limit is not None:
                                        for child_ref in self.priority_limit:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-table'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.frr_load_sharings is not None and self.frr_load_sharings._has_data():
                                    return True

                                if self.frr_load_sharings is not None and self.frr_load_sharings.is_presence():
                                    return True

                                if self.frr_remote_lfa_prefixes is not None and self.frr_remote_lfa_prefixes._has_data():
                                    return True

                                if self.frr_remote_lfa_prefixes is not None and self.frr_remote_lfa_prefixes.is_presence():
                                    return True

                                if self.frr_tiebreakers is not None and self.frr_tiebreakers._has_data():
                                    return True

                                if self.frr_tiebreakers is not None and self.frr_tiebreakers.is_presence():
                                    return True

                                if self.frr_use_cand_onlies is not None and self.frr_use_cand_onlies._has_data():
                                    return True

                                if self.frr_use_cand_onlies is not None and self.frr_use_cand_onlies.is_presence():
                                    return True

                                if self.priority_limits is not None and self.priority_limits._has_data():
                                    return True

                                if self.priority_limits is not None and self.priority_limits.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.FrrTable']['meta_info']


                        class Ispf(object):
                            """
                            ISPF configuration
                            
                            .. attribute:: states
                            
                            	ISPF state (enable/disable)
                            	**type**\: :py:class:`States <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf.States>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.states = Isis.Instances.Instance.Afs.Af.AfData.Ispf.States()
                                self.states.parent = self


                            class States(object):
                                """
                                ISPF state (enable/disable)
                                
                                .. attribute:: state
                                
                                	Enable/disable ISPF
                                	**type**\: list of :py:class:`State <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.state = YList()
                                    self.state.parent = self
                                    self.state.name = 'state'


                                class State(object):
                                    """
                                    Enable/disable ISPF
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\: :py:class:`IsisispfState_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisispfState_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.state = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:state[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.state is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:states'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.state is not None:
                                        for child_ref in self.state:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf.States']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ispf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.states is not None and self.states._has_data():
                                    return True

                                if self.states is not None and self.states.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ispf']['meta_info']


                        class MaxRedistPrefixes(object):
                            """
                            Maximum number of redistributed
                            prefixesconfiguration
                            
                            .. attribute:: max_redist_prefix
                            
                            	An upper limit on the number of redistributed prefixes which may be included in the local system's LSP
                            	**type**\: list of :py:class:`MaxRedistPrefix <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_redist_prefix = YList()
                                self.max_redist_prefix.parent = self
                                self.max_redist_prefix.name = 'max_redist_prefix'


                            class MaxRedistPrefix(object):
                                """
                                An upper limit on the number of
                                redistributed prefixes which may be
                                included in the local system's LSP
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: prefix_limit
                                
                                	Max number of prefixes
                                	**type**\: int
                                
                                	**range:** 1..28000
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.prefix_limit = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-redist-prefix[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.prefix_limit is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-redist-prefixes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.max_redist_prefix is not None:
                                    for child_ref in self.max_redist_prefix:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes']['meta_info']


                        class MetricStyles(object):
                            """
                            Metric\-style configuration
                            
                            .. attribute:: metric_style
                            
                            	Configuration of metric style in LSPs
                            	**type**\: list of :py:class:`MetricStyle <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.metric_style = YList()
                                self.metric_style.parent = self
                                self.metric_style.name = 'metric_style'


                            class MetricStyle(object):
                                """
                                Configuration of metric style in LSPs
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: style
                                
                                	Metric Style
                                	**type**\: :py:class:`IsisMetricStyle_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyle_Enum>`
                                
                                .. attribute:: transition_state
                                
                                	Transition state
                                	**type**\: :py:class:`IsisMetricStyleTransition_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyleTransition_Enum>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.style = None
                                    self.transition_state = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric-style[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.style is not None:
                                        return True

                                    if self.transition_state is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric-styles'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.metric_style is not None:
                                    for child_ref in self.metric_style:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MetricStyles']['meta_info']


                        class Metrics(object):
                            """
                            Metric configuration
                            
                            .. attribute:: metric
                            
                            	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                            	**type**\: list of :py:class:`Metric <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.metric = YList()
                                self.metric.parent = self
                                self.metric.name = 'metric'


                            class Metric(object):
                                """
                                Metric configuration. Legal value depends on
                                the metric\-style specified for the topology. If
                                the metric\-style defined is narrow, then only a
                                value between <1\-63> is allowed and if the
                                metric\-style is defined as wide, then a value
                                between <1\-16777215> is allowed as the metric
                                value.  All routers exclude links with the
                                maximum wide metric (16777215) from their SPF
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: metric
                                
                                	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                	**type**\: one of { :py:class:`Metric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_Enum>` | int }
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.metric = None

                                class Metric_Enum(Enum):
                                    """
                                    Metric_Enum

                                    Allowed metric\: <1\-63> for narrow,
                                    <1\-16777215> for wide

                                    """

                                    """

                                    Maximum wide metric.  All routers will
                                    exclude this link from their SPF

                                    """
                                    MAXIMUM = 16777215


                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric.Metric_Enum']


                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.metric is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metrics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.metric is not None:
                                    for child_ref in self.metric:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Metrics']['meta_info']


                        class MicroLoopAvoidance(object):
                            """
                            Micro Loop Avoidance configuration
                            
                            .. attribute:: enable
                            
                            	MicroLoop avoidance enable configuration
                            	**type**\: :py:class:`IsisMicroLoopAvoidance_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMicroLoopAvoidance_Enum>`
                            
                            .. attribute:: rib_update_delay
                            
                            	Value of delay in msecs in updating RIB
                            	**type**\: int
                            
                            	**range:** 1000..65535
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.rib_update_delay = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:micro-loop-avoidance'

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

                                if self.rib_update_delay is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance']['meta_info']


                        class MonitorConvergence(object):
                            """
                            Enable convergence monitoring
                            
                            .. attribute:: enable
                            
                            	Enable convergence monitoring
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: prefix_list
                            
                            	Enable the monitoring of individual prefixes (prefix list name)
                            	**type**\: str
                            
                            .. attribute:: track_ip_frr
                            
                            	Enable the Tracking of IP\-Frr Convergence
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.prefix_list = None
                                self.track_ip_frr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:monitor-convergence'

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

                                if self.prefix_list is not None:
                                    return True

                                if self.track_ip_frr is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence']['meta_info']


                        class Mpls(object):
                            """
                            MPLS configuration. MPLS configuration will
                            only be applied for the IPv4\-unicast
                            address\-family.
                            
                            .. attribute:: igp_intact
                            
                            	Install TE and non\-TE nexthops in the RIB
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: level
                            
                            	Enable MPLS for an IS\-IS at the given levels
                            	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                            
                            .. attribute:: multicast_intact
                            
                            	Install non\-TE nexthops in the RIB for use by multicast
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: router_id
                            
                            	Traffic Engineering stable IP address for system
                            	**type**\: :py:class:`RouterId <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.igp_intact = None
                                self.level = None
                                self.multicast_intact = None
                                self.router_id = Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId()
                                self.router_id.parent = self


                            class RouterId(object):
                                """
                                Traffic Engineering stable IP address for
                                system
                                
                                .. attribute:: address
                                
                                	IPv4 address to be used as a router ID. Precisely one of Address and Interface must be specified
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                                	**type**\: str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None
                                    self.interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:router-id'

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

                                    if self.interface_name is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.igp_intact is not None:
                                    return True

                                if self.level is not None:
                                    return True

                                if self.multicast_intact is not None:
                                    return True

                                if self.router_id is not None and self.router_id._has_data():
                                    return True

                                if self.router_id is not None and self.router_id.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Mpls']['meta_info']


                        class MplsLdpGlobal(object):
                            """
                            MPLS LDP configuration. MPLS LDP
                            configuration will only be applied for the
                            IPv4\-unicast address\-family.
                            
                            .. attribute:: auto_config
                            
                            	If TRUE, LDP will be enabled onall IS\-IS interfaces enabled for this address\-family
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.auto_config = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls-ldp-global'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.auto_config is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal']['meta_info']


                        class Propagations(object):
                            """
                            Route propagation configuration
                            
                            .. attribute:: propagation
                            
                            	Propagate routes between IS\-IS levels
                            	**type**\: list of :py:class:`Propagation <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.propagation = YList()
                                self.propagation.parent = self
                                self.propagation.name = 'propagation'


                            class Propagation(object):
                                """
                                Propagate routes between IS\-IS levels
                                
                                .. attribute:: destination_level
                                
                                	Destination level for routes.  Must differ from SourceLevel
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: source_level
                                
                                	Source level for routes
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: route_policy_name
                                
                                	Route policy limiting routes to be propagated
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.destination_level = None
                                    self.source_level = None
                                    self.route_policy_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.destination_level is None:
                                        raise YPYDataValidationError('Key property destination_level is None')
                                    if self.source_level is None:
                                        raise YPYDataValidationError('Key property source_level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:propagation[Cisco-IOS-XR-clns-isis-cfg:destination-level = ' + str(self.destination_level) + '][Cisco-IOS-XR-clns-isis-cfg:source-level = ' + str(self.source_level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.destination_level is not None:
                                        return True

                                    if self.source_level is not None:
                                        return True

                                    if self.route_policy_name is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:propagations'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.propagation is not None:
                                    for child_ref in self.propagation:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Propagations']['meta_info']


                        class Redistributions(object):
                            """
                            Protocol redistribution configuration
                            
                            .. attribute:: redistribution
                            
                            	Redistribution of other protocols into this IS\-IS instance
                            	**type**\: list of :py:class:`Redistribution <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.redistribution = YList()
                                self.redistribution.parent = self
                                self.redistribution.name = 'redistribution'


                            class Redistribution(object):
                                """
                                Redistribution of other protocols into
                                this IS\-IS instance
                                
                                .. attribute:: protocol_name
                                
                                	The protocol to be redistributed.  OSPFv3 may not be specified for an IPv4 topology and OSPF may not be specified for an IPv6 topology
                                	**type**\: :py:class:`IsisRedistProto_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisRedistProto_Enum>`
                                
                                .. attribute:: bgp
                                
                                	bgp
                                	**type**\: list of :py:class:`Bgp <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp>`
                                
                                .. attribute:: connected_or_static_or_rip_or_subscriber_or_mobile
                                
                                	connected or static or rip or subscriber or mobile
                                	**type**\: :py:class:`ConnectedOrStaticOrRipOrSubscriberOrMobile <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile>`
                                
                                .. attribute:: eigrp
                                
                                	eigrp
                                	**type**\: list of :py:class:`Eigrp <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp>`
                                
                                .. attribute:: ospf_or_ospfv3_or_isis_or_application
                                
                                	ospf or ospfv3 or isis or application
                                	**type**\: list of :py:class:`OspfOrOspfv3OrIsisOrApplication <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.protocol_name = None
                                    self.bgp = YList()
                                    self.bgp.parent = self
                                    self.bgp.name = 'bgp'
                                    self.connected_or_static_or_rip_or_subscriber_or_mobile = None
                                    self.eigrp = YList()
                                    self.eigrp.parent = self
                                    self.eigrp.name = 'eigrp'
                                    self.ospf_or_ospfv3_or_isis_or_application = YList()
                                    self.ospf_or_ospfv3_or_isis_or_application.parent = self
                                    self.ospf_or_ospfv3_or_isis_or_application.name = 'ospf_or_ospfv3_or_isis_or_application'


                                class Bgp(object):
                                    """
                                    bgp
                                    
                                    .. attribute:: as_xx
                                    
                                    	First half of BGP AS number in XX.YY format.  Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if second half is zero
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: as_yy
                                    
                                    	Second half of BGP AS number in XX.YY format. Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if first half is zero
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\: :py:class:`IsisMetric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetric_Enum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.as_xx = None
                                        self.as_yy = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.as_xx is None:
                                            raise YPYDataValidationError('Key property as_xx is None')
                                        if self.as_yy is None:
                                            raise YPYDataValidationError('Key property as_yy is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:bgp[Cisco-IOS-XR-clns-isis-cfg:as-xx = ' + str(self.as_xx) + '][Cisco-IOS-XR-clns-isis-cfg:as-yy = ' + str(self.as_yy) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.as_xx is not None:
                                            return True

                                        if self.as_yy is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp']['meta_info']


                                class ConnectedOrStaticOrRipOrSubscriberOrMobile(object):
                                    """
                                    connected or static or rip or subscriber
                                    or mobile
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\: :py:class:`IsisMetric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetric_Enum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:connected-or-static-or-rip-or-subscriber-or-mobile'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return True

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile']['meta_info']


                                class Eigrp(object):
                                    """
                                    eigrp
                                    
                                    .. attribute:: as_zz
                                    
                                    	Eigrp as number
                                    	**type**\: int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\: :py:class:`IsisMetric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetric_Enum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.as_zz = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.as_zz is None:
                                            raise YPYDataValidationError('Key property as_zz is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:eigrp[Cisco-IOS-XR-clns-isis-cfg:as-zz = ' + str(self.as_zz) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.as_zz is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp']['meta_info']


                                class OspfOrOspfv3OrIsisOrApplication(object):
                                    """
                                    ospf or ospfv3 or isis or application
                                    
                                    .. attribute:: instance_name
                                    
                                    	Protocol Instance Identifier.  Mandatory for ISIS, OSPF and application, must not be specified otherwise
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\: :py:class:`IsisMetric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetric_Enum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.instance_name = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.instance_name is None:
                                            raise YPYDataValidationError('Key property instance_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ospf-or-ospfv3-or-isis-or-application[Cisco-IOS-XR-clns-isis-cfg:instance-name = ' + str(self.instance_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.instance_name is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.protocol_name is None:
                                        raise YPYDataValidationError('Key property protocol_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:redistribution[Cisco-IOS-XR-clns-isis-cfg:protocol-name = ' + str(self.protocol_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.protocol_name is not None:
                                        return True

                                    if self.bgp is not None:
                                        for child_ref in self.bgp:
                                            if child_ref._has_data():
                                                return True

                                    if self.connected_or_static_or_rip_or_subscriber_or_mobile is not None and self.connected_or_static_or_rip_or_subscriber_or_mobile._has_data():
                                        return True

                                    if self.connected_or_static_or_rip_or_subscriber_or_mobile is not None and self.connected_or_static_or_rip_or_subscriber_or_mobile.is_presence():
                                        return True

                                    if self.eigrp is not None:
                                        for child_ref in self.eigrp:
                                            if child_ref._has_data():
                                                return True

                                    if self.ospf_or_ospfv3_or_isis_or_application is not None:
                                        for child_ref in self.ospf_or_ospfv3_or_isis_or_application:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:redistributions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.redistribution is not None:
                                    for child_ref in self.redistribution:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Redistributions']['meta_info']


                        class SegmentRouting(object):
                            """
                            Enable Segment Routing configuration
                            
                            .. attribute:: mpls
                            
                            	Prefer segment routing labels over LDP labels
                            	**type**\: :py:class:`IsisLabelPreference_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisLabelPreference_Enum>`
                            
                            .. attribute:: prefix_sid_map
                            
                            	Enable Segment Routing prefix SID map configuration
                            	**type**\: :py:class:`PrefixSidMap <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mpls = None
                                self.prefix_sid_map = Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap()
                                self.prefix_sid_map.parent = self


                            class PrefixSidMap(object):
                                """
                                Enable Segment Routing prefix SID map
                                configuration
                                
                                .. attribute:: advertise_local
                                
                                	Enable Segment Routing prefix SID map advertise local
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: receive
                                
                                	If TRUE, remote prefix SID map advertisements will be used. If FALSE, they will not be used
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.advertise_local = None
                                    self.receive = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-sid-map'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.advertise_local is not None:
                                        return True

                                    if self.receive is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:segment-routing'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.mpls is not None:
                                    return True

                                if self.prefix_sid_map is not None and self.prefix_sid_map._has_data():
                                    return True

                                if self.prefix_sid_map is not None and self.prefix_sid_map.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting']['meta_info']


                        class SpfIntervals(object):
                            """
                            SPF\-interval configuration
                            
                            .. attribute:: spf_interval
                            
                            	Route calculation scheduling parameters
                            	**type**\: list of :py:class:`SpfInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_interval = YList()
                                self.spf_interval.parent = self
                                self.spf_interval.name = 'spf_interval'


                            class SpfInterval(object):
                                """
                                Route calculation scheduling parameters
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: initial_wait
                                
                                	Initial wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                .. attribute:: maximum_wait
                                
                                	Maximum wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                .. attribute:: secondary_wait
                                
                                	Secondary wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.initial_wait = None
                                    self.maximum_wait = None
                                    self.secondary_wait = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.initial_wait is not None:
                                        return True

                                    if self.maximum_wait is not None:
                                        return True

                                    if self.secondary_wait is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-intervals'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.spf_interval is not None:
                                    for child_ref in self.spf_interval:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals']['meta_info']


                        class SpfPeriodicIntervals(object):
                            """
                            Peoridic SPF configuration
                            
                            .. attribute:: spf_periodic_interval
                            
                            	Maximum interval between spf runs
                            	**type**\: list of :py:class:`SpfPeriodicInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_periodic_interval = YList()
                                self.spf_periodic_interval.parent = self
                                self.spf_periodic_interval.name = 'spf_periodic_interval'


                            class SpfPeriodicInterval(object):
                                """
                                Maximum interval between spf runs
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: periodic_interval
                                
                                	Maximum interval in between SPF runs in seconds
                                	**type**\: int
                                
                                	**range:** 0..3600
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.periodic_interval = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-periodic-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.periodic_interval is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-periodic-intervals'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.spf_periodic_interval is not None:
                                    for child_ref in self.spf_periodic_interval:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals']['meta_info']


                        class SpfPrefixPriorities(object):
                            """
                            SPF Prefix Priority configuration
                            
                            .. attribute:: spf_prefix_priority
                            
                            	Determine SPF priority for prefixes
                            	**type**\: list of :py:class:`SpfPrefixPriority <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_prefix_priority = YList()
                                self.spf_prefix_priority.parent = self
                                self.spf_prefix_priority.name = 'spf_prefix_priority'


                            class SpfPrefixPriority(object):
                                """
                                Determine SPF priority for prefixes
                                
                                .. attribute:: level
                                
                                	SPF Level for prefix prioritization
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: prefix_priority_type
                                
                                	SPF Priority to assign matching prefixes
                                	**type**\: :py:class:`IsisPrefixPriority_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority_Enum>`
                                
                                .. attribute:: access_list_name
                                
                                	Access List to determine prefixes for this priority
                                	**type**\: str
                                
                                .. attribute:: admin_tag
                                
                                	Tag value to determine prefixes for this priority
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.prefix_priority_type = None
                                    self.access_list_name = None
                                    self.admin_tag = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')
                                    if self.prefix_priority_type is None:
                                        raise YPYDataValidationError('Key property prefix_priority_type is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-prefix-priority[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:prefix-priority-type = ' + str(self.prefix_priority_type) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.prefix_priority_type is not None:
                                        return True

                                    if self.access_list_name is not None:
                                        return True

                                    if self.admin_tag is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-prefix-priorities'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.spf_prefix_priority is not None:
                                    for child_ref in self.spf_prefix_priority:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities']['meta_info']


                        class SummaryPrefixes(object):
                            """
                            Summary\-prefix configuration
                            
                            .. attribute:: summary_prefix
                            
                            	Configure IP address prefixes to advertise
                            	**type**\: list of :py:class:`SummaryPrefix <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.summary_prefix = YList()
                                self.summary_prefix.parent = self
                                self.summary_prefix.name = 'summary_prefix'


                            class SummaryPrefix(object):
                                """
                                Configure IP address prefixes to advertise
                                
                                .. attribute:: address_prefix
                                
                                	IP summary address prefix
                                	**type**\: one of { str | str }
                                
                                .. attribute:: level
                                
                                	Level in which to summarize routes
                                	**type**\: int
                                
                                	**range:** 1..2
                                
                                .. attribute:: tag
                                
                                	The tag value
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address_prefix = None
                                    self.level = None
                                    self.tag = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.address_prefix is None:
                                        raise YPYDataValidationError('Key property address_prefix is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:summary-prefix[Cisco-IOS-XR-clns-isis-cfg:address-prefix = ' + str(self.address_prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.address_prefix is not None:
                                        return True

                                    if self.level is not None:
                                        return True

                                    if self.tag is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:summary-prefixes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.summary_prefix is not None:
                                    for child_ref in self.summary_prefix:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes']['meta_info']


                        class Ucmp(object):
                            """
                            UCMP (UnEqual Cost MultiPath) configuration
                            
                            .. attribute:: delay_interval
                            
                            	Delay in msecs between primary SPF and UCMP computation
                            	**type**\: int
                            
                            	**range:** 100..65535
                            
                            .. attribute:: enable
                            
                            	UCMP feature enable configuration
                            	**type**\: :py:class:`Enable <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable>`
                            
                            .. attribute:: exclude_interfaces
                            
                            	Interfaces excluded from UCMP path computation
                            	**type**\: :py:class:`ExcludeInterfaces <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.delay_interval = None
                                self.enable = Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable()
                                self.enable.parent = self
                                self.exclude_interfaces = Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces()
                                self.exclude_interfaces.parent = self


                            class Enable(object):
                                """
                                UCMP feature enable configuration
                                
                                .. attribute:: prefix_list_name
                                
                                	Name of the Prefix List
                                	**type**\: str
                                
                                .. attribute:: variance
                                
                                	Value of variance
                                	**type**\: int
                                
                                	**range:** 101..10000
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.prefix_list_name = None
                                    self.variance = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:enable'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.prefix_list_name is not None:
                                        return True

                                    if self.variance is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable']['meta_info']


                            class ExcludeInterfaces(object):
                                """
                                Interfaces excluded from UCMP path
                                computation
                                
                                .. attribute:: exclude_interface
                                
                                	Exclude this interface from UCMP path computation
                                	**type**\: list of :py:class:`ExcludeInterface <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.exclude_interface = YList()
                                    self.exclude_interface.parent = self
                                    self.exclude_interface.name = 'exclude_interface'


                                class ExcludeInterface(object):
                                    """
                                    Exclude this interface from UCMP path
                                    computation
                                    
                                    .. attribute:: interface_name
                                    
                                    	Name of the interface to be excluded
                                    	**type**\: str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
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

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:exclude-interface[Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + ']'

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
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:exclude-interfaces'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.exclude_interface is not None:
                                        for child_ref in self.exclude_interface:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ucmp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.delay_interval is not None:
                                    return True

                                if self.enable is not None and self.enable._has_data():
                                    return True

                                if self.enable is not None and self.enable.is_presence():
                                    return True

                                if self.exclude_interfaces is not None and self.exclude_interfaces._has_data():
                                    return True

                                if self.exclude_interfaces is not None and self.exclude_interfaces.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Ucmp']['meta_info']


                        class Weights(object):
                            """
                            Weight configuration
                            
                            .. attribute:: weight
                            
                            	Weight configuration under interface for load balancing
                            	**type**\: list of :py:class:`Weight <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.weight = YList()
                                self.weight.parent = self
                                self.weight.name = 'weight'


                            class Weight(object):
                                """
                                Weight configuration under interface for load
                                balancing
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: weight
                                
                                	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                	**type**\: int
                                
                                	**range:** 1..16777214
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.weight = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weight[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.weight is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weights'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.weight is not None:
                                    for child_ref in self.weight:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData.Weights']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:af-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.adjacency_check is not None:
                                return True

                            if self.admin_distances is not None and self.admin_distances._has_data():
                                return True

                            if self.admin_distances is not None and self.admin_distances.is_presence():
                                return True

                            if self.advertise_passive_only is not None:
                                return True

                            if self.apply_weight is not None:
                                return True

                            if self.attached_bit is not None:
                                return True

                            if self.default_admin_distance is not None:
                                return True

                            if self.default_information is not None and self.default_information._has_data():
                                return True

                            if self.default_information is not None and self.default_information.is_presence():
                                return True

                            if self.frr_table is not None and self.frr_table._has_data():
                                return True

                            if self.frr_table is not None and self.frr_table.is_presence():
                                return True

                            if self.ignore_attached_bit is not None:
                                return True

                            if self.ispf is not None and self.ispf._has_data():
                                return True

                            if self.ispf is not None and self.ispf.is_presence():
                                return True

                            if self.max_redist_prefixes is not None and self.max_redist_prefixes._has_data():
                                return True

                            if self.max_redist_prefixes is not None and self.max_redist_prefixes.is_presence():
                                return True

                            if self.maximum_paths is not None:
                                return True

                            if self.metric_styles is not None and self.metric_styles._has_data():
                                return True

                            if self.metric_styles is not None and self.metric_styles.is_presence():
                                return True

                            if self.metrics is not None and self.metrics._has_data():
                                return True

                            if self.metrics is not None and self.metrics.is_presence():
                                return True

                            if self.micro_loop_avoidance is not None and self.micro_loop_avoidance._has_data():
                                return True

                            if self.micro_loop_avoidance is not None and self.micro_loop_avoidance.is_presence():
                                return True

                            if self.monitor_convergence is not None and self.monitor_convergence._has_data():
                                return True

                            if self.monitor_convergence is not None and self.monitor_convergence.is_presence():
                                return True

                            if self.mpls is not None and self.mpls._has_data():
                                return True

                            if self.mpls is not None and self.mpls.is_presence():
                                return True

                            if self.mpls_ldp_global is not None and self.mpls_ldp_global._has_data():
                                return True

                            if self.mpls_ldp_global is not None and self.mpls_ldp_global.is_presence():
                                return True

                            if self.propagations is not None and self.propagations._has_data():
                                return True

                            if self.propagations is not None and self.propagations.is_presence():
                                return True

                            if self.redistributions is not None and self.redistributions._has_data():
                                return True

                            if self.redistributions is not None and self.redistributions.is_presence():
                                return True

                            if self.route_source_first_hop is not None:
                                return True

                            if self.segment_routing is not None and self.segment_routing._has_data():
                                return True

                            if self.segment_routing is not None and self.segment_routing.is_presence():
                                return True

                            if self.single_topology is not None:
                                return True

                            if self.spf_intervals is not None and self.spf_intervals._has_data():
                                return True

                            if self.spf_intervals is not None and self.spf_intervals.is_presence():
                                return True

                            if self.spf_periodic_intervals is not None and self.spf_periodic_intervals._has_data():
                                return True

                            if self.spf_periodic_intervals is not None and self.spf_periodic_intervals.is_presence():
                                return True

                            if self.spf_prefix_priorities is not None and self.spf_prefix_priorities._has_data():
                                return True

                            if self.spf_prefix_priorities is not None and self.spf_prefix_priorities.is_presence():
                                return True

                            if self.summary_prefixes is not None and self.summary_prefixes._has_data():
                                return True

                            if self.summary_prefixes is not None and self.summary_prefixes.is_presence():
                                return True

                            if self.topology_id is not None:
                                return True

                            if self.ucmp is not None and self.ucmp._has_data():
                                return True

                            if self.ucmp is not None and self.ucmp.is_presence():
                                return True

                            if self.weights is not None and self.weights._has_data():
                                return True

                            if self.weights is not None and self.weights.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return True

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Afs.Af.AfData']['meta_info']


                    class TopologyName(object):
                        """
                        keys\: topology\-name
                        
                        .. attribute:: topology_name
                        
                        	Topology Name
                        	**type**\: str
                        
                        	**range:** 0..32
                        
                        .. attribute:: adjacency_check
                        
                        	Suppress check for consistent AF support on received IIHs
                        	**type**\: :py:class:`IsisAdjCheck_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisAdjCheck_Enum>`
                        
                        .. attribute:: admin_distances
                        
                        	Per\-route administrative distanceconfiguration
                        	**type**\: :py:class:`AdminDistances <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances>`
                        
                        .. attribute:: advertise_passive_only
                        
                        	If enabled, advertise prefixes of passive interfaces only
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: apply_weight
                        
                        	Apply weights to UCMP or ECMP only
                        	**type**\: :py:class:`IsisApplyWeight_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisApplyWeight_Enum>`
                        
                        .. attribute:: attached_bit
                        
                        	Set the attached bit in this router's level 1 System LSP
                        	**type**\: :py:class:`IsisAttachedBit_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisAttachedBit_Enum>`
                        
                        .. attribute:: default_admin_distance
                        
                        	Default IS\-IS administrative distance configuration
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        .. attribute:: default_information
                        
                        	Control origination of a default route with the option of using a policy.  If no policy is specified the default route is advertised with zero cost in level 2 only
                        	**type**\: :py:class:`DefaultInformation <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation>`
                        
                        .. attribute:: frr_table
                        
                        	Fast\-ReRoute configuration
                        	**type**\: :py:class:`FrrTable <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable>`
                        
                        .. attribute:: ignore_attached_bit
                        
                        	If TRUE, Ignore other routers attached bit
                        	**type**\: bool
                        
                        .. attribute:: ispf
                        
                        	ISPF configuration
                        	**type**\: :py:class:`Ispf <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf>`
                        
                        .. attribute:: max_redist_prefixes
                        
                        	Maximum number of redistributed prefixesconfiguration
                        	**type**\: :py:class:`MaxRedistPrefixes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes>`
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of active parallel paths per route
                        	**type**\: int
                        
                        	**range:** 1..64
                        
                        .. attribute:: metric_styles
                        
                        	Metric\-style configuration
                        	**type**\: :py:class:`MetricStyles <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles>`
                        
                        .. attribute:: metrics
                        
                        	Metric configuration
                        	**type**\: :py:class:`Metrics <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Metrics>`
                        
                        .. attribute:: micro_loop_avoidance
                        
                        	Micro Loop Avoidance configuration
                        	**type**\: :py:class:`MicroLoopAvoidance <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance>`
                        
                        .. attribute:: monitor_convergence
                        
                        	Enable convergence monitoring
                        	**type**\: :py:class:`MonitorConvergence <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence>`
                        
                        .. attribute:: mpls
                        
                        	MPLS configuration. MPLS configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\: :py:class:`Mpls <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Mpls>`
                        
                        .. attribute:: mpls_ldp_global
                        
                        	MPLS LDP configuration. MPLS LDP configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\: :py:class:`MplsLdpGlobal <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal>`
                        
                        .. attribute:: propagations
                        
                        	Route propagation configuration
                        	**type**\: :py:class:`Propagations <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Propagations>`
                        
                        .. attribute:: redistributions
                        
                        	Protocol redistribution configuration
                        	**type**\: :py:class:`Redistributions <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions>`
                        
                        .. attribute:: route_source_first_hop
                        
                        	If TRUE, routes will be installed with the IP address of the first\-hop node as the source instead of the originating node
                        	**type**\: bool
                        
                        .. attribute:: segment_routing
                        
                        	Enable Segment Routing configuration
                        	**type**\: :py:class:`SegmentRouting <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting>`
                        
                        .. attribute:: single_topology
                        
                        	Run IPv6 Unicast using the standard (IPv4 Unicast) topology
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: spf_intervals
                        
                        	SPF\-interval configuration
                        	**type**\: :py:class:`SpfIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals>`
                        
                        .. attribute:: spf_periodic_intervals
                        
                        	Peoridic SPF configuration
                        	**type**\: :py:class:`SpfPeriodicIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals>`
                        
                        .. attribute:: spf_prefix_priorities
                        
                        	SPF Prefix Priority configuration
                        	**type**\: :py:class:`SpfPrefixPriorities <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities>`
                        
                        .. attribute:: summary_prefixes
                        
                        	Summary\-prefix configuration
                        	**type**\: :py:class:`SummaryPrefixes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes>`
                        
                        .. attribute:: topology_id
                        
                        	Set the topology ID for a named (non\-default) topology. This object must be set before any other configuration is supplied for a named (non\-default) topology , and must be the last configuration object to be removed. This item should not be supplied for the non\-named default topologies
                        	**type**\: int
                        
                        	**range:** 6..4095
                        
                        .. attribute:: ucmp
                        
                        	UCMP (UnEqual Cost MultiPath) configuration
                        	**type**\: :py:class:`Ucmp <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp>`
                        
                        .. attribute:: weights
                        
                        	Weight configuration
                        	**type**\: :py:class:`Weights <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Weights>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.topology_name = None
                            self.adjacency_check = None
                            self.admin_distances = Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances()
                            self.admin_distances.parent = self
                            self.advertise_passive_only = None
                            self.apply_weight = None
                            self.attached_bit = None
                            self.default_admin_distance = None
                            self.default_information = Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation()
                            self.default_information.parent = self
                            self.frr_table = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable()
                            self.frr_table.parent = self
                            self.ignore_attached_bit = None
                            self.ispf = Isis.Instances.Instance.Afs.Af.TopologyName.Ispf()
                            self.ispf.parent = self
                            self.max_redist_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes()
                            self.max_redist_prefixes.parent = self
                            self.maximum_paths = None
                            self.metric_styles = Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles()
                            self.metric_styles.parent = self
                            self.metrics = Isis.Instances.Instance.Afs.Af.TopologyName.Metrics()
                            self.metrics.parent = self
                            self.micro_loop_avoidance = Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance()
                            self.micro_loop_avoidance.parent = self
                            self.monitor_convergence = Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence()
                            self.monitor_convergence.parent = self
                            self.mpls = Isis.Instances.Instance.Afs.Af.TopologyName.Mpls()
                            self.mpls.parent = self
                            self.mpls_ldp_global = Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal()
                            self.mpls_ldp_global.parent = self
                            self.propagations = Isis.Instances.Instance.Afs.Af.TopologyName.Propagations()
                            self.propagations.parent = self
                            self.redistributions = Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions()
                            self.redistributions.parent = self
                            self.route_source_first_hop = None
                            self.segment_routing = Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting()
                            self.segment_routing.parent = self
                            self.single_topology = None
                            self.spf_intervals = Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals()
                            self.spf_intervals.parent = self
                            self.spf_periodic_intervals = Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals()
                            self.spf_periodic_intervals.parent = self
                            self.spf_prefix_priorities = Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities()
                            self.spf_prefix_priorities.parent = self
                            self.summary_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes()
                            self.summary_prefixes.parent = self
                            self.topology_id = None
                            self.ucmp = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp()
                            self.ucmp.parent = self
                            self.weights = Isis.Instances.Instance.Afs.Af.TopologyName.Weights()
                            self.weights.parent = self


                        class AdminDistances(object):
                            """
                            Per\-route administrative
                            distanceconfiguration
                            
                            .. attribute:: admin_distance
                            
                            	Administrative distance configuration. The supplied distance is applied to all routes discovered from the specified source, or only those that match the supplied prefix list if this is specified
                            	**type**\: list of :py:class:`AdminDistance <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.admin_distance = YList()
                                self.admin_distance.parent = self
                                self.admin_distance.name = 'admin_distance'


                            class AdminDistance(object):
                                """
                                Administrative distance configuration. The
                                supplied distance is applied to all routes
                                discovered from the specified source, or
                                only those that match the supplied prefix
                                list if this is specified
                                
                                .. attribute:: address_prefix
                                
                                	IP route source prefix
                                	**type**\: one of { str | str }
                                
                                .. attribute:: distance
                                
                                	Administrative distance
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                .. attribute:: prefix_list
                                
                                	List of prefixes to which this distance applies
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address_prefix = None
                                    self.distance = None
                                    self.prefix_list = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.address_prefix is None:
                                        raise YPYDataValidationError('Key property address_prefix is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-distance[Cisco-IOS-XR-clns-isis-cfg:address-prefix = ' + str(self.address_prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.address_prefix is not None:
                                        return True

                                    if self.distance is not None:
                                        return True

                                    if self.prefix_list is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-distances'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.admin_distance is not None:
                                    for child_ref in self.admin_distance:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances']['meta_info']


                        class DefaultInformation(object):
                            """
                            Control origination of a default route with
                            the option of using a policy.  If no policy
                            is specified the default route is
                            advertised with zero cost in level 2 only.
                            
                            .. attribute:: external
                            
                            	Flag to indicate that the default prefix should be originated as an external route
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\: str
                            
                            .. attribute:: use_policy
                            
                            	Flag to indicate whether default origination is controlled using a policy
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.external = None
                                self.policy_name = None
                                self.use_policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:default-information'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.external is not None:
                                    return True

                                if self.policy_name is not None:
                                    return True

                                if self.use_policy is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation']['meta_info']


                        class FrrTable(object):
                            """
                            Fast\-ReRoute configuration
                            
                            .. attribute:: frr_load_sharings
                            
                            	Load share prefixes across multiple backups
                            	**type**\: :py:class:`FrrLoadSharings <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings>`
                            
                            .. attribute:: frr_remote_lfa_prefixes
                            
                            	FRR remote LFA prefix list filter configuration
                            	**type**\: :py:class:`FrrRemoteLfaPrefixes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes>`
                            
                            .. attribute:: frr_tiebreakers
                            
                            	FRR tiebreakers configuration
                            	**type**\: :py:class:`FrrTiebreakers <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers>`
                            
                            .. attribute:: frr_use_cand_onlies
                            
                            	FRR use candidate only configuration
                            	**type**\: :py:class:`FrrUseCandOnlies <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies>`
                            
                            .. attribute:: priority_limits
                            
                            	FRR prefix\-limit configuration
                            	**type**\: :py:class:`PriorityLimits <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.frr_load_sharings = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings()
                                self.frr_load_sharings.parent = self
                                self.frr_remote_lfa_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes()
                                self.frr_remote_lfa_prefixes.parent = self
                                self.frr_tiebreakers = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers()
                                self.frr_tiebreakers.parent = self
                                self.frr_use_cand_onlies = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies()
                                self.frr_use_cand_onlies.parent = self
                                self.priority_limits = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits()
                                self.priority_limits.parent = self


                            class FrrLoadSharings(object):
                                """
                                Load share prefixes across multiple
                                backups
                                
                                .. attribute:: frr_load_sharing
                                
                                	Disable load sharing
                                	**type**\: list of :py:class:`FrrLoadSharing <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_load_sharing = YList()
                                    self.frr_load_sharing.parent = self
                                    self.frr_load_sharing.name = 'frr_load_sharing'


                                class FrrLoadSharing(object):
                                    """
                                    Disable load sharing
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    .. attribute:: load_sharing
                                    
                                    	Load sharing
                                    	**type**\: :py:class:`IsisfrrLoadSharing_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisfrrLoadSharing_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.load_sharing = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-load-sharing[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.load_sharing is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-load-sharings'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.frr_load_sharing is not None:
                                        for child_ref in self.frr_load_sharing:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings']['meta_info']


                            class FrrRemoteLfaPrefixes(object):
                                """
                                FRR remote LFA prefix list filter
                                configuration
                                
                                .. attribute:: frr_remote_lfa_prefix
                                
                                	Filter remote LFA router IDs using prefix\-list
                                	**type**\: list of :py:class:`FrrRemoteLfaPrefix <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_remote_lfa_prefix = YList()
                                    self.frr_remote_lfa_prefix.parent = self
                                    self.frr_remote_lfa_prefix.name = 'frr_remote_lfa_prefix'


                                class FrrRemoteLfaPrefix(object):
                                    """
                                    Filter remote LFA router IDs using
                                    prefix\-list
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    .. attribute:: prefix_list_name
                                    
                                    	Name of the prefix list
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.prefix_list_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-prefix[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.prefix_list_name is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-prefixes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.frr_remote_lfa_prefix is not None:
                                        for child_ref in self.frr_remote_lfa_prefix:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes']['meta_info']


                            class FrrTiebreakers(object):
                                """
                                FRR tiebreakers configuration
                                
                                .. attribute:: frr_tiebreaker
                                
                                	Configure tiebreaker for multiple backups
                                	**type**\: list of :py:class:`FrrTiebreaker <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_tiebreaker = YList()
                                    self.frr_tiebreaker.parent = self
                                    self.frr_tiebreaker.name = 'frr_tiebreaker'


                                class FrrTiebreaker(object):
                                    """
                                    Configure tiebreaker for multiple backups
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    .. attribute:: tiebreaker
                                    
                                    	Tiebreaker for which configuration applies
                                    	**type**\: :py:class:`IsisfrrTiebreaker_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisfrrTiebreaker_Enum>`
                                    
                                    .. attribute:: index
                                    
                                    	Preference order among tiebreakers
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.tiebreaker = None
                                        self.index = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')
                                        if self.tiebreaker is None:
                                            raise YPYDataValidationError('Key property tiebreaker is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-tiebreaker[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:tiebreaker = ' + str(self.tiebreaker) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.tiebreaker is not None:
                                            return True

                                        if self.index is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-tiebreakers'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.frr_tiebreaker is not None:
                                        for child_ref in self.frr_tiebreaker:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers']['meta_info']


                            class FrrUseCandOnlies(object):
                                """
                                FRR use candidate only configuration
                                
                                .. attribute:: frr_use_cand_only
                                
                                	Configure use candidate only to exclude interfaces as backup
                                	**type**\: list of :py:class:`FrrUseCandOnly <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.frr_use_cand_only = YList()
                                    self.frr_use_cand_only.parent = self
                                    self.frr_use_cand_only.name = 'frr_use_cand_only'


                                class FrrUseCandOnly(object):
                                    """
                                    Configure use candidate only to exclude
                                    interfaces as backup
                                    
                                    .. attribute:: frr_type
                                    
                                    	Computation Type
                                    	**type**\: :py:class:`Isisfrr_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isisfrr_Enum>`
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.frr_type = None
                                        self.level = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.frr_type is None:
                                            raise YPYDataValidationError('Key property frr_type is None')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-use-cand-only[Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + '][Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.frr_type is not None:
                                            return True

                                        if self.level is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-use-cand-onlies'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.frr_use_cand_only is not None:
                                        for child_ref in self.frr_use_cand_only:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies']['meta_info']


                            class PriorityLimits(object):
                                """
                                FRR prefix\-limit configuration
                                
                                .. attribute:: priority_limit
                                
                                	Limit backup computation upto the prefix priority
                                	**type**\: list of :py:class:`PriorityLimit <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.priority_limit = YList()
                                    self.priority_limit.parent = self
                                    self.priority_limit.name = 'priority_limit'


                                class PriorityLimit(object):
                                    """
                                    Limit backup computation upto the prefix
                                    priority
                                    
                                    .. attribute:: frr_type
                                    
                                    	Computation Type
                                    	**type**\: :py:class:`Isisfrr_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isisfrr_Enum>`
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    .. attribute:: priority
                                    
                                    	Compute for all prefixes upto the specified priority
                                    	**type**\: :py:class:`IsisPrefixPriority_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.frr_type = None
                                        self.level = None
                                        self.priority = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.frr_type is None:
                                            raise YPYDataValidationError('Key property frr_type is None')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priority-limit[Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + '][Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.frr_type is not None:
                                            return True

                                        if self.level is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priority-limits'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.priority_limit is not None:
                                        for child_ref in self.priority_limit:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-table'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.frr_load_sharings is not None and self.frr_load_sharings._has_data():
                                    return True

                                if self.frr_load_sharings is not None and self.frr_load_sharings.is_presence():
                                    return True

                                if self.frr_remote_lfa_prefixes is not None and self.frr_remote_lfa_prefixes._has_data():
                                    return True

                                if self.frr_remote_lfa_prefixes is not None and self.frr_remote_lfa_prefixes.is_presence():
                                    return True

                                if self.frr_tiebreakers is not None and self.frr_tiebreakers._has_data():
                                    return True

                                if self.frr_tiebreakers is not None and self.frr_tiebreakers.is_presence():
                                    return True

                                if self.frr_use_cand_onlies is not None and self.frr_use_cand_onlies._has_data():
                                    return True

                                if self.frr_use_cand_onlies is not None and self.frr_use_cand_onlies.is_presence():
                                    return True

                                if self.priority_limits is not None and self.priority_limits._has_data():
                                    return True

                                if self.priority_limits is not None and self.priority_limits.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable']['meta_info']


                        class Ispf(object):
                            """
                            ISPF configuration
                            
                            .. attribute:: states
                            
                            	ISPF state (enable/disable)
                            	**type**\: :py:class:`States <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.states = Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States()
                                self.states.parent = self


                            class States(object):
                                """
                                ISPF state (enable/disable)
                                
                                .. attribute:: state
                                
                                	Enable/disable ISPF
                                	**type**\: list of :py:class:`State <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.state = YList()
                                    self.state.parent = self
                                    self.state.name = 'state'


                                class State(object):
                                    """
                                    Enable/disable ISPF
                                    
                                    .. attribute:: level
                                    
                                    	Level to which configuration applies
                                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\: :py:class:`IsisispfState_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisispfState_Enum>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.state = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.level is None:
                                            raise YPYDataValidationError('Key property level is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:state[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.state is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:states'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.state is not None:
                                        for child_ref in self.state:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ispf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.states is not None and self.states._has_data():
                                    return True

                                if self.states is not None and self.states.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ispf']['meta_info']


                        class MaxRedistPrefixes(object):
                            """
                            Maximum number of redistributed
                            prefixesconfiguration
                            
                            .. attribute:: max_redist_prefix
                            
                            	An upper limit on the number of redistributed prefixes which may be included in the local system's LSP
                            	**type**\: list of :py:class:`MaxRedistPrefix <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.max_redist_prefix = YList()
                                self.max_redist_prefix.parent = self
                                self.max_redist_prefix.name = 'max_redist_prefix'


                            class MaxRedistPrefix(object):
                                """
                                An upper limit on the number of
                                redistributed prefixes which may be
                                included in the local system's LSP
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: prefix_limit
                                
                                	Max number of prefixes
                                	**type**\: int
                                
                                	**range:** 1..28000
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.prefix_limit = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-redist-prefix[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.prefix_limit is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-redist-prefixes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.max_redist_prefix is not None:
                                    for child_ref in self.max_redist_prefix:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes']['meta_info']


                        class MetricStyles(object):
                            """
                            Metric\-style configuration
                            
                            .. attribute:: metric_style
                            
                            	Configuration of metric style in LSPs
                            	**type**\: list of :py:class:`MetricStyle <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.metric_style = YList()
                                self.metric_style.parent = self
                                self.metric_style.name = 'metric_style'


                            class MetricStyle(object):
                                """
                                Configuration of metric style in LSPs
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: style
                                
                                	Metric Style
                                	**type**\: :py:class:`IsisMetricStyle_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyle_Enum>`
                                
                                .. attribute:: transition_state
                                
                                	Transition state
                                	**type**\: :py:class:`IsisMetricStyleTransition_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyleTransition_Enum>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.style = None
                                    self.transition_state = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric-style[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.style is not None:
                                        return True

                                    if self.transition_state is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric-styles'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.metric_style is not None:
                                    for child_ref in self.metric_style:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles']['meta_info']


                        class Metrics(object):
                            """
                            Metric configuration
                            
                            .. attribute:: metric
                            
                            	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                            	**type**\: list of :py:class:`Metric <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.metric = YList()
                                self.metric.parent = self
                                self.metric.name = 'metric'


                            class Metric(object):
                                """
                                Metric configuration. Legal value depends on
                                the metric\-style specified for the topology. If
                                the metric\-style defined is narrow, then only a
                                value between <1\-63> is allowed and if the
                                metric\-style is defined as wide, then a value
                                between <1\-16777215> is allowed as the metric
                                value.  All routers exclude links with the
                                maximum wide metric (16777215) from their SPF
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: metric
                                
                                	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                	**type**\: one of { :py:class:`Metric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_Enum>` | int }
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.metric = None

                                class Metric_Enum(Enum):
                                    """
                                    Metric_Enum

                                    Allowed metric\: <1\-63> for narrow,
                                    <1\-16777215> for wide

                                    """

                                    """

                                    Maximum wide metric.  All routers will
                                    exclude this link from their SPF

                                    """
                                    MAXIMUM = 16777215


                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric.Metric_Enum']


                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.metric is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metrics'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.metric is not None:
                                    for child_ref in self.metric:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Metrics']['meta_info']


                        class MicroLoopAvoidance(object):
                            """
                            Micro Loop Avoidance configuration
                            
                            .. attribute:: enable
                            
                            	MicroLoop avoidance enable configuration
                            	**type**\: :py:class:`IsisMicroLoopAvoidance_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMicroLoopAvoidance_Enum>`
                            
                            .. attribute:: rib_update_delay
                            
                            	Value of delay in msecs in updating RIB
                            	**type**\: int
                            
                            	**range:** 1000..65535
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.rib_update_delay = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:micro-loop-avoidance'

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

                                if self.rib_update_delay is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance']['meta_info']


                        class MonitorConvergence(object):
                            """
                            Enable convergence monitoring
                            
                            .. attribute:: enable
                            
                            	Enable convergence monitoring
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: prefix_list
                            
                            	Enable the monitoring of individual prefixes (prefix list name)
                            	**type**\: str
                            
                            .. attribute:: track_ip_frr
                            
                            	Enable the Tracking of IP\-Frr Convergence
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None
                                self.prefix_list = None
                                self.track_ip_frr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:monitor-convergence'

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

                                if self.prefix_list is not None:
                                    return True

                                if self.track_ip_frr is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence']['meta_info']


                        class Mpls(object):
                            """
                            MPLS configuration. MPLS configuration will
                            only be applied for the IPv4\-unicast
                            address\-family.
                            
                            .. attribute:: igp_intact
                            
                            	Install TE and non\-TE nexthops in the RIB
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: level
                            
                            	Enable MPLS for an IS\-IS at the given levels
                            	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                            
                            .. attribute:: multicast_intact
                            
                            	Install non\-TE nexthops in the RIB for use by multicast
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: router_id
                            
                            	Traffic Engineering stable IP address for system
                            	**type**\: :py:class:`RouterId <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.igp_intact = None
                                self.level = None
                                self.multicast_intact = None
                                self.router_id = Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId()
                                self.router_id.parent = self


                            class RouterId(object):
                                """
                                Traffic Engineering stable IP address for
                                system
                                
                                .. attribute:: address
                                
                                	IPv4 address to be used as a router ID. Precisely one of Address and Interface must be specified
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                                	**type**\: str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None
                                    self.interface_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:router-id'

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

                                    if self.interface_name is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.igp_intact is not None:
                                    return True

                                if self.level is not None:
                                    return True

                                if self.multicast_intact is not None:
                                    return True

                                if self.router_id is not None and self.router_id._has_data():
                                    return True

                                if self.router_id is not None and self.router_id.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Mpls']['meta_info']


                        class MplsLdpGlobal(object):
                            """
                            MPLS LDP configuration. MPLS LDP
                            configuration will only be applied for the
                            IPv4\-unicast address\-family.
                            
                            .. attribute:: auto_config
                            
                            	If TRUE, LDP will be enabled onall IS\-IS interfaces enabled for this address\-family
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.auto_config = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls-ldp-global'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.auto_config is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal']['meta_info']


                        class Propagations(object):
                            """
                            Route propagation configuration
                            
                            .. attribute:: propagation
                            
                            	Propagate routes between IS\-IS levels
                            	**type**\: list of :py:class:`Propagation <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.propagation = YList()
                                self.propagation.parent = self
                                self.propagation.name = 'propagation'


                            class Propagation(object):
                                """
                                Propagate routes between IS\-IS levels
                                
                                .. attribute:: destination_level
                                
                                	Destination level for routes.  Must differ from SourceLevel
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: source_level
                                
                                	Source level for routes
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: route_policy_name
                                
                                	Route policy limiting routes to be propagated
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.destination_level = None
                                    self.source_level = None
                                    self.route_policy_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.destination_level is None:
                                        raise YPYDataValidationError('Key property destination_level is None')
                                    if self.source_level is None:
                                        raise YPYDataValidationError('Key property source_level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:propagation[Cisco-IOS-XR-clns-isis-cfg:destination-level = ' + str(self.destination_level) + '][Cisco-IOS-XR-clns-isis-cfg:source-level = ' + str(self.source_level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.destination_level is not None:
                                        return True

                                    if self.source_level is not None:
                                        return True

                                    if self.route_policy_name is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:propagations'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.propagation is not None:
                                    for child_ref in self.propagation:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Propagations']['meta_info']


                        class Redistributions(object):
                            """
                            Protocol redistribution configuration
                            
                            .. attribute:: redistribution
                            
                            	Redistribution of other protocols into this IS\-IS instance
                            	**type**\: list of :py:class:`Redistribution <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.redistribution = YList()
                                self.redistribution.parent = self
                                self.redistribution.name = 'redistribution'


                            class Redistribution(object):
                                """
                                Redistribution of other protocols into
                                this IS\-IS instance
                                
                                .. attribute:: protocol_name
                                
                                	The protocol to be redistributed.  OSPFv3 may not be specified for an IPv4 topology and OSPF may not be specified for an IPv6 topology
                                	**type**\: :py:class:`IsisRedistProto_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisRedistProto_Enum>`
                                
                                .. attribute:: bgp
                                
                                	bgp
                                	**type**\: list of :py:class:`Bgp <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp>`
                                
                                .. attribute:: connected_or_static_or_rip_or_subscriber_or_mobile
                                
                                	connected or static or rip or subscriber or mobile
                                	**type**\: :py:class:`ConnectedOrStaticOrRipOrSubscriberOrMobile <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile>`
                                
                                .. attribute:: eigrp
                                
                                	eigrp
                                	**type**\: list of :py:class:`Eigrp <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp>`
                                
                                .. attribute:: ospf_or_ospfv3_or_isis_or_application
                                
                                	ospf or ospfv3 or isis or application
                                	**type**\: list of :py:class:`OspfOrOspfv3OrIsisOrApplication <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.protocol_name = None
                                    self.bgp = YList()
                                    self.bgp.parent = self
                                    self.bgp.name = 'bgp'
                                    self.connected_or_static_or_rip_or_subscriber_or_mobile = None
                                    self.eigrp = YList()
                                    self.eigrp.parent = self
                                    self.eigrp.name = 'eigrp'
                                    self.ospf_or_ospfv3_or_isis_or_application = YList()
                                    self.ospf_or_ospfv3_or_isis_or_application.parent = self
                                    self.ospf_or_ospfv3_or_isis_or_application.name = 'ospf_or_ospfv3_or_isis_or_application'


                                class Bgp(object):
                                    """
                                    bgp
                                    
                                    .. attribute:: as_xx
                                    
                                    	First half of BGP AS number in XX.YY format.  Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if second half is zero
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: as_yy
                                    
                                    	Second half of BGP AS number in XX.YY format. Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if first half is zero
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\: :py:class:`IsisMetric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetric_Enum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.as_xx = None
                                        self.as_yy = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.as_xx is None:
                                            raise YPYDataValidationError('Key property as_xx is None')
                                        if self.as_yy is None:
                                            raise YPYDataValidationError('Key property as_yy is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:bgp[Cisco-IOS-XR-clns-isis-cfg:as-xx = ' + str(self.as_xx) + '][Cisco-IOS-XR-clns-isis-cfg:as-yy = ' + str(self.as_yy) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.as_xx is not None:
                                            return True

                                        if self.as_yy is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp']['meta_info']


                                class ConnectedOrStaticOrRipOrSubscriberOrMobile(object):
                                    """
                                    connected or static or rip or subscriber
                                    or mobile
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\: :py:class:`IsisMetric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetric_Enum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:connected-or-static-or-rip-or-subscriber-or-mobile'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return True

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile']['meta_info']


                                class Eigrp(object):
                                    """
                                    eigrp
                                    
                                    .. attribute:: as_zz
                                    
                                    	Eigrp as number
                                    	**type**\: int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\: :py:class:`IsisMetric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetric_Enum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.as_zz = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.as_zz is None:
                                            raise YPYDataValidationError('Key property as_zz is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:eigrp[Cisco-IOS-XR-clns-isis-cfg:as-zz = ' + str(self.as_zz) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.as_zz is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp']['meta_info']


                                class OspfOrOspfv3OrIsisOrApplication(object):
                                    """
                                    ospf or ospfv3 or isis or application
                                    
                                    .. attribute:: instance_name
                                    
                                    	Protocol Instance Identifier.  Mandatory for ISIS, OSPF and application, must not be specified otherwise
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\: :py:class:`IsisMetric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisMetric_Enum>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.instance_name = None
                                        self.levels = None
                                        self.metric = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self.route_policy_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.instance_name is None:
                                            raise YPYDataValidationError('Key property instance_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ospf-or-ospfv3-or-isis-or-application[Cisco-IOS-XR-clns-isis-cfg:instance-name = ' + str(self.instance_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.instance_name is not None:
                                            return True

                                        if self.levels is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.metric_type is not None:
                                            return True

                                        if self.ospf_route_type is not None:
                                            return True

                                        if self.route_policy_name is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.protocol_name is None:
                                        raise YPYDataValidationError('Key property protocol_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:redistribution[Cisco-IOS-XR-clns-isis-cfg:protocol-name = ' + str(self.protocol_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.protocol_name is not None:
                                        return True

                                    if self.bgp is not None:
                                        for child_ref in self.bgp:
                                            if child_ref._has_data():
                                                return True

                                    if self.connected_or_static_or_rip_or_subscriber_or_mobile is not None and self.connected_or_static_or_rip_or_subscriber_or_mobile._has_data():
                                        return True

                                    if self.connected_or_static_or_rip_or_subscriber_or_mobile is not None and self.connected_or_static_or_rip_or_subscriber_or_mobile.is_presence():
                                        return True

                                    if self.eigrp is not None:
                                        for child_ref in self.eigrp:
                                            if child_ref._has_data():
                                                return True

                                    if self.ospf_or_ospfv3_or_isis_or_application is not None:
                                        for child_ref in self.ospf_or_ospfv3_or_isis_or_application:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:redistributions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.redistribution is not None:
                                    for child_ref in self.redistribution:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions']['meta_info']


                        class SegmentRouting(object):
                            """
                            Enable Segment Routing configuration
                            
                            .. attribute:: mpls
                            
                            	Prefer segment routing labels over LDP labels
                            	**type**\: :py:class:`IsisLabelPreference_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisLabelPreference_Enum>`
                            
                            .. attribute:: prefix_sid_map
                            
                            	Enable Segment Routing prefix SID map configuration
                            	**type**\: :py:class:`PrefixSidMap <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mpls = None
                                self.prefix_sid_map = Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap()
                                self.prefix_sid_map.parent = self


                            class PrefixSidMap(object):
                                """
                                Enable Segment Routing prefix SID map
                                configuration
                                
                                .. attribute:: advertise_local
                                
                                	Enable Segment Routing prefix SID map advertise local
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: receive
                                
                                	If TRUE, remote prefix SID map advertisements will be used. If FALSE, they will not be used
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.advertise_local = None
                                    self.receive = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-sid-map'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.advertise_local is not None:
                                        return True

                                    if self.receive is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:segment-routing'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.mpls is not None:
                                    return True

                                if self.prefix_sid_map is not None and self.prefix_sid_map._has_data():
                                    return True

                                if self.prefix_sid_map is not None and self.prefix_sid_map.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting']['meta_info']


                        class SpfIntervals(object):
                            """
                            SPF\-interval configuration
                            
                            .. attribute:: spf_interval
                            
                            	Route calculation scheduling parameters
                            	**type**\: list of :py:class:`SpfInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_interval = YList()
                                self.spf_interval.parent = self
                                self.spf_interval.name = 'spf_interval'


                            class SpfInterval(object):
                                """
                                Route calculation scheduling parameters
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: initial_wait
                                
                                	Initial wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                .. attribute:: maximum_wait
                                
                                	Maximum wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                .. attribute:: secondary_wait
                                
                                	Secondary wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.initial_wait = None
                                    self.maximum_wait = None
                                    self.secondary_wait = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.initial_wait is not None:
                                        return True

                                    if self.maximum_wait is not None:
                                        return True

                                    if self.secondary_wait is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-intervals'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.spf_interval is not None:
                                    for child_ref in self.spf_interval:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals']['meta_info']


                        class SpfPeriodicIntervals(object):
                            """
                            Peoridic SPF configuration
                            
                            .. attribute:: spf_periodic_interval
                            
                            	Maximum interval between spf runs
                            	**type**\: list of :py:class:`SpfPeriodicInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_periodic_interval = YList()
                                self.spf_periodic_interval.parent = self
                                self.spf_periodic_interval.name = 'spf_periodic_interval'


                            class SpfPeriodicInterval(object):
                                """
                                Maximum interval between spf runs
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: periodic_interval
                                
                                	Maximum interval in between SPF runs in seconds
                                	**type**\: int
                                
                                	**range:** 0..3600
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.periodic_interval = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-periodic-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.periodic_interval is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-periodic-intervals'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.spf_periodic_interval is not None:
                                    for child_ref in self.spf_periodic_interval:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals']['meta_info']


                        class SpfPrefixPriorities(object):
                            """
                            SPF Prefix Priority configuration
                            
                            .. attribute:: spf_prefix_priority
                            
                            	Determine SPF priority for prefixes
                            	**type**\: list of :py:class:`SpfPrefixPriority <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.spf_prefix_priority = YList()
                                self.spf_prefix_priority.parent = self
                                self.spf_prefix_priority.name = 'spf_prefix_priority'


                            class SpfPrefixPriority(object):
                                """
                                Determine SPF priority for prefixes
                                
                                .. attribute:: level
                                
                                	SPF Level for prefix prioritization
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: prefix_priority_type
                                
                                	SPF Priority to assign matching prefixes
                                	**type**\: :py:class:`IsisPrefixPriority_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority_Enum>`
                                
                                .. attribute:: access_list_name
                                
                                	Access List to determine prefixes for this priority
                                	**type**\: str
                                
                                .. attribute:: admin_tag
                                
                                	Tag value to determine prefixes for this priority
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.prefix_priority_type = None
                                    self.access_list_name = None
                                    self.admin_tag = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')
                                    if self.prefix_priority_type is None:
                                        raise YPYDataValidationError('Key property prefix_priority_type is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-prefix-priority[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + '][Cisco-IOS-XR-clns-isis-cfg:prefix-priority-type = ' + str(self.prefix_priority_type) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.prefix_priority_type is not None:
                                        return True

                                    if self.access_list_name is not None:
                                        return True

                                    if self.admin_tag is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:spf-prefix-priorities'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.spf_prefix_priority is not None:
                                    for child_ref in self.spf_prefix_priority:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities']['meta_info']


                        class SummaryPrefixes(object):
                            """
                            Summary\-prefix configuration
                            
                            .. attribute:: summary_prefix
                            
                            	Configure IP address prefixes to advertise
                            	**type**\: list of :py:class:`SummaryPrefix <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.summary_prefix = YList()
                                self.summary_prefix.parent = self
                                self.summary_prefix.name = 'summary_prefix'


                            class SummaryPrefix(object):
                                """
                                Configure IP address prefixes to advertise
                                
                                .. attribute:: address_prefix
                                
                                	IP summary address prefix
                                	**type**\: one of { str | str }
                                
                                .. attribute:: level
                                
                                	Level in which to summarize routes
                                	**type**\: int
                                
                                	**range:** 1..2
                                
                                .. attribute:: tag
                                
                                	The tag value
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address_prefix = None
                                    self.level = None
                                    self.tag = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.address_prefix is None:
                                        raise YPYDataValidationError('Key property address_prefix is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:summary-prefix[Cisco-IOS-XR-clns-isis-cfg:address-prefix = ' + str(self.address_prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.address_prefix is not None:
                                        return True

                                    if self.level is not None:
                                        return True

                                    if self.tag is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:summary-prefixes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.summary_prefix is not None:
                                    for child_ref in self.summary_prefix:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes']['meta_info']


                        class Ucmp(object):
                            """
                            UCMP (UnEqual Cost MultiPath) configuration
                            
                            .. attribute:: delay_interval
                            
                            	Delay in msecs between primary SPF and UCMP computation
                            	**type**\: int
                            
                            	**range:** 100..65535
                            
                            .. attribute:: enable
                            
                            	UCMP feature enable configuration
                            	**type**\: :py:class:`Enable <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable>`
                            
                            .. attribute:: exclude_interfaces
                            
                            	Interfaces excluded from UCMP path computation
                            	**type**\: :py:class:`ExcludeInterfaces <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.delay_interval = None
                                self.enable = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable()
                                self.enable.parent = self
                                self.exclude_interfaces = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces()
                                self.exclude_interfaces.parent = self


                            class Enable(object):
                                """
                                UCMP feature enable configuration
                                
                                .. attribute:: prefix_list_name
                                
                                	Name of the Prefix List
                                	**type**\: str
                                
                                .. attribute:: variance
                                
                                	Value of variance
                                	**type**\: int
                                
                                	**range:** 101..10000
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.prefix_list_name = None
                                    self.variance = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:enable'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.prefix_list_name is not None:
                                        return True

                                    if self.variance is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable']['meta_info']


                            class ExcludeInterfaces(object):
                                """
                                Interfaces excluded from UCMP path
                                computation
                                
                                .. attribute:: exclude_interface
                                
                                	Exclude this interface from UCMP path computation
                                	**type**\: list of :py:class:`ExcludeInterface <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.exclude_interface = YList()
                                    self.exclude_interface.parent = self
                                    self.exclude_interface.name = 'exclude_interface'


                                class ExcludeInterface(object):
                                    """
                                    Exclude this interface from UCMP path
                                    computation
                                    
                                    .. attribute:: interface_name
                                    
                                    	Name of the interface to be excluded
                                    	**type**\: str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
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

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:exclude-interface[Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + ']'

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
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:exclude-interfaces'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.exclude_interface is not None:
                                        for child_ref in self.exclude_interface:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:ucmp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.delay_interval is not None:
                                    return True

                                if self.enable is not None and self.enable._has_data():
                                    return True

                                if self.enable is not None and self.enable.is_presence():
                                    return True

                                if self.exclude_interfaces is not None and self.exclude_interfaces._has_data():
                                    return True

                                if self.exclude_interfaces is not None and self.exclude_interfaces.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp']['meta_info']


                        class Weights(object):
                            """
                            Weight configuration
                            
                            .. attribute:: weight
                            
                            	Weight configuration under interface for load balancing
                            	**type**\: list of :py:class:`Weight <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.weight = YList()
                                self.weight.parent = self
                                self.weight.name = 'weight'


                            class Weight(object):
                                """
                                Weight configuration under interface for load
                                balancing
                                
                                .. attribute:: level
                                
                                	Level to which configuration applies
                                	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                
                                .. attribute:: weight
                                
                                	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                	**type**\: int
                                
                                	**range:** 1..16777214
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.level = None
                                    self.weight = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.level is None:
                                        raise YPYDataValidationError('Key property level is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weight[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.level is not None:
                                        return True

                                    if self.weight is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weights'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.weight is not None:
                                    for child_ref in self.weight:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName.Weights']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.topology_name is None:
                                raise YPYDataValidationError('Key property topology_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:topology-name[Cisco-IOS-XR-clns-isis-cfg:topology-name = ' + str(self.topology_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.topology_name is not None:
                                return True

                            if self.adjacency_check is not None:
                                return True

                            if self.admin_distances is not None and self.admin_distances._has_data():
                                return True

                            if self.admin_distances is not None and self.admin_distances.is_presence():
                                return True

                            if self.advertise_passive_only is not None:
                                return True

                            if self.apply_weight is not None:
                                return True

                            if self.attached_bit is not None:
                                return True

                            if self.default_admin_distance is not None:
                                return True

                            if self.default_information is not None and self.default_information._has_data():
                                return True

                            if self.default_information is not None and self.default_information.is_presence():
                                return True

                            if self.frr_table is not None and self.frr_table._has_data():
                                return True

                            if self.frr_table is not None and self.frr_table.is_presence():
                                return True

                            if self.ignore_attached_bit is not None:
                                return True

                            if self.ispf is not None and self.ispf._has_data():
                                return True

                            if self.ispf is not None and self.ispf.is_presence():
                                return True

                            if self.max_redist_prefixes is not None and self.max_redist_prefixes._has_data():
                                return True

                            if self.max_redist_prefixes is not None and self.max_redist_prefixes.is_presence():
                                return True

                            if self.maximum_paths is not None:
                                return True

                            if self.metric_styles is not None and self.metric_styles._has_data():
                                return True

                            if self.metric_styles is not None and self.metric_styles.is_presence():
                                return True

                            if self.metrics is not None and self.metrics._has_data():
                                return True

                            if self.metrics is not None and self.metrics.is_presence():
                                return True

                            if self.micro_loop_avoidance is not None and self.micro_loop_avoidance._has_data():
                                return True

                            if self.micro_loop_avoidance is not None and self.micro_loop_avoidance.is_presence():
                                return True

                            if self.monitor_convergence is not None and self.monitor_convergence._has_data():
                                return True

                            if self.monitor_convergence is not None and self.monitor_convergence.is_presence():
                                return True

                            if self.mpls is not None and self.mpls._has_data():
                                return True

                            if self.mpls is not None and self.mpls.is_presence():
                                return True

                            if self.mpls_ldp_global is not None and self.mpls_ldp_global._has_data():
                                return True

                            if self.mpls_ldp_global is not None and self.mpls_ldp_global.is_presence():
                                return True

                            if self.propagations is not None and self.propagations._has_data():
                                return True

                            if self.propagations is not None and self.propagations.is_presence():
                                return True

                            if self.redistributions is not None and self.redistributions._has_data():
                                return True

                            if self.redistributions is not None and self.redistributions.is_presence():
                                return True

                            if self.route_source_first_hop is not None:
                                return True

                            if self.segment_routing is not None and self.segment_routing._has_data():
                                return True

                            if self.segment_routing is not None and self.segment_routing.is_presence():
                                return True

                            if self.single_topology is not None:
                                return True

                            if self.spf_intervals is not None and self.spf_intervals._has_data():
                                return True

                            if self.spf_intervals is not None and self.spf_intervals.is_presence():
                                return True

                            if self.spf_periodic_intervals is not None and self.spf_periodic_intervals._has_data():
                                return True

                            if self.spf_periodic_intervals is not None and self.spf_periodic_intervals.is_presence():
                                return True

                            if self.spf_prefix_priorities is not None and self.spf_prefix_priorities._has_data():
                                return True

                            if self.spf_prefix_priorities is not None and self.spf_prefix_priorities.is_presence():
                                return True

                            if self.summary_prefixes is not None and self.summary_prefixes._has_data():
                                return True

                            if self.summary_prefixes is not None and self.summary_prefixes.is_presence():
                                return True

                            if self.topology_id is not None:
                                return True

                            if self.ucmp is not None and self.ucmp._has_data():
                                return True

                            if self.ucmp is not None and self.ucmp.is_presence():
                                return True

                            if self.weights is not None and self.weights._has_data():
                                return True

                            if self.weights is not None and self.weights.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Afs.Af.TopologyName']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.af_name is None:
                            raise YPYDataValidationError('Key property af_name is None')
                        if self.saf_name is None:
                            raise YPYDataValidationError('Key property saf_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:af[Cisco-IOS-XR-clns-isis-cfg:af-name = ' + str(self.af_name) + '][Cisco-IOS-XR-clns-isis-cfg:saf-name = ' + str(self.saf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.af_name is not None:
                            return True

                        if self.saf_name is not None:
                            return True

                        if self.af_data is not None and self.af_data._has_data():
                            return True

                        if self.af_data is not None and self.af_data.is_presence():
                            return True

                        if self.topology_name is not None:
                            for child_ref in self.topology_name:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.Afs.Af']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:afs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.af is not None:
                        for child_ref in self.af:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Afs']['meta_info']


            class Distribute(object):
                """
                IS\-IS Distribute BGP\-LS configuration
                
                .. attribute:: dist_inst_id
                
                	Instance ID
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: dist_throttle
                
                	Seconds
                	**type**\: int
                
                	**range:** 5..20
                
                .. attribute:: level
                
                	Level
                	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.dist_inst_id = None
                    self.dist_throttle = None
                    self.level = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:distribute'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.dist_inst_id is not None:
                        return True

                    if self.dist_throttle is not None:
                        return True

                    if self.level is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return True

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Distribute']['meta_info']


            class Interfaces(object):
                """
                Per\-interface configuration
                
                .. attribute:: interface
                
                	Configuration for an IS\-IS interface
                	**type**\: list of :py:class:`Interface <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    Configuration for an IS\-IS interface
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: bfd
                    
                    	BFD configuration
                    	**type**\: :py:class:`Bfd <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Bfd>`
                    
                    .. attribute:: circuit_type
                    
                    	Configure circuit type for interface
                    	**type**\: :py:class:`IsisConfigurableLevels_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels_Enum>`
                    
                    .. attribute:: csnp_intervals
                    
                    	CSNP\-interval configuration
                    	**type**\: :py:class:`CsnpIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals>`
                    
                    .. attribute:: hello_accept_passwords
                    
                    	IIH accept password configuration
                    	**type**\: :py:class:`HelloAcceptPasswords <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords>`
                    
                    .. attribute:: hello_intervals
                    
                    	Hello\-interval configuration
                    	**type**\: :py:class:`HelloIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloIntervals>`
                    
                    .. attribute:: hello_multipliers
                    
                    	Hello\-multiplier configuration
                    	**type**\: :py:class:`HelloMultipliers <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers>`
                    
                    .. attribute:: hello_paddings
                    
                    	Hello\-padding configuration
                    	**type**\: :py:class:`HelloPaddings <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPaddings>`
                    
                    .. attribute:: hello_passwords
                    
                    	IIH password configuration
                    	**type**\: :py:class:`HelloPasswords <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPasswords>`
                    
                    .. attribute:: interface_afs
                    
                    	Per\-interface address\-family configuration
                    	**type**\: :py:class:`InterfaceAfs <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs>`
                    
                    .. attribute:: link_down_fast_detect
                    
                    	Configure high priority detection of interface down event
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: lsp_fast_flood_thresholds
                    
                    	LSP fast flood threshold configuration
                    	**type**\: :py:class:`LspFastFloodThresholds <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds>`
                    
                    .. attribute:: lsp_intervals
                    
                    	LSP\-interval configuration
                    	**type**\: :py:class:`LspIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspIntervals>`
                    
                    .. attribute:: lsp_retransmit_intervals
                    
                    	LSP\-retransmission\-interval configuration
                    	**type**\: :py:class:`LspRetransmitIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals>`
                    
                    .. attribute:: lsp_retransmit_throttle_intervals
                    
                    	LSP\-retransmission\-throttle\-interval configuration
                    	**type**\: :py:class:`LspRetransmitThrottleIntervals <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals>`
                    
                    .. attribute:: mesh_group
                    
                    	Mesh\-group configuration
                    	**type**\: one of { :py:class:`MeshGroup_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.MeshGroup_Enum>` | int }
                    
                    .. attribute:: point_to_point
                    
                    	IS\-IS will attempt to form point\-to\-point over LAN adjacencies over this interface
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: priorities
                    
                    	DIS\-election priority configuration
                    	**type**\: :py:class:`Priorities <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Priorities>`
                    
                    .. attribute:: running
                    
                    	This object must be set before any other configuration is supplied for an interface, and must be the last per\-interface configuration object to be removed
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: state
                    
                    	Enable/Disable routing
                    	**type**\: :py:class:`IsisInterfaceState_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceState_Enum>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.bfd = Isis.Instances.Instance.Interfaces.Interface.Bfd()
                        self.bfd.parent = self
                        self.circuit_type = None
                        self.csnp_intervals = Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals()
                        self.csnp_intervals.parent = self
                        self.hello_accept_passwords = Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords()
                        self.hello_accept_passwords.parent = self
                        self.hello_intervals = Isis.Instances.Instance.Interfaces.Interface.HelloIntervals()
                        self.hello_intervals.parent = self
                        self.hello_multipliers = Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers()
                        self.hello_multipliers.parent = self
                        self.hello_paddings = Isis.Instances.Instance.Interfaces.Interface.HelloPaddings()
                        self.hello_paddings.parent = self
                        self.hello_passwords = Isis.Instances.Instance.Interfaces.Interface.HelloPasswords()
                        self.hello_passwords.parent = self
                        self.interface_afs = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs()
                        self.interface_afs.parent = self
                        self.link_down_fast_detect = None
                        self.lsp_fast_flood_thresholds = Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds()
                        self.lsp_fast_flood_thresholds.parent = self
                        self.lsp_intervals = Isis.Instances.Instance.Interfaces.Interface.LspIntervals()
                        self.lsp_intervals.parent = self
                        self.lsp_retransmit_intervals = Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals()
                        self.lsp_retransmit_intervals.parent = self
                        self.lsp_retransmit_throttle_intervals = Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals()
                        self.lsp_retransmit_throttle_intervals.parent = self
                        self.mesh_group = None
                        self.point_to_point = None
                        self.priorities = Isis.Instances.Instance.Interfaces.Interface.Priorities()
                        self.priorities.parent = self
                        self.running = None
                        self.state = None

                    class MeshGroup_Enum(Enum):
                        """
                        MeshGroup_Enum

                        Mesh\-group configuration

                        """

                        """

                        Blocked mesh group.  Changed LSPs are not
                        flooded over blocked interfaces

                        """
                        BLOCKED = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.MeshGroup_Enum']



                    class Bfd(object):
                        """
                        BFD configuration
                        
                        .. attribute:: detection_multiplier
                        
                        	Detection multiplier for BFD sessions created by isis
                        	**type**\: int
                        
                        	**range:** 2..50
                        
                        .. attribute:: enable_ipv4
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\: bool
                        
                        .. attribute:: enable_ipv6
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\: bool
                        
                        .. attribute:: interval
                        
                        	Hello interval for BFD sessions created by isis
                        	**type**\: int
                        
                        	**range:** 3..30000
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.detection_multiplier = None
                            self.enable_ipv4 = None
                            self.enable_ipv6 = None
                            self.interval = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:bfd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.detection_multiplier is not None:
                                return True

                            if self.enable_ipv4 is not None:
                                return True

                            if self.enable_ipv6 is not None:
                                return True

                            if self.interval is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.Bfd']['meta_info']


                    class CsnpIntervals(object):
                        """
                        CSNP\-interval configuration
                        
                        .. attribute:: csnp_interval
                        
                        	CSNP\-interval configuration. No fixed default value as this depends on the media type of the interface
                        	**type**\: list of :py:class:`CsnpInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.csnp_interval = YList()
                            self.csnp_interval.parent = self
                            self.csnp_interval.name = 'csnp_interval'


                        class CsnpInterval(object):
                            """
                            CSNP\-interval configuration. No fixed
                            default value as this depends on the media
                            type of the interface.
                            
                            .. attribute:: level
                            
                            	Level to which configuration applies
                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYDataValidationError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:csnp-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.level is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:csnp-intervals'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.csnp_interval is not None:
                                for child_ref in self.csnp_interval:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals']['meta_info']


                    class HelloAcceptPasswords(object):
                        """
                        IIH accept password configuration
                        
                        .. attribute:: hello_accept_password
                        
                        	IIH accept passwords. This requires the existence of a HelloPassword of the same level
                        	**type**\: list of :py:class:`HelloAcceptPassword <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hello_accept_password = YList()
                            self.hello_accept_password.parent = self
                            self.hello_accept_password.name = 'hello_accept_password'


                        class HelloAcceptPassword(object):
                            """
                            IIH accept passwords. This requires the
                            existence of a HelloPassword of the same
                            level.
                            
                            .. attribute:: level
                            
                            	Level to which configuration applies
                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                            
                            .. attribute:: password
                            
                            	Password
                            	**type**\: str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.password = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYDataValidationError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-accept-password[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.level is not None:
                                    return True

                                if self.password is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-accept-passwords'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.hello_accept_password is not None:
                                for child_ref in self.hello_accept_password:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords']['meta_info']


                    class HelloIntervals(object):
                        """
                        Hello\-interval configuration
                        
                        .. attribute:: hello_interval
                        
                        	Hello\-interval configuration. The interval at which IIH packets will be sent. This will be three times quicker on a LAN interface which has been electted DIS
                        	**type**\: list of :py:class:`HelloInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hello_interval = YList()
                            self.hello_interval.parent = self
                            self.hello_interval.name = 'hello_interval'


                        class HelloInterval(object):
                            """
                            Hello\-interval configuration. The interval
                            at which IIH packets will be sent. This
                            will be three times quicker on a LAN
                            interface which has been electted DIS.
                            
                            .. attribute:: level
                            
                            	Level to which configuration applies
                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYDataValidationError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.level is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-intervals'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.hello_interval is not None:
                                for child_ref in self.hello_interval:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloIntervals']['meta_info']


                    class HelloMultipliers(object):
                        """
                        Hello\-multiplier configuration
                        
                        .. attribute:: hello_multiplier
                        
                        	Hello\-multiplier configuration. The number of successive IIHs that may be missed on an adjacency before it is considered down
                        	**type**\: list of :py:class:`HelloMultiplier <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hello_multiplier = YList()
                            self.hello_multiplier.parent = self
                            self.hello_multiplier.name = 'hello_multiplier'


                        class HelloMultiplier(object):
                            """
                            Hello\-multiplier configuration. The number
                            of successive IIHs that may be missed on an
                            adjacency before it is considered down.
                            
                            .. attribute:: level
                            
                            	Level to which configuration applies
                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                            
                            .. attribute:: multiplier
                            
                            	Hello multiplier value
                            	**type**\: int
                            
                            	**range:** 3..1000
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.multiplier = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYDataValidationError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-multiplier[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.level is not None:
                                    return True

                                if self.multiplier is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-multipliers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.hello_multiplier is not None:
                                for child_ref in self.hello_multiplier:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers']['meta_info']


                    class HelloPaddings(object):
                        """
                        Hello\-padding configuration
                        
                        .. attribute:: hello_padding
                        
                        	Pad IIHs to the interface MTU
                        	**type**\: list of :py:class:`HelloPadding <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hello_padding = YList()
                            self.hello_padding.parent = self
                            self.hello_padding.name = 'hello_padding'


                        class HelloPadding(object):
                            """
                            Pad IIHs to the interface MTU
                            
                            .. attribute:: level
                            
                            	Level to which configuration applies
                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                            
                            .. attribute:: padding_type
                            
                            	Hello padding type value
                            	**type**\: :py:class:`IsisHelloPadding_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisHelloPadding_Enum>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.padding_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYDataValidationError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-padding[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.level is not None:
                                    return True

                                if self.padding_type is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-paddings'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.hello_padding is not None:
                                for child_ref in self.hello_padding:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPaddings']['meta_info']


                    class HelloPasswords(object):
                        """
                        IIH password configuration
                        
                        .. attribute:: hello_password
                        
                        	IIH passwords. This must exist if a HelloAcceptPassword of the same level exists
                        	**type**\: list of :py:class:`HelloPassword <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.hello_password = YList()
                            self.hello_password.parent = self
                            self.hello_password.name = 'hello_password'


                        class HelloPassword(object):
                            """
                            IIH passwords. This must exist if a
                            HelloAcceptPassword of the same level
                            exists.
                            
                            .. attribute:: level
                            
                            	Level to which configuration applies
                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                            
                            .. attribute:: algorithm
                            
                            	Algorithm
                            	**type**\: :py:class:`IsisAuthenticationAlgorithm_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationAlgorithm_Enum>`
                            
                            .. attribute:: failure_mode
                            
                            	Failure Mode
                            	**type**\: :py:class:`IsisAuthenticationFailureMode_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationFailureMode_Enum>`
                            
                            .. attribute:: password
                            
                            	Password or unencrypted Key Chain name
                            	**type**\: str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.algorithm = None
                                self.failure_mode = None
                                self.password = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYDataValidationError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-password[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.level is not None:
                                    return True

                                if self.algorithm is not None:
                                    return True

                                if self.failure_mode is not None:
                                    return True

                                if self.password is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:hello-passwords'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.hello_password is not None:
                                for child_ref in self.hello_password:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.HelloPasswords']['meta_info']


                    class InterfaceAfs(object):
                        """
                        Per\-interface address\-family configuration
                        
                        .. attribute:: interface_af
                        
                        	Configuration for an IS\-IS address\-family on a single interface. If a named (non\-default) topology is being created it must be multicast. Also the topology ID mustbe set first and delete last in the router configuration
                        	**type**\: list of :py:class:`InterfaceAf <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_af = YList()
                            self.interface_af.parent = self
                            self.interface_af.name = 'interface_af'


                        class InterfaceAf(object):
                            """
                            Configuration for an IS\-IS address\-family
                            on a single interface. If a named
                            (non\-default) topology is being created it
                            must be multicast. Also the topology ID
                            mustbe set first and delete last in the
                            router configuration.
                            
                            .. attribute:: af_name
                            
                            	Address family
                            	**type**\: :py:class:`IsisAddressFamily_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisAddressFamily_Enum>`
                            
                            .. attribute:: saf_name
                            
                            	Sub address family
                            	**type**\: :py:class:`IsisSubAddressFamily_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisSubAddressFamily_Enum>`
                            
                            .. attribute:: interface_af_data
                            
                            	Data container
                            	**type**\: :py:class:`InterfaceAfData <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData>`
                            
                            .. attribute:: topology_name
                            
                            	keys\: topology\-name
                            	**type**\: list of :py:class:`TopologyName <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.saf_name = None
                                self.interface_af_data = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData()
                                self.interface_af_data.parent = self
                                self.topology_name = YList()
                                self.topology_name.parent = self
                                self.topology_name.name = 'topology_name'


                            class InterfaceAfData(object):
                                """
                                Data container.
                                
                                .. attribute:: admin_tags
                                
                                	admin\-tag configuration
                                	**type**\: :py:class:`AdminTags <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags>`
                                
                                .. attribute:: auto_metrics
                                
                                	AutoMetric configuration
                                	**type**\: :py:class:`AutoMetrics <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics>`
                                
                                .. attribute:: interface_af_state
                                
                                	Interface state
                                	**type**\: :py:class:`IsisInterfaceAfState_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceAfState_Enum>`
                                
                                .. attribute:: interface_frr_table
                                
                                	Fast\-ReRoute configuration
                                	**type**\: :py:class:`InterfaceFrrTable <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable>`
                                
                                .. attribute:: interface_link_group
                                
                                	Provide link group name and level
                                	**type**\: :py:class:`InterfaceLinkGroup <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup>`
                                
                                .. attribute:: metrics
                                
                                	Metric configuration
                                	**type**\: :py:class:`Metrics <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics>`
                                
                                .. attribute:: mpls_ldp
                                
                                	MPLS LDP configuration
                                	**type**\: :py:class:`MplsLdp <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp>`
                                
                                .. attribute:: prefix_sid
                                
                                	Assign prefix SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\: :py:class:`PrefixSid <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid>`
                                
                                .. attribute:: running
                                
                                	The presence of this object allows an address\-family to be run over the interface in question.This must be the first object created under the InterfaceAddressFamily container, and the last one deleted
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: weights
                                
                                	Weight configuration
                                	**type**\: :py:class:`Weights <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.admin_tags = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags()
                                    self.admin_tags.parent = self
                                    self.auto_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics()
                                    self.auto_metrics.parent = self
                                    self.interface_af_state = None
                                    self.interface_frr_table = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable()
                                    self.interface_frr_table.parent = self
                                    self.interface_link_group = None
                                    self.metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics()
                                    self.metrics.parent = self
                                    self.mpls_ldp = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp()
                                    self.mpls_ldp.parent = self
                                    self.prefix_sid = None
                                    self.running = None
                                    self.weights = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights()
                                    self.weights.parent = self


                                class AdminTags(object):
                                    """
                                    admin\-tag configuration
                                    
                                    .. attribute:: admin_tag
                                    
                                    	Admin tag for advertised interface connected routes
                                    	**type**\: list of :py:class:`AdminTag <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.admin_tag = YList()
                                        self.admin_tag.parent = self
                                        self.admin_tag.name = 'admin_tag'


                                    class AdminTag(object):
                                        """
                                        Admin tag for advertised interface
                                        connected routes
                                        
                                        .. attribute:: level
                                        
                                        	Level to which configuration applies
                                        	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                        
                                        .. attribute:: admin_tag
                                        
                                        	Tag to associate with connected routes
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.admin_tag = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYDataValidationError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-tag[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.level is not None:
                                                return True

                                            if self.admin_tag is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-tags'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.admin_tag is not None:
                                            for child_ref in self.admin_tag:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags']['meta_info']


                                class AutoMetrics(object):
                                    """
                                    AutoMetric configuration
                                    
                                    .. attribute:: auto_metric
                                    
                                    	AutoMetric Proactive\-Protect configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777214> is allowed as the auto\-metric value
                                    	**type**\: list of :py:class:`AutoMetric <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.auto_metric = YList()
                                        self.auto_metric.parent = self
                                        self.auto_metric.name = 'auto_metric'


                                    class AutoMetric(object):
                                        """
                                        AutoMetric Proactive\-Protect
                                        configuration. Legal value depends on
                                        the metric\-style specified for the
                                        topology. If the metric\-style defined is
                                        narrow, then only a value between <1\-63>
                                        is allowed and if the metric\-style is
                                        defined as wide, then a value between
                                        <1\-16777214> is allowed as the
                                        auto\-metric value.
                                        
                                        .. attribute:: level
                                        
                                        	Level to which configuration applies
                                        	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                        
                                        .. attribute:: proactive_protect
                                        
                                        	Allowed auto metric\:<1\-63> for narrow ,<1\-16777214> for wide
                                        	**type**\: int
                                        
                                        	**range:** 1..16777214
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.proactive_protect = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYDataValidationError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:auto-metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.level is not None:
                                                return True

                                            if self.proactive_protect is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:auto-metrics'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.auto_metric is not None:
                                            for child_ref in self.auto_metric:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics']['meta_info']


                                class InterfaceFrrTable(object):
                                    """
                                    Fast\-ReRoute configuration
                                    
                                    .. attribute:: frr_exclude_interfaces
                                    
                                    	FRR exclusion configuration
                                    	**type**\: :py:class:`FrrExcludeInterfaces <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces>`
                                    
                                    .. attribute:: frr_remote_lfa_max_metrics
                                    
                                    	Remote LFA maxmimum metric
                                    	**type**\: :py:class:`FrrRemoteLfaMaxMetrics <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics>`
                                    
                                    .. attribute:: frr_remote_lfa_types
                                    
                                    	Remote LFA Enable
                                    	**type**\: :py:class:`FrrRemoteLfaTypes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes>`
                                    
                                    .. attribute:: frr_types
                                    
                                    	Type of FRR computation per level
                                    	**type**\: :py:class:`FrrTypes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes>`
                                    
                                    .. attribute:: frrlfa_candidate_interfaces
                                    
                                    	FRR LFA candidate configuration
                                    	**type**\: :py:class:`FrrlfaCandidateInterfaces <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces>`
                                    
                                    .. attribute:: frrtilfa_types
                                    
                                    	TI LFA Enable
                                    	**type**\: :py:class:`FrrtilfaTypes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.frr_exclude_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces()
                                        self.frr_exclude_interfaces.parent = self
                                        self.frr_remote_lfa_max_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics()
                                        self.frr_remote_lfa_max_metrics.parent = self
                                        self.frr_remote_lfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes()
                                        self.frr_remote_lfa_types.parent = self
                                        self.frr_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes()
                                        self.frr_types.parent = self
                                        self.frrlfa_candidate_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces()
                                        self.frrlfa_candidate_interfaces.parent = self
                                        self.frrtilfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes()
                                        self.frrtilfa_types.parent = self


                                    class FrrExcludeInterfaces(object):
                                        """
                                        FRR exclusion configuration
                                        
                                        .. attribute:: frr_exclude_interface
                                        
                                        	Exclude an interface from computation
                                        	**type**\: list of :py:class:`FrrExcludeInterface <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_exclude_interface = YList()
                                            self.frr_exclude_interface.parent = self
                                            self.frr_exclude_interface.name = 'frr_exclude_interface'


                                        class FrrExcludeInterface(object):
                                            """
                                            Exclude an interface from computation
                                            
                                            .. attribute:: frr_type
                                            
                                            	Computation Type
                                            	**type**\: :py:class:`Isisfrr_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isisfrr_Enum>`
                                            
                                            .. attribute:: interface_name
                                            
                                            	Interface
                                            	**type**\: str
                                            
                                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\: int
                                            
                                            	**range:** 0..2
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.frr_type = None
                                                self.interface_name = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.frr_type is None:
                                                    raise YPYDataValidationError('Key property frr_type is None')
                                                if self.interface_name is None:
                                                    raise YPYDataValidationError('Key property interface_name is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-exclude-interface[Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + '][Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.frr_type is not None:
                                                    return True

                                                if self.interface_name is not None:
                                                    return True

                                                if self.level is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-exclude-interfaces'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frr_exclude_interface is not None:
                                                for child_ref in self.frr_exclude_interface:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info']


                                    class FrrRemoteLfaMaxMetrics(object):
                                        """
                                        Remote LFA maxmimum metric
                                        
                                        .. attribute:: frr_remote_lfa_max_metric
                                        
                                        	Configure the maximum metric for selecting a remote LFA node
                                        	**type**\: list of :py:class:`FrrRemoteLfaMaxMetric <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_remote_lfa_max_metric = YList()
                                            self.frr_remote_lfa_max_metric.parent = self
                                            self.frr_remote_lfa_max_metric.name = 'frr_remote_lfa_max_metric'


                                        class FrrRemoteLfaMaxMetric(object):
                                            """
                                            Configure the maximum metric for
                                            selecting a remote LFA node
                                            
                                            .. attribute:: level
                                            
                                            	Level to which configuration applies
                                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                            
                                            .. attribute:: max_metric
                                            
                                            	Value of the metric
                                            	**type**\: int
                                            
                                            	**range:** 1..16777215
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.max_metric = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYDataValidationError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-max-metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.level is not None:
                                                    return True

                                                if self.max_metric is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-max-metrics'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frr_remote_lfa_max_metric is not None:
                                                for child_ref in self.frr_remote_lfa_max_metric:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info']


                                    class FrrRemoteLfaTypes(object):
                                        """
                                        Remote LFA Enable
                                        
                                        .. attribute:: frr_remote_lfa_type
                                        
                                        	Enable remote lfa for a particular level
                                        	**type**\: list of :py:class:`FrrRemoteLfaType <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_remote_lfa_type = YList()
                                            self.frr_remote_lfa_type.parent = self
                                            self.frr_remote_lfa_type.name = 'frr_remote_lfa_type'


                                        class FrrRemoteLfaType(object):
                                            """
                                            Enable remote lfa for a particular
                                            level
                                            
                                            .. attribute:: level
                                            
                                            	Level to which configuration applies
                                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                            
                                            .. attribute:: type
                                            
                                            	Remote LFA Type
                                            	**type**\: :py:class:`IsisRemoteLfa_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisRemoteLfa_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYDataValidationError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.level is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frr_remote_lfa_type is not None:
                                                for child_ref in self.frr_remote_lfa_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info']


                                    class FrrTypes(object):
                                        """
                                        Type of FRR computation per level
                                        
                                        .. attribute:: frr_type
                                        
                                        	Type of computation for prefixes reachable via interface
                                        	**type**\: list of :py:class:`FrrType <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_type = YList()
                                            self.frr_type.parent = self
                                            self.frr_type.name = 'frr_type'


                                        class FrrType(object):
                                            """
                                            Type of computation for prefixes
                                            reachable via interface
                                            
                                            .. attribute:: level
                                            
                                            	Level to which configuration applies
                                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                            
                                            .. attribute:: type
                                            
                                            	Computation Type
                                            	**type**\: :py:class:`Isisfrr_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isisfrr_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYDataValidationError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.level is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frr_type is not None:
                                                for child_ref in self.frr_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes']['meta_info']


                                    class FrrlfaCandidateInterfaces(object):
                                        """
                                        FRR LFA candidate configuration
                                        
                                        .. attribute:: frrlfa_candidate_interface
                                        
                                        	Include an interface to LFA candidate in computation
                                        	**type**\: list of :py:class:`FrrlfaCandidateInterface <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frrlfa_candidate_interface = YList()
                                            self.frrlfa_candidate_interface.parent = self
                                            self.frrlfa_candidate_interface.name = 'frrlfa_candidate_interface'


                                        class FrrlfaCandidateInterface(object):
                                            """
                                            Include an interface to LFA candidate
                                            in computation
                                            
                                            .. attribute:: frr_type
                                            
                                            	Computation Type
                                            	**type**\: :py:class:`Isisfrr_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isisfrr_Enum>`
                                            
                                            .. attribute:: interface_name
                                            
                                            	Interface
                                            	**type**\: str
                                            
                                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\: int
                                            
                                            	**range:** 0..2
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.frr_type = None
                                                self.interface_name = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.frr_type is None:
                                                    raise YPYDataValidationError('Key property frr_type is None')
                                                if self.interface_name is None:
                                                    raise YPYDataValidationError('Key property interface_name is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrlfa-candidate-interface[Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + '][Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.frr_type is not None:
                                                    return True

                                                if self.interface_name is not None:
                                                    return True

                                                if self.level is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrlfa-candidate-interfaces'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frrlfa_candidate_interface is not None:
                                                for child_ref in self.frrlfa_candidate_interface:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info']


                                    class FrrtilfaTypes(object):
                                        """
                                        TI LFA Enable
                                        
                                        .. attribute:: frrtilfa_type
                                        
                                        	Enable TI lfa for a particular level
                                        	**type**\: list of :py:class:`FrrtilfaType <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frrtilfa_type = YList()
                                            self.frrtilfa_type.parent = self
                                            self.frrtilfa_type.name = 'frrtilfa_type'


                                        class FrrtilfaType(object):
                                            """
                                            Enable TI lfa for a particular level
                                            
                                            .. attribute:: level
                                            
                                            	Level to which configuration applies
                                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYDataValidationError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrtilfa-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.level is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrtilfa-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frrtilfa_type is not None:
                                                for child_ref in self.frrtilfa_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-table'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.frr_exclude_interfaces is not None and self.frr_exclude_interfaces._has_data():
                                            return True

                                        if self.frr_exclude_interfaces is not None and self.frr_exclude_interfaces.is_presence():
                                            return True

                                        if self.frr_remote_lfa_max_metrics is not None and self.frr_remote_lfa_max_metrics._has_data():
                                            return True

                                        if self.frr_remote_lfa_max_metrics is not None and self.frr_remote_lfa_max_metrics.is_presence():
                                            return True

                                        if self.frr_remote_lfa_types is not None and self.frr_remote_lfa_types._has_data():
                                            return True

                                        if self.frr_remote_lfa_types is not None and self.frr_remote_lfa_types.is_presence():
                                            return True

                                        if self.frr_types is not None and self.frr_types._has_data():
                                            return True

                                        if self.frr_types is not None and self.frr_types.is_presence():
                                            return True

                                        if self.frrlfa_candidate_interfaces is not None and self.frrlfa_candidate_interfaces._has_data():
                                            return True

                                        if self.frrlfa_candidate_interfaces is not None and self.frrlfa_candidate_interfaces.is_presence():
                                            return True

                                        if self.frrtilfa_types is not None and self.frrtilfa_types._has_data():
                                            return True

                                        if self.frrtilfa_types is not None and self.frrtilfa_types.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable']['meta_info']


                                class InterfaceLinkGroup(object):
                                    """
                                    Provide link group name and level
                                    
                                    .. attribute:: level
                                    
                                    	Level in which link group will be effective
                                    	**type**\: int
                                    
                                    	**range:** 0..2
                                    
                                    .. attribute:: link_group
                                    
                                    	Link Group
                                    	**type**\: str
                                    
                                    	**range:** 0..40
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.link_group = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-link-group'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.link_group is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return True

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup']['meta_info']


                                class Metrics(object):
                                    """
                                    Metric configuration
                                    
                                    .. attribute:: metric
                                    
                                    	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                                    	**type**\: list of :py:class:`Metric <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.metric = YList()
                                        self.metric.parent = self
                                        self.metric.name = 'metric'


                                    class Metric(object):
                                        """
                                        Metric configuration. Legal value depends on
                                        the metric\-style specified for the topology. If
                                        the metric\-style defined is narrow, then only a
                                        value between <1\-63> is allowed and if the
                                        metric\-style is defined as wide, then a value
                                        between <1\-16777215> is allowed as the metric
                                        value.  All routers exclude links with the
                                        maximum wide metric (16777215) from their SPF
                                        
                                        .. attribute:: level
                                        
                                        	Level to which configuration applies
                                        	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                        
                                        .. attribute:: metric
                                        
                                        	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                        	**type**\: one of { :py:class:`Metric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_Enum>` | int }
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.metric = None

                                        class Metric_Enum(Enum):
                                            """
                                            Metric_Enum

                                            Allowed metric\: <1\-63> for narrow,
                                            <1\-16777215> for wide

                                            """

                                            """

                                            Maximum wide metric.  All routers will
                                            exclude this link from their SPF

                                            """
                                            MAXIMUM = 16777215


                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric.Metric_Enum']


                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYDataValidationError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.level is not None:
                                                return True

                                            if self.metric is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metrics'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.metric is not None:
                                            for child_ref in self.metric:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics']['meta_info']


                                class MplsLdp(object):
                                    """
                                    MPLS LDP configuration
                                    
                                    .. attribute:: sync_level
                                    
                                    	Enable MPLS LDP Synchronization for an IS\-IS level
                                    	**type**\: int
                                    
                                    	**range:** 0..2
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.sync_level = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls-ldp'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.sync_level is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp']['meta_info']


                                class PrefixSid(object):
                                    """
                                    Assign prefix SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\: :py:class:`IsisexplicitNullFlag_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag_Enum>`
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\: :py:class:`NflagClear_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.NflagClear_Enum>`
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\: :py:class:`IsisphpFlag_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag_Enum>`
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\: :py:class:`Isissid_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isissid_Enum>`
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\: int
                                    
                                    	**range:** 0..1048575
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.explicit_null = None
                                        self.nflag_clear = None
                                        self.php = None
                                        self.type = None
                                        self.value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-sid'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.explicit_null is not None:
                                            return True

                                        if self.nflag_clear is not None:
                                            return True

                                        if self.php is not None:
                                            return True

                                        if self.type is not None:
                                            return True

                                        if self.value is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return True

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid']['meta_info']


                                class Weights(object):
                                    """
                                    Weight configuration
                                    
                                    .. attribute:: weight
                                    
                                    	Weight configuration under interface for load balancing
                                    	**type**\: list of :py:class:`Weight <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.weight = YList()
                                        self.weight.parent = self
                                        self.weight.name = 'weight'


                                    class Weight(object):
                                        """
                                        Weight configuration under interface for load
                                        balancing
                                        
                                        .. attribute:: level
                                        
                                        	Level to which configuration applies
                                        	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                        
                                        .. attribute:: weight
                                        
                                        	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                        	**type**\: int
                                        
                                        	**range:** 1..16777214
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.weight = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYDataValidationError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weight[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.level is not None:
                                                return True

                                            if self.weight is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weights'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.weight is not None:
                                            for child_ref in self.weight:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-af-data'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.admin_tags is not None and self.admin_tags._has_data():
                                        return True

                                    if self.admin_tags is not None and self.admin_tags.is_presence():
                                        return True

                                    if self.auto_metrics is not None and self.auto_metrics._has_data():
                                        return True

                                    if self.auto_metrics is not None and self.auto_metrics.is_presence():
                                        return True

                                    if self.interface_af_state is not None:
                                        return True

                                    if self.interface_frr_table is not None and self.interface_frr_table._has_data():
                                        return True

                                    if self.interface_frr_table is not None and self.interface_frr_table.is_presence():
                                        return True

                                    if self.interface_link_group is not None and self.interface_link_group._has_data():
                                        return True

                                    if self.interface_link_group is not None and self.interface_link_group.is_presence():
                                        return True

                                    if self.metrics is not None and self.metrics._has_data():
                                        return True

                                    if self.metrics is not None and self.metrics.is_presence():
                                        return True

                                    if self.mpls_ldp is not None and self.mpls_ldp._has_data():
                                        return True

                                    if self.mpls_ldp is not None and self.mpls_ldp.is_presence():
                                        return True

                                    if self.prefix_sid is not None and self.prefix_sid._has_data():
                                        return True

                                    if self.prefix_sid is not None and self.prefix_sid.is_presence():
                                        return True

                                    if self.running is not None:
                                        return True

                                    if self.weights is not None and self.weights._has_data():
                                        return True

                                    if self.weights is not None and self.weights.is_presence():
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData']['meta_info']


                            class TopologyName(object):
                                """
                                keys\: topology\-name
                                
                                .. attribute:: topology_name
                                
                                	Topology Name
                                	**type**\: str
                                
                                	**range:** 0..32
                                
                                .. attribute:: admin_tags
                                
                                	admin\-tag configuration
                                	**type**\: :py:class:`AdminTags <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags>`
                                
                                .. attribute:: auto_metrics
                                
                                	AutoMetric configuration
                                	**type**\: :py:class:`AutoMetrics <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics>`
                                
                                .. attribute:: interface_af_state
                                
                                	Interface state
                                	**type**\: :py:class:`IsisInterfaceAfState_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceAfState_Enum>`
                                
                                .. attribute:: interface_frr_table
                                
                                	Fast\-ReRoute configuration
                                	**type**\: :py:class:`InterfaceFrrTable <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable>`
                                
                                .. attribute:: interface_link_group
                                
                                	Provide link group name and level
                                	**type**\: :py:class:`InterfaceLinkGroup <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup>`
                                
                                .. attribute:: metrics
                                
                                	Metric configuration
                                	**type**\: :py:class:`Metrics <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics>`
                                
                                .. attribute:: mpls_ldp
                                
                                	MPLS LDP configuration
                                	**type**\: :py:class:`MplsLdp <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp>`
                                
                                .. attribute:: prefix_sid
                                
                                	Assign prefix SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\: :py:class:`PrefixSid <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid>`
                                
                                .. attribute:: running
                                
                                	The presence of this object allows an address\-family to be run over the interface in question.This must be the first object created under the InterfaceAddressFamily container, and the last one deleted
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: weights
                                
                                	Weight configuration
                                	**type**\: :py:class:`Weights <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.topology_name = None
                                    self.admin_tags = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags()
                                    self.admin_tags.parent = self
                                    self.auto_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics()
                                    self.auto_metrics.parent = self
                                    self.interface_af_state = None
                                    self.interface_frr_table = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable()
                                    self.interface_frr_table.parent = self
                                    self.interface_link_group = None
                                    self.metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics()
                                    self.metrics.parent = self
                                    self.mpls_ldp = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp()
                                    self.mpls_ldp.parent = self
                                    self.prefix_sid = None
                                    self.running = None
                                    self.weights = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights()
                                    self.weights.parent = self


                                class AdminTags(object):
                                    """
                                    admin\-tag configuration
                                    
                                    .. attribute:: admin_tag
                                    
                                    	Admin tag for advertised interface connected routes
                                    	**type**\: list of :py:class:`AdminTag <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.admin_tag = YList()
                                        self.admin_tag.parent = self
                                        self.admin_tag.name = 'admin_tag'


                                    class AdminTag(object):
                                        """
                                        Admin tag for advertised interface
                                        connected routes
                                        
                                        .. attribute:: level
                                        
                                        	Level to which configuration applies
                                        	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                        
                                        .. attribute:: admin_tag
                                        
                                        	Tag to associate with connected routes
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.admin_tag = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYDataValidationError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-tag[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.level is not None:
                                                return True

                                            if self.admin_tag is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:admin-tags'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.admin_tag is not None:
                                            for child_ref in self.admin_tag:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags']['meta_info']


                                class AutoMetrics(object):
                                    """
                                    AutoMetric configuration
                                    
                                    .. attribute:: auto_metric
                                    
                                    	AutoMetric Proactive\-Protect configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777214> is allowed as the auto\-metric value
                                    	**type**\: list of :py:class:`AutoMetric <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.auto_metric = YList()
                                        self.auto_metric.parent = self
                                        self.auto_metric.name = 'auto_metric'


                                    class AutoMetric(object):
                                        """
                                        AutoMetric Proactive\-Protect
                                        configuration. Legal value depends on
                                        the metric\-style specified for the
                                        topology. If the metric\-style defined is
                                        narrow, then only a value between <1\-63>
                                        is allowed and if the metric\-style is
                                        defined as wide, then a value between
                                        <1\-16777214> is allowed as the
                                        auto\-metric value.
                                        
                                        .. attribute:: level
                                        
                                        	Level to which configuration applies
                                        	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                        
                                        .. attribute:: proactive_protect
                                        
                                        	Allowed auto metric\:<1\-63> for narrow ,<1\-16777214> for wide
                                        	**type**\: int
                                        
                                        	**range:** 1..16777214
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.proactive_protect = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYDataValidationError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:auto-metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.level is not None:
                                                return True

                                            if self.proactive_protect is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:auto-metrics'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.auto_metric is not None:
                                            for child_ref in self.auto_metric:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics']['meta_info']


                                class InterfaceFrrTable(object):
                                    """
                                    Fast\-ReRoute configuration
                                    
                                    .. attribute:: frr_exclude_interfaces
                                    
                                    	FRR exclusion configuration
                                    	**type**\: :py:class:`FrrExcludeInterfaces <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces>`
                                    
                                    .. attribute:: frr_remote_lfa_max_metrics
                                    
                                    	Remote LFA maxmimum metric
                                    	**type**\: :py:class:`FrrRemoteLfaMaxMetrics <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics>`
                                    
                                    .. attribute:: frr_remote_lfa_types
                                    
                                    	Remote LFA Enable
                                    	**type**\: :py:class:`FrrRemoteLfaTypes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes>`
                                    
                                    .. attribute:: frr_types
                                    
                                    	Type of FRR computation per level
                                    	**type**\: :py:class:`FrrTypes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes>`
                                    
                                    .. attribute:: frrlfa_candidate_interfaces
                                    
                                    	FRR LFA candidate configuration
                                    	**type**\: :py:class:`FrrlfaCandidateInterfaces <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces>`
                                    
                                    .. attribute:: frrtilfa_types
                                    
                                    	TI LFA Enable
                                    	**type**\: :py:class:`FrrtilfaTypes <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.frr_exclude_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces()
                                        self.frr_exclude_interfaces.parent = self
                                        self.frr_remote_lfa_max_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics()
                                        self.frr_remote_lfa_max_metrics.parent = self
                                        self.frr_remote_lfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes()
                                        self.frr_remote_lfa_types.parent = self
                                        self.frr_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes()
                                        self.frr_types.parent = self
                                        self.frrlfa_candidate_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces()
                                        self.frrlfa_candidate_interfaces.parent = self
                                        self.frrtilfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes()
                                        self.frrtilfa_types.parent = self


                                    class FrrExcludeInterfaces(object):
                                        """
                                        FRR exclusion configuration
                                        
                                        .. attribute:: frr_exclude_interface
                                        
                                        	Exclude an interface from computation
                                        	**type**\: list of :py:class:`FrrExcludeInterface <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_exclude_interface = YList()
                                            self.frr_exclude_interface.parent = self
                                            self.frr_exclude_interface.name = 'frr_exclude_interface'


                                        class FrrExcludeInterface(object):
                                            """
                                            Exclude an interface from computation
                                            
                                            .. attribute:: frr_type
                                            
                                            	Computation Type
                                            	**type**\: :py:class:`Isisfrr_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isisfrr_Enum>`
                                            
                                            .. attribute:: interface_name
                                            
                                            	Interface
                                            	**type**\: str
                                            
                                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\: int
                                            
                                            	**range:** 0..2
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.frr_type = None
                                                self.interface_name = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.frr_type is None:
                                                    raise YPYDataValidationError('Key property frr_type is None')
                                                if self.interface_name is None:
                                                    raise YPYDataValidationError('Key property interface_name is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-exclude-interface[Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + '][Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.frr_type is not None:
                                                    return True

                                                if self.interface_name is not None:
                                                    return True

                                                if self.level is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-exclude-interfaces'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frr_exclude_interface is not None:
                                                for child_ref in self.frr_exclude_interface:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces']['meta_info']


                                    class FrrRemoteLfaMaxMetrics(object):
                                        """
                                        Remote LFA maxmimum metric
                                        
                                        .. attribute:: frr_remote_lfa_max_metric
                                        
                                        	Configure the maximum metric for selecting a remote LFA node
                                        	**type**\: list of :py:class:`FrrRemoteLfaMaxMetric <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_remote_lfa_max_metric = YList()
                                            self.frr_remote_lfa_max_metric.parent = self
                                            self.frr_remote_lfa_max_metric.name = 'frr_remote_lfa_max_metric'


                                        class FrrRemoteLfaMaxMetric(object):
                                            """
                                            Configure the maximum metric for
                                            selecting a remote LFA node
                                            
                                            .. attribute:: level
                                            
                                            	Level to which configuration applies
                                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                            
                                            .. attribute:: max_metric
                                            
                                            	Value of the metric
                                            	**type**\: int
                                            
                                            	**range:** 1..16777215
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.max_metric = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYDataValidationError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-max-metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.level is not None:
                                                    return True

                                                if self.max_metric is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-max-metrics'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frr_remote_lfa_max_metric is not None:
                                                for child_ref in self.frr_remote_lfa_max_metric:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics']['meta_info']


                                    class FrrRemoteLfaTypes(object):
                                        """
                                        Remote LFA Enable
                                        
                                        .. attribute:: frr_remote_lfa_type
                                        
                                        	Enable remote lfa for a particular level
                                        	**type**\: list of :py:class:`FrrRemoteLfaType <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_remote_lfa_type = YList()
                                            self.frr_remote_lfa_type.parent = self
                                            self.frr_remote_lfa_type.name = 'frr_remote_lfa_type'


                                        class FrrRemoteLfaType(object):
                                            """
                                            Enable remote lfa for a particular
                                            level
                                            
                                            .. attribute:: level
                                            
                                            	Level to which configuration applies
                                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                            
                                            .. attribute:: type
                                            
                                            	Remote LFA Type
                                            	**type**\: :py:class:`IsisRemoteLfa_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisRemoteLfa_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYDataValidationError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.level is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-remote-lfa-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frr_remote_lfa_type is not None:
                                                for child_ref in self.frr_remote_lfa_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes']['meta_info']


                                    class FrrTypes(object):
                                        """
                                        Type of FRR computation per level
                                        
                                        .. attribute:: frr_type
                                        
                                        	Type of computation for prefixes reachable via interface
                                        	**type**\: list of :py:class:`FrrType <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frr_type = YList()
                                            self.frr_type.parent = self
                                            self.frr_type.name = 'frr_type'


                                        class FrrType(object):
                                            """
                                            Type of computation for prefixes
                                            reachable via interface
                                            
                                            .. attribute:: level
                                            
                                            	Level to which configuration applies
                                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                            
                                            .. attribute:: type
                                            
                                            	Computation Type
                                            	**type**\: :py:class:`Isisfrr_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isisfrr_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None
                                                self.type = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYDataValidationError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.level is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frr-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frr_type is not None:
                                                for child_ref in self.frr_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes']['meta_info']


                                    class FrrlfaCandidateInterfaces(object):
                                        """
                                        FRR LFA candidate configuration
                                        
                                        .. attribute:: frrlfa_candidate_interface
                                        
                                        	Include an interface to LFA candidate in computation
                                        	**type**\: list of :py:class:`FrrlfaCandidateInterface <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frrlfa_candidate_interface = YList()
                                            self.frrlfa_candidate_interface.parent = self
                                            self.frrlfa_candidate_interface.name = 'frrlfa_candidate_interface'


                                        class FrrlfaCandidateInterface(object):
                                            """
                                            Include an interface to LFA candidate
                                            in computation
                                            
                                            .. attribute:: frr_type
                                            
                                            	Computation Type
                                            	**type**\: :py:class:`Isisfrr_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isisfrr_Enum>`
                                            
                                            .. attribute:: interface_name
                                            
                                            	Interface
                                            	**type**\: str
                                            
                                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\: int
                                            
                                            	**range:** 0..2
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.frr_type = None
                                                self.interface_name = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.frr_type is None:
                                                    raise YPYDataValidationError('Key property frr_type is None')
                                                if self.interface_name is None:
                                                    raise YPYDataValidationError('Key property interface_name is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrlfa-candidate-interface[Cisco-IOS-XR-clns-isis-cfg:frr-type = ' + str(self.frr_type) + '][Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.frr_type is not None:
                                                    return True

                                                if self.interface_name is not None:
                                                    return True

                                                if self.level is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrlfa-candidate-interfaces'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frrlfa_candidate_interface is not None:
                                                for child_ref in self.frrlfa_candidate_interface:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces']['meta_info']


                                    class FrrtilfaTypes(object):
                                        """
                                        TI LFA Enable
                                        
                                        .. attribute:: frrtilfa_type
                                        
                                        	Enable TI lfa for a particular level
                                        	**type**\: list of :py:class:`FrrtilfaType <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.frrtilfa_type = YList()
                                            self.frrtilfa_type.parent = self
                                            self.frrtilfa_type.name = 'frrtilfa_type'


                                        class FrrtilfaType(object):
                                            """
                                            Enable TI lfa for a particular level
                                            
                                            .. attribute:: level
                                            
                                            	Level to which configuration applies
                                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.level = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                                if self.level is None:
                                                    raise YPYDataValidationError('Key property level is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrtilfa-type[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.is_presence():
                                                    return True
                                                if self.level is not None:
                                                    return True

                                                return False

                                            def is_presence(self):
                                                ''' Returns True if this instance represents presence container else returns False '''
                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:frrtilfa-types'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.frrtilfa_type is not None:
                                                for child_ref in self.frrtilfa_type:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-frr-table'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.frr_exclude_interfaces is not None and self.frr_exclude_interfaces._has_data():
                                            return True

                                        if self.frr_exclude_interfaces is not None and self.frr_exclude_interfaces.is_presence():
                                            return True

                                        if self.frr_remote_lfa_max_metrics is not None and self.frr_remote_lfa_max_metrics._has_data():
                                            return True

                                        if self.frr_remote_lfa_max_metrics is not None and self.frr_remote_lfa_max_metrics.is_presence():
                                            return True

                                        if self.frr_remote_lfa_types is not None and self.frr_remote_lfa_types._has_data():
                                            return True

                                        if self.frr_remote_lfa_types is not None and self.frr_remote_lfa_types.is_presence():
                                            return True

                                        if self.frr_types is not None and self.frr_types._has_data():
                                            return True

                                        if self.frr_types is not None and self.frr_types.is_presence():
                                            return True

                                        if self.frrlfa_candidate_interfaces is not None and self.frrlfa_candidate_interfaces._has_data():
                                            return True

                                        if self.frrlfa_candidate_interfaces is not None and self.frrlfa_candidate_interfaces.is_presence():
                                            return True

                                        if self.frrtilfa_types is not None and self.frrtilfa_types._has_data():
                                            return True

                                        if self.frrtilfa_types is not None and self.frrtilfa_types.is_presence():
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable']['meta_info']


                                class InterfaceLinkGroup(object):
                                    """
                                    Provide link group name and level
                                    
                                    .. attribute:: level
                                    
                                    	Level in which link group will be effective
                                    	**type**\: int
                                    
                                    	**range:** 0..2
                                    
                                    .. attribute:: link_group
                                    
                                    	Link Group
                                    	**type**\: str
                                    
                                    	**range:** 0..40
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.level = None
                                        self.link_group = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-link-group'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.level is not None:
                                            return True

                                        if self.link_group is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return True

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup']['meta_info']


                                class Metrics(object):
                                    """
                                    Metric configuration
                                    
                                    .. attribute:: metric
                                    
                                    	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                                    	**type**\: list of :py:class:`Metric <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.metric = YList()
                                        self.metric.parent = self
                                        self.metric.name = 'metric'


                                    class Metric(object):
                                        """
                                        Metric configuration. Legal value depends on
                                        the metric\-style specified for the topology. If
                                        the metric\-style defined is narrow, then only a
                                        value between <1\-63> is allowed and if the
                                        metric\-style is defined as wide, then a value
                                        between <1\-16777215> is allowed as the metric
                                        value.  All routers exclude links with the
                                        maximum wide metric (16777215) from their SPF
                                        
                                        .. attribute:: level
                                        
                                        	Level to which configuration applies
                                        	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                        
                                        .. attribute:: metric
                                        
                                        	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                        	**type**\: one of { :py:class:`Metric_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_Enum>` | int }
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.metric = None

                                        class Metric_Enum(Enum):
                                            """
                                            Metric_Enum

                                            Allowed metric\: <1\-63> for narrow,
                                            <1\-16777215> for wide

                                            """

                                            """

                                            Maximum wide metric.  All routers will
                                            exclude this link from their SPF

                                            """
                                            MAXIMUM = 16777215


                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_Enum']


                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYDataValidationError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.level is not None:
                                                return True

                                            if self.metric is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:metrics'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.metric is not None:
                                            for child_ref in self.metric:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics']['meta_info']


                                class MplsLdp(object):
                                    """
                                    MPLS LDP configuration
                                    
                                    .. attribute:: sync_level
                                    
                                    	Enable MPLS LDP Synchronization for an IS\-IS level
                                    	**type**\: int
                                    
                                    	**range:** 0..2
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.sync_level = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:mpls-ldp'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.sync_level is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp']['meta_info']


                                class PrefixSid(object):
                                    """
                                    Assign prefix SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\: :py:class:`IsisexplicitNullFlag_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag_Enum>`
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\: :py:class:`NflagClear_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.NflagClear_Enum>`
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\: :py:class:`IsisphpFlag_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag_Enum>`
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\: :py:class:`Isissid_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isissid_Enum>`
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\: int
                                    
                                    	**range:** 0..1048575
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.explicit_null = None
                                        self.nflag_clear = None
                                        self.php = None
                                        self.type = None
                                        self.value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:prefix-sid'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.explicit_null is not None:
                                            return True

                                        if self.nflag_clear is not None:
                                            return True

                                        if self.php is not None:
                                            return True

                                        if self.type is not None:
                                            return True

                                        if self.value is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return True

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid']['meta_info']


                                class Weights(object):
                                    """
                                    Weight configuration
                                    
                                    .. attribute:: weight
                                    
                                    	Weight configuration under interface for load balancing
                                    	**type**\: list of :py:class:`Weight <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.weight = YList()
                                        self.weight.parent = self
                                        self.weight.name = 'weight'


                                    class Weight(object):
                                        """
                                        Weight configuration under interface for load
                                        balancing
                                        
                                        .. attribute:: level
                                        
                                        	Level to which configuration applies
                                        	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                                        
                                        .. attribute:: weight
                                        
                                        	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                        	**type**\: int
                                        
                                        	**range:** 1..16777214
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.level = None
                                            self.weight = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.level is None:
                                                raise YPYDataValidationError('Key property level is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weight[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.level is not None:
                                                return True

                                            if self.weight is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:weights'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.weight is not None:
                                            for child_ref in self.weight:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.topology_name is None:
                                        raise YPYDataValidationError('Key property topology_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:topology-name[Cisco-IOS-XR-clns-isis-cfg:topology-name = ' + str(self.topology_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.topology_name is not None:
                                        return True

                                    if self.admin_tags is not None and self.admin_tags._has_data():
                                        return True

                                    if self.admin_tags is not None and self.admin_tags.is_presence():
                                        return True

                                    if self.auto_metrics is not None and self.auto_metrics._has_data():
                                        return True

                                    if self.auto_metrics is not None and self.auto_metrics.is_presence():
                                        return True

                                    if self.interface_af_state is not None:
                                        return True

                                    if self.interface_frr_table is not None and self.interface_frr_table._has_data():
                                        return True

                                    if self.interface_frr_table is not None and self.interface_frr_table.is_presence():
                                        return True

                                    if self.interface_link_group is not None and self.interface_link_group._has_data():
                                        return True

                                    if self.interface_link_group is not None and self.interface_link_group.is_presence():
                                        return True

                                    if self.metrics is not None and self.metrics._has_data():
                                        return True

                                    if self.metrics is not None and self.metrics.is_presence():
                                        return True

                                    if self.mpls_ldp is not None and self.mpls_ldp._has_data():
                                        return True

                                    if self.mpls_ldp is not None and self.mpls_ldp.is_presence():
                                        return True

                                    if self.prefix_sid is not None and self.prefix_sid._has_data():
                                        return True

                                    if self.prefix_sid is not None and self.prefix_sid.is_presence():
                                        return True

                                    if self.running is not None:
                                        return True

                                    if self.weights is not None and self.weights._has_data():
                                        return True

                                    if self.weights is not None and self.weights.is_presence():
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                    return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.af_name is None:
                                    raise YPYDataValidationError('Key property af_name is None')
                                if self.saf_name is None:
                                    raise YPYDataValidationError('Key property saf_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-af[Cisco-IOS-XR-clns-isis-cfg:af-name = ' + str(self.af_name) + '][Cisco-IOS-XR-clns-isis-cfg:saf-name = ' + str(self.saf_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.af_name is not None:
                                    return True

                                if self.saf_name is not None:
                                    return True

                                if self.interface_af_data is not None and self.interface_af_data._has_data():
                                    return True

                                if self.interface_af_data is not None and self.interface_af_data.is_presence():
                                    return True

                                if self.topology_name is not None:
                                    for child_ref in self.topology_name:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface-afs'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.interface_af is not None:
                                for child_ref in self.interface_af:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs']['meta_info']


                    class LspFastFloodThresholds(object):
                        """
                        LSP fast flood threshold configuration
                        
                        .. attribute:: lsp_fast_flood_threshold
                        
                        	Number of LSPs to send back to back on an interface
                        	**type**\: list of :py:class:`LspFastFloodThreshold <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.lsp_fast_flood_threshold = YList()
                            self.lsp_fast_flood_threshold.parent = self
                            self.lsp_fast_flood_threshold.name = 'lsp_fast_flood_threshold'


                        class LspFastFloodThreshold(object):
                            """
                            Number of LSPs to send back to back on an
                            interface.
                            
                            .. attribute:: level
                            
                            	Level to which configuration applies
                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                            
                            .. attribute:: count
                            
                            	Count
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.count = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYDataValidationError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-fast-flood-threshold[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.level is not None:
                                    return True

                                if self.count is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-fast-flood-thresholds'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.lsp_fast_flood_threshold is not None:
                                for child_ref in self.lsp_fast_flood_threshold:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds']['meta_info']


                    class LspIntervals(object):
                        """
                        LSP\-interval configuration
                        
                        .. attribute:: lsp_interval
                        
                        	Interval between transmission of LSPs on interface
                        	**type**\: list of :py:class:`LspInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.lsp_interval = YList()
                            self.lsp_interval.parent = self
                            self.lsp_interval.name = 'lsp_interval'


                        class LspInterval(object):
                            """
                            Interval between transmission of LSPs on
                            interface.
                            
                            .. attribute:: level
                            
                            	Level to which configuration applies
                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                            
                            .. attribute:: interval
                            
                            	Milliseconds
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYDataValidationError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.level is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-intervals'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.lsp_interval is not None:
                                for child_ref in self.lsp_interval:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspIntervals']['meta_info']


                    class LspRetransmitIntervals(object):
                        """
                        LSP\-retransmission\-interval configuration
                        
                        .. attribute:: lsp_retransmit_interval
                        
                        	Interval between retransmissions of the same LSP
                        	**type**\: list of :py:class:`LspRetransmitInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.lsp_retransmit_interval = YList()
                            self.lsp_retransmit_interval.parent = self
                            self.lsp_retransmit_interval.name = 'lsp_retransmit_interval'


                        class LspRetransmitInterval(object):
                            """
                            Interval between retransmissions of the
                            same LSP
                            
                            .. attribute:: level
                            
                            	Level to which configuration applies
                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYDataValidationError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-retransmit-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.level is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-retransmit-intervals'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.lsp_retransmit_interval is not None:
                                for child_ref in self.lsp_retransmit_interval:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals']['meta_info']


                    class LspRetransmitThrottleIntervals(object):
                        """
                        LSP\-retransmission\-throttle\-interval
                        configuration
                        
                        .. attribute:: lsp_retransmit_throttle_interval
                        
                        	Minimum interval betwen retransissions of different LSPs
                        	**type**\: list of :py:class:`LspRetransmitThrottleInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.lsp_retransmit_throttle_interval = YList()
                            self.lsp_retransmit_throttle_interval.parent = self
                            self.lsp_retransmit_throttle_interval.name = 'lsp_retransmit_throttle_interval'


                        class LspRetransmitThrottleInterval(object):
                            """
                            Minimum interval betwen retransissions of
                            different LSPs
                            
                            .. attribute:: level
                            
                            	Level to which configuration applies
                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                            
                            .. attribute:: interval
                            
                            	Milliseconds
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYDataValidationError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-retransmit-throttle-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.level is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-retransmit-throttle-intervals'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.lsp_retransmit_throttle_interval is not None:
                                for child_ref in self.lsp_retransmit_throttle_interval:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals']['meta_info']


                    class Priorities(object):
                        """
                        DIS\-election priority configuration
                        
                        .. attribute:: priority
                        
                        	DIS\-election priority
                        	**type**\: list of :py:class:`Priority <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.priority = YList()
                            self.priority.parent = self
                            self.priority.name = 'priority'


                        class Priority(object):
                            """
                            DIS\-election priority
                            
                            .. attribute:: level
                            
                            	Level to which configuration applies
                            	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                            
                            .. attribute:: priority_value
                            
                            	Priority
                            	**type**\: int
                            
                            	**range:** 0..127
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.level = None
                                self.priority_value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.level is None:
                                    raise YPYDataValidationError('Key property level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priority[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.level is not None:
                                    return True

                                if self.priority_value is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                                return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:priorities'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.priority is not None:
                                for child_ref in self.priority:
                                    if child_ref._has_data():
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                            return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface.Priorities']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYDataValidationError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interface[Cisco-IOS-XR-clns-isis-cfg:interface-name = ' + str(self.interface_name) + ']'

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

                        if self.bfd is not None and self.bfd._has_data():
                            return True

                        if self.bfd is not None and self.bfd.is_presence():
                            return True

                        if self.circuit_type is not None:
                            return True

                        if self.csnp_intervals is not None and self.csnp_intervals._has_data():
                            return True

                        if self.csnp_intervals is not None and self.csnp_intervals.is_presence():
                            return True

                        if self.hello_accept_passwords is not None and self.hello_accept_passwords._has_data():
                            return True

                        if self.hello_accept_passwords is not None and self.hello_accept_passwords.is_presence():
                            return True

                        if self.hello_intervals is not None and self.hello_intervals._has_data():
                            return True

                        if self.hello_intervals is not None and self.hello_intervals.is_presence():
                            return True

                        if self.hello_multipliers is not None and self.hello_multipliers._has_data():
                            return True

                        if self.hello_multipliers is not None and self.hello_multipliers.is_presence():
                            return True

                        if self.hello_paddings is not None and self.hello_paddings._has_data():
                            return True

                        if self.hello_paddings is not None and self.hello_paddings.is_presence():
                            return True

                        if self.hello_passwords is not None and self.hello_passwords._has_data():
                            return True

                        if self.hello_passwords is not None and self.hello_passwords.is_presence():
                            return True

                        if self.interface_afs is not None and self.interface_afs._has_data():
                            return True

                        if self.interface_afs is not None and self.interface_afs.is_presence():
                            return True

                        if self.link_down_fast_detect is not None:
                            return True

                        if self.lsp_fast_flood_thresholds is not None and self.lsp_fast_flood_thresholds._has_data():
                            return True

                        if self.lsp_fast_flood_thresholds is not None and self.lsp_fast_flood_thresholds.is_presence():
                            return True

                        if self.lsp_intervals is not None and self.lsp_intervals._has_data():
                            return True

                        if self.lsp_intervals is not None and self.lsp_intervals.is_presence():
                            return True

                        if self.lsp_retransmit_intervals is not None and self.lsp_retransmit_intervals._has_data():
                            return True

                        if self.lsp_retransmit_intervals is not None and self.lsp_retransmit_intervals.is_presence():
                            return True

                        if self.lsp_retransmit_throttle_intervals is not None and self.lsp_retransmit_throttle_intervals._has_data():
                            return True

                        if self.lsp_retransmit_throttle_intervals is not None and self.lsp_retransmit_throttle_intervals.is_presence():
                            return True

                        if self.mesh_group is not None:
                            return True

                        if self.point_to_point is not None:
                            return True

                        if self.priorities is not None and self.priorities._has_data():
                            return True

                        if self.priorities is not None and self.priorities.is_presence():
                            return True

                        if self.running is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:interfaces'

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
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Interfaces']['meta_info']


            class LinkGroups(object):
                """
                Link Group
                
                .. attribute:: link_group
                
                	Configuration for link group name
                	**type**\: list of :py:class:`LinkGroup <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LinkGroups.LinkGroup>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.link_group = YList()
                    self.link_group.parent = self
                    self.link_group.name = 'link_group'


                class LinkGroup(object):
                    """
                    Configuration for link group name
                    
                    .. attribute:: link_group_name
                    
                    	Link Group Name
                    	**type**\: str
                    
                    	**range:** 0..40
                    
                    .. attribute:: enable
                    
                    	Flag to indicate that linkgroup should be running.  This must be the first object created when a linkgroup is configured, and the last object deleted when it is deconfigured.  When this object is deleted, the IS\-IS linkgroup will be removed
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: metric_offset
                    
                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                    	**type**\: int
                    
                    	**range:** 0..16777215
                    
                    .. attribute:: minimum_members
                    
                    	Minimum Members
                    	**type**\: int
                    
                    	**range:** 2..64
                    
                    .. attribute:: revert_members
                    
                    	Revert Members
                    	**type**\: int
                    
                    	**range:** 2..64
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.link_group_name = None
                        self.enable = None
                        self.metric_offset = None
                        self.minimum_members = None
                        self.revert_members = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.link_group_name is None:
                            raise YPYDataValidationError('Key property link_group_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:link-group[Cisco-IOS-XR-clns-isis-cfg:link-group-name = ' + str(self.link_group_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.link_group_name is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.metric_offset is not None:
                            return True

                        if self.minimum_members is not None:
                            return True

                        if self.revert_members is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LinkGroups.LinkGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:link-groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.link_group is not None:
                        for child_ref in self.link_group:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LinkGroups']['meta_info']


            class LspAcceptPasswords(object):
                """
                LSP/SNP accept password configuration
                
                .. attribute:: lsp_accept_password
                
                	LSP/SNP accept passwords. This requires the existence of an LSPPassword of the same level 
                	**type**\: list of :py:class:`LspAcceptPassword <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_accept_password = YList()
                    self.lsp_accept_password.parent = self
                    self.lsp_accept_password.name = 'lsp_accept_password'


                class LspAcceptPassword(object):
                    """
                    LSP/SNP accept passwords. This requires the
                    existence of an LSPPassword of the same level
                    .
                    
                    .. attribute:: level
                    
                    	Level to which configuration applies
                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                    
                    .. attribute:: password
                    
                    	Password
                    	**type**\: str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.password = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYDataValidationError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-accept-password[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.level is not None:
                            return True

                        if self.password is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-accept-passwords'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.lsp_accept_password is not None:
                        for child_ref in self.lsp_accept_password:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspAcceptPasswords']['meta_info']


            class LspArrivalTimes(object):
                """
                LSP arrival time configuration
                
                .. attribute:: lsp_arrival_time
                
                	Minimum LSP arrival time
                	**type**\: list of :py:class:`LspArrivalTime <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_arrival_time = YList()
                    self.lsp_arrival_time.parent = self
                    self.lsp_arrival_time.name = 'lsp_arrival_time'


                class LspArrivalTime(object):
                    """
                    Minimum LSP arrival time
                    
                    .. attribute:: level
                    
                    	Level to which configuration applies
                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                    
                    .. attribute:: initial_wait
                    
                    	Initial delay expected to take since last LSPin milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    .. attribute:: maximum_wait
                    
                    	Maximum delay expected to take since last LSPin milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    .. attribute:: secondary_wait
                    
                    	Secondary delay expected to take since last LSPin milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.initial_wait = None
                        self.maximum_wait = None
                        self.secondary_wait = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYDataValidationError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-arrival-time[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.level is not None:
                            return True

                        if self.initial_wait is not None:
                            return True

                        if self.maximum_wait is not None:
                            return True

                        if self.secondary_wait is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-arrival-times'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.lsp_arrival_time is not None:
                        for child_ref in self.lsp_arrival_time:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspArrivalTimes']['meta_info']


            class LspCheckIntervals(object):
                """
                LSP checksum check interval configuration
                
                .. attribute:: lsp_check_interval
                
                	LSP checksum check interval parameters
                	**type**\: list of :py:class:`LspCheckInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_check_interval = YList()
                    self.lsp_check_interval.parent = self
                    self.lsp_check_interval.name = 'lsp_check_interval'


                class LspCheckInterval(object):
                    """
                    LSP checksum check interval parameters
                    
                    .. attribute:: level
                    
                    	Level to which configuration applies
                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                    
                    .. attribute:: interval
                    
                    	LSP checksum check interval time in seconds
                    	**type**\: int
                    
                    	**range:** 10..65535
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYDataValidationError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-check-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.level is not None:
                            return True

                        if self.interval is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-check-intervals'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.lsp_check_interval is not None:
                        for child_ref in self.lsp_check_interval:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspCheckIntervals']['meta_info']


            class LspGenerationIntervals(object):
                """
                LSP generation\-interval configuration
                
                .. attribute:: lsp_generation_interval
                
                	LSP generation scheduling parameters
                	**type**\: list of :py:class:`LspGenerationInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_generation_interval = YList()
                    self.lsp_generation_interval.parent = self
                    self.lsp_generation_interval.name = 'lsp_generation_interval'


                class LspGenerationInterval(object):
                    """
                    LSP generation scheduling parameters
                    
                    .. attribute:: level
                    
                    	Level to which configuration applies
                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                    
                    .. attribute:: initial_wait
                    
                    	Initial wait before generating local LSP in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    .. attribute:: maximum_wait
                    
                    	Maximum wait before generating local LSP in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    .. attribute:: secondary_wait
                    
                    	Secondary wait before generating local LSP in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.initial_wait = None
                        self.maximum_wait = None
                        self.secondary_wait = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYDataValidationError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-generation-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.level is not None:
                            return True

                        if self.initial_wait is not None:
                            return True

                        if self.maximum_wait is not None:
                            return True

                        if self.secondary_wait is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-generation-intervals'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.lsp_generation_interval is not None:
                        for child_ref in self.lsp_generation_interval:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspGenerationIntervals']['meta_info']


            class LspLifetimes(object):
                """
                LSP lifetime configuration
                
                .. attribute:: lsp_lifetime
                
                	Maximum LSP lifetime
                	**type**\: list of :py:class:`LspLifetime <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspLifetimes.LspLifetime>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_lifetime = YList()
                    self.lsp_lifetime.parent = self
                    self.lsp_lifetime.name = 'lsp_lifetime'


                class LspLifetime(object):
                    """
                    Maximum LSP lifetime
                    
                    .. attribute:: level
                    
                    	Level to which configuration applies
                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                    
                    .. attribute:: lifetime
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.lifetime = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYDataValidationError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-lifetime[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.level is not None:
                            return True

                        if self.lifetime is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspLifetimes.LspLifetime']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-lifetimes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.lsp_lifetime is not None:
                        for child_ref in self.lsp_lifetime:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspLifetimes']['meta_info']


            class LspMtus(object):
                """
                LSP MTU configuration
                
                .. attribute:: lsp_mtu
                
                	LSP MTU
                	**type**\: list of :py:class:`LspMtu <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspMtus.LspMtu>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_mtu = YList()
                    self.lsp_mtu.parent = self
                    self.lsp_mtu.name = 'lsp_mtu'


                class LspMtu(object):
                    """
                    LSP MTU
                    
                    .. attribute:: level
                    
                    	Level to which configuration applies
                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                    
                    .. attribute:: mtu
                    
                    	Bytes
                    	**type**\: int
                    
                    	**range:** 128..4352
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.mtu = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYDataValidationError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-mtu[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.level is not None:
                            return True

                        if self.mtu is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspMtus.LspMtu']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-mtus'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.lsp_mtu is not None:
                        for child_ref in self.lsp_mtu:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspMtus']['meta_info']


            class LspPasswords(object):
                """
                LSP/SNP password configuration
                
                .. attribute:: lsp_password
                
                	LSP/SNP passwords. This must exist if an LSPAcceptPassword of the same level exists
                	**type**\: list of :py:class:`LspPassword <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspPasswords.LspPassword>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_password = YList()
                    self.lsp_password.parent = self
                    self.lsp_password.name = 'lsp_password'


                class LspPassword(object):
                    """
                    LSP/SNP passwords. This must exist if an
                    LSPAcceptPassword of the same level exists.
                    
                    .. attribute:: level
                    
                    	Level to which configuration applies
                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                    
                    .. attribute:: algorithm
                    
                    	Algorithm
                    	**type**\: :py:class:`IsisAuthenticationAlgorithm_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationAlgorithm_Enum>`
                    
                    .. attribute:: authentication_type
                    
                    	SNP packet authentication mode
                    	**type**\: :py:class:`IsisSnpAuth_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisSnpAuth_Enum>`
                    
                    .. attribute:: failure_mode
                    
                    	Failure Mode
                    	**type**\: :py:class:`IsisAuthenticationFailureMode_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationFailureMode_Enum>`
                    
                    .. attribute:: password
                    
                    	Password or unencrypted Key Chain name
                    	**type**\: str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.algorithm = None
                        self.authentication_type = None
                        self.failure_mode = None
                        self.password = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYDataValidationError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-password[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.level is not None:
                            return True

                        if self.algorithm is not None:
                            return True

                        if self.authentication_type is not None:
                            return True

                        if self.failure_mode is not None:
                            return True

                        if self.password is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspPasswords.LspPassword']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-passwords'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.lsp_password is not None:
                        for child_ref in self.lsp_password:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspPasswords']['meta_info']


            class LspRefreshIntervals(object):
                """
                LSP refresh\-interval configuration
                
                .. attribute:: lsp_refresh_interval
                
                	Interval between re\-flooding of unchanged LSPs
                	**type**\: list of :py:class:`LspRefreshInterval <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp_refresh_interval = YList()
                    self.lsp_refresh_interval.parent = self
                    self.lsp_refresh_interval.name = 'lsp_refresh_interval'


                class LspRefreshInterval(object):
                    """
                    Interval between re\-flooding of unchanged
                    LSPs
                    
                    .. attribute:: level
                    
                    	Level to which configuration applies
                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                    
                    .. attribute:: interval
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYDataValidationError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-refresh-interval[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.level is not None:
                            return True

                        if self.interval is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:lsp-refresh-intervals'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.lsp_refresh_interval is not None:
                        for child_ref in self.lsp_refresh_interval:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.LspRefreshIntervals']['meta_info']


            class MaxLinkMetrics(object):
                """
                Max Link Metric configuration
                
                .. attribute:: max_link_metric
                
                	Max Link Metric
                	**type**\: list of :py:class:`MaxLinkMetric <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.max_link_metric = YList()
                    self.max_link_metric.parent = self
                    self.max_link_metric.name = 'max_link_metric'


                class MaxLinkMetric(object):
                    """
                    Max Link Metric
                    
                    .. attribute:: level
                    
                    	Level to which configuration applies
                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYDataValidationError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-link-metric[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.level is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:max-link-metrics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.max_link_metric is not None:
                        for child_ref in self.max_link_metric:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.MaxLinkMetrics']['meta_info']


            class Nets(object):
                """
                NET configuration
                
                .. attribute:: net
                
                	Network Entity Title (NET)
                	**type**\: list of :py:class:`Net <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nets.Net>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.net = YList()
                    self.net.parent = self
                    self.net.name = 'net'


                class Net(object):
                    """
                    Network Entity Title (NET)
                    
                    .. attribute:: net_name
                    
                    	Network Entity Title
                    	**type**\: str
                    
                    	**pattern:** [a\-fA\-F0\-9]{2}(\\.[a\-fA\-F0\-9]{4}){3,9}\\.[a\-fA\-F0\-9]{2}
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.net_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.net_name is None:
                            raise YPYDataValidationError('Key property net_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:net[Cisco-IOS-XR-clns-isis-cfg:net-name = ' + str(self.net_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.net_name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.Nets.Net']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:nets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.net is not None:
                        for child_ref in self.net:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Nets']['meta_info']


            class Nsf(object):
                """
                IS\-IS NSF configuration
                
                .. attribute:: flavor
                
                	NSF not configured if item is deleted
                	**type**\: :py:class:`IsisNsfFlavor_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisNsfFlavor_Enum>`
                
                .. attribute:: interface_timer
                
                	Per\-interface time period to wait for a restart ACK during an IETF\-NSF restart. This configuration has no effect if IETF\-NSF is not configured
                	**type**\: int
                
                	**range:** 1..20
                
                .. attribute:: lifetime
                
                	Maximum route lifetime following restart. When this lifetime expires, old routes will be purged from the RIB
                	**type**\: int
                
                	**range:** 5..300
                
                .. attribute:: max_interface_timer_expiry
                
                	Maximum number of times an interface timer may expire during an IETF\-NSF restart before the NSF restart is aborted. This configuration has no effect if IETF NSF is not configured
                	**type**\: int
                
                	**range:** 1..10
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.flavor = None
                    self.interface_timer = None
                    self.lifetime = None
                    self.max_interface_timer_expiry = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:nsf'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.flavor is not None:
                        return True

                    if self.interface_timer is not None:
                        return True

                    if self.lifetime is not None:
                        return True

                    if self.max_interface_timer_expiry is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Nsf']['meta_info']


            class OverloadBits(object):
                """
                LSP overload\-bit configuration
                
                .. attribute:: overload_bit
                
                	Set the overload bit in the System LSP so that other routers avoid this one in SPF calculations. This may be done either unconditionally, or on startup until either a set time has passed or IS\-IS is informed that BGP has converged. This is an Object with a union discriminated on an integer value of the ISISOverloadBitModeType
                	**type**\: list of :py:class:`OverloadBit <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.OverloadBits.OverloadBit>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.overload_bit = YList()
                    self.overload_bit.parent = self
                    self.overload_bit.name = 'overload_bit'


                class OverloadBit(object):
                    """
                    Set the overload bit in the System LSP so
                    that other routers avoid this one in SPF
                    calculations. This may be done either
                    unconditionally, or on startup until either a
                    set time has passed or IS\-IS is informed that
                    BGP has converged. This is an Object with a
                    union discriminated on an integer value of
                    the ISISOverloadBitModeType.
                    
                    .. attribute:: level
                    
                    	Level to which configuration applies
                    	**type**\: :py:class:`IsisInternalLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel_Enum>`
                    
                    .. attribute:: external_adv_type
                    
                    	Advertise prefixes from other protocols
                    	**type**\: :py:class:`IsisAdvTypeExternal_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisAdvTypeExternal_Enum>`
                    
                    .. attribute:: hippity_period
                    
                    	Time in seconds to advertise ourself as overloaded after process startup
                    	**type**\: int
                    
                    	**range:** 5..86400
                    
                    .. attribute:: inter_level_adv_type
                    
                    	Advertise prefixes across ISIS levels
                    	**type**\: :py:class:`IsisAdvTypeInterLevel_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisAdvTypeInterLevel_Enum>`
                    
                    .. attribute:: overload_bit_mode
                    
                    	Circumstances under which the overload bit is set in the system LSP
                    	**type**\: :py:class:`IsisOverloadBitMode_Enum <ydk.models.clns.Cisco_IOS_XR_clns_isis_cfg.IsisOverloadBitMode_Enum>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.level = None
                        self.external_adv_type = None
                        self.hippity_period = None
                        self.inter_level_adv_type = None
                        self.overload_bit_mode = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.level is None:
                            raise YPYDataValidationError('Key property level is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:overload-bit[Cisco-IOS-XR-clns-isis-cfg:level = ' + str(self.level) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.level is not None:
                            return True

                        if self.external_adv_type is not None:
                            return True

                        if self.hippity_period is not None:
                            return True

                        if self.inter_level_adv_type is not None:
                            return True

                        if self.overload_bit_mode is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                        return meta._meta_table['Isis.Instances.Instance.OverloadBits.OverloadBit']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:overload-bits'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.overload_bit is not None:
                        for child_ref in self.overload_bit:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.OverloadBits']['meta_info']


            class Srgb(object):
                """
                Segment Routing Global Block configuration
                
                .. attribute:: lower_bound
                
                	The lower bound of the SRGB
                	**type**\: int
                
                	**range:** 16000..1048574
                
                .. attribute:: upper_bound
                
                	The upper bound of the SRGB
                	**type**\: int
                
                	**range:** 16001..1048575
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lower_bound = None
                    self.upper_bound = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:srgb'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.lower_bound is not None:
                        return True

                    if self.upper_bound is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return True

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.Srgb']['meta_info']


            class TraceBufferSize(object):
                """
                Trace buffer size configuration
                
                .. attribute:: detailed
                
                	Buffer size for detailed traces
                	**type**\: int
                
                	**range:** 1..1000000
                
                .. attribute:: severe
                
                	Buffer size for severe trace
                	**type**\: int
                
                	**range:** 1..1000000
                
                .. attribute:: standard
                
                	Buffer size for standard traces
                	**type**\: int
                
                	**range:** 1..1000000
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.detailed = None
                    self.severe = None
                    self.standard = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-clns-isis-cfg:trace-buffer-size'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.detailed is not None:
                        return True

                    if self.severe is not None:
                        return True

                    if self.standard is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                    return meta._meta_table['Isis.Instances.Instance.TraceBufferSize']['meta_info']

            @property
            def _common_path(self):
                if self.instance_name is None:
                    raise YPYDataValidationError('Key property instance_name is None')

                return '/Cisco-IOS-XR-clns-isis-cfg:isis/Cisco-IOS-XR-clns-isis-cfg:instances/Cisco-IOS-XR-clns-isis-cfg:instance[Cisco-IOS-XR-clns-isis-cfg:instance-name = ' + str(self.instance_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.instance_name is not None:
                    return True

                if self.afs is not None and self.afs._has_data():
                    return True

                if self.afs is not None and self.afs.is_presence():
                    return True

                if self.distribute is not None and self.distribute._has_data():
                    return True

                if self.distribute is not None and self.distribute.is_presence():
                    return True

                if self.dynamic_host_name is not None:
                    return True

                if self.ignore_lsp_errors is not None:
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.interfaces is not None and self.interfaces.is_presence():
                    return True

                if self.is_type is not None:
                    return True

                if self.link_groups is not None and self.link_groups._has_data():
                    return True

                if self.link_groups is not None and self.link_groups.is_presence():
                    return True

                if self.log_adjacency_changes is not None:
                    return True

                if self.log_pdu_drops is not None:
                    return True

                if self.lsp_accept_passwords is not None and self.lsp_accept_passwords._has_data():
                    return True

                if self.lsp_accept_passwords is not None and self.lsp_accept_passwords.is_presence():
                    return True

                if self.lsp_arrival_times is not None and self.lsp_arrival_times._has_data():
                    return True

                if self.lsp_arrival_times is not None and self.lsp_arrival_times.is_presence():
                    return True

                if self.lsp_check_intervals is not None and self.lsp_check_intervals._has_data():
                    return True

                if self.lsp_check_intervals is not None and self.lsp_check_intervals.is_presence():
                    return True

                if self.lsp_generation_intervals is not None and self.lsp_generation_intervals._has_data():
                    return True

                if self.lsp_generation_intervals is not None and self.lsp_generation_intervals.is_presence():
                    return True

                if self.lsp_lifetimes is not None and self.lsp_lifetimes._has_data():
                    return True

                if self.lsp_lifetimes is not None and self.lsp_lifetimes.is_presence():
                    return True

                if self.lsp_mtus is not None and self.lsp_mtus._has_data():
                    return True

                if self.lsp_mtus is not None and self.lsp_mtus.is_presence():
                    return True

                if self.lsp_passwords is not None and self.lsp_passwords._has_data():
                    return True

                if self.lsp_passwords is not None and self.lsp_passwords.is_presence():
                    return True

                if self.lsp_refresh_intervals is not None and self.lsp_refresh_intervals._has_data():
                    return True

                if self.lsp_refresh_intervals is not None and self.lsp_refresh_intervals.is_presence():
                    return True

                if self.max_link_metrics is not None and self.max_link_metrics._has_data():
                    return True

                if self.max_link_metrics is not None and self.max_link_metrics.is_presence():
                    return True

                if self.nets is not None and self.nets._has_data():
                    return True

                if self.nets is not None and self.nets.is_presence():
                    return True

                if self.nsf is not None and self.nsf._has_data():
                    return True

                if self.nsf is not None and self.nsf.is_presence():
                    return True

                if self.nsr is not None:
                    return True

                if self.overload_bits is not None and self.overload_bits._has_data():
                    return True

                if self.overload_bits is not None and self.overload_bits.is_presence():
                    return True

                if self.running is not None:
                    return True

                if self.srgb is not None and self.srgb._has_data():
                    return True

                if self.srgb is not None and self.srgb.is_presence():
                    return True

                if self.trace_buffer_size is not None and self.trace_buffer_size._has_data():
                    return True

                if self.trace_buffer_size is not None and self.trace_buffer_size.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
                return meta._meta_table['Isis.Instances.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-clns-isis-cfg:isis/Cisco-IOS-XR-clns-isis-cfg:instances'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.instance is not None:
                for child_ref in self.instance:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
            return meta._meta_table['Isis.Instances']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-clns-isis-cfg:isis'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.instances is not None and self.instances._has_data():
            return True

        if self.instances is not None and self.instances.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.clns._meta import _Cisco_IOS_XR_clns_isis_cfg as meta
        return meta._meta_table['Isis']['meta_info']


