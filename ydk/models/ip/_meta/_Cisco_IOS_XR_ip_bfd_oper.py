


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'BfdApiFec_Enum' : _MetaInfoEnum('BfdApiFec_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-api-fec-type-none':'BFD_API_FEC_TYPE_NONE',
            'bfd-api-fec-type-p2p-te':'BFD_API_FEC_TYPE_P2P_TE',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdSession_Enum' : _MetaInfoEnum('BfdSession_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper',
        {
            'undefined':'UNDEFINED',
            'bundle-member':'BUNDLE_MEMBER',
            'bundle-interface':'BUNDLE_INTERFACE',
            'state-inheriting':'STATE_INHERITING',
            'bundle-vlan':'BUNDLE_VLAN',
            'mpls-tp':'MPLS_TP',
            'gre':'GRE',
            'pseudowire-headend':'PSEUDOWIRE_HEADEND',
            'ip-single-hop':'IP_SINGLE_HOP',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdAfId_Enum' : _MetaInfoEnum('BfdAfId_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-af-id-none':'BFD_AF_ID_NONE',
            'bfd-af-id-ipv4':'BFD_AF_ID_IPV4',
            'bfd-af-id-ipv6':'BFD_AF_ID_IPV6',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdMpDownloadState_Enum' : _MetaInfoEnum('BfdMpDownloadState_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-mp-download-none':'BFD_MP_DOWNLOAD_NONE',
            'bfd-mp-download-no-lc':'BFD_MP_DOWNLOAD_NO_LC',
            'bfd-mp-download-downloaded':'BFD_MP_DOWNLOAD_DOWNLOADED',
            'bfd-mp-download-ack':'BFD_MP_DOWNLOAD_ACK',
            'bfd-mp-download-nack':'BFD_MP_DOWNLOAD_NACK',
            'bfd-mp-download-delete':'BFD_MP_DOWNLOAD_DELETE',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdMgmtSessionState_Enum' : _MetaInfoEnum('BfdMgmtSessionState_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-mgmt-session-state-admin-down':'BFD_MGMT_SESSION_STATE_ADMIN_DOWN',
            'bfd-mgmt-session-state-down':'BFD_MGMT_SESSION_STATE_DOWN',
            'bfd-mgmt-session-state-init':'BFD_MGMT_SESSION_STATE_INIT',
            'bfd-mgmt-session-state-up':'BFD_MGMT_SESSION_STATE_UP',
            'bfd-mgmt-session-state-failing':'BFD_MGMT_SESSION_STATE_FAILING',
            'bfd-mgmt-session-state-unknown':'BFD_MGMT_SESSION_STATE_UNKNOWN',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdMgmtSessionDiag_Enum' : _MetaInfoEnum('BfdMgmtSessionDiag_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-mgmt-session-diag-none':'BFD_MGMT_SESSION_DIAG_NONE',
            'bfd-mgmt-session-diag-control-detect-expired':'BFD_MGMT_SESSION_DIAG_CONTROL_DETECT_EXPIRED',
            'bfd-mgmt-session-diag-echo-function-failed':'BFD_MGMT_SESSION_DIAG_ECHO_FUNCTION_FAILED',
            'bfd-mgmt-session-diag-nb-or-signaled-down':'BFD_MGMT_SESSION_DIAG_NB_OR_SIGNALED_DOWN',
            'bfd-mgmt-session-diag-fwding-plane-reset':'BFD_MGMT_SESSION_DIAG_FWDING_PLANE_RESET',
            'bfd-mgmt-session-diag-path-down':'BFD_MGMT_SESSION_DIAG_PATH_DOWN',
            'bfd-mgmt-session-diag-conc-path-down':'BFD_MGMT_SESSION_DIAG_CONC_PATH_DOWN',
            'bfd-mgmt-session-diag-admin-down':'BFD_MGMT_SESSION_DIAG_ADMIN_DOWN',
            'bfd-mgmt-session-diag-rev-conc-path-down':'BFD_MGMT_SESSION_DIAG_REV_CONC_PATH_DOWN',
            'bfd-mgmt-session-diag-num':'BFD_MGMT_SESSION_DIAG_NUM',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'BfdMgmtPktDisplay_Enum' : _MetaInfoEnum('BfdMgmtPktDisplay_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper',
        {
            'bfd-mgmt-pkt-display-type-none':'BFD_MGMT_PKT_DISPLAY_TYPE_NONE',
            'bfd-mgmt-pkt-display-type-bob-mbr':'BFD_MGMT_PKT_DISPLAY_TYPE_BOB_MBR',
            'bfd-mgmt-pkt-display-type-max':'BFD_MGMT_PKT_DISPLAY_TYPE_MAX',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'MplsLibC_Enum' : _MetaInfoEnum('MplsLibC_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper',
        {
            'mpls-lib-c-type-null':'MPLS_LIB_C_TYPE_NULL',
            'mpls-lib-c-type-ipv4':'MPLS_LIB_C_TYPE_IPV4',
            'mpls-lib-c-type-ipv4-p2p-tunnel':'MPLS_LIB_C_TYPE_IPV4_P2P_TUNNEL',
            'mpls-lib-c-type-ipv6-p2p-tunnel':'MPLS_LIB_C_TYPE_IPV6_P2P_TUNNEL',
            'mpls-lib-c-type-ipv4-uni':'MPLS_LIB_C_TYPE_IPV4_UNI',
            'mpls-lib-c-type-ipv4-p2mp-tunnel':'MPLS_LIB_C_TYPE_IPV4_P2MP_TUNNEL',
            'mpls-lib-c-type-ipv6-p2mp-tunnel':'MPLS_LIB_C_TYPE_IPV6_P2MP_TUNNEL',
            'mpls-lib-c-type-ipv4-tp-tunnel':'MPLS_LIB_C_TYPE_IPV4_TP_TUNNEL',
            'mpls-lib-c-type-ipv6-tp-tunnel':'MPLS_LIB_C_TYPE_IPV6_TP_TUNNEL',
            'mpls-lib-c-type-p2p-binding-label':'MPLS_LIB_C_TYPE_P2P_BINDING_LABEL',
        }, 'Cisco-IOS-XR-ip-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper']),
    'Bfd.ClientBriefs.ClientBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientBriefs.ClientBrief',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client Name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where client resides
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions created by this client
                ''',
                'session_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'client-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.ClientBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientBriefs',
            False, 
            [
            _MetaInfoClassMember('client-brief', REFERENCE_LIST, 'ClientBrief' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientBriefs.ClientBrief', 
                [], [], 
                '''                Brief information of client
                ''',
                'client_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'client-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.ClientDetails.ClientDetail.Brief' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientDetails.ClientDetail.Brief',
            False, 
            [
            _MetaInfoClassMember('name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where client resides
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions created by this client
                ''',
                'session_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.ClientDetails.ClientDetail.Flags' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientDetails.ClientDetail.Flags',
            False, 
            [
            _MetaInfoClassMember('is-recreate-state', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Client is in Recreate State
                ''',
                'is_recreate_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('is-zombie-state', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Client is in Zombie State
                ''',
                'is_zombie_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.ClientDetails.ClientDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientDetails.ClientDetail',
            False, 
            [
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client Name
                ''',
                'client_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('brief', REFERENCE_CLASS, 'Brief' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientDetails.ClientDetail.Brief', 
                [], [], 
                '''                Brief client information
                ''',
                'brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('flags', REFERENCE_CLASS, 'Flags' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientDetails.ClientDetail.Flags', 
                [], [], 
                '''                The BFD Client Flags
                ''',
                'flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('recreate-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Recreate Time in Seconds
                ''',
                'recreate_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'client-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.ClientDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.ClientDetails',
            False, 
            [
            _MetaInfoClassMember('client-detail', REFERENCE_LIST, 'ClientDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientDetails.ClientDetail', 
                [], [], 
                '''                Detailed information of client
                ''',
                'client_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'client-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Counters.PacketCounters.PacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Counters.PacketCounters.PacketCounter',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplay_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplay_Enum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Counters.PacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Counters.PacketCounters',
            False, 
            [
            _MetaInfoClassMember('packet-counter', REFERENCE_LIST, 'PacketCounter' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Counters.PacketCounters.PacketCounter', 
                [], [], 
                '''                Interface Packet counters
                ''',
                'packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Counters' : {
        'meta_info' : _MetaInfoClass('Bfd.Counters',
            False, 
            [
            _MetaInfoClassMember('packet-counters', REFERENCE_CLASS, 'PacketCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Counters.PacketCounters', 
                [], [], 
                '''                Table of Packet counters
                ''',
                'packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.GenericSummaries.GenericSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.GenericSummaries.GenericSummary',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('max-session-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Max Session Number
                ''',
                'max_session_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-session-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                MP Session Number
                ''',
                'mp_session_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('pps-allocated-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Allocated PPS value
                ''',
                'pps_allocated_value',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('pps-max-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Max PPS value
                ''',
                'pps_max_value',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ppsmp-allocated-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Allocated MP PPS value
                ''',
                'ppsmp_allocated_value',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ppsmp-max-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Max MP PPS value
                ''',
                'ppsmp_max_value',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-session-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total Session Number
                ''',
                'total_session_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'generic-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.GenericSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.GenericSummaries',
            False, 
            [
            _MetaInfoClassMember('generic-summary', REFERENCE_LIST, 'GenericSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.GenericSummaries.GenericSummary', 
                [], [], 
                '''                Generic summary information for bfd location
                table
                ''',
                'generic_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'generic-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters.Ipv4MultiHopPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters.Ipv4MultiHopPacketCounter',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplay_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplay_Enum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-packet-counter', REFERENCE_LIST, 'Ipv4MultiHopPacketCounter' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters.Ipv4MultiHopPacketCounter', 
                [], [], 
                '''                IPv4 multiple hop Packet counters
                ''',
                'ipv4_multi_hop_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-packet-counters', REFERENCE_CLASS, 'Ipv4MultiHopPacketCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters', 
                [], [], 
                '''                Table of IPv4 multiple hop Packet counters
                ''',
                'ipv4_multi_hop_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopMultiPaths.Ipv4MultiHopMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopMultiPaths.Ipv4MultiHopMultiPath',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-multi-path', REFERENCE_LIST, 'Ipv4MultiHopMultiPath' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopMultiPaths.Ipv4MultiHopMultiPath', 
                [], [], 
                '''                IPv4 multi hop multipath table
                ''',
                'ipv4_multi_hop_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-node-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopNodeLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopNodeLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-node-location-summary', REFERENCE_LIST, 'Ipv4MultiHopNodeLocationSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv4 multihop
                sessions for location
                ''',
                'ipv4_multi_hop_node_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-node-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-session-brief', REFERENCE_LIST, 'Ipv4MultiHopSessionBrief' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv4 multihop
                BFD session
                ''',
                'ipv4_multi_hop_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibC_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibC_Enum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFec_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFec_Enum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2lFec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadState_Enum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv4-multi-hop-session-detail', REFERENCE_LIST, 'Ipv4MultiHopSessionDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv4 multihop
                BFD session
                ''',
                'ipv4_multi_hop_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4MultiHopSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4MultiHopSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-multi-hop-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters.Ipv4SingleHopPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters.Ipv4SingleHopPacketCounter',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplay_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplay_Enum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-packet-counter', REFERENCE_LIST, 'Ipv4SingleHopPacketCounter' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters.Ipv4SingleHopPacketCounter', 
                [], [], 
                '''                Interface IPv4 single hop Packet counters
                ''',
                'ipv4_single_hop_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-packet-counters', REFERENCE_CLASS, 'Ipv4SingleHopPacketCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters', 
                [], [], 
                '''                Table of IPv4 single hop Packet counters
                ''',
                'ipv4_single_hop_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Location Name
                ''',
                'location_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-location-summary', REFERENCE_LIST, 'Ipv4SingleHopLocationSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv4 singlehop
                sessions for location
                ''',
                'ipv4_single_hop_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopMultiPaths.Ipv4SingleHopMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopMultiPaths.Ipv4SingleHopMultiPath',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-multi-path', REFERENCE_LIST, 'Ipv4SingleHopMultiPath' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopMultiPaths.Ipv4SingleHopMultiPath', 
                [], [], 
                '''                IPv4 single hop multipath table
                ''',
                'ipv4_single_hop_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-node-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopNodeLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopNodeLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-node-location-summary', REFERENCE_LIST, 'Ipv4SingleHopNodeLocationSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv4 singlehop
                sessions for location
                ''',
                'ipv4_single_hop_node_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-node-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-session-brief', REFERENCE_LIST, 'Ipv4SingleHopSessionBrief' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv4 singlehop
                BFD session
                ''',
                'ipv4_single_hop_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibC_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibC_Enum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFec_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFec_Enum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2lFec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadState_Enum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv4-single-hop-session-detail', REFERENCE_LIST, 'Ipv4SingleHopSessionDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv4
                singlehop BFD session
                ''',
                'ipv4_single_hop_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4SingleHopSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4SingleHopSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4-single-hop-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadCounters.Ipv4bfDoMplsteHeadPacketCounters.Ipv4bfDoMplsteHeadPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadCounters.Ipv4bfDoMplsteHeadPacketCounters.Ipv4bfDoMplsteHeadPacketCounter',
            False, 
            [
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplay_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplay_Enum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadCounters.Ipv4bfDoMplsteHeadPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadCounters.Ipv4bfDoMplsteHeadPacketCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-head-packet-counter', REFERENCE_LIST, 'Ipv4bfDoMplsteHeadPacketCounter' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadCounters.Ipv4bfDoMplsteHeadPacketCounters.Ipv4bfDoMplsteHeadPacketCounter', 
                [], [], 
                '''                Interface  IPv4 BFD over MPLS-TE Packet
                counters
                ''',
                'ipv4bf_do_mplste_head_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-head-packet-counters', REFERENCE_CLASS, 'Ipv4bfDoMplsteHeadPacketCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadCounters.Ipv4bfDoMplsteHeadPacketCounters', 
                [], [], 
                '''                Table of IPv4 BFD over MPLS-TE Packet counters
                ''',
                'ipv4bf_do_mplste_head_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadMultiPaths.Ipv4bfDoMplsteHeadMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadMultiPaths.Ipv4bfDoMplsteHeadMultiPath',
            False, 
            [
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-head-multi-path', REFERENCE_LIST, 'Ipv4bfDoMplsteHeadMultiPath' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadMultiPaths.Ipv4bfDoMplsteHeadMultiPath', 
                [], [], 
                '''                Label multipath table
                ''',
                'ipv4bf_do_mplste_head_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief',
            False, 
            [
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-head-session-brief', REFERENCE_LIST, 'Ipv4bfDoMplsteHeadSessionBrief' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv4 BFD over
                MPLS-TE Head session
                ''',
                'ipv4bf_do_mplste_head_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibC_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibC_Enum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFec_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFec_Enum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2lFec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadState_Enum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-head-session-detail', REFERENCE_LIST, 'Ipv4bfDoMplsteHeadSessionDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv4 BFD over
                MPLS-TE head session
                ''',
                'ipv4bf_do_mplste_head_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteHeadSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteHeadSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-head-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailCounters.Ipv4bfDoMplsteTailPacketCounters.Ipv4bfDoMplsteTailPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailCounters.Ipv4bfDoMplsteTailPacketCounters.Ipv4bfDoMplsteTailPacketCounter',
            False, 
            [
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplay_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplay_Enum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailCounters.Ipv4bfDoMplsteTailPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailCounters.Ipv4bfDoMplsteTailPacketCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-packet-counter', REFERENCE_LIST, 'Ipv4bfDoMplsteTailPacketCounter' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailCounters.Ipv4bfDoMplsteTailPacketCounters.Ipv4bfDoMplsteTailPacketCounter', 
                [], [], 
                '''                Interface  IPv4 BFD over MPLS-TE Packet
                counters
                ''',
                'ipv4bf_do_mplste_tail_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailCounters',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-packet-counters', REFERENCE_CLASS, 'Ipv4bfDoMplsteTailPacketCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailCounters.Ipv4bfDoMplsteTailPacketCounters', 
                [], [], 
                '''                Table of IPv4 BFD over MPLS-TE Packet counters
                ''',
                'ipv4bf_do_mplste_tail_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailMultiPaths.Ipv4bfDoMplsteTailMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailMultiPaths.Ipv4bfDoMplsteTailMultiPath',
            False, 
            [
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-multi-path', REFERENCE_LIST, 'Ipv4bfDoMplsteTailMultiPath' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailMultiPaths.Ipv4bfDoMplsteTailMultiPath', 
                [], [], 
                '''                Label multipath table
                ''',
                'ipv4bf_do_mplste_tail_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief',
            False, 
            [
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-session-brief', REFERENCE_LIST, 'Ipv4bfDoMplsteTailSessionBrief' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv4 BFD over
                MPLS-TE session
                ''',
                'ipv4bf_do_mplste_tail_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibC_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibC_Enum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFec_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFec_Enum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2lFec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadState_Enum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fe-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Type
                ''',
                'fe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-ctype', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC C Type
                ''',
                'fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-destination', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Destination
                ''',
                'fec_destination',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Extended Tunnel ID
                ''',
                'fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Source
                ''',
                'fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Subgroup ID
                ''',
                'fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                FEC Subgroup originator
                ''',
                'fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC Tunnel ID
                ''',
                'fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('feclspid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC LSP ID
                ''',
                'feclspid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('fecp2mpid', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                FEC P2MP ID
                ''',
                'fecp2mpid',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-session-detail', REFERENCE_LIST, 'Ipv4bfDoMplsteTailSessionDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv4 BFD over
                MPLS-TE Tail session
                ''',
                'ipv4bf_do_mplste_tail_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfDoMplsteTailSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfDoMplsteTailSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bf-do-mplste-tail-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfdMplsteHeadSummaryNodes.Ipv4bfdMplsteHeadSummaryNode.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfdMplsteHeadSummaryNodes.Ipv4bfdMplsteHeadSummaryNode.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfdMplsteHeadSummaryNodes.Ipv4bfdMplsteHeadSummaryNode' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfdMplsteHeadSummaryNodes.Ipv4bfdMplsteHeadSummaryNode',
            False, 
            [
            _MetaInfoClassMember('location-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Location name
                ''',
                'location_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfdMplsteHeadSummaryNodes.Ipv4bfdMplsteHeadSummaryNode.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bfd-mplste-head-summary-node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfdMplsteHeadSummaryNodes' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfdMplsteHeadSummaryNodes',
            False, 
            [
            _MetaInfoClassMember('ipv4bfd-mplste-head-summary-node', REFERENCE_LIST, 'Ipv4bfdMplsteHeadSummaryNode' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfdMplsteHeadSummaryNodes.Ipv4bfdMplsteHeadSummaryNode', 
                [], [], 
                '''                Summary of IPv4 BFD over MPLS-TE head
                ''',
                'ipv4bfd_mplste_head_summary_node',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bfd-mplste-head-summary-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfdMplsteTailNodeSummaries.Ipv4bfdMplsteTailNodeSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfdMplsteTailNodeSummaries.Ipv4bfdMplsteTailNodeSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfdMplsteTailNodeSummaries.Ipv4bfdMplsteTailNodeSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfdMplsteTailNodeSummaries.Ipv4bfdMplsteTailNodeSummary',
            False, 
            [
            _MetaInfoClassMember('location-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Location name
                ''',
                'location_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfdMplsteTailNodeSummaries.Ipv4bfdMplsteTailNodeSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bfd-mplste-tail-node-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv4bfdMplsteTailNodeSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv4bfdMplsteTailNodeSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv4bfd-mplste-tail-node-summary', REFERENCE_LIST, 'Ipv4bfdMplsteTailNodeSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfdMplsteTailNodeSummaries.Ipv4bfdMplsteTailNodeSummary', 
                [], [], 
                '''                Summary of IPv4 BFD over MPLS-TE tail
                ''',
                'ipv4bfd_mplste_tail_node_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv4bfd-mplste-tail-node-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopMultiPaths.Ipv6MultiHopMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopMultiPaths.Ipv6MultiHopMultiPath',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv6-multi-hop-multi-path', REFERENCE_LIST, 'Ipv6MultiHopMultiPath' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopMultiPaths.Ipv6MultiHopMultiPath', 
                [], [], 
                '''                IPv6 multihop multipath table
                ''',
                'ipv6_multi_hop_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-node-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopNodeLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopNodeLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv6-multi-hop-node-location-summary', REFERENCE_LIST, 'Ipv6MultiHopNodeLocationSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv6 multihop
                sessions for location
                ''',
                'ipv6_multi_hop_node_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-node-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv6-multi-hop-session-brief', REFERENCE_LIST, 'Ipv6MultiHopSessionBrief' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv6 multihop
                BFD session
                ''',
                'ipv6_multi_hop_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibC_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibC_Enum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFec_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFec_Enum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2lFec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadState_Enum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source Address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv6-multi-hop-session-detail', REFERENCE_LIST, 'Ipv6MultiHopSessionDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv6 multihop
                BFD session
                ''',
                'ipv6_multi_hop_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6MultiHopSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6MultiHopSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-multi-hop-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters.Ipv6SingleHopPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters.Ipv6SingleHopPacketCounter',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplay_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplay_Enum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-packet-counter', REFERENCE_LIST, 'Ipv6SingleHopPacketCounter' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters.Ipv6SingleHopPacketCounter', 
                [], [], 
                '''                Interface IPv6 single hop Packet counters
                ''',
                'ipv6_single_hop_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopCounters',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-packet-counters', REFERENCE_CLASS, 'Ipv6SingleHopPacketCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters', 
                [], [], 
                '''                Table of IPv6 single hop Packet counters
                ''',
                'ipv6_single_hop_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Location Name
                ''',
                'location_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-location-summary', REFERENCE_LIST, 'Ipv6SingleHopLocationSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv6 singlehop
                sessions for location
                ''',
                'ipv6_single_hop_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopMultiPaths.Ipv6SingleHopMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopMultiPaths.Ipv6SingleHopMultiPath',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopMultiPaths',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-multi-path', REFERENCE_LIST, 'Ipv6SingleHopMultiPath' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopMultiPaths.Ipv6SingleHopMultiPath', 
                [], [], 
                '''                IPv6 single hop multipath table
                ''',
                'ipv6_single_hop_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-node-location-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopNodeLocationSummaries' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopNodeLocationSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-node-location-summary', REFERENCE_LIST, 'Ipv6SingleHopNodeLocationSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary', 
                [], [], 
                '''                Summary information for BFD IPv6 singlehop
                sessions for location
                ''',
                'ipv6_single_hop_node_location_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-node-location-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-session-brief', REFERENCE_LIST, 'Ipv6SingleHopSessionBrief' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief', 
                [], [], 
                '''                Brief information for a single IPv6 singlehop
                BFD session
                ''',
                'ipv6_single_hop_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibC_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibC_Enum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFec_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFec_Enum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2lFec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadState_Enum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSessionDetails',
            False, 
            [
            _MetaInfoClassMember('ipv6-single-hop-session-detail', REFERENCE_LIST, 'Ipv6SingleHopSessionDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv6
                singlehop BFD session
                ''',
                'ipv6_single_hop_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Ipv6SingleHopSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.Ipv6SingleHopSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ipv6-single-hop-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelCounters.LabelPacketCounters.LabelPacketCounter' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelCounters.LabelPacketCounters.LabelPacketCounter',
            False, 
            [
            _MetaInfoClassMember('display-type', REFERENCE_ENUM_CLASS, 'BfdMgmtPktDisplay_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtPktDisplay_Enum', 
                [], [], 
                '''                Packet Display Type
                ''',
                'display_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets received
                ''',
                'echo_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of echo packets transmitted
                ''',
                'echo_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-receive-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos received
                ''',
                'hello_receive_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hello-transmit-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Hellos transmitted
                ''',
                'hello_transmit_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-packet-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelCounters.LabelPacketCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelCounters.LabelPacketCounters',
            False, 
            [
            _MetaInfoClassMember('label-packet-counter', REFERENCE_LIST, 'LabelPacketCounter' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelCounters.LabelPacketCounters.LabelPacketCounter', 
                [], [], 
                '''                Interface Label Packet counters
                ''',
                'label_packet_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-packet-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelCounters' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelCounters',
            False, 
            [
            _MetaInfoClassMember('label-packet-counters', REFERENCE_CLASS, 'LabelPacketCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelCounters.LabelPacketCounters', 
                [], [], 
                '''                Table of Label Packet counters
                ''',
                'label_packet_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelMultiPaths.LabelMultiPath' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelMultiPaths.LabelMultiPath',
            False, 
            [
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label_xr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'session_interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-multi-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelMultiPaths' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelMultiPaths',
            False, 
            [
            _MetaInfoClassMember('label-multi-path', REFERENCE_LIST, 'LabelMultiPath' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelMultiPaths.LabelMultiPath', 
                [], [], 
                '''                Label multipath table
                ''',
                'label_multi_path',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-multi-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionBriefs.LabelSessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionBriefs.LabelSessionBrief',
            False, 
            [
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionBriefs',
            False, 
            [
            _MetaInfoClassMember('label-session-brief', REFERENCE_LIST, 'LabelSessionBrief' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionBriefs.LabelSessionBrief', 
                [], [], 
                '''                Brief information for a single Label BFD
                session
                ''',
                'label_session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibC_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibC_Enum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFec_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFec_Enum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2lFec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadState_Enum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails.LabelSessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSessionDetails',
            False, 
            [
            _MetaInfoClassMember('label-session-detail', REFERENCE_LIST, 'LabelSessionDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails.LabelSessionDetail', 
                [], [], 
                '''                Detailed information for a single BFD session
                ''',
                'label_session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSummary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSummary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSummary' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSummary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSummary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSummaryNodes.LabelSummaryNode.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSummaryNodes.LabelSummaryNode.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in retry state
                ''',
                'retry_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('standby-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in standby state
                ''',
                'standby_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSummaryNodes.LabelSummaryNode' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSummaryNodes.LabelSummaryNode',
            False, 
            [
            _MetaInfoClassMember('location-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Location name
                ''',
                'location_name',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSummaryNodes.LabelSummaryNode.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-summary-node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.LabelSummaryNodes' : {
        'meta_info' : _MetaInfoClass('Bfd.LabelSummaryNodes',
            False, 
            [
            _MetaInfoClassMember('label-summary-node', REFERENCE_LIST, 'LabelSummaryNode' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSummaryNodes.LabelSummaryNode', 
                [], [], 
                '''                Summary of Label BFD 
                ''',
                'label_summary_node',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'label-summary-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationBriefs.RelationBrief.LinkInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationBriefs.RelationBrief.LinkInformation',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'link-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationBriefs.RelationBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationBriefs.RelationBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('link-information', REFERENCE_LIST, 'LinkInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationBriefs.RelationBrief.LinkInformation', 
                [], [], 
                '''                Brief Member Link Information
                ''',
                'link_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'relation-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationBriefs',
            False, 
            [
            _MetaInfoClassMember('relation-brief', REFERENCE_LIST, 'RelationBrief' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationBriefs.RelationBrief', 
                [], [], 
                '''                Brief information for relation of a single BFD
                session
                ''',
                'relation_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'relation-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibC_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibC_Enum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFec_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFec_Enum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2lFec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail.LinkInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail.LinkInformation',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'link-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails.RelationDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails.RelationDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination Address
                        ''',
                        'destination_address',
                        'Cisco-IOS-XR-ip-bfd-oper', False),
                ]),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('link-information', REFERENCE_LIST, 'LinkInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail.LinkInformation', 
                [], [], 
                '''                Detail Member Link Information
                ''',
                'link_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'relation-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.RelationDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.RelationDetails',
            False, 
            [
            _MetaInfoClassMember('relation-detail', REFERENCE_LIST, 'RelationDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails.RelationDetail', 
                [], [], 
                '''                Detail information for relation of a single BFD
                session
                ''',
                'relation_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'relation-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionBriefs.SessionBrief.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionBriefs.SessionBrief' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionBriefs.SessionBrief',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-flags', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Flags
                ''',
                'session_flags',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionBriefs.SessionBrief.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionBriefs' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionBriefs',
            False, 
            [
            _MetaInfoClassMember('session-brief', REFERENCE_LIST, 'SessionBrief' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionBriefs.SessionBrief', 
                [], [], 
                '''                Brief information for a single IPv4 singlehop
                BFD session
                ''',
                'session_brief',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dummy',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec',
            False, 
            [
            _MetaInfoClassMember('s2l-fec-ctype', REFERENCE_ENUM_CLASS, 'MplsLibC_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'MplsLibC_Enum', 
                [], [], 
                '''                Session identifier (ctype)
                ''',
                's2l_fec_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                sub-LSP destination address
                ''',
                's2l_fec_dest',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-extended-tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Extended tunnel ID
                ''',
                's2l_fec_extended_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-lsp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                LSP ID
                ''',
                's2l_fec_lsp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-p2mp-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                P2MP ID
                ''',
                's2l_fec_p2mp_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSP source address
                ''',
                's2l_fec_source',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                sub-LSP subgroup ID
                ''',
                's2l_fec_subgroup_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-subgroup-originator', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subgroup Originator
                ''',
                's2l_fec_subgroup_originator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Tunnel ID
                ''',
                's2l_fec_tunnel_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('s2l-fec-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF; currently only for GMPLS tunnels
                ''',
                's2l_fec_vrf',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'te-s2l-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec',
            False, 
            [
            _MetaInfoClassMember('bfdfe-ctype', REFERENCE_ENUM_CLASS, 'BfdApiFec_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdApiFec_Enum', 
                [], [], 
                '''                BFDFECType
                ''',
                'bfdfe_ctype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', REFERENCE_CLASS, 'Dummy' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy', 
                [], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('te-s2l-fec', REFERENCE_CLASS, 'TeS2lFec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec', 
                [], [], 
                '''                te s2l fec
                ''',
                'te_s2l_fec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfdfec',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpDestinationAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpDestinationAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-destination-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpSourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpSourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'ip-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey',
            False, 
            [
            _MetaInfoClassMember('bfdfec', REFERENCE_CLASS, 'Bfdfec' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec', 
                [], [], 
                '''                Union of FECs
                ''',
                'bfdfec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Incoming Label
                ''',
                'incoming_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-destination-address', REFERENCE_CLASS, 'IpDestinationAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpDestinationAddress', 
                [], [], 
                '''                IPv4/v6 dest address
                ''',
                'ip_destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ip-source-address', REFERENCE_CLASS, 'IpSourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpSourceAddress', 
                [], [], 
                '''                IPv4/v6 source address
                ''',
                'ip_source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Key Type
                ''',
                'session_key_type',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Session VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.AssociationInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.AssociationInformation',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-key', REFERENCE_CLASS, 'SessionKey' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey', 
                [], [], 
                '''                Session Key
                ''',
                'session_key',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'association-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingRxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingRxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-rx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastErrorTime' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastErrorTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-error-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastTime' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-tx-last-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.LspPingInfo' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.LspPingInfo',
            False, 
            [
            _MetaInfoClassMember('lsp-ping-rx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping numer of times received
                ''',
                'lsp_ping_rx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Code
                ''',
                'lsp_ping_rx_last_code',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-discr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Rx last received discriminator
                ''',
                'lsp_ping_rx_last_discr',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Rx Last Output
                ''',
                'lsp_ping_rx_last_output',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-subcode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                LSP Ping Rx Last Subcode
                ''',
                'lsp_ping_rx_last_subcode',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-rx-last-time', REFERENCE_CLASS, 'LspPingRxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingRxLastTime', 
                [], [], 
                '''                LSP Ping last received time
                ''',
                'lsp_ping_rx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx count
                ''',
                'lsp_ping_tx_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-error-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                LSP Ping Tx error count
                ''',
                'lsp_ping_tx_error_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last error
                ''',
                'lsp_ping_tx_last_error_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-error-time', REFERENCE_CLASS, 'LspPingTxLastErrorTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastErrorTime', 
                [], [], 
                '''                LSP Ping last error time
                ''',
                'lsp_ping_tx_last_error_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-rc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Ping Tx last result
                ''',
                'lsp_ping_tx_last_rc',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-tx-last-time', REFERENCE_CLASS, 'LspPingTxLastTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastTime', 
                [], [], 
                '''                LSP Ping last sent time
                ''',
                'lsp_ping_tx_last_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'lsp-ping-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.MpDownloadState.ChangeTime' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.MpDownloadState.ChangeTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'change-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.MpDownloadState' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.MpDownloadState',
            False, 
            [
            _MetaInfoClassMember('change-time', REFERENCE_CLASS, 'ChangeTime' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.MpDownloadState.ChangeTime', 
                [], [], 
                '''                Change time
                ''',
                'change_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_ENUM_CLASS, 'BfdMpDownloadState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMpDownloadState_Enum', 
                [], [], 
                '''                MP Download State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'mp-download-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.OwnerInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.OwnerInformation',
            False, 
            [
            _MetaInfoClassMember('adjusted-detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted detection multiplier to compute
                detection time
                ''',
                'adjusted_detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('adjusted-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Adjusted minimum transmit interval in
                milli-seconds
                ''',
                'adjusted_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified detection multiplier to compute
                detection time
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Client specified minimum transmit interval in
                micro-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Client process name
                ''',
                'name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'owner-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncReceiveStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncReceiveStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-receive-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.EchoReceivedStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.EchoReceivedStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-received-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.EchoTransmitStatistics' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.EchoTransmitStatistics',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time since last Transmit/Receive (in
                milli-seconds)
                ''',
                'last',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum of Transmit/Receive Interval (in
                milli-seconds)
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Interval Samples between Packets
                sent/received
                ''',
                'number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-transmit-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.LastStateChange' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.LastStateChange',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of days since last session state
                transition
                ''',
                'days',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of hours since last session state
                transition
                ''',
                'hours',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of mins since last session state
                transition
                ''',
                'minutes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Number of seconds since last session state
                transition
                ''',
                'seconds',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'last-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.ReceivePacket' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.ReceivePacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'receive-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.SourceAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.SourceAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-local-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated local transmit interval in
                micro-seconds
                ''',
                'negotiated_local_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-remote-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated remote transmit interval in
                micro-seconds
                ''',
                'negotiated_remote_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'async-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection time in micro-seconds
                ''',
                'detection_time',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('negotiated-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Negotiated transmit interval in micro-seconds
                ''',
                'negotiated_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'echo-interval-multiplier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation',
            False, 
            [
            _MetaInfoClassMember('async-interval-multiplier', REFERENCE_CLASS, 'AsyncIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier', 
                [], [], 
                '''                Async Interval and Detect Multiplier Information
                ''',
                'async_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-interval-multiplier', REFERENCE_CLASS, 'EchoIntervalMultiplier' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier', 
                [], [], 
                '''                Echo Interval and Detect Multiplier Information
                ''',
                'echo_interval_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-brief-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation.TransmitPacket' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation.TransmitPacket',
            False, 
            [
            _MetaInfoClassMember('authentication-present', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Requesting authentication for the session
                ''',
                'authentication_present',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('control-plane-independent', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                BFD implementation does not share fate with its
                control plane
                ''',
                'control_plane_independent',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('demand', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Demand mode
                ''',
                'demand',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum transmit interval in
                micro-seconds
                ''',
                'desired_minimum_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('diagnostic', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Diagnostic
                ''',
                'diagnostic',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('final', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Final bit
                ''',
                'final',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ihear-you', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                I Hear You (v0)
                ''',
                'ihear_you',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Length
                ''',
                'length',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('my-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                My Discriminator
                ''',
                'my_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('poll', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Poll bit
                ''',
                'poll',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-echo-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required echo receive interval in micro-seconds
                ''',
                'required_minimum_echo_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-minimum-receive-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required receive interval in micro-seconds
                ''',
                'required_minimum_receive_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State (v1)
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('your-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Your Discriminator
                ''',
                'your_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'transmit-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail.StatusInformation' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail.StatusInformation',
            False, 
            [
            _MetaInfoClassMember('async-receive-statistics', REFERENCE_CLASS, 'AsyncReceiveStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncReceiveStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Received (in milli-seconds)
                ''',
                'async_receive_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('async-transmit-statistics', REFERENCE_CLASS, 'AsyncTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Async Packets
                Transmitted (in milli-seconds)
                ''',
                'async_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('desired-minimum-echo-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired minimum echo transmit interval in
                milli-seconds
                ''',
                'desired_minimum_echo_transmit_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-received-statistics', REFERENCE_CLASS, 'EchoReceivedStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.EchoReceivedStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Received (in milli-seconds)
                ''',
                'echo_received_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('echo-transmit-statistics', REFERENCE_CLASS, 'EchoTransmitStatistics' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.EchoTransmitStatistics', 
                [], [], 
                '''                Statistics of Interval between Echo Packets
                Transmitted (in milli-seconds)
                ''',
                'echo_transmit_statistics',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-state-change', REFERENCE_CLASS, 'LastStateChange' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.LastStateChange', 
                [], [], 
                '''                Time since last state change
                ''',
                'last_state_change',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-average', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average value of Latency (in micro-seconds)
                ''',
                'latency_average',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-maximum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum value of Latency (in micro-seconds)
                ''',
                'latency_maximum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-minimum', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minimum value of Latency (in micro-seconds)
                ''',
                'latency_minimum',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('latency-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Latency Samples. Time between Transmit
                and Receive
                ''',
                'latency_number',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where session is housed
                ''',
                'node_id',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('receive-packet', REFERENCE_CLASS, 'ReceivePacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.ReceivePacket', 
                [], [], 
                '''                Receive Packet
                ''',
                'receive_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session's Remote discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-negotiated-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Remote Negotiated Interval in milli-seconds
                ''',
                'remote_negotiated_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-subtype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session subtype
                ''',
                'session_subtype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessiontype', REFERENCE_ENUM_CLASS, 'BfdSession_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdSession_Enum', 
                [], [], 
                '''                Session type
                ''',
                'sessiontype',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('source-address', REFERENCE_CLASS, 'SourceAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.SourceAddress', 
                [], [], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionState_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionState_Enum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-brief-information', REFERENCE_CLASS, 'StatusBriefInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation', 
                [], [], 
                '''                Brief Status Information
                ''',
                'status_brief_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('to-up-state-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times session state went to UP
                ''',
                'to_up_state_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('transmit-packet', REFERENCE_CLASS, 'TransmitPacket' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation.TransmitPacket', 
                [], [], 
                '''                Transmit Packet
                ''',
                'transmit_packet',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'status-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails.SessionDetail' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails.SessionDetail',
            False, 
            [
            _MetaInfoClassMember('association-information', REFERENCE_LIST, 'AssociationInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.AssociationInformation', 
                [], [], 
                '''                Association session information
                ''',
                'association_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('lsp-ping-info', REFERENCE_CLASS, 'LspPingInfo' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.LspPingInfo', 
                [], [], 
                '''                LSP Ping Info
                ''',
                'lsp_ping_info',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('mp-download-state', REFERENCE_CLASS, 'MpDownloadState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.MpDownloadState', 
                [], [], 
                '''                MP Dowload State
                ''',
                'mp_download_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('owner-information', REFERENCE_LIST, 'OwnerInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.OwnerInformation', 
                [], [], 
                '''                Client applications owning the session
                ''',
                'owner_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('status-information', REFERENCE_CLASS, 'StatusInformation' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail.StatusInformation', 
                [], [], 
                '''                Session status information
                ''',
                'status_information',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionDetails' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionDetails',
            False, 
            [
            _MetaInfoClassMember('session-detail', REFERENCE_LIST, 'SessionDetail' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails.SessionDetail', 
                [], [], 
                '''                Detailed information for a single IPv4
                singlehop BFD session
                ''',
                'session_detail',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionMibs.SessionMib.DestAddress' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionMibs.SessionMib.DestAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfId_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdAfId_Enum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'dest-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionMibs.SessionMib' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionMibs.SessionMib',
            False, 
            [
            _MetaInfoClassMember('discriminator', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Sesison Discr 
                ''',
                'discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', True),
            _MetaInfoClassMember('desired-min-tx-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Desired Min TX Interval
                ''',
                'desired_min_tx_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('dest-address', REFERENCE_CLASS, 'DestAddress' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionMibs.SessionMib.DestAddress', 
                [], [], 
                '''                Session Destination address
                ''',
                'dest_address',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Detection Multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('int-handle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session Interface Handle
                ''',
                'int_handle',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Session Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-down-diag', REFERENCE_ENUM_CLASS, 'BfdMgmtSessionDiag_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'BfdMgmtSessionDiag_Enum', 
                [], [], 
                '''                Last Session Down Diag
                ''',
                'last_down_diag',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-down-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Last Session Down Time (nanoseconds)
                ''',
                'last_down_time_nsec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-down-time-sec', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Last Session Down Time (seconds)
                ''',
                'last_down_time_sec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-time-cached', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Last Time Session Info Queried
                ''',
                'last_time_cached',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-up-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Last Session Up Time (nanoseconds)
                ''',
                'last_up_time_nsec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('last-up-time-sec', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Last Session Up Time (seconds)
                ''',
                'last_up_time_sec',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Sessions' Local Discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('pkt-in', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Packet In Counter
                ''',
                'pkt_in',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('pkt-out', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Packet Out Counter
                ''',
                'pkt_out',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Sessions' Remote Discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-min-rx-echo-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required Min RX Echo Interval
                ''',
                'required_min_rx_echo_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('required-min-rx-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Required Min RX Interval
                ''',
                'required_min_rx_interval',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session State
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('sessionversion', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Session BFD Version
                ''',
                'sessionversion',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('trap-bitmap', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Trap Generator Bitmap
                ''',
                'trap_bitmap',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Up Count
                ''',
                'up_counter',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.SessionMibs' : {
        'meta_info' : _MetaInfoClass('Bfd.SessionMibs',
            False, 
            [
            _MetaInfoClassMember('session-mib', REFERENCE_LIST, 'SessionMib' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionMibs.SessionMib', 
                [], [], 
                '''                Brief information for BFD session MIB
                ''',
                'session_mib',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-mibs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Summary.SessionState' : {
        'meta_info' : _MetaInfoClass('Bfd.Summary.SessionState',
            False, 
            [
            _MetaInfoClassMember('down-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in down state
                ''',
                'down_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in database
                ''',
                'total_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('unknown-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in unknown state
                ''',
                'unknown_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('up-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of sessions in up state
                ''',
                'up_count',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd.Summary' : {
        'meta_info' : _MetaInfoClass('Bfd.Summary',
            False, 
            [
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Summary.SessionState', 
                [], [], 
                '''                Statistics of states for sessions
                ''',
                'session_state',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
    'Bfd' : {
        'meta_info' : _MetaInfoClass('Bfd',
            False, 
            [
            _MetaInfoClassMember('client-briefs', REFERENCE_CLASS, 'ClientBriefs' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientBriefs', 
                [], [], 
                '''                Table of Brief information about BFD clients
                ''',
                'client_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('client-details', REFERENCE_CLASS, 'ClientDetails' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.ClientDetails', 
                [], [], 
                '''                Table of detailed information about BFD clients
                ''',
                'client_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Counters', 
                [], [], 
                '''                Counters
                ''',
                'counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('generic-summaries', REFERENCE_CLASS, 'GenericSummaries' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.GenericSummaries', 
                [], [], 
                '''                Generic summary information about BFD location
                ''',
                'generic_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-counters', REFERENCE_CLASS, 'Ipv4MultiHopCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopCounters', 
                [], [], 
                '''                IPv4 multiple hop Counters
                ''',
                'ipv4_multi_hop_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-multi-paths', REFERENCE_CLASS, 'Ipv4MultiHopMultiPaths' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopMultiPaths', 
                [], [], 
                '''                IPv4 multi-hop multipath
                ''',
                'ipv4_multi_hop_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-node-location-summaries', REFERENCE_CLASS, 'Ipv4MultiHopNodeLocationSummaries' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopNodeLocationSummaries', 
                [], [], 
                '''                Table of summary information about BFD IPv4
                multihop sessions per location
                ''',
                'ipv4_multi_hop_node_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-session-briefs', REFERENCE_CLASS, 'Ipv4MultiHopSessionBriefs' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv4
                multihop BFD sessions in the System
                ''',
                'ipv4_multi_hop_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-session-details', REFERENCE_CLASS, 'Ipv4MultiHopSessionDetails' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv4
                multihop BFD sessions in the System 
                ''',
                'ipv4_multi_hop_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-multi-hop-summary', REFERENCE_CLASS, 'Ipv4MultiHopSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4MultiHopSummary', 
                [], [], 
                '''                Summary information of BFD IPv4 multihop
                sessions
                ''',
                'ipv4_multi_hop_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-counters', REFERENCE_CLASS, 'Ipv4SingleHopCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopCounters', 
                [], [], 
                '''                IPv4 single hop Counters
                ''',
                'ipv4_single_hop_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-location-summaries', REFERENCE_CLASS, 'Ipv4SingleHopLocationSummaries' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopLocationSummaries', 
                [], [], 
                '''                Table of summary information about IPv4
                singlehop BFD sessions for location
                ''',
                'ipv4_single_hop_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-multi-paths', REFERENCE_CLASS, 'Ipv4SingleHopMultiPaths' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopMultiPaths', 
                [], [], 
                '''                IPv4 single hop multipath
                ''',
                'ipv4_single_hop_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-node-location-summaries', REFERENCE_CLASS, 'Ipv4SingleHopNodeLocationSummaries' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopNodeLocationSummaries', 
                [], [], 
                '''                Table of summary information about BFD IPv4
                singlehop sessions per location
                ''',
                'ipv4_single_hop_node_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-session-briefs', REFERENCE_CLASS, 'Ipv4SingleHopSessionBriefs' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv4
                singlehop BFD sessions in the System
                ''',
                'ipv4_single_hop_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-session-details', REFERENCE_CLASS, 'Ipv4SingleHopSessionDetails' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv4
                singlehop BFD sessions in the System 
                ''',
                'ipv4_single_hop_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4-single-hop-summary', REFERENCE_CLASS, 'Ipv4SingleHopSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4SingleHopSummary', 
                [], [], 
                '''                Summary information of BFD IPv4 singlehop
                sessions
                ''',
                'ipv4_single_hop_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-head-counters', REFERENCE_CLASS, 'Ipv4bfDoMplsteHeadCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadCounters', 
                [], [], 
                '''                IPv4 BFD over MPLS-TE Counters
                ''',
                'ipv4bf_do_mplste_head_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-head-multi-paths', REFERENCE_CLASS, 'Ipv4bfDoMplsteHeadMultiPaths' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadMultiPaths', 
                [], [], 
                '''                IPv4 BFD over MPLS-TE Head multipath
                ''',
                'ipv4bf_do_mplste_head_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-head-session-briefs', REFERENCE_CLASS, 'Ipv4bfDoMplsteHeadSessionBriefs' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv4 BFD
                over MPLS-TE Head sessions in the System
                ''',
                'ipv4bf_do_mplste_head_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-head-session-details', REFERENCE_CLASS, 'Ipv4bfDoMplsteHeadSessionDetails' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv4 BFD
                over MPLS-TE Head sessions in the System
                ''',
                'ipv4bf_do_mplste_head_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-head-summary', REFERENCE_CLASS, 'Ipv4bfDoMplsteHeadSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteHeadSummary', 
                [], [], 
                '''                Summary information of IPv4 BFD over MPLS-TE
                Head
                ''',
                'ipv4bf_do_mplste_head_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-counters', REFERENCE_CLASS, 'Ipv4bfDoMplsteTailCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailCounters', 
                [], [], 
                '''                IPv4 BFD over MPLS-TE Counters
                ''',
                'ipv4bf_do_mplste_tail_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-multi-paths', REFERENCE_CLASS, 'Ipv4bfDoMplsteTailMultiPaths' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailMultiPaths', 
                [], [], 
                '''                IPv4 BFD over MPLS-TE Tail multipath
                ''',
                'ipv4bf_do_mplste_tail_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-session-briefs', REFERENCE_CLASS, 'Ipv4bfDoMplsteTailSessionBriefs' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv4 BFD
                over MPLS-TE Tail sessions in the System
                ''',
                'ipv4bf_do_mplste_tail_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-session-details', REFERENCE_CLASS, 'Ipv4bfDoMplsteTailSessionDetails' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv4 BFD
                over MPLS-TE Tail sessions in the System
                ''',
                'ipv4bf_do_mplste_tail_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bf-do-mplste-tail-summary', REFERENCE_CLASS, 'Ipv4bfDoMplsteTailSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfDoMplsteTailSummary', 
                [], [], 
                '''                Summary information of IPv4 BFD over MPLS-TE
                Tail
                ''',
                'ipv4bf_do_mplste_tail_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bfd-mplste-head-summary-nodes', REFERENCE_CLASS, 'Ipv4bfdMplsteHeadSummaryNodes' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfdMplsteHeadSummaryNodes', 
                [], [], 
                '''                Table of summary about IPv4 TE head BFD sessions
                for location
                ''',
                'ipv4bfd_mplste_head_summary_nodes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv4bfd-mplste-tail-node-summaries', REFERENCE_CLASS, 'Ipv4bfdMplsteTailNodeSummaries' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv4bfdMplsteTailNodeSummaries', 
                [], [], 
                '''                Table of summary about IPv4 TE tail BFD sessions
                for location
                ''',
                'ipv4bfd_mplste_tail_node_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-multi-hop-multi-paths', REFERENCE_CLASS, 'Ipv6MultiHopMultiPaths' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopMultiPaths', 
                [], [], 
                '''                IPv6 multi hop multipath
                ''',
                'ipv6_multi_hop_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-multi-hop-node-location-summaries', REFERENCE_CLASS, 'Ipv6MultiHopNodeLocationSummaries' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopNodeLocationSummaries', 
                [], [], 
                '''                Table of summary information about BFD IPv6
                multihop sessions per location
                ''',
                'ipv6_multi_hop_node_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-multi-hop-session-briefs', REFERENCE_CLASS, 'Ipv6MultiHopSessionBriefs' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv6
                multihop BFD sessions in the System
                ''',
                'ipv6_multi_hop_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-multi-hop-session-details', REFERENCE_CLASS, 'Ipv6MultiHopSessionDetails' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv6
                multihop BFD sessions in the System 
                ''',
                'ipv6_multi_hop_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-multi-hop-summary', REFERENCE_CLASS, 'Ipv6MultiHopSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6MultiHopSummary', 
                [], [], 
                '''                Summary information of BFD IPv6 multihop
                sessions
                ''',
                'ipv6_multi_hop_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-counters', REFERENCE_CLASS, 'Ipv6SingleHopCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopCounters', 
                [], [], 
                '''                IPv6 single hop Counters
                ''',
                'ipv6_single_hop_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-location-summaries', REFERENCE_CLASS, 'Ipv6SingleHopLocationSummaries' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopLocationSummaries', 
                [], [], 
                '''                Table of summary information about BFD IPv6
                singlehop sessions per location
                ''',
                'ipv6_single_hop_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-multi-paths', REFERENCE_CLASS, 'Ipv6SingleHopMultiPaths' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopMultiPaths', 
                [], [], 
                '''                IPv6 single hop multipath
                ''',
                'ipv6_single_hop_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-node-location-summaries', REFERENCE_CLASS, 'Ipv6SingleHopNodeLocationSummaries' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopNodeLocationSummaries', 
                [], [], 
                '''                Table of summary information about BFD IPv6
                singlehop sessions per location
                ''',
                'ipv6_single_hop_node_location_summaries',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-session-briefs', REFERENCE_CLASS, 'Ipv6SingleHopSessionBriefs' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionBriefs', 
                [], [], 
                '''                Table of brief information about all IPv6
                singlehop BFD sessions in the System
                ''',
                'ipv6_single_hop_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-session-details', REFERENCE_CLASS, 'Ipv6SingleHopSessionDetails' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSessionDetails', 
                [], [], 
                '''                Table of detailed information about all IPv6
                singlehop BFD sessions in the System 
                ''',
                'ipv6_single_hop_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('ipv6-single-hop-summary', REFERENCE_CLASS, 'Ipv6SingleHopSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Ipv6SingleHopSummary', 
                [], [], 
                '''                Summary information of BFD IPv6 singlehop
                sessions
                ''',
                'ipv6_single_hop_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-counters', REFERENCE_CLASS, 'LabelCounters' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelCounters', 
                [], [], 
                '''                Label Counters
                ''',
                'label_counters',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-multi-paths', REFERENCE_CLASS, 'LabelMultiPaths' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelMultiPaths', 
                [], [], 
                '''                Label multipath
                ''',
                'label_multi_paths',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-session-briefs', REFERENCE_CLASS, 'LabelSessionBriefs' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionBriefs', 
                [], [], 
                '''                Table of brief information about all Label BFD
                sessions in the System
                ''',
                'label_session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-session-details', REFERENCE_CLASS, 'LabelSessionDetails' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSessionDetails', 
                [], [], 
                '''                Table of detailed information about all Label
                BFD sessions in the System 
                ''',
                'label_session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-summary', REFERENCE_CLASS, 'LabelSummary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSummary', 
                [], [], 
                '''                Summary information of Label BFD
                ''',
                'label_summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('label-summary-nodes', REFERENCE_CLASS, 'LabelSummaryNodes' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.LabelSummaryNodes', 
                [], [], 
                '''                Table of summary about Label BFD sessions for
                location
                ''',
                'label_summary_nodes',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('relation-briefs', REFERENCE_CLASS, 'RelationBriefs' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationBriefs', 
                [], [], 
                '''                Table of brief information about all BFD
                relations in the System
                ''',
                'relation_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('relation-details', REFERENCE_CLASS, 'RelationDetails' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.RelationDetails', 
                [], [], 
                '''                Table of detail information about all BFD
                relations in the System
                ''',
                'relation_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-briefs', REFERENCE_CLASS, 'SessionBriefs' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionBriefs', 
                [], [], 
                '''                Table of brief information about singlehop IPv4
                BFD sessions in the System
                ''',
                'session_briefs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-details', REFERENCE_CLASS, 'SessionDetails' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionDetails', 
                [], [], 
                '''                Table of detailed information about IPv4
                singlehop BFD sessions in the System 
                ''',
                'session_details',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('session-mibs', REFERENCE_CLASS, 'SessionMibs' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.SessionMibs', 
                [], [], 
                '''                BFD session MIB database
                ''',
                'session_mibs',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper', 'Bfd.Summary', 
                [], [], 
                '''                Summary information of BFD IPv4 singlehop
                sessions
                ''',
                'summary',
                'Cisco-IOS-XR-ip-bfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-bfd-oper',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_bfd_oper'
        ),
    },
}
_meta_table['Bfd.ClientBriefs.ClientBrief']['meta_info'].parent =_meta_table['Bfd.ClientBriefs']['meta_info']
_meta_table['Bfd.ClientDetails.ClientDetail.Brief']['meta_info'].parent =_meta_table['Bfd.ClientDetails.ClientDetail']['meta_info']
_meta_table['Bfd.ClientDetails.ClientDetail.Flags']['meta_info'].parent =_meta_table['Bfd.ClientDetails.ClientDetail']['meta_info']
_meta_table['Bfd.ClientDetails.ClientDetail']['meta_info'].parent =_meta_table['Bfd.ClientDetails']['meta_info']
_meta_table['Bfd.Counters.PacketCounters.PacketCounter']['meta_info'].parent =_meta_table['Bfd.Counters.PacketCounters']['meta_info']
_meta_table['Bfd.Counters.PacketCounters']['meta_info'].parent =_meta_table['Bfd.Counters']['meta_info']
_meta_table['Bfd.GenericSummaries.GenericSummary']['meta_info'].parent =_meta_table['Bfd.GenericSummaries']['meta_info']
_meta_table['Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters.Ipv4MultiHopPacketCounter']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters']['meta_info']
_meta_table['Bfd.Ipv4MultiHopCounters.Ipv4MultiHopPacketCounters']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopCounters']['meta_info']
_meta_table['Bfd.Ipv4MultiHopMultiPaths.Ipv4MultiHopMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopMultiPaths']['meta_info']
_meta_table['Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary']['meta_info']
_meta_table['Bfd.Ipv4MultiHopNodeLocationSummaries.Ipv4MultiHopNodeLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopNodeLocationSummaries']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionBriefs.Ipv4MultiHopSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionBriefs']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSessionDetails']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4MultiHopSummary']['meta_info']
_meta_table['Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters.Ipv4SingleHopPacketCounter']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters']['meta_info']
_meta_table['Bfd.Ipv4SingleHopCounters.Ipv4SingleHopPacketCounters']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopCounters']['meta_info']
_meta_table['Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary']['meta_info']
_meta_table['Bfd.Ipv4SingleHopLocationSummaries.Ipv4SingleHopLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopLocationSummaries']['meta_info']
_meta_table['Bfd.Ipv4SingleHopMultiPaths.Ipv4SingleHopMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopMultiPaths']['meta_info']
_meta_table['Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary']['meta_info']
_meta_table['Bfd.Ipv4SingleHopNodeLocationSummaries.Ipv4SingleHopNodeLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopNodeLocationSummaries']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionBriefs.Ipv4SingleHopSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionBriefs']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSessionDetails']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4SingleHopSummary']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadCounters.Ipv4bfDoMplsteHeadPacketCounters.Ipv4bfDoMplsteHeadPacketCounter']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadCounters.Ipv4bfDoMplsteHeadPacketCounters']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadCounters.Ipv4bfDoMplsteHeadPacketCounters']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadCounters']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadMultiPaths.Ipv4bfDoMplsteHeadMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadMultiPaths']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionBriefs.Ipv4bfDoMplsteHeadSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionBriefs']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails.Ipv4bfDoMplsteHeadSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteHeadSummary']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailCounters.Ipv4bfDoMplsteTailPacketCounters.Ipv4bfDoMplsteTailPacketCounter']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailCounters.Ipv4bfDoMplsteTailPacketCounters']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailCounters.Ipv4bfDoMplsteTailPacketCounters']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailCounters']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailMultiPaths.Ipv4bfDoMplsteTailMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailMultiPaths']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionBriefs.Ipv4bfDoMplsteTailSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionBriefs']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails.Ipv4bfDoMplsteTailSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4bfDoMplsteTailSummary']['meta_info']
_meta_table['Bfd.Ipv4bfdMplsteHeadSummaryNodes.Ipv4bfdMplsteHeadSummaryNode.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4bfdMplsteHeadSummaryNodes.Ipv4bfdMplsteHeadSummaryNode']['meta_info']
_meta_table['Bfd.Ipv4bfdMplsteHeadSummaryNodes.Ipv4bfdMplsteHeadSummaryNode']['meta_info'].parent =_meta_table['Bfd.Ipv4bfdMplsteHeadSummaryNodes']['meta_info']
_meta_table['Bfd.Ipv4bfdMplsteTailNodeSummaries.Ipv4bfdMplsteTailNodeSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv4bfdMplsteTailNodeSummaries.Ipv4bfdMplsteTailNodeSummary']['meta_info']
_meta_table['Bfd.Ipv4bfdMplsteTailNodeSummaries.Ipv4bfdMplsteTailNodeSummary']['meta_info'].parent =_meta_table['Bfd.Ipv4bfdMplsteTailNodeSummaries']['meta_info']
_meta_table['Bfd.Ipv6MultiHopMultiPaths.Ipv6MultiHopMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopMultiPaths']['meta_info']
_meta_table['Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary']['meta_info']
_meta_table['Bfd.Ipv6MultiHopNodeLocationSummaries.Ipv6MultiHopNodeLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopNodeLocationSummaries']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionBriefs.Ipv6MultiHopSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionBriefs']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSessionDetails']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv6MultiHopSummary']['meta_info']
_meta_table['Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters.Ipv6SingleHopPacketCounter']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters']['meta_info']
_meta_table['Bfd.Ipv6SingleHopCounters.Ipv6SingleHopPacketCounters']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopCounters']['meta_info']
_meta_table['Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary']['meta_info']
_meta_table['Bfd.Ipv6SingleHopLocationSummaries.Ipv6SingleHopLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopLocationSummaries']['meta_info']
_meta_table['Bfd.Ipv6SingleHopMultiPaths.Ipv6SingleHopMultiPath']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopMultiPaths']['meta_info']
_meta_table['Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary']['meta_info']
_meta_table['Bfd.Ipv6SingleHopNodeLocationSummaries.Ipv6SingleHopNodeLocationSummary']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopNodeLocationSummaries']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionBriefs.Ipv6SingleHopSessionBrief']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionBriefs']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSessionDetails']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.Ipv6SingleHopSummary']['meta_info']
_meta_table['Bfd.LabelCounters.LabelPacketCounters.LabelPacketCounter']['meta_info'].parent =_meta_table['Bfd.LabelCounters.LabelPacketCounters']['meta_info']
_meta_table['Bfd.LabelCounters.LabelPacketCounters']['meta_info'].parent =_meta_table['Bfd.LabelCounters']['meta_info']
_meta_table['Bfd.LabelMultiPaths.LabelMultiPath']['meta_info'].parent =_meta_table['Bfd.LabelMultiPaths']['meta_info']
_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief']['meta_info']
_meta_table['Bfd.LabelSessionBriefs.LabelSessionBrief']['meta_info'].parent =_meta_table['Bfd.LabelSessionBriefs']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info']
_meta_table['Bfd.LabelSessionDetails.LabelSessionDetail']['meta_info'].parent =_meta_table['Bfd.LabelSessionDetails']['meta_info']
_meta_table['Bfd.LabelSummary.SessionState']['meta_info'].parent =_meta_table['Bfd.LabelSummary']['meta_info']
_meta_table['Bfd.LabelSummaryNodes.LabelSummaryNode.SessionState']['meta_info'].parent =_meta_table['Bfd.LabelSummaryNodes.LabelSummaryNode']['meta_info']
_meta_table['Bfd.LabelSummaryNodes.LabelSummaryNode']['meta_info'].parent =_meta_table['Bfd.LabelSummaryNodes']['meta_info']
_meta_table['Bfd.RelationBriefs.RelationBrief.LinkInformation']['meta_info'].parent =_meta_table['Bfd.RelationBriefs.RelationBrief']['meta_info']
_meta_table['Bfd.RelationBriefs.RelationBrief']['meta_info'].parent =_meta_table['Bfd.RelationBriefs']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail.LinkInformation']['meta_info'].parent =_meta_table['Bfd.RelationDetails.RelationDetail']['meta_info']
_meta_table['Bfd.RelationDetails.RelationDetail']['meta_info'].parent =_meta_table['Bfd.RelationDetails']['meta_info']
_meta_table['Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.SessionBriefs.SessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.SessionBriefs.SessionBrief.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.SessionBriefs.SessionBrief.StatusBriefInformation']['meta_info']
_meta_table['Bfd.SessionBriefs.SessionBrief.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.SessionBriefs.SessionBrief']['meta_info']
_meta_table['Bfd.SessionBriefs.SessionBrief']['meta_info'].parent =_meta_table['Bfd.SessionBriefs']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.Dummy']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec.TeS2lFec']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.Bfdfec']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpDestinationAddress']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey.IpSourceAddress']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation.SessionKey']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingRxLastTime']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastErrorTime']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastTime']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.MpDownloadState.ChangeTime']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.MpDownloadState']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.AsyncIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation.EchoIntervalMultiplier']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncReceiveStatistics']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.AsyncTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.EchoReceivedStatistics']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.EchoTransmitStatistics']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.LastStateChange']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.ReceivePacket']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.SourceAddress']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.StatusBriefInformation']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation.TransmitPacket']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.AssociationInformation']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.LspPingInfo']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.MpDownloadState']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.OwnerInformation']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail.StatusInformation']['meta_info'].parent =_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info']
_meta_table['Bfd.SessionDetails.SessionDetail']['meta_info'].parent =_meta_table['Bfd.SessionDetails']['meta_info']
_meta_table['Bfd.SessionMibs.SessionMib.DestAddress']['meta_info'].parent =_meta_table['Bfd.SessionMibs.SessionMib']['meta_info']
_meta_table['Bfd.SessionMibs.SessionMib']['meta_info'].parent =_meta_table['Bfd.SessionMibs']['meta_info']
_meta_table['Bfd.Summary.SessionState']['meta_info'].parent =_meta_table['Bfd.Summary']['meta_info']
_meta_table['Bfd.ClientBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.ClientDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Counters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.GenericSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopNodeLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4MultiHopSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopNodeLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4SingleHopSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteHeadSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfDoMplsteTailSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfdMplsteHeadSummaryNodes']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv4bfdMplsteTailNodeSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6MultiHopMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6MultiHopNodeLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6MultiHopSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopNodeLocationSummaries']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Ipv6SingleHopSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.LabelCounters']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.LabelMultiPaths']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.LabelSessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.LabelSessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.LabelSummary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.LabelSummaryNodes']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.RelationBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.RelationDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.SessionBriefs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.SessionDetails']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.SessionMibs']['meta_info'].parent =_meta_table['Bfd']['meta_info']
_meta_table['Bfd.Summary']['meta_info'].parent =_meta_table['Bfd']['meta_info']
