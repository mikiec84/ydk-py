""" CISCO_VOICE_DIAL_CONTROL_MIB 

This MIB module enhances the IETF Dial Control MIB
(RFC2128) by providing management of voice telephony
peers on both a circuit\-switched telephony network,
and an IP data network.

\*\*\* ABBREVIATIONS, ACRONYMS AND SYMBOLS \*\*\*

GSM    \- Global System for Mobile Communication

AMR\-NB \- Adaptive Multi Rate \- Narrow Band 

iLBC   \- internet Low Bitrate Codec 

KPML   \- Key Press Markup Language

MGCP   \- Media Gateway Control Protocol.

SIP    \- Session Initiation Protocol.

H323   \- One of the voip signalling protocol.

SCCP   \- Skinny Client Control Protocol.

dialpeer \- This represents a configured interface that 
           carries the dial map.  A dialpeer maps the 
           called and calling numbers with the port or 
           IP interface to be used.

License call capacity \- This represents the licensed 
                        maximum call capacity of 
                        the gateway.

iSAC    \-  Internet Speech Audio Codec

RPH    \- Resource Priority Header

DSCP   \- Diffserv Code Points

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.int.INT_SERV_MIB import QosService_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB import CvcCoderTypeRate_Enum
from ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB import CvcFaxTransmitRate_Enum
from ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB import CvcInBandSignaling_Enum
from ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB import CvcSpeechCoderRate_Enum

class CvAmrNbRtpEncap_Enum(Enum):
    """
    CvAmrNbRtpEncap_Enum

    Represents GSM AMR\-NB codec RTP encapsulation type.

    """

    RFC3267 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvAmrNbRtpEncap_Enum']


class CvCallConnectionType_Enum(Enum):
    """
    CvCallConnectionType_Enum

    Call connection represents the connection/association/session
    between two media call end points. Following are the different
    connection types.
    
    h323       \- h323 protocol.
    sip        \- Session Initiation Protocol.
    mgcp       \- Media Gateway Control Protocol.
    sccp       \- Cisco proprietary Skinny Call Control Protocol.
    multicast  \- multicast call connections.
    cacontrol  \- Call Agent Control.
    telephony  \- telephony signal call connections.

    """

    H323 = 1

    SIP = 2

    MGCP = 3

    SCCP = 4

    MULTICAST = 5

    CACONTROL = 6

    TELEPHONY = 7


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvCallConnectionType_Enum']


class CvCallVolumeStatsIntvlType_Enum(Enum):
    """
    CvCallVolumeStatsIntvlType_Enum

    Represents the ids of the stats vlolume table
    Here is what each entry corresponds.
    1 \: Seconds Table\: Here each entry corresponds to a second
    2 \: Minutes Table\: Here each entry corresponds to a minute
    3 \: Hours Table\: Here each entry corresponds to an hour

    """

    SECONDSTATS = 1

    MINUTESTATS = 2

    HOURSTATS = 3


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvCallVolumeStatsIntvlType_Enum']


class CvCallVolumeWMIntvlType_Enum(Enum):
    """
    CvCallVolumeWMIntvlType_Enum

    Represents the Id of the watermark table.
    Here is what different values represent
    
    1 \: Seconds Table\: Here the entries are among last 60 second
    2 \: Minutes Table\: Here the entries are among last 60 minutes
    3 \: Hours Table\: Here the entries are among last 72 Hours
    4 \: Uptime Table\: Here the entries are from last reload/reboot

    """

    SECONDSTATS = 1

    MINUTESTATS = 2

    HOURSTATS = 3

    FROMRELOADSTATS = 4


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvCallVolumeWMIntvlType_Enum']


class CvIlbcFrameMode_Enum(Enum):
    """
    CvIlbcFrameMode_Enum

    This Texatual Convention represents the iLBC codec
    frame modes.  
    The possible values are \:
    frameMode20\: This mode operates at 15.2 kbps and each 
                 frame is packetized in 38 bytes. 
    frameMode30\: This mode operates at 13.33 kbps and each 
                 frame is packetized in 50 bytes.

    """

    FRAMEMODE20 = 20

    FRAMEMODE30 = 30


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvIlbcFrameMode_Enum']


class CvSessionProtocol_Enum(Enum):
    """
    CvSessionProtocol_Enum

    Represents a Session Protocol used by Voice calls between a
    local and remote router via the IP backbone.
    
    other \- none of the following.
    cisco \- cisco proprietary H.323 Lite session protocol.
    sdp   \- Session Description Protocol.
    sip   \- Session Initiation Protocol.
    sccp  \- Skinny Call Control Protocol.

    """

    OTHER = 1

    CISCO = 2

    SDP = 3

    SIP = 4

    MULTICAST = 5

    SCCP = 6


    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CvSessionProtocol_Enum']


class CvAmrNbBitRateMode_Bits(FixedBitsDict):
    """
    CvAmrNbBitRateMode_Bits

    Represents GSM AMR\-NB bit rate modes.
    
    CodecMode             Bit\-rate (kbps)
    0                     4.75
    1                     5.15
    2                     5.90
    3                     6.70
    4                     7.40
    5                     7.95
    6                     10.2
    7                     12.2
    Keys are:- amrBitRateMode1 , amrBitRateMode0 , amrBitRateMode3 , amrBitRateMode2 , amrBitRateMode5 , amrBitRateMode4 , amrBitRateMode7 , amrBitRateMode6

    """

    def __init__(self):
        self._dictionary = { 
            'amrBitRateMode1':False,
            'amrBitRateMode0':False,
            'amrBitRateMode3':False,
            'amrBitRateMode2':False,
            'amrBitRateMode5':False,
            'amrBitRateMode4':False,
            'amrBitRateMode7':False,
            'amrBitRateMode6':False,
        }
        self._pos_map = { 
            'amrBitRateMode1':1,
            'amrBitRateMode0':0,
            'amrBitRateMode3':3,
            'amrBitRateMode2':2,
            'amrBitRateMode5':5,
            'amrBitRateMode4':4,
            'amrBitRateMode7':7,
            'amrBitRateMode6':6,
        }


class CISCOVOICEDIALCONTROLMIB(object):
    """
    
    
    .. attribute:: cvactivecallstatstable
    
    	This table represents the active voice calls in various interval lengths defined by the  CvCallVolumeStatsIntvlType object.  Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\: :py:class:`CvActiveCallStatsTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvActiveCallStatsTable>`
    
    .. attribute:: cvactivecallwmtable
    
    	This table represents high watermarks achieved by active calls in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow  for detailed measurement to be collected
    	**type**\: :py:class:`CvActiveCallWMTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvActiveCallWMTable>`
    
    .. attribute:: cvcallactivetable
    
    	This table is the voice extension to the call active table of IETF Dial Control MIB. It contains voice encapsulation call leg information that is derived from the statistics of lower layer telephony interface
    	**type**\: :py:class:`CvCallActiveTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallActiveTable>`
    
    .. attribute:: cvcalldurationstatstable
    
    	This table represents the number of calls below a specific duration in various interval length defined by  the CvCallVolumeStatsIntvlType object.    The specific duration is configurable value of   cvCallDurationStatsThreshold object.  Each interval may contain one or more entries to allow for  detailed measurement to be collected
    	**type**\: :py:class:`CvCallDurationStatsTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallDurationStatsTable>`
    
    .. attribute:: cvcallhistorytable
    
    	This table is the voice extension to the call history table of IETF Dial Control MIB. It contains voice encapsulation call leg information such as voice packet statistics, coder usage and end to end bandwidth of the call leg
    	**type**\: :py:class:`CvCallHistoryTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallHistoryTable>`
    
    .. attribute:: cvcalllegratestatstable
    
    	cvCallLegRateStatsTable table represents voice call leg rate measurement in various interval lengths defined by  the CvCallVolumeStatsIntvlType object. Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\: :py:class:`CvCallLegRateStatsTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallLegRateStatsTable>`
    
    .. attribute:: cvcalllegratewmtable
    
    	cvCallLegRateWMTable table represents high watermarks achieved by call\-leg rate in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow for  detailed measurement to be collected
    	**type**\: :py:class:`CvCallLegRateWMTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallLegRateWMTable>`
    
    .. attribute:: cvcallratemonitor
    
    	
    	**type**\: :py:class:`CvCallRateMonitor <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallRateMonitor>`
    
    .. attribute:: cvcallratestatstable
    
    	This table represents voice call rate measurement in various interval lengths defined by the  CvCallVolumeStatsIntvlType object.  Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\: :py:class:`CvCallRateStatsTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallRateStatsTable>`
    
    .. attribute:: cvcallratewmtable
    
    	This table represents high watermarks achieved by call rate in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow for  detailed measurement to be collected
    	**type**\: :py:class:`CvCallRateWMTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallRateWMTable>`
    
    .. attribute:: cvcallvolconntable
    
    	This table represents the number of active call connections for each call connection type in the voice gateway
    	**type**\: :py:class:`CvCallVolConnTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallVolConnTable>`
    
    .. attribute:: cvcallvoliftable
    
    	This table represents the information about the usage of an IP interface in a voice gateway for voice media calls. This table has a sparse\-dependent relationship with   ifTable. There exists an entry in this table,  for each of the  entries in ifTable where ifType  is one of 'ethernetCsmacd' and 'softwareLoopback'
    	**type**\: :py:class:`CvCallVolIfTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallVolIfTable>`
    
    .. attribute:: cvcallvolume
    
    	
    	**type**\: :py:class:`CvCallVolume <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallVolume>`
    
    .. attribute:: cvcallvolumestatshistory
    
    	
    	**type**\: :py:class:`CvCallVolumeStatsHistory <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallVolumeStatsHistory>`
    
    .. attribute:: cvgatewaycallactive
    
    	
    	**type**\: :py:class:`CvGatewayCallActive <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvGatewayCallActive>`
    
    .. attribute:: cvgeneralconfiguration
    
    	
    	**type**\: :py:class:`CvGeneralConfiguration <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvGeneralConfiguration>`
    
    .. attribute:: cvpeercfgtable
    
    	The table contains the Voice Generic Peer information that is used to create an ifIndexed row with an appropriate ifType that is associated with the cvPeerCfgType and cvPeerCfgPeerType objects
    	**type**\: :py:class:`CvPeerCfgTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvPeerCfgTable>`
    
    .. attribute:: cvpeercommoncfgtable
    
    	The table contains the Voice specific peer common configuration information that is required to accept voice calls or to which it will place them or process the incoming calls
    	**type**\: :py:class:`CvPeerCommonCfgTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvPeerCommonCfgTable>`
    
    .. attribute:: cvsipmsgratestatstable
    
    	This table represents the SIP message rate measurement in various interval length defined by the  CvCallVolumeStatsIntvlType object.  Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\: :py:class:`CvSipMsgRateStatsTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvSipMsgRateStatsTable>`
    
    .. attribute:: cvsipmsgratewmtable
    
    	This table represents of high watermarks achieved by SIP message rate in various interval length defined  by CvCallVolumeWMIntvlType.   Each interval may contain one or more entries to allow for detailed measurement to be collected
    	**type**\: :py:class:`CvSipMsgRateWMTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvSipMsgRateWMTable>`
    
    .. attribute:: cvvoicepeercfgtable
    
    	The table contains the Voice over Telephony peer specific information that is required to accept voice calls or to which it will place them or perform various loopback tests via interface
    	**type**\: :py:class:`CvVoicePeerCfgTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoicePeerCfgTable>`
    
    .. attribute:: cvvoipcallactivetable
    
    	This table is the VoIP extension to the call active table of IETF Dial Control MIB. It contains VoIP call leg information about specific VoIP call destination and the selected QoS for the call leg
    	**type**\: :py:class:`CvVoIPCallActiveTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoIPCallActiveTable>`
    
    .. attribute:: cvvoipcallhistorytable
    
    	This table is the VoIP extension to the call history table of IETF Dial Control MIB. It contains VoIP call leg information about specific VoIP call destination and the selected QoS for the call leg
    	**type**\: :py:class:`CvVoIPCallHistoryTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoIPCallHistoryTable>`
    
    .. attribute:: cvvoippeercfgtable
    
    	The table contains the Voice over IP (VoIP) peer specific information that is required to accept voice calls or to which it will place them via IP backbone with the specified session protocol in cvVoIPPeerCfgSessionProtocol
    	**type**\: :py:class:`CvVoIPPeerCfgTable <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable>`
    
    

    """

    _prefix = 'cisco-voice-dial'
    _revision = '2012-05-15'

    def __init__(self):
        self.cvactivecallstatstable = CISCOVOICEDIALCONTROLMIB.CvActiveCallStatsTable()
        self.cvactivecallstatstable.parent = self
        self.cvactivecallwmtable = CISCOVOICEDIALCONTROLMIB.CvActiveCallWMTable()
        self.cvactivecallwmtable.parent = self
        self.cvcallactivetable = CISCOVOICEDIALCONTROLMIB.CvCallActiveTable()
        self.cvcallactivetable.parent = self
        self.cvcalldurationstatstable = CISCOVOICEDIALCONTROLMIB.CvCallDurationStatsTable()
        self.cvcalldurationstatstable.parent = self
        self.cvcallhistorytable = CISCOVOICEDIALCONTROLMIB.CvCallHistoryTable()
        self.cvcallhistorytable.parent = self
        self.cvcalllegratestatstable = CISCOVOICEDIALCONTROLMIB.CvCallLegRateStatsTable()
        self.cvcalllegratestatstable.parent = self
        self.cvcalllegratewmtable = CISCOVOICEDIALCONTROLMIB.CvCallLegRateWMTable()
        self.cvcalllegratewmtable.parent = self
        self.cvcallratemonitor = CISCOVOICEDIALCONTROLMIB.CvCallRateMonitor()
        self.cvcallratemonitor.parent = self
        self.cvcallratestatstable = CISCOVOICEDIALCONTROLMIB.CvCallRateStatsTable()
        self.cvcallratestatstable.parent = self
        self.cvcallratewmtable = CISCOVOICEDIALCONTROLMIB.CvCallRateWMTable()
        self.cvcallratewmtable.parent = self
        self.cvcallvolconntable = CISCOVOICEDIALCONTROLMIB.CvCallVolConnTable()
        self.cvcallvolconntable.parent = self
        self.cvcallvoliftable = CISCOVOICEDIALCONTROLMIB.CvCallVolIfTable()
        self.cvcallvoliftable.parent = self
        self.cvcallvolume = CISCOVOICEDIALCONTROLMIB.CvCallVolume()
        self.cvcallvolume.parent = self
        self.cvcallvolumestatshistory = CISCOVOICEDIALCONTROLMIB.CvCallVolumeStatsHistory()
        self.cvcallvolumestatshistory.parent = self
        self.cvgatewaycallactive = CISCOVOICEDIALCONTROLMIB.CvGatewayCallActive()
        self.cvgatewaycallactive.parent = self
        self.cvgeneralconfiguration = CISCOVOICEDIALCONTROLMIB.CvGeneralConfiguration()
        self.cvgeneralconfiguration.parent = self
        self.cvpeercfgtable = CISCOVOICEDIALCONTROLMIB.CvPeerCfgTable()
        self.cvpeercfgtable.parent = self
        self.cvpeercommoncfgtable = CISCOVOICEDIALCONTROLMIB.CvPeerCommonCfgTable()
        self.cvpeercommoncfgtable.parent = self
        self.cvsipmsgratestatstable = CISCOVOICEDIALCONTROLMIB.CvSipMsgRateStatsTable()
        self.cvsipmsgratestatstable.parent = self
        self.cvsipmsgratewmtable = CISCOVOICEDIALCONTROLMIB.CvSipMsgRateWMTable()
        self.cvsipmsgratewmtable.parent = self
        self.cvvoicepeercfgtable = CISCOVOICEDIALCONTROLMIB.CvVoicePeerCfgTable()
        self.cvvoicepeercfgtable.parent = self
        self.cvvoipcallactivetable = CISCOVOICEDIALCONTROLMIB.CvVoIPCallActiveTable()
        self.cvvoipcallactivetable.parent = self
        self.cvvoipcallhistorytable = CISCOVOICEDIALCONTROLMIB.CvVoIPCallHistoryTable()
        self.cvvoipcallhistorytable.parent = self
        self.cvvoippeercfgtable = CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable()
        self.cvvoippeercfgtable.parent = self


    class CvActiveCallStatsTable(object):
        """
        This table represents the active voice calls in various
        interval lengths defined by the 
        CvCallVolumeStatsIntvlType object.
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected.
        
        .. attribute:: cvactivecallstatsentry
        
        	This is a conceptual\-row in cvActiveCallStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of :py:class:`CvActiveCallStatsEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvActiveCallStatsTable.CvActiveCallStatsEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvactivecallstatsentry = YList()
            self.cvactivecallstatsentry.parent = self
            self.cvactivecallstatsentry.name = 'cvactivecallstatsentry'


        class CvActiveCallStatsEntry(object):
            """
            This is a conceptual\-row in cvActiveCallStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvactivecallstatsintvldur
            
            	This is an index that references to the different past periods in given in interval of active call table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\: int
            
            	**range:** 1..72
            
            .. attribute:: cvactivecallstatsintvldurunits
            
            	The Object indexes in Active Call Rate Table (con\-current calls table) to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\: :py:class:`CvCallVolumeStatsIntvlType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeStatsIntvlType_Enum>`
            
            .. attribute:: cvactivecallstatsavgval
            
            	This object indicates the average number of active calls that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvactivecallstatsmaxval
            
            	This object indicates the maximum number of active call that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.cvactivecallstatsintvldur = None
                self.cvactivecallstatsintvldurunits = None
                self.cvactivecallstatsavgval = None
                self.cvactivecallstatsmaxval = None

            @property
            def _common_path(self):
                if self.cvactivecallstatsintvldur is None:
                    raise YPYDataValidationError('Key property cvactivecallstatsintvldur is None')
                if self.cvactivecallstatsintvldurunits is None:
                    raise YPYDataValidationError('Key property cvactivecallstatsintvldurunits is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvActiveCallStatsTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvActiveCallStatsEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cvActiveCallStatsIntvlDur = ' + str(self.cvactivecallstatsintvldur) + '][CISCO-VOICE-DIAL-CONTROL-MIB:cvActiveCallStatsIntvlDurUnits = ' + str(self.cvactivecallstatsintvldurunits) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvactivecallstatsintvldur is not None:
                    return True

                if self.cvactivecallstatsintvldurunits is not None:
                    return True

                if self.cvactivecallstatsavgval is not None:
                    return True

                if self.cvactivecallstatsmaxval is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvActiveCallStatsTable.CvActiveCallStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvActiveCallStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvactivecallstatsentry is not None:
                for child_ref in self.cvactivecallstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvActiveCallStatsTable']['meta_info']


    class CvActiveCallWMTable(object):
        """
        This table represents high watermarks achieved
        by active calls in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow 
        for detailed measurement to be collected.
        
        .. attribute:: cvactivecallwmentry
        
        	This is a conceptual\-row in cvActiveCallWMTable This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted  if cvCallVolumeWMTableSize is changed
        	**type**\: list of :py:class:`CvActiveCallWMEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvActiveCallWMTable.CvActiveCallWMEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvactivecallwmentry = YList()
            self.cvactivecallwmentry.parent = self
            self.cvactivecallwmentry.name = 'cvactivecallwmentry'


        class CvActiveCallWMEntry(object):
            """
            This is a conceptual\-row in cvActiveCallWMTable
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted  if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvactivecallwmindex
            
            	This is an index that references to different peaks in past period in acive call watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: cvactivecallwmintvldurunits
            
            	The Object indexes in active call Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\: :py:class:`CvCallVolumeWMIntvlType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeWMIntvlType_Enum>`
            
            .. attribute:: cvactivecallwmts
            
            	This object indicates date and time when the high watermark is achieved for active calls for the given interval
            	**type**\: str
            
            .. attribute:: cvactivecallwmvalue
            
            	This object indicates high watermark value achieved by the active calls for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.cvactivecallwmindex = None
                self.cvactivecallwmintvldurunits = None
                self.cvactivecallwmts = None
                self.cvactivecallwmvalue = None

            @property
            def _common_path(self):
                if self.cvactivecallwmindex is None:
                    raise YPYDataValidationError('Key property cvactivecallwmindex is None')
                if self.cvactivecallwmintvldurunits is None:
                    raise YPYDataValidationError('Key property cvactivecallwmintvldurunits is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvActiveCallWMTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvActiveCallWMEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cvActiveCallWMIndex = ' + str(self.cvactivecallwmindex) + '][CISCO-VOICE-DIAL-CONTROL-MIB:cvActiveCallWMIntvlDurUnits = ' + str(self.cvactivecallwmintvldurunits) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvactivecallwmindex is not None:
                    return True

                if self.cvactivecallwmintvldurunits is not None:
                    return True

                if self.cvactivecallwmts is not None:
                    return True

                if self.cvactivecallwmvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvActiveCallWMTable.CvActiveCallWMEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvActiveCallWMTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvactivecallwmentry is not None:
                for child_ref in self.cvactivecallwmentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvActiveCallWMTable']['meta_info']


    class CvCallActiveTable(object):
        """
        This table is the voice extension to the call active table
        of IETF Dial Control MIB. It contains voice encapsulation
        call leg information that is derived from the statistics
        of lower layer telephony interface.
        
        .. attribute:: cvcallactiveentry
        
        	The information regarding a single voice encapsulation call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call active entry in the IETF Dial Control MIB is created and call active entry contains the call establishment to a voice over telephony network peer. The entry is deleted when its associated call active entry in the IETF Dial Control MIB is deleted
        	**type**\: list of :py:class:`CvCallActiveEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallActiveTable.CvCallActiveEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcallactiveentry = YList()
            self.cvcallactiveentry.parent = self
            self.cvcallactiveentry.name = 'cvcallactiveentry'


        class CvCallActiveEntry(object):
            """
            The information regarding a single voice encapsulation
            call leg.
            The call leg entry is identified by using the same index
            objects that are used by Call Active table of IETF Dial
            Control MIB to identify the call.
            An entry of this table is created when its associated call
            active entry in the IETF Dial Control MIB is created and
            call active entry contains the call establishment to a
            voice over telephony network peer.
            The entry is deleted when its associated call active entry
            in the IETF Dial Control MIB is deleted.
            
            .. attribute:: callactiveindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: callactivesetuptime
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvcallactiveaccountcode
            
            	The object indicates the account code input to the call. It could be used for call screen or by down stream server for billing purpose. The value of empty string indicates no account code input
            	**type**\: str
            
            	**range:** 0..50
            
            .. attribute:: cvcallactiveacomlevel
            
            	The object contains the sum of Echo Return Loss (ERL), cancellation loss (Echo Return Loss Enhancement) and nonlinear processing loss for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\: int
            
            	**range:** \-1..127
            
            .. attribute:: cvcallactivecalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this call
            	**type**\: bool
            
            .. attribute:: cvcallactivecallid
            
            	This object represents the call identifier for the active telephony leg of the call
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvcallactivecallingname
            
            	The calling party name of the call. If the name is not available, then it will have a length of zero
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvcallactivecodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call
            	**type**\: :py:class:`CvcCoderTypeRate_Enum <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate_Enum>`
            
            .. attribute:: cvcallactiveconnectionid
            
            	The global connection identifier for the active telephony leg of the call
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: cvcallactiveecanreflectorlocation
            
            	The location in milliseconds of the largest amplitude reflector detected by the echo canceller for this call.  The value 0 indicates there is no reflector or the  information is not available
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: cvcallactiveerllevel
            
            	The object contains the current Echo Return Loss (ERL) level for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\: int
            
            	**range:** \-1..45
            
            .. attribute:: cvcallactiveerllevelrev1
            
            	The object contains the current Echo Return Loss (ERL) level for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\: int
            
            	**range:** \-1..200
            
            .. attribute:: cvcallactivefaxtxduration
            
            	Duration of fax transmitted from this peer to voice gateway for this call leg. The FAX Utilization Rate can be obtained by dividing this by cvCallActiveTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvcallactiveimgpagecount
            
            	The number of FAX related image pages are received or transmitted via the peer for the call leg
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvcallactiveinsignallevel
            
            	The object contains the active input signal level from telephony interface that is used by the call leg
            	**type**\: int
            
            	**range:** \-128..8
            
            .. attribute:: cvcallactivenoiselevel
            
            	The object contains the active noise level for the call leg
            	**type**\: int
            
            	**range:** \-128..8
            
            .. attribute:: cvcallactiveoutsignallevel
            
            	The object contains the active output signal level to telephony interface that is used by the call leg
            	**type**\: int
            
            	**range:** \-128..8
            
            .. attribute:: cvcallactivesessiontarget
            
            	The object specifies the session target of the peer that is used for the call leg. This object is set with the information in the call associated cvVoicePeerCfgSessionTarget object when the call is connected
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: cvcallactivetxduration
            
            	Duration of Transmit path open from this peer to the voice gateway for the call leg. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvcallactivevoicetxduration
            
            	Duration of voice transmitted from this peer to voice gateway for this call leg. The Voice Utilization Rate can be obtained by dividing this by cvCallActiveTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.callactiveindex = None
                self.callactivesetuptime = None
                self.cvcallactiveaccountcode = None
                self.cvcallactiveacomlevel = None
                self.cvcallactivecalleridblock = None
                self.cvcallactivecallid = None
                self.cvcallactivecallingname = None
                self.cvcallactivecodertyperate = None
                self.cvcallactiveconnectionid = None
                self.cvcallactiveecanreflectorlocation = None
                self.cvcallactiveerllevel = None
                self.cvcallactiveerllevelrev1 = None
                self.cvcallactivefaxtxduration = None
                self.cvcallactiveimgpagecount = None
                self.cvcallactiveinsignallevel = None
                self.cvcallactivenoiselevel = None
                self.cvcallactiveoutsignallevel = None
                self.cvcallactivesessiontarget = None
                self.cvcallactivetxduration = None
                self.cvcallactivevoicetxduration = None

            @property
            def _common_path(self):
                if self.callactiveindex is None:
                    raise YPYDataValidationError('Key property callactiveindex is None')
                if self.callactivesetuptime is None:
                    raise YPYDataValidationError('Key property callactivesetuptime is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallActiveTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallActiveEntry[CISCO-VOICE-DIAL-CONTROL-MIB:callActiveIndex = ' + str(self.callactiveindex) + '][CISCO-VOICE-DIAL-CONTROL-MIB:callActiveSetupTime = ' + str(self.callactivesetuptime) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.callactiveindex is not None:
                    return True

                if self.callactivesetuptime is not None:
                    return True

                if self.cvcallactiveaccountcode is not None:
                    return True

                if self.cvcallactiveacomlevel is not None:
                    return True

                if self.cvcallactivecalleridblock is not None:
                    return True

                if self.cvcallactivecallid is not None:
                    return True

                if self.cvcallactivecallingname is not None:
                    return True

                if self.cvcallactivecodertyperate is not None:
                    return True

                if self.cvcallactiveconnectionid is not None:
                    return True

                if self.cvcallactiveecanreflectorlocation is not None:
                    return True

                if self.cvcallactiveerllevel is not None:
                    return True

                if self.cvcallactiveerllevelrev1 is not None:
                    return True

                if self.cvcallactivefaxtxduration is not None:
                    return True

                if self.cvcallactiveimgpagecount is not None:
                    return True

                if self.cvcallactiveinsignallevel is not None:
                    return True

                if self.cvcallactivenoiselevel is not None:
                    return True

                if self.cvcallactiveoutsignallevel is not None:
                    return True

                if self.cvcallactivesessiontarget is not None:
                    return True

                if self.cvcallactivetxduration is not None:
                    return True

                if self.cvcallactivevoicetxduration is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallActiveTable.CvCallActiveEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallActiveTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcallactiveentry is not None:
                for child_ref in self.cvcallactiveentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallActiveTable']['meta_info']


    class CvCallDurationStatsTable(object):
        """
        This table represents the number of calls below a specific
        duration in various interval length defined by 
        the CvCallVolumeStatsIntvlType object.  
        
        The specific duration is configurable value of 
         cvCallDurationStatsThreshold object.
        
        Each interval may contain one or more entries to allow for 
        detailed measurement to be collected.
        
        .. attribute:: cvcalldurationstatsentry
        
        	This is a conceptual\-row in cvCallDurationStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of :py:class:`CvCallDurationStatsEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallDurationStatsTable.CvCallDurationStatsEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcalldurationstatsentry = YList()
            self.cvcalldurationstatsentry.parent = self
            self.cvcalldurationstatsentry.name = 'cvcalldurationstatsentry'


        class CvCallDurationStatsEntry(object):
            """
            This is a conceptual\-row in cvCallDurationStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvcalldurationstatsintvldur
            
            	This is an index that references to the different past periods in given in interval of call Duration table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\: int
            
            	**range:** 1..72
            
            .. attribute:: cvcalldurationstatsintvldurunits
            
            	The Object indexes in Call Duration Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\: :py:class:`CvCallVolumeStatsIntvlType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeStatsIntvlType_Enum>`
            
            .. attribute:: cvcalldurationstatsavgval
            
            	This object indicates the average number of calls having a duration which is below the threshold for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvcalldurationstatsmaxval
            
            	This object indicates the maximum number of calls having a duration which is below the threshold for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.cvcalldurationstatsintvldur = None
                self.cvcalldurationstatsintvldurunits = None
                self.cvcalldurationstatsavgval = None
                self.cvcalldurationstatsmaxval = None

            @property
            def _common_path(self):
                if self.cvcalldurationstatsintvldur is None:
                    raise YPYDataValidationError('Key property cvcalldurationstatsintvldur is None')
                if self.cvcalldurationstatsintvldurunits is None:
                    raise YPYDataValidationError('Key property cvcalldurationstatsintvldurunits is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallDurationStatsTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallDurationStatsEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cvCallDurationStatsIntvlDur = ' + str(self.cvcalldurationstatsintvldur) + '][CISCO-VOICE-DIAL-CONTROL-MIB:cvCallDurationStatsIntvlDurUnits = ' + str(self.cvcalldurationstatsintvldurunits) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvcalldurationstatsintvldur is not None:
                    return True

                if self.cvcalldurationstatsintvldurunits is not None:
                    return True

                if self.cvcalldurationstatsavgval is not None:
                    return True

                if self.cvcalldurationstatsmaxval is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallDurationStatsTable.CvCallDurationStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallDurationStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcalldurationstatsentry is not None:
                for child_ref in self.cvcalldurationstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallDurationStatsTable']['meta_info']


    class CvCallHistoryTable(object):
        """
        This table is the voice extension to the call history table
        of IETF Dial Control MIB. It contains voice encapsulation
        call leg information such as voice packet statistics,
        coder usage and end to end bandwidth of the call leg.
        
        .. attribute:: cvcallhistoryentry
        
        	The information regarding a single voice encapsulation call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call history entry in the IETF Dial Control MIB is created and the call history entry contains the call establishment to a voice encapsulation peer. The entry is deleted when its associated call active entry in the IETF Dial Control MIB is deleted
        	**type**\: list of :py:class:`CvCallHistoryEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallHistoryTable.CvCallHistoryEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcallhistoryentry = YList()
            self.cvcallhistoryentry.parent = self
            self.cvcallhistoryentry.name = 'cvcallhistoryentry'


        class CvCallHistoryEntry(object):
            """
            The information regarding a single voice encapsulation
            call leg.
            The call leg entry is identified by using the same index
            objects that are used by Call Active table of IETF Dial
            Control MIB to identify the call.
            An entry of this table is created when its associated call
            history entry in the IETF Dial Control MIB is created and
            the call history entry contains the call establishment to
            a voice encapsulation peer.
            The entry is deleted when its associated call active entry
            in the IETF Dial Control MIB is deleted.
            
            .. attribute:: ccallhistoryindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvcallhistoryaccountcode
            
            	The object indicates the account code input to the call. It could be used by down stream billing server. The value of empty string indicates no account code input
            	**type**\: str
            
            	**range:** 0..50
            
            .. attribute:: cvcallhistoryacomlevel
            
            	The object contains the average ACOM level for the call leg. The value \-1 indicates the level can not be determined or level detection is disabled
            	**type**\: int
            
            	**range:** \-1..127
            
            .. attribute:: cvcallhistorycalleridblock
            
            	The object indicates whether or not the caller ID feature is blocked for this call
            	**type**\: bool
            
            .. attribute:: cvcallhistorycallid
            
            	This object represents the call identifier for the telephony leg, which was assigned to the call
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvcallhistorycallingname
            
            	The calling party name of the call. If the name is not available, then it will have a length of zero
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvcallhistorycodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call
            	**type**\: :py:class:`CvcCoderTypeRate_Enum <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate_Enum>`
            
            .. attribute:: cvcallhistoryconnectionid
            
            	The global connection identifier for the telephony leg, which was assigned to the call
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: cvcallhistoryfaxtxduration
            
            	Duration of fax transmitted from this peer to voice gateway for this call leg. The FAX Utilization Rate can be obtained by dividing this by cvCallHistoryTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvcallhistoryimgpagecount
            
            	The number of FAX related image pages are received or transmitted via the peer for the call leg
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvcallhistorynoiselevel
            
            	The object contains the average noise level for the call leg
            	**type**\: int
            
            	**range:** \-128..8
            
            .. attribute:: cvcallhistorysessiontarget
            
            	The object specifies the session target of the peer that is used for the call leg via telephony interface
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: cvcallhistorytxduration
            
            	Duration of Transmit path open from this peer to the voice gateway for the call leg. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvcallhistoryvoicetxduration
            
            	Duration for this call leg. The Voice Utilization Rate can be obtained by dividing this by cvCallHistoryTXDuration object. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.ccallhistoryindex = None
                self.cvcallhistoryaccountcode = None
                self.cvcallhistoryacomlevel = None
                self.cvcallhistorycalleridblock = None
                self.cvcallhistorycallid = None
                self.cvcallhistorycallingname = None
                self.cvcallhistorycodertyperate = None
                self.cvcallhistoryconnectionid = None
                self.cvcallhistoryfaxtxduration = None
                self.cvcallhistoryimgpagecount = None
                self.cvcallhistorynoiselevel = None
                self.cvcallhistorysessiontarget = None
                self.cvcallhistorytxduration = None
                self.cvcallhistoryvoicetxduration = None

            @property
            def _common_path(self):
                if self.ccallhistoryindex is None:
                    raise YPYDataValidationError('Key property ccallhistoryindex is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallHistoryTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallHistoryEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cCallHistoryIndex = ' + str(self.ccallhistoryindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ccallhistoryindex is not None:
                    return True

                if self.cvcallhistoryaccountcode is not None:
                    return True

                if self.cvcallhistoryacomlevel is not None:
                    return True

                if self.cvcallhistorycalleridblock is not None:
                    return True

                if self.cvcallhistorycallid is not None:
                    return True

                if self.cvcallhistorycallingname is not None:
                    return True

                if self.cvcallhistorycodertyperate is not None:
                    return True

                if self.cvcallhistoryconnectionid is not None:
                    return True

                if self.cvcallhistoryfaxtxduration is not None:
                    return True

                if self.cvcallhistoryimgpagecount is not None:
                    return True

                if self.cvcallhistorynoiselevel is not None:
                    return True

                if self.cvcallhistorysessiontarget is not None:
                    return True

                if self.cvcallhistorytxduration is not None:
                    return True

                if self.cvcallhistoryvoicetxduration is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallHistoryTable.CvCallHistoryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcallhistoryentry is not None:
                for child_ref in self.cvcallhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallHistoryTable']['meta_info']


    class CvCallLegRateStatsTable(object):
        """
        cvCallLegRateStatsTable table represents voice call leg rate
        measurement in various interval lengths defined by 
        the CvCallVolumeStatsIntvlType object.
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected.
        
        .. attribute:: cvcalllegratestatsentry
        
        	This is a conceptual\-row in cvCallLegRateStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of :py:class:`CvCallLegRateStatsEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallLegRateStatsTable.CvCallLegRateStatsEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcalllegratestatsentry = YList()
            self.cvcalllegratestatsentry.parent = self
            self.cvcalllegratestatsentry.name = 'cvcalllegratestatsentry'


        class CvCallLegRateStatsEntry(object):
            """
            This is a conceptual\-row in cvCallLegRateStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvcalllegratestatsintvldur
            
            	This is an index that references to the different past periods in given in interval of call rate table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\: int
            
            	**range:** 1..72
            
            .. attribute:: cvcalllegratestatsintvldurunits
            
            	The Object indexes in Call Leg Rate Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\: :py:class:`CvCallVolumeStatsIntvlType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeStatsIntvlType_Enum>`
            
            .. attribute:: cvcalllegratestatsavgval
            
            	This object indicates the average call\-legs per second that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvcalllegratestatsmaxval
            
            	This object indicates the maximum call\-legs per second that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.cvcalllegratestatsintvldur = None
                self.cvcalllegratestatsintvldurunits = None
                self.cvcalllegratestatsavgval = None
                self.cvcalllegratestatsmaxval = None

            @property
            def _common_path(self):
                if self.cvcalllegratestatsintvldur is None:
                    raise YPYDataValidationError('Key property cvcalllegratestatsintvldur is None')
                if self.cvcalllegratestatsintvldurunits is None:
                    raise YPYDataValidationError('Key property cvcalllegratestatsintvldurunits is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallLegRateStatsTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallLegRateStatsEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cvCallLegRateStatsIntvlDur = ' + str(self.cvcalllegratestatsintvldur) + '][CISCO-VOICE-DIAL-CONTROL-MIB:cvCallLegRateStatsIntvlDurUnits = ' + str(self.cvcalllegratestatsintvldurunits) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvcalllegratestatsintvldur is not None:
                    return True

                if self.cvcalllegratestatsintvldurunits is not None:
                    return True

                if self.cvcalllegratestatsavgval is not None:
                    return True

                if self.cvcalllegratestatsmaxval is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallLegRateStatsTable.CvCallLegRateStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallLegRateStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcalllegratestatsentry is not None:
                for child_ref in self.cvcalllegratestatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallLegRateStatsTable']['meta_info']


    class CvCallLegRateWMTable(object):
        """
        cvCallLegRateWMTable table represents high watermarks achieved
        by call\-leg rate in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow for 
        detailed measurement to be collected
        
        .. attribute:: cvcalllegratewmentry
        
        	This is a conceptual\-row in cvCallLegRateWMTable This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted  if cvCallVolumeWMTableSize is changed
        	**type**\: list of :py:class:`CvCallLegRateWMEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallLegRateWMTable.CvCallLegRateWMEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcalllegratewmentry = YList()
            self.cvcalllegratewmentry.parent = self
            self.cvcalllegratewmentry.name = 'cvcalllegratewmentry'


        class CvCallLegRateWMEntry(object):
            """
            This is a conceptual\-row in cvCallLegRateWMTable
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted  if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvcalllegratewmindex
            
            	This is an index that references to different peaks in past period in call leg rate watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: cvcalllegratewmintvldurunits
            
            	The Object indexes in call leg rate Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\: :py:class:`CvCallVolumeWMIntvlType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeWMIntvlType_Enum>`
            
            .. attribute:: cvcalllegratewmts
            
            	This object indicates date and time when the high watermark is achieved for call\-legs per second for the given interval
            	**type**\: str
            
            .. attribute:: cvcalllegratewmvalue
            
            	This object indicates high watermark value achieved by the call legs per second for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.cvcalllegratewmindex = None
                self.cvcalllegratewmintvldurunits = None
                self.cvcalllegratewmts = None
                self.cvcalllegratewmvalue = None

            @property
            def _common_path(self):
                if self.cvcalllegratewmindex is None:
                    raise YPYDataValidationError('Key property cvcalllegratewmindex is None')
                if self.cvcalllegratewmintvldurunits is None:
                    raise YPYDataValidationError('Key property cvcalllegratewmintvldurunits is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallLegRateWMTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallLegRateWMEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cvCallLegRateWMIndex = ' + str(self.cvcalllegratewmindex) + '][CISCO-VOICE-DIAL-CONTROL-MIB:cvCallLegRateWMIntvlDurUnits = ' + str(self.cvcalllegratewmintvldurunits) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvcalllegratewmindex is not None:
                    return True

                if self.cvcalllegratewmintvldurunits is not None:
                    return True

                if self.cvcalllegratewmts is not None:
                    return True

                if self.cvcalllegratewmvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallLegRateWMTable.CvCallLegRateWMEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallLegRateWMTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcalllegratewmentry is not None:
                for child_ref in self.cvcalllegratewmentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallLegRateWMTable']['meta_info']


    class CvCallRateMonitor(object):
        """
        
        
        .. attribute:: cvcallrate
        
        	This object represents the total number of calls handled by the gateway during the  monitored time
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: cvcallratehiwatermark
        
        	This object represents the high water mark for the number of calls handled by the  gateway in an unit interval of  cvCallRateMonitorTime, from the time  the call\-monitoring is enabled
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: cvcallratemonitorenable
        
        	This object represents the state of call\-monitoring. A value of 'true' indicates that call\-monitoring  is enabled.  A value of 'false' indicates that  call\-monitoring is disabled
        	**type**\: bool
        
        .. attribute:: cvcallratemonitortime
        
        	This object represents the interval for which the gateway monitors the call\-rate
        	**type**\: int
        
        	**range:** 1..12
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcallrate = None
            self.cvcallratehiwatermark = None
            self.cvcallratemonitorenable = None
            self.cvcallratemonitortime = None

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallRateMonitor'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcallrate is not None:
                return True

            if self.cvcallratehiwatermark is not None:
                return True

            if self.cvcallratemonitorenable is not None:
                return True

            if self.cvcallratemonitortime is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallRateMonitor']['meta_info']


    class CvCallRateStatsTable(object):
        """
        This table represents voice call rate measurement in various
        interval lengths defined by the 
        CvCallVolumeStatsIntvlType object.
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected.
        
        .. attribute:: cvcallratestatsentry
        
        	This is a conceptual\-row in cvCallRateStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of :py:class:`CvCallRateStatsEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallRateStatsTable.CvCallRateStatsEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcallratestatsentry = YList()
            self.cvcallratestatsentry.parent = self
            self.cvcallratestatsentry.name = 'cvcallratestatsentry'


        class CvCallRateStatsEntry(object):
            """
            This is a conceptual\-row in cvCallRateStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvcallratestatsintvldur
            
            	This is an index that references to the different past periods in given in interval of call rate table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\: int
            
            	**range:** 1..72
            
            .. attribute:: cvcallratestatsintvldurunits
            
            	The Object indexes in Call Rate Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\: :py:class:`CvCallVolumeStatsIntvlType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeStatsIntvlType_Enum>`
            
            .. attribute:: cvcallratestatsavgval
            
            	This object indicates the average calls per second that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvcallratestatsmaxval
            
            	This object indicates the maximum calls per second that occured for the given period for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.cvcallratestatsintvldur = None
                self.cvcallratestatsintvldurunits = None
                self.cvcallratestatsavgval = None
                self.cvcallratestatsmaxval = None

            @property
            def _common_path(self):
                if self.cvcallratestatsintvldur is None:
                    raise YPYDataValidationError('Key property cvcallratestatsintvldur is None')
                if self.cvcallratestatsintvldurunits is None:
                    raise YPYDataValidationError('Key property cvcallratestatsintvldurunits is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallRateStatsTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallRateStatsEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cvCallRateStatsIntvlDur = ' + str(self.cvcallratestatsintvldur) + '][CISCO-VOICE-DIAL-CONTROL-MIB:cvCallRateStatsIntvlDurUnits = ' + str(self.cvcallratestatsintvldurunits) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvcallratestatsintvldur is not None:
                    return True

                if self.cvcallratestatsintvldurunits is not None:
                    return True

                if self.cvcallratestatsavgval is not None:
                    return True

                if self.cvcallratestatsmaxval is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallRateStatsTable.CvCallRateStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallRateStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcallratestatsentry is not None:
                for child_ref in self.cvcallratestatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallRateStatsTable']['meta_info']


    class CvCallRateWMTable(object):
        """
        This table represents high watermarks achieved
        by call rate in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow for 
        detailed measurement to be collected
        
        .. attribute:: cvcallratewmentry
        
        	This is a conceptual\-row in cvCallRateWMTable This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted  if cvCallVolumeWMTableSize is changed
        	**type**\: list of :py:class:`CvCallRateWMEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallRateWMTable.CvCallRateWMEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcallratewmentry = YList()
            self.cvcallratewmentry.parent = self
            self.cvcallratewmentry.name = 'cvcallratewmentry'


        class CvCallRateWMEntry(object):
            """
            This is a conceptual\-row in cvCallRateWMTable
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted  if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvcallratewmindex
            
            	This is an index that references to different peaks in past period in call rate watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: cvcallratewmintvldurunits
            
            	The Object indexes in call rate Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\: :py:class:`CvCallVolumeWMIntvlType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeWMIntvlType_Enum>`
            
            .. attribute:: cvcallratewmts
            
            	This object indicates date and Time when the high watermark is achieved for calls per second for the given interval
            	**type**\: str
            
            .. attribute:: cvcallratewmvalue
            
            	This object indicates high watermark value achieved by the calls per second for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.cvcallratewmindex = None
                self.cvcallratewmintvldurunits = None
                self.cvcallratewmts = None
                self.cvcallratewmvalue = None

            @property
            def _common_path(self):
                if self.cvcallratewmindex is None:
                    raise YPYDataValidationError('Key property cvcallratewmindex is None')
                if self.cvcallratewmintvldurunits is None:
                    raise YPYDataValidationError('Key property cvcallratewmintvldurunits is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallRateWMTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallRateWMEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cvCallRateWMIndex = ' + str(self.cvcallratewmindex) + '][CISCO-VOICE-DIAL-CONTROL-MIB:cvCallRateWMIntvlDurUnits = ' + str(self.cvcallratewmintvldurunits) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvcallratewmindex is not None:
                    return True

                if self.cvcallratewmintvldurunits is not None:
                    return True

                if self.cvcallratewmts is not None:
                    return True

                if self.cvcallratewmvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallRateWMTable.CvCallRateWMEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallRateWMTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcallratewmentry is not None:
                for child_ref in self.cvcallratewmentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallRateWMTable']['meta_info']


    class CvCallVolConnTable(object):
        """
        This table represents the number of active
        call connections for each call connection type
        in the voice gateway.
        
        .. attribute:: cvcallvolconnentry
        
        	An entry in the cvCallVolConnTable indicates number of active calls for a call connection type in the voice gateway
        	**type**\: list of :py:class:`CvCallVolConnEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallVolConnTable.CvCallVolConnEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcallvolconnentry = YList()
            self.cvcallvolconnentry.parent = self
            self.cvcallvolconnentry.name = 'cvcallvolconnentry'


        class CvCallVolConnEntry(object):
            """
            An entry in the cvCallVolConnTable indicates
            number of active calls for a call connection type
            in the voice gateway.
            
            .. attribute:: cvcallvolconnindex
            
            	This object represents index to the cvCallVolConnTable
            	**type**\: :py:class:`CvCallConnectionType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallConnectionType_Enum>`
            
            .. attribute:: cvcallvolconnactiveconnection
            
            	This object represents the total number of active calls for a connection type  in the voice gateway
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.cvcallvolconnindex = None
                self.cvcallvolconnactiveconnection = None

            @property
            def _common_path(self):
                if self.cvcallvolconnindex is None:
                    raise YPYDataValidationError('Key property cvcallvolconnindex is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallVolConnTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallVolConnEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cvCallVolConnIndex = ' + str(self.cvcallvolconnindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvcallvolconnindex is not None:
                    return True

                if self.cvcallvolconnactiveconnection is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallVolConnTable.CvCallVolConnEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallVolConnTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcallvolconnentry is not None:
                for child_ref in self.cvcallvolconnentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallVolConnTable']['meta_info']


    class CvCallVolIfTable(object):
        """
        This table represents the information about
        the usage of an IP interface in a voice
        gateway for voice media calls. This table
        has a sparse\-dependent relationship with  
        ifTable. There exists an entry in this table, 
        for each of the  entries in ifTable where ifType 
        is one of 'ethernetCsmacd' and 'softwareLoopback'.
        
        .. attribute:: cvcallvolifentry
        
        	Each entry represents a row in cvCallVolIfTable and corresponds to the information about an IP  interface in the voice gateway
        	**type**\: list of :py:class:`CvCallVolIfEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvCallVolIfTable.CvCallVolIfEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcallvolifentry = YList()
            self.cvcallvolifentry.parent = self
            self.cvcallvolifentry.name = 'cvcallvolifentry'


        class CvCallVolIfEntry(object):
            """
            Each entry represents a row in cvCallVolIfTable
            and corresponds to the information about an IP 
            interface in the voice gateway.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cvcallvolmediaincomingcalls
            
            	This object represents the total number of inbound active media calls through this IP  interface
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvcallvolmediaoutgoingcalls
            
            	This object represents the total number of outbound active media calls through the IP  interface
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cvcallvolmediaincomingcalls = None
                self.cvcallvolmediaoutgoingcalls = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallVolIfTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallVolIfEntry[CISCO-VOICE-DIAL-CONTROL-MIB:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.cvcallvolmediaincomingcalls is not None:
                    return True

                if self.cvcallvolmediaoutgoingcalls is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallVolIfTable.CvCallVolIfEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallVolIfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcallvolifentry is not None:
                for child_ref in self.cvcallvolifentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallVolIfTable']['meta_info']


    class CvCallVolume(object):
        """
        
        
        .. attribute:: cvcallvolconnmaxcallconnectionlicenese
        
        	This object represents the licensed call capacity for a voice gateway.  If the value is 0, no  licensing is done and the gateway can be  accomodate as many calls depending on its capability
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: cvcallvolconntotalactiveconnections
        
        	This object represents the total number of active call legs in the voice gateway
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcallvolconnmaxcallconnectionlicenese = None
            self.cvcallvolconntotalactiveconnections = None

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallVolume'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcallvolconnmaxcallconnectionlicenese is not None:
                return True

            if self.cvcallvolconntotalactiveconnections is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallVolume']['meta_info']


    class CvCallVolumeStatsHistory(object):
        """
        
        
        .. attribute:: cvcalldurationstatsthreshold
        
        	This Object specifies the thresold duration in seconds. cvCallDurationStatsTable will monitor all the calls below this  threshold.  Decresing the value of the threshold will reset this table
        	**type**\: int
        
        	**range:** 1..3600
        
        .. attribute:: cvcallvolumewmtablesize
        
        	This Object specifies the number of entries the watermark table will maintain.  This value will decide the number of elements in cvCallRateWMTable, cvCallLegRateWMTable, cvActiveCallWMTable and cvSipMsgRateWMTable
        	**type**\: int
        
        	**range:** 3..10
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcalldurationstatsthreshold = None
            self.cvcallvolumewmtablesize = None

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvCallVolumeStatsHistory'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcalldurationstatsthreshold is not None:
                return True

            if self.cvcallvolumewmtablesize is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvCallVolumeStatsHistory']['meta_info']


    class CvGatewayCallActive(object):
        """
        
        
        .. attribute:: cvcallactiveds0s
        
        	The current number of DS0 interfaces used for the active calls
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvcallactiveds0shighnotifyenable
        
        	Specifies whether or not cvdcActiveDS0sHighNotification should be generated.  'true' \: Indicates that the cvdcActiveDS0sHighNotification          generation is enabled.  'false'\: Indicates that cvdcActiveDS0sHighNotification          generation is disabled
        	**type**\: bool
        
        .. attribute:: cvcallactiveds0shighthreshold
        
        	A high threshold used to determine when to generate the cvdcActiveDS0sHighNotification. This object  represents the percentage of active DS0s in total number  of DS0s
        	**type**\: int
        
        	**range:** 0..100
        
        .. attribute:: cvcallactiveds0slownotifyenable
        
        	Specifies whether or not cvdcActiveDS0sLowNotification should be generated.  'true' \: Indicates that the cvdcActiveDS0sLowNotification          generation is enabled.  'false'\: Indicates that cvdcActiveDS0sLowNotification          generation is disabled
        	**type**\: bool
        
        .. attribute:: cvcallactiveds0slowthreshold
        
        	A low threshold used to determine when to generate the cvdcActiveDS0sLowNotification notification. This object  represents the percentage of active DS0s in total number  of DS0s
        	**type**\: int
        
        	**range:** 0..100
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvcallactiveds0s = None
            self.cvcallactiveds0shighnotifyenable = None
            self.cvcallactiveds0shighthreshold = None
            self.cvcallactiveds0slownotifyenable = None
            self.cvcallactiveds0slowthreshold = None

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvGatewayCallActive'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvcallactiveds0s is not None:
                return True

            if self.cvcallactiveds0shighnotifyenable is not None:
                return True

            if self.cvcallactiveds0shighthreshold is not None:
                return True

            if self.cvcallactiveds0slownotifyenable is not None:
                return True

            if self.cvcallactiveds0slowthreshold is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvGatewayCallActive']['meta_info']


    class CvGeneralConfiguration(object):
        """
        
        
        .. attribute:: cvgeneraldscppolicynotificationenable
        
        	This object indicates whether cvdcPolicyViolationNotification traps should be generated for a RPH to DSCP mapping violation for SIP voice calls.  If the value of this object is 'true', cvdcPolicyViolationNotification traps will be generated for SIP voice over IP peers when a RPH to DSCP violation condition is detected .  If the value of this object is 'false', cvdcPolicyViolationNotification traps will be generated only for calls for which the  cvVoIPPeerCfgDSCPPolicyNotificationEnable object of voice over IP peers having set to 'true'
        	**type**\: bool
        
        .. attribute:: cvgeneralfallbacknotificationenable
        
        	This object indicates whether cvdcFallbackNotification traps should be generated for fallback. If the value of this object is 'true', cvdcFallbackNotification traps will be generated for all voice over IP peers
        	**type**\: bool
        
        .. attribute:: cvgeneralmediapolicynotificationenable
        
        	This object indicates whether cvdcPolicyViolationNotification traps should be generated for Media violation for SIP voice calls.  If the value of this object is 'true', cvdcPolicyViolationNotification traps will be generated for SIP voice over IP peers when media violation condition is detected .  If the value of this object is 'false', cvdcPolicyViolationNotification traps will be generated only for calls for which the  cvVoIPPeerCfgMediaPolicyNotificationEnable object of voice over IP peers having set to 'true'
        	**type**\: bool
        
        .. attribute:: cvgeneralpoorqovnotificationenable
        
        	This object indicates whether cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps should be generated for a poor quality of voice calls.  If the value of this object is 'true', cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps will be generated for all voice over IP peers when a poor quality of voice call condition is detected after the voice gateway call disconnection.  If the value of this object is 'false', cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps will be generated only for calls for which the cvVoIPPeerCfgPoorQoVNotificationEnable object of voice over IP peers having set to 'true'
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvgeneraldscppolicynotificationenable = None
            self.cvgeneralfallbacknotificationenable = None
            self.cvgeneralmediapolicynotificationenable = None
            self.cvgeneralpoorqovnotificationenable = None

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvGeneralConfiguration'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvgeneraldscppolicynotificationenable is not None:
                return True

            if self.cvgeneralfallbacknotificationenable is not None:
                return True

            if self.cvgeneralmediapolicynotificationenable is not None:
                return True

            if self.cvgeneralpoorqovnotificationenable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvGeneralConfiguration']['meta_info']


    class CvPeerCfgTable(object):
        """
        The table contains the Voice Generic Peer information that
        is used to create an ifIndexed row with an appropriate
        ifType that is associated with the cvPeerCfgType and
        cvPeerCfgPeerType objects.
        
        .. attribute:: cvpeercfgentry
        
        	A single voice generic Peer. The creation of this entry will create an associated ifEntry with an ifType that is associated with cvPeerCfgType, i.e., for 'voiceEncap' encapsulation, an ifEntry will contain an ifType voiceEncap(103); for 'voiceOverIp' encapsulation, an ifEntry will contain an ifType voiceOverIp(104). The ifAdminStatus of the newly created ifEntry is set to 'up' and ifOperStatus is set to 'down'. In addition, an associated voiceEncap/voiceOverIp Peer configuration entry is created after the successful ifEntry creation. Then ifIndex of the newly created ifEntry must be used by the network manager to create a peer configuration entry of IETF Dial Control MIB (Refer to RFC 2128 section 2.2.3.1 and the description of dialCtlPeerCfgEntry for the detailed information). In summary, the voice dial peer creation steps are as follows\: [1] create this entry (voice/data generic peer entry). [2] read the cvPeerCfgIfIndex of this entry for the     ifIndex of newly created voice/data generic peer. [3] create the dialCtlPeerCfgEntry of RFC 2128 with the     indices of dialCtlPeerCfgId and the ifIndex of newly     created voice generic peer.  For each VoIP peer, it uses IP address and UDP port with RTP protocol to transfer voice packet. Therefore, it does not have its lower layer interface. The dialCtlPeerCfgIfType object of IETF Dial Control MIB must set to 'other' and the dialCtlPeerCfgLowerIf must set to '0'.  After the successful creation of peer configuration entry of IETF Dial Control MIB, the dial plan software in managed device will set the ifOperStatus of the newly created voiceEncap/voiceOverIp ifEntry to 'up' for enabling the peer function if the peer configuration is completed. When this entry is deleted, its associated ifEntry, voiceEncap/voiceOverIp specific peer entry and the peer entry of IETF Dial Control MIB are deleted
        	**type**\: list of :py:class:`CvPeerCfgEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvPeerCfgTable.CvPeerCfgEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvpeercfgentry = YList()
            self.cvpeercfgentry.parent = self
            self.cvpeercfgentry.name = 'cvpeercfgentry'


        class CvPeerCfgEntry(object):
            """
            A single voice generic Peer. The creation of this
            entry will create an associated ifEntry with an ifType
            that is associated with cvPeerCfgType, i.e., for
            'voiceEncap' encapsulation, an ifEntry will contain an
            ifType voiceEncap(103); for 'voiceOverIp' encapsulation,
            an ifEntry will contain an ifType voiceOverIp(104). The
            ifAdminStatus of the newly created ifEntry is set to 'up'
            and ifOperStatus is set to 'down'. In addition, an
            associated voiceEncap/voiceOverIp Peer configuration
            entry is created after the successful ifEntry creation.
            Then ifIndex of the newly created ifEntry must be used by
            the network manager to create a peer configuration entry
            of IETF Dial Control MIB (Refer to RFC 2128 section
            2.2.3.1 and the description of dialCtlPeerCfgEntry for the
            detailed information).
            In summary, the voice dial peer creation steps are as
            follows\:
            [1] create this entry (voice/data generic peer entry).
            [2] read the cvPeerCfgIfIndex of this entry for the
                ifIndex of newly created voice/data generic peer.
            [3] create the dialCtlPeerCfgEntry of RFC 2128 with the
                indices of dialCtlPeerCfgId and the ifIndex of newly
                created voice generic peer.
            
            For each VoIP peer, it uses IP address and UDP port with
            RTP protocol to transfer voice packet. Therefore, it does
            not have its lower layer interface. The
            dialCtlPeerCfgIfType object of IETF Dial Control MIB must
            set to 'other' and the dialCtlPeerCfgLowerIf must set to
            '0'.
            
            After the successful creation of peer configuration entry
            of IETF Dial Control MIB, the dial plan software in
            managed device will set the ifOperStatus of the newly
            created voiceEncap/voiceOverIp ifEntry to 'up' for
            enabling the peer function if the peer configuration is
            completed.
            When this entry is deleted, its associated ifEntry,
            voiceEncap/voiceOverIp specific peer entry and the peer
            entry of IETF Dial Control MIB are deleted.
            
            .. attribute:: cvpeercfgindex
            
            	An arbitrary index that uniquely identifies a generic voice peer
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cvcallvolpeerincomingcalls
            
            	This object represents the total number of active calls that has selected the dialpeer as an incoming dialpeer
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvcallvolpeeroutgoingcalls
            
            	This object represents the total number of active calls that has selected the dialpeer as an outgoing dialpeer
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvpeercfgifindex
            
            	The ifIndex of the peer associated ifEntry. The ifIndex appears after the associated ifEntry is created successfully. This ifIndex will be used to access the objects in the Voice over Telephony or Voice over IP peer specific table. In addition, the ifIndex is also used to access the associated peer configuration entry of the IETF Dial Control MIB. If the peer associated ifEntry had not been created, then this object has a value of zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cvpeercfgpeertype
            
            	Specifies the type of a peer. voice \- peer in voice type to be defined in a voice         gateway for voice calls.  data  \- peer in data type to be defined in gateway         that supports universal ports for modem/data         calls and integrated ports for data calls
            	**type**\: :py:class:`CvPeerCfgPeerType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvPeerCfgTable.CvPeerCfgEntry.CvPeerCfgPeerType_Enum>`
            
            .. attribute:: cvpeercfgrowstatus
            
            	This object is used to create a new row or modify or delete an existing row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cvpeercfgtype
            
            	Specifies the type of voice related encapsulation. voice \- voice encapsulation (voiceEncap ifType) on the         telephony network. voip  \- VoIP encapsulation (voiceOverIp ifType) on the IP         network. mmail \- Media Mail over IP encapsulation (mediaMailOverIp         ifType) on the IP network. voatm \- VoATM encapsulation (voiceOverATM ifType) on the         ATM network. vofr  \- VoFR encapsulation (voiceOverFR ifType) on the         Frame Relay network
            	**type**\: :py:class:`CvPeerCfgType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvPeerCfgTable.CvPeerCfgEntry.CvPeerCfgType_Enum>`
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.cvpeercfgindex = None
                self.cvcallvolpeerincomingcalls = None
                self.cvcallvolpeeroutgoingcalls = None
                self.cvpeercfgifindex = None
                self.cvpeercfgpeertype = None
                self.cvpeercfgrowstatus = None
                self.cvpeercfgtype = None

            class CvPeerCfgPeerType_Enum(Enum):
                """
                CvPeerCfgPeerType_Enum

                Specifies the type of a peer.
                voice \- peer in voice type to be defined in a voice
                        gateway for voice calls. 
                data  \- peer in data type to be defined in gateway
                        that supports universal ports for modem/data
                        calls and integrated ports for data calls.

                """

                VOICE = 1

                DATA = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                    return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvPeerCfgTable.CvPeerCfgEntry.CvPeerCfgPeerType_Enum']


            class CvPeerCfgType_Enum(Enum):
                """
                CvPeerCfgType_Enum

                Specifies the type of voice related encapsulation.
                voice \- voice encapsulation (voiceEncap ifType) on the
                        telephony network.
                voip  \- VoIP encapsulation (voiceOverIp ifType) on the IP
                        network.
                mmail \- Media Mail over IP encapsulation (mediaMailOverIp
                        ifType) on the IP network.
                voatm \- VoATM encapsulation (voiceOverATM ifType) on the
                        ATM network.
                vofr  \- VoFR encapsulation (voiceOverFR ifType) on the
                        Frame Relay network.

                """

                VOICE = 1

                VOIP = 2

                MMAIL = 3

                VOATM = 4

                VOFR = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                    return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvPeerCfgTable.CvPeerCfgEntry.CvPeerCfgType_Enum']


            @property
            def _common_path(self):
                if self.cvpeercfgindex is None:
                    raise YPYDataValidationError('Key property cvpeercfgindex is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvPeerCfgTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvPeerCfgEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cvPeerCfgIndex = ' + str(self.cvpeercfgindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvpeercfgindex is not None:
                    return True

                if self.cvcallvolpeerincomingcalls is not None:
                    return True

                if self.cvcallvolpeeroutgoingcalls is not None:
                    return True

                if self.cvpeercfgifindex is not None:
                    return True

                if self.cvpeercfgpeertype is not None:
                    return True

                if self.cvpeercfgrowstatus is not None:
                    return True

                if self.cvpeercfgtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvPeerCfgTable.CvPeerCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvPeerCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpeercfgentry is not None:
                for child_ref in self.cvpeercfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvPeerCfgTable']['meta_info']


    class CvPeerCommonCfgTable(object):
        """
        The table contains the Voice specific peer common
        configuration information that is required to accept voice
        calls or to which it will place them or process the
        incoming calls.
        
        .. attribute:: cvpeercommoncfgentry
        
        	A single Voice specific Peer. One entry per voice related encapsulation. The entry is created when a voice related encapsulation ifEntry is created. This entry is deleted when its associated ifEntry is deleted
        	**type**\: list of :py:class:`CvPeerCommonCfgEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvPeerCommonCfgTable.CvPeerCommonCfgEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvpeercommoncfgentry = YList()
            self.cvpeercommoncfgentry.parent = self
            self.cvpeercommoncfgentry.name = 'cvpeercommoncfgentry'


        class CvPeerCommonCfgEntry(object):
            """
            A single Voice specific Peer. One entry per voice related
            encapsulation.
            The entry is created when a voice related encapsulation
            ifEntry is created.
            This entry is deleted when its associated ifEntry is
            deleted.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cvpeercommoncfgapplicationname
            
            	The object specifies the application to handle the incoming call after the peer is selected. If no application name is specified, then the default session application will take care of the incoming call
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cvpeercommoncfgdnismappingname
            
            	The object specifies a Dialer Number Identification Service (DNIS) map name for the Voice specific peer entry specified in this row. A DNIS is a called party number and they can be grouped and identified by DNIS map
            	**type**\: str
            
            .. attribute:: cvpeercommoncfghuntstop
            
            	This object specifies whether dialpeer hunting should stop when this peer is reached
            	**type**\: bool
            
            .. attribute:: cvpeercommoncfgincomingdnisdigits
            
            	The object specifies the prefix of the incoming Dialed Number Identification Service (DNIS) digits for the peer. The DNIS digits prefix is used to match with the incoming DNIS number for incoming call discrimination. If the digits in this object are matched with incoming DNIS number, the  associated dialCtlPeerCfgInfoType in RFC 2128 will be used as a call discriminator for differentiating speech, data, fax, video or modem calls
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: cvpeercommoncfgmaxconnections
            
            	The object specifies the maximum allowed connection to/from the peer. A value of \-1 disables the limit of maximum connections
            	**type**\: int
            
            	**range:** \-1 \| 1..2147483647
            
            .. attribute:: cvpeercommoncfgpreference
            
            	This object specifies the selection preference of a peer when multiple peers are matched to the selection criteria. The value of 0 has the lowest preference for peer selection
            	**type**\: int
            
            	**range:** 0..10
            
            .. attribute:: cvpeercommoncfgsourcecarrierid
            
            	The object specifies the Source Carrier Id for the peer. The Source Carrier Id is used to match with the Source Carrier Id of a call. If the Source Carrier Id in this object is matched with the Source Carrier Id of a call, then the associated peer will be used to handle the call.  Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvpeercommoncfgsourcetrunkgrplabel
            
            	The object specifies the Source Trunk Group Label for the peer. The Source Trunk Group Label is used to match with the Source Trunk Group Label of a call. If the Source Trunk Group Label in this object is matched with the Source Trunk Group Label of a call, then the associated peer will be used to handle the call.  Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvpeercommoncfgtargetcarrierid
            
            	The object specifies the Target Carrier Id for the peer. The Target Carrier Id is used to match with the Target Carrier Id of a call. If the Target Carrier Id in this object is matched with the Target Carrier Id of a call, then the associated peer will be used to handle the call. Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvpeercommoncfgtargettrunkgrplabel
            
            	The object specifies the Target Trunk Group Label for the peer. The Target Trunk Group Label is used to match with the Target Trunk Group Label of a call. If the Target Trunk Group Label in this object is matched with the Target Trunk Group Label of a call, then the associated peer will be used to handle the call. Only alphanumeric characters, '\-' and '\_' are allowed in the string
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cvpeercommoncfgapplicationname = None
                self.cvpeercommoncfgdnismappingname = None
                self.cvpeercommoncfghuntstop = None
                self.cvpeercommoncfgincomingdnisdigits = None
                self.cvpeercommoncfgmaxconnections = None
                self.cvpeercommoncfgpreference = None
                self.cvpeercommoncfgsourcecarrierid = None
                self.cvpeercommoncfgsourcetrunkgrplabel = None
                self.cvpeercommoncfgtargetcarrierid = None
                self.cvpeercommoncfgtargettrunkgrplabel = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvPeerCommonCfgTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvPeerCommonCfgEntry[CISCO-VOICE-DIAL-CONTROL-MIB:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.cvpeercommoncfgapplicationname is not None:
                    return True

                if self.cvpeercommoncfgdnismappingname is not None:
                    return True

                if self.cvpeercommoncfghuntstop is not None:
                    return True

                if self.cvpeercommoncfgincomingdnisdigits is not None:
                    return True

                if self.cvpeercommoncfgmaxconnections is not None:
                    return True

                if self.cvpeercommoncfgpreference is not None:
                    return True

                if self.cvpeercommoncfgsourcecarrierid is not None:
                    return True

                if self.cvpeercommoncfgsourcetrunkgrplabel is not None:
                    return True

                if self.cvpeercommoncfgtargetcarrierid is not None:
                    return True

                if self.cvpeercommoncfgtargettrunkgrplabel is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvPeerCommonCfgTable.CvPeerCommonCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvPeerCommonCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpeercommoncfgentry is not None:
                for child_ref in self.cvpeercommoncfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvPeerCommonCfgTable']['meta_info']


    class CvSipMsgRateStatsTable(object):
        """
        This table represents the SIP message rate measurement in
        various interval length defined by the 
        CvCallVolumeStatsIntvlType object.
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected
        
        .. attribute:: cvsipmsgratestatsentry
        
        	This is a conceptual\-row in cvSipMsgRateStatsTable This entry is created at the system initialization and is updated at every epoch based on CvCallVolumeStatsIntvlType
        	**type**\: list of :py:class:`CvSipMsgRateStatsEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvSipMsgRateStatsTable.CvSipMsgRateStatsEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvsipmsgratestatsentry = YList()
            self.cvsipmsgratestatsentry.parent = self
            self.cvsipmsgratestatsentry.name = 'cvsipmsgratestatsentry'


        class CvSipMsgRateStatsEntry(object):
            """
            This is a conceptual\-row in cvSipMsgRateStatsTable
            This entry is created at the system initialization and is
            updated at every epoch based on CvCallVolumeStatsIntvlType
            
            .. attribute:: cvsipmsgratestatsintvldur
            
            	This is an index that references to the different past periods in given in interval of SIP message rate table. This range is 1\-60 for Seconds and Minutes table  wherein 1\-72 for hours table
            	**type**\: int
            
            	**range:** 1..72
            
            .. attribute:: cvsipmsgratestatsintvldurunits
            
            	The Object indexes in SIP Message Rate Table to select one among three interval\-tables.  The different types in this table are represented by  CvCallVolumeStatsIntvlType
            	**type**\: :py:class:`CvCallVolumeStatsIntvlType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeStatsIntvlType_Enum>`
            
            .. attribute:: cvsipmsgratestatsavgval
            
            	This object indicates the average SIP messages per second that is received for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvsipmsgratestatsmaxval
            
            	This object indicates the maximum SIP messages  per second that is received for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.cvsipmsgratestatsintvldur = None
                self.cvsipmsgratestatsintvldurunits = None
                self.cvsipmsgratestatsavgval = None
                self.cvsipmsgratestatsmaxval = None

            @property
            def _common_path(self):
                if self.cvsipmsgratestatsintvldur is None:
                    raise YPYDataValidationError('Key property cvsipmsgratestatsintvldur is None')
                if self.cvsipmsgratestatsintvldurunits is None:
                    raise YPYDataValidationError('Key property cvsipmsgratestatsintvldurunits is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvSipMsgRateStatsTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvSipMsgRateStatsEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cvSipMsgRateStatsIntvlDur = ' + str(self.cvsipmsgratestatsintvldur) + '][CISCO-VOICE-DIAL-CONTROL-MIB:cvSipMsgRateStatsIntvlDurUnits = ' + str(self.cvsipmsgratestatsintvldurunits) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvsipmsgratestatsintvldur is not None:
                    return True

                if self.cvsipmsgratestatsintvldurunits is not None:
                    return True

                if self.cvsipmsgratestatsavgval is not None:
                    return True

                if self.cvsipmsgratestatsmaxval is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvSipMsgRateStatsTable.CvSipMsgRateStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvSipMsgRateStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvsipmsgratestatsentry is not None:
                for child_ref in self.cvsipmsgratestatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvSipMsgRateStatsTable']['meta_info']


    class CvSipMsgRateWMTable(object):
        """
        This table represents of high watermarks achieved
        by SIP message rate in various interval length defined 
        by CvCallVolumeWMIntvlType. 
        
        Each interval may contain one or more entries to allow for
        detailed measurement to be collected
        
        .. attribute:: cvsipmsgratewmentry
        
        	This is a conceptual\-row in cvSipMsgRateWMTable. This entry is created at the system initialization and is updated whenever  a) This entry is obsolete OR b) A new/higher entry is available. These entries are reinitialised/added/deleted if cvCallVolumeWMTableSize is changed
        	**type**\: list of :py:class:`CvSipMsgRateWMEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvSipMsgRateWMTable.CvSipMsgRateWMEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvsipmsgratewmentry = YList()
            self.cvsipmsgratewmentry.parent = self
            self.cvsipmsgratewmentry.name = 'cvsipmsgratewmentry'


        class CvSipMsgRateWMEntry(object):
            """
            This is a conceptual\-row in cvSipMsgRateWMTable.
            This entry is created at the system initialization and is
            updated whenever 
            a) This entry is obsolete OR
            b) A new/higher entry is available.
            These entries are reinitialised/added/deleted if
            cvCallVolumeWMTableSize is changed
            
            .. attribute:: cvsipmsgratewmindex
            
            	This is an index that references to different peaks in past period in sip message rate watermark table.  The number of watermarks entries stored for each table are  based on cvCallVolumeWMTableSize
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: cvsipmsgratewmintvldurunits
            
            	The Object indexes in SIP Message rate Water mark Table to select one among four interval\-tables.  The different types in this table are represented by  CvCallVolumeWMIntvlType
            	**type**\: :py:class:`CvCallVolumeWMIntvlType_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvCallVolumeWMIntvlType_Enum>`
            
            .. attribute:: cvsipmsgratewmts
            
            	This object indicates date and time when the high watermark is achieved for SIP messages per second for the given interval
            	**type**\: str
            
            .. attribute:: cvsipmsgratewmvalue
            
            	This object indicates high watermark value achieved by the SIP messages per second for the given interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.cvsipmsgratewmindex = None
                self.cvsipmsgratewmintvldurunits = None
                self.cvsipmsgratewmts = None
                self.cvsipmsgratewmvalue = None

            @property
            def _common_path(self):
                if self.cvsipmsgratewmindex is None:
                    raise YPYDataValidationError('Key property cvsipmsgratewmindex is None')
                if self.cvsipmsgratewmintvldurunits is None:
                    raise YPYDataValidationError('Key property cvsipmsgratewmintvldurunits is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvSipMsgRateWMTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvSipMsgRateWMEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cvSipMsgRateWMIndex = ' + str(self.cvsipmsgratewmindex) + '][CISCO-VOICE-DIAL-CONTROL-MIB:cvSipMsgRateWMIntvlDurUnits = ' + str(self.cvsipmsgratewmintvldurunits) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvsipmsgratewmindex is not None:
                    return True

                if self.cvsipmsgratewmintvldurunits is not None:
                    return True

                if self.cvsipmsgratewmts is not None:
                    return True

                if self.cvsipmsgratewmvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvSipMsgRateWMTable.CvSipMsgRateWMEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvSipMsgRateWMTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvsipmsgratewmentry is not None:
                for child_ref in self.cvsipmsgratewmentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvSipMsgRateWMTable']['meta_info']


    class CvVoIPCallActiveTable(object):
        """
        This table is the VoIP extension to the call active table of
        IETF Dial Control MIB. It contains VoIP call leg
        information about specific VoIP call destination and the
        selected QoS for the call leg.
        
        .. attribute:: cvvoipcallactiveentry
        
        	The information regarding a single VoIP call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call active entry in the IETF Dial Control MIB is created and the call active entry contains information for the call establishment to the peer on the IP backbone via a voice over  IP peer. The entry is deleted when its associated call active entry in the IETF Dial Control MIB is deleted
        	**type**\: list of :py:class:`CvVoIPCallActiveEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoIPCallActiveTable.CvVoIPCallActiveEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvvoipcallactiveentry = YList()
            self.cvvoipcallactiveentry.parent = self
            self.cvvoipcallactiveentry.name = 'cvvoipcallactiveentry'


        class CvVoIPCallActiveEntry(object):
            """
            The information regarding a single VoIP call leg.
            The call leg entry is identified by using the same index
            objects that are used by Call Active table of IETF Dial
            Control MIB to identify the call.
            An entry of this table is created when its associated call
            active entry in the IETF Dial Control MIB is created and
            the call active entry contains information for the call
            establishment to the peer on the IP backbone via a voice
            over  IP peer.
            The entry is deleted when its associated call active entry
            in the IETF Dial Control MIB is deleted.
            
            .. attribute:: callactiveindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: callactivesetuptime
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccvoipcallactivepolicyname
            
            	This object holds the policy name. It could be media policy, DSCP policy etc
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cvvoipcallactivebitrates
            
            	This object indicates modes of Bit rates. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: :py:class:`CvAmrNbBitRateMode_Bits <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvAmrNbBitRateMode_Bits>`
            
            .. attribute:: cvvoipcallactivecallid
            
            	This object represents the call identifier for the active VoIP leg of the call
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvvoipcallactivecallreferenceid
            
            	The call reference ID associates the video call entry and voice call entry of the same endpoint.  An audio\-only call may or may not have a valid call reference ID (i.e. value greater than zero), but in both cases, there will not be a video call entry associated with it.    For a video call, the video\-specific information  is stored in a call entry in cVideoSessionActive of CISCO\-VIDEO\-SESSION\-MIB, in which the call reference ID is also identified
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivechannels
            
            	The object indicates the number of audio channels. Supported value is 1. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..6
            
            .. attribute:: cvvoipcallactivecodermode
            
            	The object indicates the iLBC codec mode. The value of this object is valid only if  cvVoIPCallActiveCoderTypeRate is equal to  'iLBC'
            	**type**\: :py:class:`CvIlbcFrameMode_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvIlbcFrameMode_Enum>`
            
            .. attribute:: cvvoipcallactivecodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call. This rate is different from the configuration rate because of rate negotiation during the call
            	**type**\: :py:class:`CvcCoderTypeRate_Enum <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate_Enum>`
            
            .. attribute:: cvvoipcallactiveconnectionid
            
            	The global connection identifier for the active VoIP leg of the call
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: cvvoipcallactivecrc
            
            	If the object has a value of true(1), frame CRC will be included in the payload and if the value is false(2), frame CRC will not be included in the payload. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallactiveearlypackets
            
            	The number of received voice packets that arrived too early to store in jitter buffer during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactiveencap
            
            	The object indicates the RTP encapsulation type. Supported RTP encapsulation type is RFC3267. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: :py:class:`CvAmrNbRtpEncap_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvAmrNbRtpEncap_Enum>`
            
            .. attribute:: cvvoipcallactivegapfillwithinterpolation
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding and following in time due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivegapfillwithprediction
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding in time due to voice data not received on time (or lost) from voice gateway for this call. An example of such playout is frame\-erasure or frame\-concealment strategies in G.729 and G.723.1 compression algorithms. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivegapfillwithredundancy
            
            	Duration of voice signal played out with signal synthesized from redundancy parameters available due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivegapfillwithsilence
            
            	Duration of voice signal replaced with signal played out during silence due to voice data not received on time (or lost) from voice gateway this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivehiwaterplayoutdelay
            
            	The high water mark Voice Playout FIFO Delay during the voice call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactiveinterleaving
            
            	The object indicates the maximum number of frame\-blocks allowed in an interleaving group. It indicates that frame\-block level interleaving will be used for that session. If this object is not set, interleaving is not used. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..50
            
            .. attribute:: cvvoipcallactivelatepackets
            
            	The number of received voice packets that arrived too late to playout with CODEC (Coder/Decoder) during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivelostpackets
            
            	The number of lost voice packets during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivelowaterplayoutdelay
            
            	The low water mark Voice Playout FIFO Delay during the voice call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivemaxptime
            
            	The object indicates the maximum amount of media that can be encapsulated in a payload. Supported value is 20 msec. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 20..100
            
            .. attribute:: cvvoipcallactivemodechgneighbor
            
            	If the object has a value of true(1), mode changes will be made to only neighboring modes set to cvVoIPCallActiveBitRates object. If the value is false(2), mode changes will be allowed to any modes set to cvVoIPCallActiveBitRates object. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallactivemodechgperiod
            
            	The object indicates the interval (N frame\-blocks) at which codec mode changes are allowed. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cvvoipcallactiveoctetaligned
            
            	If the object has a value true(1) octet align operation is used, and if the value is false(2), bandwidth efficient operation is used. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallactiveontimervplayout
            
            	Duration of voice playout from data received on time for this call. This plus the durations for the GapFills in the following entries gives the Total Voice Playout Duration for Active Voice. This does not include duration for which no data was sent by the Transmit end as voice signal, e.g., silence suppression and fax signal. The On Time Playout Rate can be computed by dividing this entry by the Total Voice Playout Duration. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactiveprotocolcallid
            
            	The protocol\-specific call identifier for the VoIP call
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvvoipcallactiveptime
            
            	The object indicates the length of the time in milliseconds represented by the media of the packet. Supported value is 20 milliseconds. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 20..100
            
            .. attribute:: cvvoipcallactivereceivedelay
            
            	The average Playout FIFO Delay plus the decoder delay during the voice call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactiveremmediaipaddr
            
            	Remote media end point IP address for the VoIP call
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvvoipcallactiveremmediaipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallActiveRemMediaIPAddr
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cvvoipcallactiveremmediaport
            
            	Remote media end point listener port to which to transmit voice packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallactiveremoteipaddress
            
            	Remote system IP address for the VoIP call
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cvvoipcallactiveremoteudpport
            
            	Remote system UDP listener port to which to transmit voice packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallactiveremsigipaddr
            
            	Remote signalling IP address for the VoIP call
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvvoipcallactiveremsigipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallActiveRemSigIPAddr
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cvvoipcallactiveremsigport
            
            	Remote signalling listener port to which to transmit voice packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallactivereverseddirectionpeeraddress
            
            	This object store the reversed direction peer address  If the address is not available, then it will have a length of zero.  If the call is ingress then it contains called number and if the call is egress then it contains calling number
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cvvoipcallactiverobustsorting
            
            	If the object has a value of true(1), payload employs robust sorting and if the value is false(2), payload does not employ robust sorting. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallactiveroundtripdelay
            
            	The voice packet round trip delay between local and the remote system on the IP backbone during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactiveselectedqos
            
            	The selected RSVP QoS for the voice call
            	**type**\: :py:class:`QosService_Enum <ydk.models.int.INT_SERV_MIB.QosService_Enum>`
            
            .. attribute:: cvvoipcallactivesessionid
            
            	This object indicates the active session ID assigned by the call manager to identify call legs that belong to the same call session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallactivesessionprotocol
            
            	The object specifies the session protocol to be used for Internet call between local and remote router via IP backbone
            	**type**\: :py:class:`CvSessionProtocol_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvSessionProtocol_Enum>`
            
            .. attribute:: cvvoipcallactivesessiontarget
            
            	The object specifies the session target of the peer that is used for the call. This object is set with the information in the call associated cvVoIPPeerCfgSessionTarget object when the voice over IP call is connected
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cvvoipcallactivesrtpenable
            
            	The object indicates whether or not the SRTP (Secured RTP) was enabled for the voice call
            	**type**\: bool
            
            .. attribute:: cvvoipcallactiveusername
            
            	The textual identifier of the calling party (user) of the call. If the username is not available, then the value of this object will have a length of zero
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: cvvoipcallactivevadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) was enabled for the voice call
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.callactiveindex = None
                self.callactivesetuptime = None
                self.ccvoipcallactivepolicyname = None
                self.cvvoipcallactivebitrates = CvAmrNbBitRateMode_Bits()
                self.cvvoipcallactivecallid = None
                self.cvvoipcallactivecallreferenceid = None
                self.cvvoipcallactivechannels = None
                self.cvvoipcallactivecodermode = None
                self.cvvoipcallactivecodertyperate = None
                self.cvvoipcallactiveconnectionid = None
                self.cvvoipcallactivecrc = None
                self.cvvoipcallactiveearlypackets = None
                self.cvvoipcallactiveencap = None
                self.cvvoipcallactivegapfillwithinterpolation = None
                self.cvvoipcallactivegapfillwithprediction = None
                self.cvvoipcallactivegapfillwithredundancy = None
                self.cvvoipcallactivegapfillwithsilence = None
                self.cvvoipcallactivehiwaterplayoutdelay = None
                self.cvvoipcallactiveinterleaving = None
                self.cvvoipcallactivelatepackets = None
                self.cvvoipcallactivelostpackets = None
                self.cvvoipcallactivelowaterplayoutdelay = None
                self.cvvoipcallactivemaxptime = None
                self.cvvoipcallactivemodechgneighbor = None
                self.cvvoipcallactivemodechgperiod = None
                self.cvvoipcallactiveoctetaligned = None
                self.cvvoipcallactiveontimervplayout = None
                self.cvvoipcallactiveprotocolcallid = None
                self.cvvoipcallactiveptime = None
                self.cvvoipcallactivereceivedelay = None
                self.cvvoipcallactiveremmediaipaddr = None
                self.cvvoipcallactiveremmediaipaddrt = None
                self.cvvoipcallactiveremmediaport = None
                self.cvvoipcallactiveremoteipaddress = None
                self.cvvoipcallactiveremoteudpport = None
                self.cvvoipcallactiveremsigipaddr = None
                self.cvvoipcallactiveremsigipaddrt = None
                self.cvvoipcallactiveremsigport = None
                self.cvvoipcallactivereverseddirectionpeeraddress = None
                self.cvvoipcallactiverobustsorting = None
                self.cvvoipcallactiveroundtripdelay = None
                self.cvvoipcallactiveselectedqos = None
                self.cvvoipcallactivesessionid = None
                self.cvvoipcallactivesessionprotocol = None
                self.cvvoipcallactivesessiontarget = None
                self.cvvoipcallactivesrtpenable = None
                self.cvvoipcallactiveusername = None
                self.cvvoipcallactivevadenable = None

            @property
            def _common_path(self):
                if self.callactiveindex is None:
                    raise YPYDataValidationError('Key property callactiveindex is None')
                if self.callactivesetuptime is None:
                    raise YPYDataValidationError('Key property callactivesetuptime is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoIPCallActiveTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoIPCallActiveEntry[CISCO-VOICE-DIAL-CONTROL-MIB:callActiveIndex = ' + str(self.callactiveindex) + '][CISCO-VOICE-DIAL-CONTROL-MIB:callActiveSetupTime = ' + str(self.callactivesetuptime) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.callactiveindex is not None:
                    return True

                if self.callactivesetuptime is not None:
                    return True

                if self.ccvoipcallactivepolicyname is not None:
                    return True

                if self.cvvoipcallactivebitrates is not None:
                    if self.cvvoipcallactivebitrates._has_data():
                        return True

                if self.cvvoipcallactivecallid is not None:
                    return True

                if self.cvvoipcallactivecallreferenceid is not None:
                    return True

                if self.cvvoipcallactivechannels is not None:
                    return True

                if self.cvvoipcallactivecodermode is not None:
                    return True

                if self.cvvoipcallactivecodertyperate is not None:
                    return True

                if self.cvvoipcallactiveconnectionid is not None:
                    return True

                if self.cvvoipcallactivecrc is not None:
                    return True

                if self.cvvoipcallactiveearlypackets is not None:
                    return True

                if self.cvvoipcallactiveencap is not None:
                    return True

                if self.cvvoipcallactivegapfillwithinterpolation is not None:
                    return True

                if self.cvvoipcallactivegapfillwithprediction is not None:
                    return True

                if self.cvvoipcallactivegapfillwithredundancy is not None:
                    return True

                if self.cvvoipcallactivegapfillwithsilence is not None:
                    return True

                if self.cvvoipcallactivehiwaterplayoutdelay is not None:
                    return True

                if self.cvvoipcallactiveinterleaving is not None:
                    return True

                if self.cvvoipcallactivelatepackets is not None:
                    return True

                if self.cvvoipcallactivelostpackets is not None:
                    return True

                if self.cvvoipcallactivelowaterplayoutdelay is not None:
                    return True

                if self.cvvoipcallactivemaxptime is not None:
                    return True

                if self.cvvoipcallactivemodechgneighbor is not None:
                    return True

                if self.cvvoipcallactivemodechgperiod is not None:
                    return True

                if self.cvvoipcallactiveoctetaligned is not None:
                    return True

                if self.cvvoipcallactiveontimervplayout is not None:
                    return True

                if self.cvvoipcallactiveprotocolcallid is not None:
                    return True

                if self.cvvoipcallactiveptime is not None:
                    return True

                if self.cvvoipcallactivereceivedelay is not None:
                    return True

                if self.cvvoipcallactiveremmediaipaddr is not None:
                    return True

                if self.cvvoipcallactiveremmediaipaddrt is not None:
                    return True

                if self.cvvoipcallactiveremmediaport is not None:
                    return True

                if self.cvvoipcallactiveremoteipaddress is not None:
                    return True

                if self.cvvoipcallactiveremoteudpport is not None:
                    return True

                if self.cvvoipcallactiveremsigipaddr is not None:
                    return True

                if self.cvvoipcallactiveremsigipaddrt is not None:
                    return True

                if self.cvvoipcallactiveremsigport is not None:
                    return True

                if self.cvvoipcallactivereverseddirectionpeeraddress is not None:
                    return True

                if self.cvvoipcallactiverobustsorting is not None:
                    return True

                if self.cvvoipcallactiveroundtripdelay is not None:
                    return True

                if self.cvvoipcallactiveselectedqos is not None:
                    return True

                if self.cvvoipcallactivesessionid is not None:
                    return True

                if self.cvvoipcallactivesessionprotocol is not None:
                    return True

                if self.cvvoipcallactivesessiontarget is not None:
                    return True

                if self.cvvoipcallactivesrtpenable is not None:
                    return True

                if self.cvvoipcallactiveusername is not None:
                    return True

                if self.cvvoipcallactivevadenable is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoIPCallActiveTable.CvVoIPCallActiveEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoIPCallActiveTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvvoipcallactiveentry is not None:
                for child_ref in self.cvvoipcallactiveentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoIPCallActiveTable']['meta_info']


    class CvVoIPCallHistoryTable(object):
        """
        This table is the VoIP extension to the call history table
        of IETF Dial Control MIB. It contains VoIP call leg
        information about specific VoIP call destination and the
        selected QoS for the call leg.
        
        .. attribute:: cvvoipcallhistoryentry
        
        	The information regarding a single VoIP call leg. The call leg entry is identified by using the same index objects that are used by Call Active table of IETF Dial Control MIB to identify the call. An entry of this table is created when its associated call history entry in the IETF Dial Control MIB is created and the call history entry contains information for the call establishment to the peer on the IP backbone via a voice over IP peer. The entry is deleted when its associated call history entry in the IETF Dial Control MIB is deleted
        	**type**\: list of :py:class:`CvVoIPCallHistoryEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoIPCallHistoryTable.CvVoIPCallHistoryEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvvoipcallhistoryentry = YList()
            self.cvvoipcallhistoryentry.parent = self
            self.cvvoipcallhistoryentry.name = 'cvvoipcallhistoryentry'


        class CvVoIPCallHistoryEntry(object):
            """
            The information regarding a single VoIP call leg.
            The call leg entry is identified by using the same index
            objects that are used by Call Active table of IETF Dial
            Control MIB to identify the call.
            An entry of this table is created when its associated call
            history entry in the IETF Dial Control MIB is created and
            the call history entry contains information for the call
            establishment to the peer on the IP backbone via a voice
            over IP peer.
            The entry is deleted when its associated call history
            entry in the IETF Dial Control MIB is deleted.
            
            .. attribute:: ccallhistoryindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvvoipcallhistorybitrates
            
            	This object indicates modes of Bit rates. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: :py:class:`CvAmrNbBitRateMode_Bits <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvAmrNbBitRateMode_Bits>`
            
            .. attribute:: cvvoipcallhistorycallid
            
            	This object represents the call identifier for the VoIP leg, which was assigned to the call
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cvvoipcallhistorycallreferenceid
            
            	The call reference ID associates the video call entry and voice call entry of the same endpoint.  An audio\-only call may or may not have a valid call reference ID (i.e. value greater than zero), but in both cases, there will not be a video call entry associated with it.   For a video call, the video\-specific information  is stored in a call entry in cVideoSessionActive of CISCO\-VIDEO\-SESSION\-MIB, in which the call reference ID is also identified
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorychannels
            
            	The object indicates the number of audio channels. Supported value is 1. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..6
            
            .. attribute:: cvvoipcallhistorycodermode
            
            	The object indicates the iLBC mode. The value of this object is valid only if  cvVoIPCallHistoryCoderTypeRate is equal to  'iLBC'
            	**type**\: :py:class:`CvIlbcFrameMode_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvIlbcFrameMode_Enum>`
            
            .. attribute:: cvvoipcallhistorycodertyperate
            
            	The negotiated coder rate. It specifies the transmit rate of voice/fax compression to its associated call leg for the call. This rate is different from the configuration rate because of rate negotiation during the call
            	**type**\: :py:class:`CvcCoderTypeRate_Enum <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcCoderTypeRate_Enum>`
            
            .. attribute:: cvvoipcallhistoryconnectionid
            
            	The global connection identifier for the VoIP leg, which was assigned to the call
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: cvvoipcallhistorycrc
            
            	If the object has a value of true(1), frame CRC will be included in the payload and if the value is false(2), frame CRC will not be included in the payload. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallhistoryearlypackets
            
            	The number of received voice packets that are arrived too early to store in jitter buffer during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryencap
            
            	The object indicates the RTP encapsulation type. Supported RTP encapsulation type is RFC3267. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: :py:class:`CvAmrNbRtpEncap_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvAmrNbRtpEncap_Enum>`
            
            .. attribute:: cvvoipcallhistoryfallbackdelay
            
            	The FallbackDelay is calculated as follows \- Take the sum of the round trips for all the probes,  divide by the number of probes,  and divide by two to get the one\-way delay.   Then add in jitter\_in or jiter\_out, which ever is higher
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryfallbackicpif
            
            	The Calculated Planning Impairment Factor (Icpif) of the call  that is associated to this call leg. The value in this object is computed by the following equation. Icpif of the fallback probe = Itotal (total impairment value)  \- configured fallback (Expectation Factor). A value of 0 implies that Icpif was not calculated and is meaningless for this attempt
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cvvoipcallhistoryfallbackloss
            
            	FallbackLoss is the percentage of loss packets based on the total packets sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorygapfillwithinterpolation
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding and following in time due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorygapfillwithprediction
            
            	Duration of voice signal played out with signal synthesized from parameters or samples of data preceding in time due to voice data not received on time (or lost) from voice gateway for this call. An example of such playout is frame\-erasure or  frame\-concealment strategies in G.729 and G.723.1 compression algorithms. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorygapfillwithredundancy
            
            	Duration of voice signal played out with signal synthesized from redundancy parameters available due to voice data not received on time (or lost) from voice gateway for this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorygapfillwithsilence
            
            	Duration of voice signal replaced with signal played out during silence due to voice data not received on time (or lost) from voice gateway this call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryhiwaterplayoutdelay
            
            	The high water mark Voice Playout FIFO Delay during the voice call. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryicpif
            
            	The Calculated Planning Impairment Factor (Icpif) of the call  that is associated to this call leg. The value in this object is computed by the following equation. Icpif of the call = Itotal (total impairment value) of the call \- A (Expectation Factor) in the cvVoIPPeerCfgExpectFactor of the call leg associated peer. A value of \-1 implies that Icpif was not calculated and is meaningless for this call
            	**type**\: int
            
            	**range:** \-1..55
            
            .. attribute:: cvvoipcallhistoryinterleaving
            
            	The object indicates the maximum number of frame\-blocks allowed in an interleaving group. It indicates that frame\-block level interleaving will be used for that session. If this object is not set, interleaving is not used. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..50
            
            .. attribute:: cvvoipcallhistorylatepackets
            
            	The number of received voice packets that are arrived too late to playout with CODEC (Coder/Decoder) during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorylostpackets
            
            	The number of lost voice packets during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorylowaterplayoutdelay
            
            	The low water mark Voice Playout FIFO Delay during the voice call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorymaxptime
            
            	The object indicates the maximum amount of media that can be encapsulated in a payload. Supported value is 20 msec. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 20..100
            
            .. attribute:: cvvoipcallhistorymodechgneighbor
            
            	If the object has a value of true(1), mode changes will be made to only neighboring modes set to cvVoIPCallHistoryBitRates object. If the value is false(2), mode changes will be allowed to any modes set to cvVoIPCallHistoryBitRates object. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallhistorymodechgperiod
            
            	The object indicates the interval (N frame\-blocks) at which codec mode changes are allowed. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cvvoipcallhistoryoctetaligned
            
            	If the object has a value true(1) octet align operation is used, and if the value is false(2), bandwidth efficient operation is used. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallhistoryontimervplayout
            
            	Duration of voice playout from data received on time for this call. This plus the durations for the GapFills in the following entries gives the Total Voice Playout Duration for Active Voice. This does not include duration for which no data was sent by the Transmit end as voice signal, e.g., silence suppression and fax signal. The On Time Playout Rate can be computed by dividing this entry by the Total Voice Playout Duration. This counter object will lock at the maximum value which is approximately two days
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryprotocolcallid
            
            	The protocol\-specific call identifier for the VoIP call
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvvoipcallhistoryptime
            
            	The object indicates the length of the time in milliseconds represented by the media of the packet. Supported value is 20 milliseconds. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: int
            
            	**range:** 20..100
            
            .. attribute:: cvvoipcallhistoryreceivedelay
            
            	The average Playout FIFO Delay plus the decoder delay during the voice call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryremmediaipaddr
            
            	Remote media end point IP address for the VoIP call
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvvoipcallhistoryremmediaipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallHistoryRemMediaIPAddr
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cvvoipcallhistoryremmediaport
            
            	Remote media end point listener port to which to transmit voice packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallhistoryremoteipaddress
            
            	Remote system IP address for the call
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cvvoipcallhistoryremoteudpport
            
            	Remote system UDP listener port to which to transmit voice packets for the call
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallhistoryremsigipaddr
            
            	Remote signalling IP address for the VoIP call
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvvoipcallhistoryremsigipaddrt
            
            	This object specifies the type of address contained in the associated instance of cvVoIPCallHistoryRemSigIPAddr
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cvvoipcallhistoryremsigport
            
            	Remote signalling listener port to which to transmit voice packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvvoipcallhistoryrobustsorting
            
            	If the object has a value of true(1), payload employs robust sorting and if the value is false(2), payload does not employ robust sorting. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoipcallhistoryroundtripdelay
            
            	The voice packet round trip delay between local and the remote system on the IP backbone during the call
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistoryselectedqos
            
            	The selected RSVP QoS for the call
            	**type**\: :py:class:`QosService_Enum <ydk.models.int.INT_SERV_MIB.QosService_Enum>`
            
            .. attribute:: cvvoipcallhistorysessionid
            
            	This object indicates the session ID assigned by the call manager to identify call legs that belong to the same call session.  This session ID (history) represents a completed call session, whereas the active session ID (cvVoIPCallActiveSessionId) represents an ongoing session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvvoipcallhistorysessionprotocol
            
            	The object specifies the session protocol to be used for Internet call between local and remote router via IP backbone
            	**type**\: :py:class:`CvSessionProtocol_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvSessionProtocol_Enum>`
            
            .. attribute:: cvvoipcallhistorysessiontarget
            
            	The object specifies the session target of the peer that is used for the Voice over IP call
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cvvoipcallhistorysrtpenable
            
            	The object indicates whether or not the SRTP (Secured RTP) was enabled for the voice call
            	**type**\: bool
            
            .. attribute:: cvvoipcallhistoryusername
            
            	The textual identifier of the calling party (user) of the call. If the username is not available, then the value of this object will have a length of zero
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: cvvoipcallhistoryvadenable
            
            	The object indicates whether or not the VAD (Voice Activity Detection) was enabled for the voice call
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.ccallhistoryindex = None
                self.cvvoipcallhistorybitrates = CvAmrNbBitRateMode_Bits()
                self.cvvoipcallhistorycallid = None
                self.cvvoipcallhistorycallreferenceid = None
                self.cvvoipcallhistorychannels = None
                self.cvvoipcallhistorycodermode = None
                self.cvvoipcallhistorycodertyperate = None
                self.cvvoipcallhistoryconnectionid = None
                self.cvvoipcallhistorycrc = None
                self.cvvoipcallhistoryearlypackets = None
                self.cvvoipcallhistoryencap = None
                self.cvvoipcallhistoryfallbackdelay = None
                self.cvvoipcallhistoryfallbackicpif = None
                self.cvvoipcallhistoryfallbackloss = None
                self.cvvoipcallhistorygapfillwithinterpolation = None
                self.cvvoipcallhistorygapfillwithprediction = None
                self.cvvoipcallhistorygapfillwithredundancy = None
                self.cvvoipcallhistorygapfillwithsilence = None
                self.cvvoipcallhistoryhiwaterplayoutdelay = None
                self.cvvoipcallhistoryicpif = None
                self.cvvoipcallhistoryinterleaving = None
                self.cvvoipcallhistorylatepackets = None
                self.cvvoipcallhistorylostpackets = None
                self.cvvoipcallhistorylowaterplayoutdelay = None
                self.cvvoipcallhistorymaxptime = None
                self.cvvoipcallhistorymodechgneighbor = None
                self.cvvoipcallhistorymodechgperiod = None
                self.cvvoipcallhistoryoctetaligned = None
                self.cvvoipcallhistoryontimervplayout = None
                self.cvvoipcallhistoryprotocolcallid = None
                self.cvvoipcallhistoryptime = None
                self.cvvoipcallhistoryreceivedelay = None
                self.cvvoipcallhistoryremmediaipaddr = None
                self.cvvoipcallhistoryremmediaipaddrt = None
                self.cvvoipcallhistoryremmediaport = None
                self.cvvoipcallhistoryremoteipaddress = None
                self.cvvoipcallhistoryremoteudpport = None
                self.cvvoipcallhistoryremsigipaddr = None
                self.cvvoipcallhistoryremsigipaddrt = None
                self.cvvoipcallhistoryremsigport = None
                self.cvvoipcallhistoryrobustsorting = None
                self.cvvoipcallhistoryroundtripdelay = None
                self.cvvoipcallhistoryselectedqos = None
                self.cvvoipcallhistorysessionid = None
                self.cvvoipcallhistorysessionprotocol = None
                self.cvvoipcallhistorysessiontarget = None
                self.cvvoipcallhistorysrtpenable = None
                self.cvvoipcallhistoryusername = None
                self.cvvoipcallhistoryvadenable = None

            @property
            def _common_path(self):
                if self.ccallhistoryindex is None:
                    raise YPYDataValidationError('Key property ccallhistoryindex is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoIPCallHistoryTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoIPCallHistoryEntry[CISCO-VOICE-DIAL-CONTROL-MIB:cCallHistoryIndex = ' + str(self.ccallhistoryindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ccallhistoryindex is not None:
                    return True

                if self.cvvoipcallhistorybitrates is not None:
                    if self.cvvoipcallhistorybitrates._has_data():
                        return True

                if self.cvvoipcallhistorycallid is not None:
                    return True

                if self.cvvoipcallhistorycallreferenceid is not None:
                    return True

                if self.cvvoipcallhistorychannels is not None:
                    return True

                if self.cvvoipcallhistorycodermode is not None:
                    return True

                if self.cvvoipcallhistorycodertyperate is not None:
                    return True

                if self.cvvoipcallhistoryconnectionid is not None:
                    return True

                if self.cvvoipcallhistorycrc is not None:
                    return True

                if self.cvvoipcallhistoryearlypackets is not None:
                    return True

                if self.cvvoipcallhistoryencap is not None:
                    return True

                if self.cvvoipcallhistoryfallbackdelay is not None:
                    return True

                if self.cvvoipcallhistoryfallbackicpif is not None:
                    return True

                if self.cvvoipcallhistoryfallbackloss is not None:
                    return True

                if self.cvvoipcallhistorygapfillwithinterpolation is not None:
                    return True

                if self.cvvoipcallhistorygapfillwithprediction is not None:
                    return True

                if self.cvvoipcallhistorygapfillwithredundancy is not None:
                    return True

                if self.cvvoipcallhistorygapfillwithsilence is not None:
                    return True

                if self.cvvoipcallhistoryhiwaterplayoutdelay is not None:
                    return True

                if self.cvvoipcallhistoryicpif is not None:
                    return True

                if self.cvvoipcallhistoryinterleaving is not None:
                    return True

                if self.cvvoipcallhistorylatepackets is not None:
                    return True

                if self.cvvoipcallhistorylostpackets is not None:
                    return True

                if self.cvvoipcallhistorylowaterplayoutdelay is not None:
                    return True

                if self.cvvoipcallhistorymaxptime is not None:
                    return True

                if self.cvvoipcallhistorymodechgneighbor is not None:
                    return True

                if self.cvvoipcallhistorymodechgperiod is not None:
                    return True

                if self.cvvoipcallhistoryoctetaligned is not None:
                    return True

                if self.cvvoipcallhistoryontimervplayout is not None:
                    return True

                if self.cvvoipcallhistoryprotocolcallid is not None:
                    return True

                if self.cvvoipcallhistoryptime is not None:
                    return True

                if self.cvvoipcallhistoryreceivedelay is not None:
                    return True

                if self.cvvoipcallhistoryremmediaipaddr is not None:
                    return True

                if self.cvvoipcallhistoryremmediaipaddrt is not None:
                    return True

                if self.cvvoipcallhistoryremmediaport is not None:
                    return True

                if self.cvvoipcallhistoryremoteipaddress is not None:
                    return True

                if self.cvvoipcallhistoryremoteudpport is not None:
                    return True

                if self.cvvoipcallhistoryremsigipaddr is not None:
                    return True

                if self.cvvoipcallhistoryremsigipaddrt is not None:
                    return True

                if self.cvvoipcallhistoryremsigport is not None:
                    return True

                if self.cvvoipcallhistoryrobustsorting is not None:
                    return True

                if self.cvvoipcallhistoryroundtripdelay is not None:
                    return True

                if self.cvvoipcallhistoryselectedqos is not None:
                    return True

                if self.cvvoipcallhistorysessionid is not None:
                    return True

                if self.cvvoipcallhistorysessionprotocol is not None:
                    return True

                if self.cvvoipcallhistorysessiontarget is not None:
                    return True

                if self.cvvoipcallhistorysrtpenable is not None:
                    return True

                if self.cvvoipcallhistoryusername is not None:
                    return True

                if self.cvvoipcallhistoryvadenable is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoIPCallHistoryTable.CvVoIPCallHistoryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoIPCallHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvvoipcallhistoryentry is not None:
                for child_ref in self.cvvoipcallhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoIPCallHistoryTable']['meta_info']


    class CvVoIPPeerCfgTable(object):
        """
        The table contains the Voice over IP (VoIP) peer specific
        information that is required to accept voice calls or to
        which it will place them via IP backbone with the
        specified session protocol in cvVoIPPeerCfgSessionProtocol.
        
        .. attribute:: cvvoippeercfgentry
        
        	A single VoIP specific Peer. One entry per VoIP encapsulation. The entry is created when its associated 'voiceOverIp(104)' encapsulation ifEntry is created. This entry is deleted when its associated ifEntry is deleted
        	**type**\: list of :py:class:`CvVoIPPeerCfgEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable.CvVoIPPeerCfgEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvvoippeercfgentry = YList()
            self.cvvoippeercfgentry.parent = self
            self.cvvoippeercfgentry.name = 'cvvoippeercfgentry'


        class CvVoIPPeerCfgEntry(object):
            """
            A single VoIP specific Peer. One entry per VoIP
            encapsulation.
            The entry is created when its associated 'voiceOverIp(104)'
            encapsulation ifEntry is created.
            This entry is deleted when its associated ifEntry is
            deleted.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cvvoippeercfgbitrate
            
            	This object specifies the target bit rate. The object is instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'
            	**type**\: int
            
            	**range:** 10000..32000
            
            .. attribute:: cvvoippeercfgbitrates
            
            	This object indicates modes of Bit rates. One or more upto four modes can be configured at the same time as bit rates can be changed dynamically for AMR\-NB codec. This object is not instantiated when the object cvVoIPPeerCfgCoderRate is not equal to gsmAmrNb enum
            	**type**\: :py:class:`CvAmrNbBitRateMode_Bits <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvAmrNbBitRateMode_Bits>`
            
            .. attribute:: cvvoippeercfgcoderbytes
            
            	This object specifies the size of the voice payload sample to be produced by the coder specified in cvVoIPPeerCfgCoderRate. Each coder sample produces 10 bytes of voice payload. The specified value will be rounded down to the nearest valid size.  A value of 0, specifies that the coder defined by cvVoIPPeerCfgCoderRate should produce its default payload size
            	**type**\: int
            
            	**range:** 0 \| 10..240
            
            .. attribute:: cvvoippeercfgcodermode
            
            	This object indicates the iLBC codec mode to be used. The value of this object is valid only if  cvVoIPPeerCfgCoderRate is equal to 'iLBC'
            	**type**\: :py:class:`CvIlbcFrameMode_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvIlbcFrameMode_Enum>`
            
            .. attribute:: cvvoippeercfgcoderrate
            
            	This object specifies the most desirable codec of speech for the VoIP peer
            	**type**\: :py:class:`CvcSpeechCoderRate_Enum <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcSpeechCoderRate_Enum>`
            
            .. attribute:: cvvoippeercfgcodingmode
            
            	This object specifies the coding mode to be used. The object is instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'. Following coding modes are supported\: adaptive    (1) \- adaptive mode where iSAC performs bandwidth                     estimation and adapts to the available channel                    bandwidth. independent (2) \- independent mode in which no bandwidth estimation                    is performed
            	**type**\: :py:class:`CvVoIPPeerCfgCodingMode_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable.CvVoIPPeerCfgEntry.CvVoIPPeerCfgCodingMode_Enum>`
            
            .. attribute:: cvvoippeercfgcrc
            
            	If the object has a value of true(1), frame CRC will be included in the payload and if the value is false(2), frame CRC will not be included in the payload. This object is applicable only when RTP frame type is octet aligned. This object is not instantiated when the object cvVoIPPeerCfgCoderRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgdesiredqos
            
            	The object specifies the user requested Quality of Service for the call
            	**type**\: :py:class:`QosService_Enum <ydk.models.int.INT_SERV_MIB.QosService_Enum>`
            
            .. attribute:: cvvoippeercfgdesiredqosvideo
            
            	The object specifies the user requested Quality of Service for the video portion of the call
            	**type**\: :py:class:`QosService_Enum <ydk.models.int.INT_SERV_MIB.QosService_Enum>`
            
            .. attribute:: cvvoippeercfgdigitrelay
            
            	This object specifies the methods to transmit dial digits (DTMF or MF digits) via IP network. rtpCisco       \- Enable capability to transmit dial digits                  with Cisco proprietary RTP payload type. h245Signal     \- Enable capability to transmit dtmf digits                  across the H.245 channel, via the signal                  field of the UserInputIndication message h245Alphanumeric \- Enable capability to transmit dtmf                  digit across the H.245 channel, via the                  string or alphanumeric fields of the                  UserInputIndication message rtpNte         \- Enable capability to transmit dial digits                  using Named Telephony Event per RFC 2833                  section 3. sipNotify      \- Enable capability to transmit dtmf                  digits using unsolicited SIP NOTIFY                  messages. This mechanism is only available                  for SIP dialpeers. sipKpml        \- Enable capability to transmit dtmf                  digits using KPML over SIP SUBSCRIBE                  and NOTIFY messages. This mechanism is                  only available for SIP dialpeers.   Modifying the value of cvVoIPPeerCfgSessionProtocol can reset the digit\-relay method associated bits value in this object if the modified session protocol does not support  these digit\-relay methods
            	**type**\: :py:class:`CvVoIPPeerCfgDigitRelay_Bits <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable.CvVoIPPeerCfgEntry.CvVoIPPeerCfgDigitRelay_Bits>`
            
            .. attribute:: cvvoippeercfgdscppolicynotificationenable
            
            	This object specifies whether cvdcPolicyViolationNotification traps should be generated for the call that is associated with this peer for RPH to DSCP mapping and policing feature
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgexpectfactor
            
            	This object specifies the user requested Expectation Factor of voice quality for the call via this peer
            	**type**\: int
            
            	**range:** 0..20
            
            .. attribute:: cvvoippeercfgfaxbytes
            
            	This object specifies the payload size to be produced by the coder when it is generating fax data. A value of 0, specifies that the coder specified in cvVoIPCfgPeerCoderRate should produce its default fax payload size
            	**type**\: int
            
            	**range:** 0 \| 10..255
            
            .. attribute:: cvvoippeercfgfaxrate
            
            	This object specifies the default transmit rate of FAX the VoIP peer. If the value of this object is 'none', then the Fax relay feature is disabled; otherwise the Fax relay feature is enabled
            	**type**\: :py:class:`CvcFaxTransmitRate_Enum <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcFaxTransmitRate_Enum>`
            
            .. attribute:: cvvoippeercfgframesize
            
            	This object specifies the frame size used. The object is instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'. The frame size can be 30 ms or 60 ms, and it can be fixed for all packets or vary depending on the configuration and bandwidth estimation. Thus it can have the following values\: frameSize30      \- initial frame size of 30 ms frameSize60      \- initial frame size of 60 ms frameSize30fixed \- fixed frame size 30 ms frameSize60fixed \- fixed frame size 60 ms
            	**type**\: :py:class:`CvVoIPPeerCfgFrameSize_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable.CvVoIPPeerCfgEntry.CvVoIPPeerCfgFrameSize_Enum>`
            
            .. attribute:: cvvoippeercfgicpif
            
            	This object specifies the user requested Calculated Planning Impairment Factor (Icpif) for the call via this peer
            	**type**\: int
            
            	**range:** 0..55
            
            .. attribute:: cvvoippeercfginbandsignaling
            
            	This object specifies the type of in\-band signaling that will be used between the end points of the call. It is used by the router to determine how to interpret ABCD signaling bits sent as part of voice payload data
            	**type**\: :py:class:`CvcInBandSignaling_Enum <ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB.CvcInBandSignaling_Enum>`
            
            .. attribute:: cvvoippeercfgipprecedence
            
            	This object specifies the value to be stored in the IP Precedence field of voice packets, with values ranging from 0 (normal precedence) through 7 (network control), allowing the managed system to set the importance of each voice packet for delivering them to the destination peer
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: cvvoippeercfgmediapolicynotificationenable
            
            	This object specifies whether cvdcPolicyViolationNotification traps should be generated for the call that is associated with this peer for Media policing feature.
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgmediasetting
            
            	This object specifies how the media is to be setup on an IP\-IP Gateway. Two choices are valid\: flow\-through and flow\-around. When in flow\-through mode, which is the default setting, the IP\-IP Gateway will terminate and  then re\-originate the media stream. When flow\-around is configured the Gateway will not be involved with the media, since it will flow\-around the Gateway and will be established directly between the endpoints
            	**type**\: :py:class:`CvVoIPPeerCfgMediaSetting_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable.CvVoIPPeerCfgEntry.CvVoIPPeerCfgMediaSetting_Enum>`
            
            .. attribute:: cvvoippeercfgminacceptableqos
            
            	The object specifies the minimally acceptable Quality of Service for the call
            	**type**\: :py:class:`QosService_Enum <ydk.models.int.INT_SERV_MIB.QosService_Enum>`
            
            .. attribute:: cvvoippeercfgminacceptableqosvideo
            
            	The object specifies the minimally acceptable Quality of Service for the video portion of the call
            	**type**\: :py:class:`QosService_Enum <ydk.models.int.INT_SERV_MIB.QosService_Enum>`
            
            .. attribute:: cvvoippeercfgoctetaligned
            
            	If the object has a value true(1) octet align operation is used, and if the value is false(2), bandwidth efficient operation is used. This object is not instantiated when the object cvVoIPPeerCfgCoderRate is not equal to gsmAmrNb enum
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgpoorqovnotificationenable
            
            	This object specifies whether cvdcPoorQoVNotification (or the newer cvdcPoorQoVNotificationRev1) traps should be generated for the call that is associated with this peer
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgredirectip2ip
            
            	This object specifies the Inbound VoIP calls that match an outbound VoIP dialpeer will be responded with a SIP  redirect(for inbound SIP) or H.450.3 call\-forward(for  inbound H.323)
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgsessionprotocol
            
            	The object specifies the session protocol to be used for Internet call between local and remote router via IP backbone
            	**type**\: :py:class:`CvSessionProtocol_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CvSessionProtocol_Enum>`
            
            .. attribute:: cvvoippeercfgsessiontarget
            
            	The object specifies the session target of the peer. Session Targets definitions\: The session target has the syntax used by the IETF service location protocol. The syntax is as follows\:  mapping\-type\:type\-specific\-syntax  the mapping\-type specifies a scheme for mapping the matching dial string to a session target. The type\-specific\-syntax is exactly that, something that the particular mapping scheme can understand. For example, Session target           Meaning ipv4\:171.68.13.55\:1006   The session target is the IP                          version 4 address of 171.68.13.55                          and port 1006. dns\:pots.cisco.com\:1661  The session target is the IP host                          with dns name pots.cisco.com, and                          port 1661. ras                      The session target is the                          gatekeeper with RAS (Registration                          , Admission,  Status protocol). settlement               The session target is the                          settlement server. enum\:1                   The session target is the enum                           profile match table 1.  The valid Mapping type definitions for the peer are as follows\: ipv4       \- Syntax\: ipv4\:w.x.y.z\:port or  ipv4\:w.x.y.z dns        \- Syntax\: dns\:host.domain\:port or                      dns\:host.domain ras        \- Syntax\: ras settlement \- Syntax\: settlement enum       \- Syntax\: enum\:  loopback \- Syntax\: loopback\:where    'where' string is defined as follows\:    rtp \- loopback is performed at the transport protocol          level.  Local loopback case\: rtp \- the session application sets up an RTP stream to     itself (i.e. actually allocates a port pair and opens     the appropriate UDP sockets). It then does the full     RTP encapsulation, sends the packets to the loopback     IP address, receives the RTP packets, and hands the     compressed voice back to the CODEC. This tests the     entire local processing path, both transmit and     receive, in the router, as well as all of the above     paths.  Remote loopback case\: rtp\: RTP packets received from the network are decapsulated and      immediately re\-encapsulated in the outbound RTP      stream, using the same media clock (i.e. timestamp)      as the received packet. They are then sent back to      the remote source router as if the voice had      originated on a telephony port on the local router
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cvvoippeercfgtechprefix
            
            	This object specifies the technology prefix of the peer, The technology prefix and the called party address are passed in Admission Request (ARQ) to gatekeeper for the called party address resolution during call setup
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: cvvoippeercfgudpchecksumenable
            
            	This object specifies whether the outgoing voice related UDP packet contains a valid checksum value. true  \- enable the checksum of outgoing voice UDP packets false \- disable the checksum of outgoing voice UDP packets
            	**type**\: bool
            
            .. attribute:: cvvoippeercfgvadenable
            
            	This object specifies whether or not the VAD (Voice Activity Detection) voice data is continuously transmitted to IP backbone
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cvvoippeercfgbitrate = None
                self.cvvoippeercfgbitrates = CvAmrNbBitRateMode_Bits()
                self.cvvoippeercfgcoderbytes = None
                self.cvvoippeercfgcodermode = None
                self.cvvoippeercfgcoderrate = None
                self.cvvoippeercfgcodingmode = None
                self.cvvoippeercfgcrc = None
                self.cvvoippeercfgdesiredqos = None
                self.cvvoippeercfgdesiredqosvideo = None
                self.cvvoippeercfgdigitrelay = CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable.CvVoIPPeerCfgEntry.CvVoIPPeerCfgDigitRelay_Bits()
                self.cvvoippeercfgdscppolicynotificationenable = None
                self.cvvoippeercfgexpectfactor = None
                self.cvvoippeercfgfaxbytes = None
                self.cvvoippeercfgfaxrate = None
                self.cvvoippeercfgframesize = None
                self.cvvoippeercfgicpif = None
                self.cvvoippeercfginbandsignaling = None
                self.cvvoippeercfgipprecedence = None
                self.cvvoippeercfgmediapolicynotificationenable = None
                self.cvvoippeercfgmediasetting = None
                self.cvvoippeercfgminacceptableqos = None
                self.cvvoippeercfgminacceptableqosvideo = None
                self.cvvoippeercfgoctetaligned = None
                self.cvvoippeercfgpoorqovnotificationenable = None
                self.cvvoippeercfgredirectip2ip = None
                self.cvvoippeercfgsessionprotocol = None
                self.cvvoippeercfgsessiontarget = None
                self.cvvoippeercfgtechprefix = None
                self.cvvoippeercfgudpchecksumenable = None
                self.cvvoippeercfgvadenable = None

            class CvVoIPPeerCfgCodingMode_Enum(Enum):
                """
                CvVoIPPeerCfgCodingMode_Enum

                This object specifies the coding mode to be used. The object is
                instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'. Following
                coding modes are supported\:
                adaptive    (1) \- adaptive mode where iSAC performs bandwidth  
                                  estimation and adapts to the available channel
                
                                  bandwidth.
                independent (2) \- independent mode in which no bandwidth
                estimation 
                                  is performed.

                """

                ADAPTIVE = 1

                INDEPENDENT = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                    return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable.CvVoIPPeerCfgEntry.CvVoIPPeerCfgCodingMode_Enum']


            class CvVoIPPeerCfgFrameSize_Enum(Enum):
                """
                CvVoIPPeerCfgFrameSize_Enum

                This object specifies the frame size used. The object is
                instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'.
                The frame size can be 30 ms or 60 ms, and it can be fixed for
                all packets or vary depending on the configuration and bandwidth
                estimation. Thus it can have the following values\:
                frameSize30      \- initial frame size of 30 ms
                frameSize60      \- initial frame size of 60 ms
                frameSize30fixed \- fixed frame size 30 ms
                frameSize60fixed \- fixed frame size 60 ms

                """

                FRAMESIZE30 = 1

                FRAMESIZE60 = 2

                FRAMESIZE30FIXED = 3

                FRAMESIZE60FIXED = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                    return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable.CvVoIPPeerCfgEntry.CvVoIPPeerCfgFrameSize_Enum']


            class CvVoIPPeerCfgMediaSetting_Enum(Enum):
                """
                CvVoIPPeerCfgMediaSetting_Enum

                This object specifies how the media is to be setup on
                an IP\-IP Gateway. Two choices are valid\: flow\-through
                and flow\-around. When in flow\-through mode, which is the
                default setting, the IP\-IP Gateway will terminate and 
                then re\-originate the media stream. When flow\-around
                is configured the Gateway will not be involved with the
                media, since it will flow\-around the Gateway and will
                be established directly between the endpoints.

                """

                FLOWTHROUGH = 1

                FLOWAROUND = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                    return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable.CvVoIPPeerCfgEntry.CvVoIPPeerCfgMediaSetting_Enum']


            class CvVoIPPeerCfgDigitRelay_Bits(FixedBitsDict):
                """
                CvVoIPPeerCfgDigitRelay_Bits

                This object specifies the methods to transmit dial digits
                (DTMF or MF digits) via IP network.
                rtpCisco       \- Enable capability to transmit dial digits
                                 with Cisco proprietary RTP payload type.
                h245Signal     \- Enable capability to transmit dtmf digits
                                 across the H.245 channel, via the signal
                                 field of the UserInputIndication message
                h245Alphanumeric \- Enable capability to transmit dtmf
                                 digit across the H.245 channel, via the
                                 string or alphanumeric fields of the
                                 UserInputIndication message
                rtpNte         \- Enable capability to transmit dial digits
                                 using Named Telephony Event per RFC 2833
                                 section 3.
                sipNotify      \- Enable capability to transmit dtmf
                                 digits using unsolicited SIP NOTIFY
                                 messages. This mechanism is only available
                                 for SIP dialpeers.
                sipKpml        \- Enable capability to transmit dtmf
                                 digits using KPML over SIP SUBSCRIBE
                                 and NOTIFY messages. This mechanism is
                                 only available for SIP dialpeers.
                
                
                Modifying the value of cvVoIPPeerCfgSessionProtocol
                can reset the digit\-relay method associated bits value in
                this object if the modified session protocol does not
                support  these digit\-relay methods.
                Keys are:- h245Signal , rtpCisco , h245Alphanumeric , sipKpml , rtpNte , sipNotify

                """

                def __init__(self):
                    self._dictionary = { 
                        'h245Signal':False,
                        'rtpCisco':False,
                        'h245Alphanumeric':False,
                        'sipKpml':False,
                        'rtpNte':False,
                        'sipNotify':False,
                    }
                    self._pos_map = { 
                        'h245Signal':1,
                        'rtpCisco':0,
                        'h245Alphanumeric':2,
                        'sipKpml':5,
                        'rtpNte':3,
                        'sipNotify':4,
                    }

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoIPPeerCfgTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoIPPeerCfgEntry[CISCO-VOICE-DIAL-CONTROL-MIB:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.cvvoippeercfgbitrate is not None:
                    return True

                if self.cvvoippeercfgbitrates is not None:
                    if self.cvvoippeercfgbitrates._has_data():
                        return True

                if self.cvvoippeercfgcoderbytes is not None:
                    return True

                if self.cvvoippeercfgcodermode is not None:
                    return True

                if self.cvvoippeercfgcoderrate is not None:
                    return True

                if self.cvvoippeercfgcodingmode is not None:
                    return True

                if self.cvvoippeercfgcrc is not None:
                    return True

                if self.cvvoippeercfgdesiredqos is not None:
                    return True

                if self.cvvoippeercfgdesiredqosvideo is not None:
                    return True

                if self.cvvoippeercfgdigitrelay is not None:
                    if self.cvvoippeercfgdigitrelay._has_data():
                        return True

                if self.cvvoippeercfgdscppolicynotificationenable is not None:
                    return True

                if self.cvvoippeercfgexpectfactor is not None:
                    return True

                if self.cvvoippeercfgfaxbytes is not None:
                    return True

                if self.cvvoippeercfgfaxrate is not None:
                    return True

                if self.cvvoippeercfgframesize is not None:
                    return True

                if self.cvvoippeercfgicpif is not None:
                    return True

                if self.cvvoippeercfginbandsignaling is not None:
                    return True

                if self.cvvoippeercfgipprecedence is not None:
                    return True

                if self.cvvoippeercfgmediapolicynotificationenable is not None:
                    return True

                if self.cvvoippeercfgmediasetting is not None:
                    return True

                if self.cvvoippeercfgminacceptableqos is not None:
                    return True

                if self.cvvoippeercfgminacceptableqosvideo is not None:
                    return True

                if self.cvvoippeercfgoctetaligned is not None:
                    return True

                if self.cvvoippeercfgpoorqovnotificationenable is not None:
                    return True

                if self.cvvoippeercfgredirectip2ip is not None:
                    return True

                if self.cvvoippeercfgsessionprotocol is not None:
                    return True

                if self.cvvoippeercfgsessiontarget is not None:
                    return True

                if self.cvvoippeercfgtechprefix is not None:
                    return True

                if self.cvvoippeercfgudpchecksumenable is not None:
                    return True

                if self.cvvoippeercfgvadenable is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable.CvVoIPPeerCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoIPPeerCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvvoippeercfgentry is not None:
                for child_ref in self.cvvoippeercfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoIPPeerCfgTable']['meta_info']


    class CvVoicePeerCfgTable(object):
        """
        The table contains the Voice over Telephony peer specific
        information that is required to accept voice calls or to
        which it will place them or perform various loopback tests
        via interface.
        
        .. attribute:: cvvoicepeercfgentry
        
        	A single Voice specific Peer. One entry per voice encapsulation. The entry is created when its associated 'voiceEncap(103)' encapsulation ifEntry is created. This entry is deleted when its associated ifEntry is deleted
        	**type**\: list of :py:class:`CvVoicePeerCfgEntry <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoicePeerCfgTable.CvVoicePeerCfgEntry>`
        
        

        """

        _prefix = 'cisco-voice-dial'
        _revision = '2012-05-15'

        def __init__(self):
            self.parent = None
            self.cvvoicepeercfgentry = YList()
            self.cvvoicepeercfgentry.parent = self
            self.cvvoicepeercfgentry.name = 'cvvoicepeercfgentry'


        class CvVoicePeerCfgEntry(object):
            """
            A single Voice specific Peer. One entry per voice
            encapsulation.
            The entry is created when its associated 'voiceEncap(103)'
            encapsulation ifEntry is created.
            This entry is deleted when its associated ifEntry is
            deleted.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cvvoicepeercfgcasgroup
            
            	The object specifies the CAS group number of a CAS capable T1/E1  that is in the dialCtlPeerCfgLowerIf object of RFC2128. This object can be set to a valid CAS group number only if the dialCtlPeerCfgLowerIf contains a valid ifIndex for a CAS capable T1/E1. The object must set to \-1 before the value of the  dialCtlPeerCfgLowerIf object of RFC2128 can be changed
            	**type**\: int
            
            	**range:** \-1..30
            
            .. attribute:: cvvoicepeercfgdialdigitsprefix
            
            	The object specifies the prefix of the dial digits for the peer. The dial digits prefix is sent to telephony interface before the real phone number when the system places the outgoing call to the voice encapsulation peer over telephony interface
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: cvvoicepeercfgdidcallenable
            
            	The object enables/disables the DID call treatment for incoming DNIS digits. true  \- treat the incoming DNIS digits as if the digits         are received from DID trunk. false \- Disable DID call treatment for incoming DNIS         digits
            	**type**\: bool
            
            .. attribute:: cvvoicepeercfgechocancellertest
            
            	This object specifies which, if any, test to run in the echo canceller when a call from the network is connected. echoCancellerTestNone    \- do not run a test. echoCancellerG168Test2A  \- run ITU\-T G.168 Test 2A. echoCancellerG168Test2B  \- run ITU\-T G.168 Test 2B. echoCancellerG168Test2Ca \- run ITU\-T G.168 Test 2C(a). echoCancellerG168Test2Cb \- run ITU\-T G.168 Test 2C(b). echoCancellerG168Test3A  \- run ITU\-T G.168 Test 3A. echoCancellerG168Test3B  \- run ITU\-T G.168 Test 3B. echoCancellerG168Test3C  \- run ITU\-T G.168 Test 3C. echoCancellerG168Test4   \- run ITU\-T G.168 Test 4. echoCancellerG168Test5   \- run ITU\-T G.168 Test 5. echoCancellerG168Test6   \- run ITU\-T G.168 Test 6. echoCancellerG168Test7   \- run ITU\-T G.168 Test 7. echoCancellerG168Test9   \- run ITU\-T G.168 Test 9
            	**type**\: :py:class:`CvVoicePeerCfgEchoCancellerTest_Enum <ydk.models.voice.CISCO_VOICE_DIAL_CONTROL_MIB.CISCOVOICEDIALCONTROLMIB.CvVoicePeerCfgTable.CvVoicePeerCfgEntry.CvVoicePeerCfgEchoCancellerTest_Enum>`
            
            .. attribute:: cvvoicepeercfgforwarddigits
            
            	This object specifies the number of dialed digits to forward to the remote destination in the setup message. The object can take the value\:     0\-32 number of right justified digits to forward     \-1 default     \-2 forward extra digits i.e those over and above        those needed to match to the destination pattern     \-3 forward all digits
            	**type**\: int
            
            	**range:** \-3..32
            
            .. attribute:: cvvoicepeercfgregistere164
            
            	This object specifies that the E.164 number specified in the dialCtlPeerCfgOriginateAddress field of the associated dialCtlPeerCfgTable entry be registered as an extension  phone number of this gateway for H323 gatekeeper and/or  SIP registrar
            	**type**\: bool
            
            .. attribute:: cvvoicepeercfgsessiontarget
            
            	The object specifies the session target of the peer. Session Targets definitions\: The session target has the syntax used by the IETF service location protocol. The syntax is as follows\:  mapping\-type\:type\-specific\-syntax  the mapping\-type specifies a scheme for mapping the matching dial string to a session target.  The valid Mapping type definitions for the peer are as follows\: loopback \- Syntax\: loopback\:where    'where' string is defined as follows\:    compressed \- loopback is performed on compressed voice                 as close to the CODEC which processes the                 data as possible.    uncompressed \- loopback is performed on the PCM or                 analog voice as close to the telephony                 endpoint as possible.  Local loopback case\: uncompressed \- the PCM voice coming into the DSP is simply     turned around and sent back out, allowing testing of     the transmit\-\-> receive paths in the telephony     endpoint. compressed \- the compressed voice coming out of the CODEC is     turned around on the DSP module and fed back into the     decompressor through the jitter buffer. In addition to     the telephony endpoint, this tests both the encode and     decode paths without involving data paths or packet     handling on the host router.  Remote loopback case\: compressed \- RTP packets received from the network are     decapsulated and passed to the DSP board. Instead of     feeding these into the CODEC for decompression, they     are immediately sent back to the session application     as if they had originated locally and been compressed. uncompressed \- In addition to the above, the voice samples     are sent all the way through the CODEC and then turned     around instead of being sent to the telephony     endpoint
            	**type**\: str
            
            	**range:** 0..64
            
            

            """

            _prefix = 'cisco-voice-dial'
            _revision = '2012-05-15'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cvvoicepeercfgcasgroup = None
                self.cvvoicepeercfgdialdigitsprefix = None
                self.cvvoicepeercfgdidcallenable = None
                self.cvvoicepeercfgechocancellertest = None
                self.cvvoicepeercfgforwarddigits = None
                self.cvvoicepeercfgregistere164 = None
                self.cvvoicepeercfgsessiontarget = None

            class CvVoicePeerCfgEchoCancellerTest_Enum(Enum):
                """
                CvVoicePeerCfgEchoCancellerTest_Enum

                This object specifies which, if any, test to run in the
                echo canceller when a call from the network is connected.
                echoCancellerTestNone    \- do not run a test.
                echoCancellerG168Test2A  \- run ITU\-T G.168 Test 2A.
                echoCancellerG168Test2B  \- run ITU\-T G.168 Test 2B.
                echoCancellerG168Test2Ca \- run ITU\-T G.168 Test 2C(a).
                echoCancellerG168Test2Cb \- run ITU\-T G.168 Test 2C(b).
                echoCancellerG168Test3A  \- run ITU\-T G.168 Test 3A.
                echoCancellerG168Test3B  \- run ITU\-T G.168 Test 3B.
                echoCancellerG168Test3C  \- run ITU\-T G.168 Test 3C.
                echoCancellerG168Test4   \- run ITU\-T G.168 Test 4.
                echoCancellerG168Test5   \- run ITU\-T G.168 Test 5.
                echoCancellerG168Test6   \- run ITU\-T G.168 Test 6.
                echoCancellerG168Test7   \- run ITU\-T G.168 Test 7.
                echoCancellerG168Test9   \- run ITU\-T G.168 Test 9.

                """

                ECHOCANCELLERTESTNONE = 1

                ECHOCANCELLERG168TEST2A = 2

                ECHOCANCELLERG168TEST2B = 3

                ECHOCANCELLERG168TEST2CA = 4

                ECHOCANCELLERG168TEST2CB = 5

                ECHOCANCELLERG168TEST3A = 6

                ECHOCANCELLERG168TEST3B = 7

                ECHOCANCELLERG168TEST3C = 8

                ECHOCANCELLERG168TEST4 = 9

                ECHOCANCELLERG168TEST6 = 10

                ECHOCANCELLERG168TEST9 = 11

                ECHOCANCELLERG168TEST5 = 12

                ECHOCANCELLERG168TEST7 = 13


                @staticmethod
                def _meta_info():
                    from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                    return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoicePeerCfgTable.CvVoicePeerCfgEntry.CvVoicePeerCfgEchoCancellerTest_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoicePeerCfgTable/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoicePeerCfgEntry[CISCO-VOICE-DIAL-CONTROL-MIB:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.cvvoicepeercfgcasgroup is not None:
                    return True

                if self.cvvoicepeercfgdialdigitsprefix is not None:
                    return True

                if self.cvvoicepeercfgdidcallenable is not None:
                    return True

                if self.cvvoicepeercfgechocancellertest is not None:
                    return True

                if self.cvvoicepeercfgforwarddigits is not None:
                    return True

                if self.cvvoicepeercfgregistere164 is not None:
                    return True

                if self.cvvoicepeercfgsessiontarget is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
                return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoicePeerCfgTable.CvVoicePeerCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB/CISCO-VOICE-DIAL-CONTROL-MIB:cvVoicePeerCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvvoicepeercfgentry is not None:
                for child_ref in self.cvvoicepeercfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
            return meta._meta_table['CISCOVOICEDIALCONTROLMIB.CvVoicePeerCfgTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-VOICE-DIAL-CONTROL-MIB:CISCO-VOICE-DIAL-CONTROL-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cvactivecallstatstable is not None and self.cvactivecallstatstable._has_data():
            return True

        if self.cvactivecallstatstable is not None and self.cvactivecallstatstable.is_presence():
            return True

        if self.cvactivecallwmtable is not None and self.cvactivecallwmtable._has_data():
            return True

        if self.cvactivecallwmtable is not None and self.cvactivecallwmtable.is_presence():
            return True

        if self.cvcallactivetable is not None and self.cvcallactivetable._has_data():
            return True

        if self.cvcallactivetable is not None and self.cvcallactivetable.is_presence():
            return True

        if self.cvcalldurationstatstable is not None and self.cvcalldurationstatstable._has_data():
            return True

        if self.cvcalldurationstatstable is not None and self.cvcalldurationstatstable.is_presence():
            return True

        if self.cvcallhistorytable is not None and self.cvcallhistorytable._has_data():
            return True

        if self.cvcallhistorytable is not None and self.cvcallhistorytable.is_presence():
            return True

        if self.cvcalllegratestatstable is not None and self.cvcalllegratestatstable._has_data():
            return True

        if self.cvcalllegratestatstable is not None and self.cvcalllegratestatstable.is_presence():
            return True

        if self.cvcalllegratewmtable is not None and self.cvcalllegratewmtable._has_data():
            return True

        if self.cvcalllegratewmtable is not None and self.cvcalllegratewmtable.is_presence():
            return True

        if self.cvcallratemonitor is not None and self.cvcallratemonitor._has_data():
            return True

        if self.cvcallratemonitor is not None and self.cvcallratemonitor.is_presence():
            return True

        if self.cvcallratestatstable is not None and self.cvcallratestatstable._has_data():
            return True

        if self.cvcallratestatstable is not None and self.cvcallratestatstable.is_presence():
            return True

        if self.cvcallratewmtable is not None and self.cvcallratewmtable._has_data():
            return True

        if self.cvcallratewmtable is not None and self.cvcallratewmtable.is_presence():
            return True

        if self.cvcallvolconntable is not None and self.cvcallvolconntable._has_data():
            return True

        if self.cvcallvolconntable is not None and self.cvcallvolconntable.is_presence():
            return True

        if self.cvcallvoliftable is not None and self.cvcallvoliftable._has_data():
            return True

        if self.cvcallvoliftable is not None and self.cvcallvoliftable.is_presence():
            return True

        if self.cvcallvolume is not None and self.cvcallvolume._has_data():
            return True

        if self.cvcallvolume is not None and self.cvcallvolume.is_presence():
            return True

        if self.cvcallvolumestatshistory is not None and self.cvcallvolumestatshistory._has_data():
            return True

        if self.cvcallvolumestatshistory is not None and self.cvcallvolumestatshistory.is_presence():
            return True

        if self.cvgatewaycallactive is not None and self.cvgatewaycallactive._has_data():
            return True

        if self.cvgatewaycallactive is not None and self.cvgatewaycallactive.is_presence():
            return True

        if self.cvgeneralconfiguration is not None and self.cvgeneralconfiguration._has_data():
            return True

        if self.cvgeneralconfiguration is not None and self.cvgeneralconfiguration.is_presence():
            return True

        if self.cvpeercfgtable is not None and self.cvpeercfgtable._has_data():
            return True

        if self.cvpeercfgtable is not None and self.cvpeercfgtable.is_presence():
            return True

        if self.cvpeercommoncfgtable is not None and self.cvpeercommoncfgtable._has_data():
            return True

        if self.cvpeercommoncfgtable is not None and self.cvpeercommoncfgtable.is_presence():
            return True

        if self.cvsipmsgratestatstable is not None and self.cvsipmsgratestatstable._has_data():
            return True

        if self.cvsipmsgratestatstable is not None and self.cvsipmsgratestatstable.is_presence():
            return True

        if self.cvsipmsgratewmtable is not None and self.cvsipmsgratewmtable._has_data():
            return True

        if self.cvsipmsgratewmtable is not None and self.cvsipmsgratewmtable.is_presence():
            return True

        if self.cvvoicepeercfgtable is not None and self.cvvoicepeercfgtable._has_data():
            return True

        if self.cvvoicepeercfgtable is not None and self.cvvoicepeercfgtable.is_presence():
            return True

        if self.cvvoipcallactivetable is not None and self.cvvoipcallactivetable._has_data():
            return True

        if self.cvvoipcallactivetable is not None and self.cvvoipcallactivetable.is_presence():
            return True

        if self.cvvoipcallhistorytable is not None and self.cvvoipcallhistorytable._has_data():
            return True

        if self.cvvoipcallhistorytable is not None and self.cvvoipcallhistorytable.is_presence():
            return True

        if self.cvvoippeercfgtable is not None and self.cvvoippeercfgtable._has_data():
            return True

        if self.cvvoippeercfgtable is not None and self.cvvoippeercfgtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.voice._meta import _CISCO_VOICE_DIAL_CONTROL_MIB as meta
        return meta._meta_table['CISCOVOICEDIALCONTROLMIB']['meta_info']


