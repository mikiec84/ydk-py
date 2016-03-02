


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'TunnelStatus_Enum' : _MetaInfoEnum('TunnelStatus_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'active':'ACTIVE',
            'destroy':'DESTROY',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'IkeHashAlgo_Enum' : _MetaInfoEnum('IkeHashAlgo_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'none':'NONE',
            'md5':'MD5',
            'sha':'SHA',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'IkeAuthMethod_Enum' : _MetaInfoEnum('IkeAuthMethod_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'none':'NONE',
            'preSharedKey':'PRESHAREDKEY',
            'rsaSig':'RSASIG',
            'rsaEncrypt':'RSAENCRYPT',
            'revPublicKey':'REVPUBLICKEY',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'KeyType_Enum' : _MetaInfoEnum('KeyType_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'ike':'IKE',
            'manual':'MANUAL',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'TrapStatus_Enum' : _MetaInfoEnum('TrapStatus_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'CompAlgo_Enum' : _MetaInfoEnum('CompAlgo_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'none':'NONE',
            'ldf':'LDF',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'EncryptAlgo_Enum' : _MetaInfoEnum('EncryptAlgo_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'none':'NONE',
            'des':'DES',
            'des3':'DES3',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'IkePeerType_Enum' : _MetaInfoEnum('IkePeerType_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'ipAddrPeer':'IPADDRPEER',
            'namePeer':'NAMEPEER',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'IkeNegoMode_Enum' : _MetaInfoEnum('IkeNegoMode_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'main':'MAIN',
            'aggressive':'AGGRESSIVE',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'EncapMode_Enum' : _MetaInfoEnum('EncapMode_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'tunnel':'TUNNEL',
            'transport':'TRANSPORT',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'AuthAlgo_Enum' : _MetaInfoEnum('AuthAlgo_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'none':'NONE',
            'hmacMd5':'HMACMD5',
            'hmacSha':'HMACSHA',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'EndPtType_Enum' : _MetaInfoEnum('EndPtType_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'singleIpAddr':'SINGLEIPADDR',
            'ipAddrRange':'IPADDRRANGE',
            'ipSubnet':'IPSUBNET',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'DiffHellmanGrp_Enum' : _MetaInfoEnum('DiffHellmanGrp_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'none':'NONE',
            'dhGroup1':'DHGROUP1',
            'dhGroup2':'DHGROUP2',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'CISCOIPSECFLOWMONITORMIB.CikeFailTable.CikeFailEntry.CikeFailReason_Enum' : _MetaInfoEnum('CikeFailReason_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'other':'OTHER',
            'peerDelRequest':'PEERDELREQUEST',
            'peerLost':'PEERLOST',
            'localFailure':'LOCALFAILURE',
            'authFailure':'AUTHFAILURE',
            'hashValidation':'HASHVALIDATION',
            'encryptFailure':'ENCRYPTFAILURE',
            'internalError':'INTERNALERROR',
            'sysCapExceeded':'SYSCAPEXCEEDED',
            'proposalFailure':'PROPOSALFAILURE',
            'peerCertUnavailable':'PEERCERTUNAVAILABLE',
            'peerCertNotValid':'PEERCERTNOTVALID',
            'localCertExpired':'LOCALCERTEXPIRED',
            'crlFailure':'CRLFAILURE',
            'peerEncodingError':'PEERENCODINGERROR',
            'nonExistentSa':'NONEXISTENTSA',
            'operRequest':'OPERREQUEST',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'CISCOIPSECFLOWMONITORMIB.CikeFailTable.CikeFailEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikeFailTable.CikeFailEntry',
            False, 
            [
            _MetaInfoClassMember('cikeFailIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The IPsec Phase-1 Failure Table index.
                The value of the index is a number which 
                begins at one and is incremented with each 
                IPsec Phase-1 failure. The value
                of this object will wrap at 2,147,483,647.
                ''',
                'cikefailindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikeFailLocalAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the local peer.
                ''',
                'cikefaillocaladdr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeFailLocalType', REFERENCE_ENUM_CLASS, 'IkePeerType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkePeerType_Enum', 
                [], [], 
                '''                The type of local peer identity.  The local peer
                may be identified by:
                 1. an IP address, or
                 2. a host name.
                ''',
                'cikefaillocaltype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeFailLocalValue', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The value of the local peer identity.
                
                If the local peer type is an IP Address, then this
                is the IP Address used to identify the local peer.
                
                If the local peer type is a host name, then this is
                the host name used to identify the local peer.
                ''',
                'cikefaillocalvalue',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeFailReason', REFERENCE_ENUM_CLASS, 'CikeFailReason_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikeFailTable.CikeFailEntry.CikeFailReason_Enum', 
                [], [], 
                '''                The reason for the failure.  Possible reasons include:
                1 = other
                2 = peer delete request was received
                3 = contact with peer was lost
                4 = local failure occurred
                5 = authentication failure
                6 = hash validation failure
                7 = encryption failure
                8 = internal error occurred
                9 = system capacity failure
                10 = proposal failure
                11 = peer's certificate is unavailable
                12 = peer's certificate was found invalid
                13 = local certificate expired
                14 = certificate revoke list (crl) failure
                15 = peer encoding error
                16 = non-existent security association
                17 = operator requested termination.
                ''',
                'cikefailreason',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeFailRemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the remote peer.
                ''',
                'cikefailremoteaddr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeFailRemoteType', REFERENCE_ENUM_CLASS, 'IkePeerType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkePeerType_Enum', 
                [], [], 
                '''                The type of remote peer identity.  The remote
                peer may be identified by:
                 1. an IP address, or
                 2. a host name.
                ''',
                'cikefailremotetype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeFailRemoteValue', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The value of the remote peer identity.
                
                If the remote peer type is an IP Address, then this
                is the IP Address used to identify the remote peer.
                
                If the remote peer type is a host name, then this is
                the host name used to identify the remote peer.
                ''',
                'cikefailremotevalue',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeFailTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime in hundredths of seconds
                at the time of the failure.
                ''',
                'cikefailtime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikeFailEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikeFailTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikeFailTable',
            False, 
            [
            _MetaInfoClassMember('cikeFailEntry', REFERENCE_LIST, 'CikeFailEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikeFailTable.CikeFailEntry', 
                [], [], 
                '''                Each entry contains the attributes associated
                with
                 an IPsec Phase-1 failure.
                ''',
                'cikefailentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikeFailTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikeGlobalStats' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikeGlobalStats',
            False, 
            [
            _MetaInfoClassMember('cikeGlobalActiveTunnels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of currently active IPsec
                Phase-1 IKE Tunnels.
                ''',
                'cikeglobalactivetunnels',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of authentications which ended
                in failure by all current and previous IPsec Phase-1
                IKE Tunnels.
                ''',
                'cikeglobalauthfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalDecryptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of decryptions which ended
                in failure by all current and previous IPsec Phase-1
                IKE Tunnels.
                ''',
                'cikeglobaldecryptfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalHashValidFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of hash validations which ended
                in failure by all current and previous IPsec Phase-1
                IKE Tunnels.
                ''',
                'cikeglobalhashvalidfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalInDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets which were
                dropped during receive processing by all 
                currently and previously
                 active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobalindroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalInitTunnelFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-1 IKE Tunnels
                which were locally initiated and failed to activate.
                ''',
                'cikeglobalinittunnelfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalInitTunnels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-1 IKE
                Tunnels which were locally initiated.
                ''',
                'cikeglobalinittunnels',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalInNotifys', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of notifys received by
                all currently and previously active IPsec 
                Phase-1 IKE Tunnels.
                ''',
                'cikeglobalinnotifys',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets received by all currently
                and previously active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobalinoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalInP2ExchgInvalids', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                which were received and found to be invalid 
                by all currently and previously active IPsec 
                Phase-1 IKE Tunnels.
                ''',
                'cikeglobalinp2exchginvalids',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalInP2ExchgRejects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                which were received and rejected by all 
                currently and previously active IPsec Phase-1 
                IKE Tunnels.
                ''',
                'cikeglobalinp2exchgrejects',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalInP2Exchgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                received by all currently and previously 
                active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobalinp2exchgs',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalInP2SaDelRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 security
                association delete requests received by all 
                currently and previously
                 active and IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobalinp2sadelrequests',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received by all
                currently and previously active IPsec 
                Phase-1 IKE Tunnels.
                ''',
                'cikeglobalinpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalNoSaFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of non-existent Security Association
                in failures which occurred during processing of 
                all current and previous IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobalnosafails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalOutDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets which were dropped
                during send processing by all currently 
                and previously
                 active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobaloutdroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalOutNotifys', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of notifys sent by all currently
                and previously active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobaloutnotifys',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets sent by all currently
                and previously active and IPsec Phase-1 
                IKE Tunnels.
                ''',
                'cikeglobaloutoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalOutP2ExchgInvalids', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                which were sent and found to be invalid by 
                all currently and previously active IPsec Phase-1 
                Tunnels.
                ''',
                'cikeglobaloutp2exchginvalids',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalOutP2ExchgRejects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                which were sent and rejected by all currently and
                 previously active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobaloutp2exchgrejects',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalOutP2Exchgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                which were sent by all currently and previously 
                active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobaloutp2exchgs',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalOutP2SaDelRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 SA
                delete requests sent by all currently and 
                previously active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobaloutp2sadelrequests',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets sent by all currently
                and previously active and IPsec Phase-1 
                Tunnels.
                ''',
                'cikeglobaloutpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalPreviousTunnels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of previously active
                IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobalprevioustunnels',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalRespTunnelFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-1 IKE Tunnels
                which were remotely initiated and failed to activate.
                ''',
                'cikeglobalresptunnelfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalSysCapFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of system capacity failures
                which occurred during processing of all current 
                and previously active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikeglobalsyscapfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikeGlobalStats',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable.CikePeerCorrEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable.CikePeerCorrEntry',
            False, 
            [
            _MetaInfoClassMember('cikePeerCorrIntIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The internal index of the local-remote
                peer association.  This internal index is 
                used to uniquely identify multiple associations 
                between the local and remote peer.
                ''',
                'cikepeercorrintindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePeerCorrLocalType', REFERENCE_ENUM_CLASS, 'IkePeerType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkePeerType_Enum', 
                [], [], 
                '''                The type of local peer identity. The local peer
                may be identified by:
                1. an IP address, or
                2. a host name.
                ''',
                'cikepeercorrlocaltype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePeerCorrLocalValue', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The value of the local peer identity.
                
                If the local peer type is an IP Address, then this
                is the IP Address used to identify the local peer.
                
                If the local peer type is a host name, then this is
                the host name used to identify the local peer.
                ''',
                'cikepeercorrlocalvalue',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePeerCorrRemoteType', REFERENCE_ENUM_CLASS, 'IkePeerType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkePeerType_Enum', 
                [], [], 
                '''                The type of remote peer identity. The remote peer
                may be identified by:
                1. an IP address, or
                2. a host name.
                ''',
                'cikepeercorrremotetype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePeerCorrRemoteValue', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The value of the remote peer identity.
                
                If the remote peer type is an IP Address, then this
                is the IP Address used to identify the remote peer.
                
                If the remote peer type is a host name, then this is
                the host name used to identify the remote peer.
                ''',
                'cikepeercorrremotevalue',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePeerCorrSeqNum', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The sequence number of the local-remote
                peer association.  This sequence number is 
                used to uniquely identify multiple instances 
                of an unique association between
                 the local and remote peer.
                ''',
                'cikepeercorrseqnum',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePeerCorrIpSecTunIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the active IPsec Phase-2 Tunnel
                (cipSecTunIndex in the cipSecTunnelTable) for this
                IPsec Phase-1 IKE Peer Association.
                ''',
                'cikepeercorripsectunindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikePeerCorrEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable',
            False, 
            [
            _MetaInfoClassMember('cikePeerCorrEntry', REFERENCE_LIST, 'CikePeerCorrEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable.CikePeerCorrEntry', 
                [], [], 
                '''                Each entry contains the attributes of an
                IPsec Phase-1 IKE Peer Association to IPsec
                Phase-2 Tunnel Correlation.
                ''',
                'cikepeercorrentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikePeerCorrTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikePeerTable.CikePeerEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikePeerTable.CikePeerEntry',
            False, 
            [
            _MetaInfoClassMember('cikePeerIntIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The internal index of the local-remote
                peer association.  This internal index is used 
                to uniquely identify multiple associations between 
                the local and remote peer.
                ''',
                'cikepeerintindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePeerLocalType', REFERENCE_ENUM_CLASS, 'IkePeerType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkePeerType_Enum', 
                [], [], 
                '''                The type of local peer identity.  The local peer
                may be identified by:
                1. an IP address, or
                2. a host name.
                ''',
                'cikepeerlocaltype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePeerLocalValue', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The value of the local peer identity.
                
                If the local peer type is an IP Address, then this
                is the IP Address used to identify the local peer.
                
                If the local peer type is a host name, then this is
                the host name used to identify the local peer.
                ''',
                'cikepeerlocalvalue',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePeerRemoteType', REFERENCE_ENUM_CLASS, 'IkePeerType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkePeerType_Enum', 
                [], [], 
                '''                The type of remote peer identity.  The remote peer
                may be identified by:
                1. an IP address, or
                2. a host name.
                ''',
                'cikepeerremotetype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePeerRemoteValue', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The value of the remote peer identity.
                
                If the remote peer type is an IP Address, then this
                is the IP Address used to identify the remote peer.
                
                If the remote peer type is a host name, then this is
                the host name used to identify the remote peer.
                ''',
                'cikepeerremotevalue',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePeerActiveTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The length of time that the peer association has
                existed in hundredths of a second.
                ''',
                'cikepeeractivetime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePeerActiveTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the active IPsec Phase-1 IKE Tunnel
                (cikeTunIndex in the cikeTunnelTable) for this peer
                association.  If an IPsec Phase-1 IKE Tunnel is
                not currently active, then the value of this
                object will be zero.
                ''',
                'cikepeeractivetunnelindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePeerLocalAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the local peer.
                ''',
                'cikepeerlocaladdr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePeerRemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the remote peer.
                ''',
                'cikepeerremoteaddr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikePeerEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikePeerTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikePeerTable',
            False, 
            [
            _MetaInfoClassMember('cikePeerEntry', REFERENCE_LIST, 'CikePeerEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikePeerTable.CikePeerEntry', 
                [], [], 
                '''                Each entry contains the attributes associated
                with an IPsec Phase-1 IKE peer association.
                ''',
                'cikepeerentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikePeerTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable.CikePhase1GWStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable.CikePhase1GWStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cmgwIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'cmgwindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikePhase1GWActiveTunnels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of currently active IPsec
                Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwactivetunnels',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of authentications which ended
                in failure by all current and previous IPsec Phase-1
                IKE Tunnels.
                ''',
                'cikephase1gwauthfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWDecryptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of decryptions which ended
                in failure by all current and previous IPsec Phase-1
                IKE Tunnels.
                ''',
                'cikephase1gwdecryptfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWHashValidFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of hash validations which ended
                in failure by all current and previous IPsec Phase-1
                IKE Tunnels.
                ''',
                'cikephase1gwhashvalidfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWInDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets which were
                dropped during receive processing by all 
                currently and previously
                active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwindroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWInitTunnelFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-1 IKE Tunnels
                which were locally initiated and failed to activate.
                ''',
                'cikephase1gwinittunnelfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWInitTunnels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-1 IKE
                Tunnels which were locally initiated.
                ''',
                'cikephase1gwinittunnels',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWInNotifys', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of notifys received by
                all currently and previously active IPsec 
                Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwinnotifys',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets received by all currently
                and previously active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwinoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWInP2ExchgInvalids', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                which were received and found to be invalid 
                by all currently and previously active IPsec 
                Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwinp2exchginvalids',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWInP2ExchgRejects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                which were received and rejected by all 
                currently and previously active IPsec Phase-1 
                IKE Tunnels.
                ''',
                'cikephase1gwinp2exchgrejects',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWInP2Exchgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                received by all currently and previously 
                active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwinp2exchgs',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWInP2SaDelRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 'Security
                Association' delete requests received by all 
                currently and previously active and IPsec 
                Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwinp2sadelrequests',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received by all
                currently and previously active IPsec 
                Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwinpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWNoSaFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of non-existent 'Security Association'
                failures occurred during processing of current and 
                previous IPsec Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwnosafails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWOutDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets which were dropped
                during send processing by all currently 
                and previously
                active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwoutdroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWOutNotifys', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of notifys sent by all currently
                and previously active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwoutnotifys',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets sent by all currently
                and previously active and IPsec Phase-1 
                IKE Tunnels.
                ''',
                'cikephase1gwoutoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWOutP2ExchgInvalids', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                which were sent and found to be invalid by 
                all currently and previously active IPsec Phase-1 
                Tunnels.
                ''',
                'cikephase1gwoutp2exchginvalids',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWOutP2ExchgRejects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                which were sent and rejected by all currently and
                previously active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwoutp2exchgrejects',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWOutP2Exchgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                which were sent by all currently and previously 
                active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwoutp2exchgs',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWOutP2SaDelRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 SA
                delete requests sent by all currently and 
                previously active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwoutp2sadelrequests',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets sent by all currently
                and previously active and IPsec Phase-1 
                Tunnels.
                ''',
                'cikephase1gwoutpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWPreviousTunnels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of previously active
                IPsec Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwprevioustunnels',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWRespTunnelFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-1 IKE Tunnels
                which were remotely initiated and failed to activate.
                ''',
                'cikephase1gwresptunnelfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWSysCapFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of system capacity failures
                which occurred during processing of all current 
                and previously active IPsec Phase-1 IKE Tunnels.
                ''',
                'cikephase1gwsyscapfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikePhase1GWStatsEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable',
            False, 
            [
            _MetaInfoClassMember('cikePhase1GWStatsEntry', REFERENCE_LIST, 'CikePhase1GWStatsEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable.CikePhase1GWStatsEntry', 
                [], [], 
                '''                Each entry contains the attributes of an Phase-1 IKE stats
                information for the related gateway.
                
                There is only one entry for each gateway. The entry 
                is created when a gateway up and cannot be deleted.
                ''',
                'cikephase1gwstatsentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikePhase1GWStatsTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable.CikeTunnelHistEntry.CikeTunHistTermReason_Enum' : _MetaInfoEnum('CikeTunHistTermReason_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'other':'OTHER',
            'normal':'NORMAL',
            'operRequest':'OPERREQUEST',
            'peerDelRequest':'PEERDELREQUEST',
            'peerLost':'PEERLOST',
            'localFailure':'LOCALFAILURE',
            'checkPointReg':'CHECKPOINTREG',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable.CikeTunnelHistEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable.CikeTunnelHistEntry',
            False, 
            [
            _MetaInfoClassMember('cikeTunHistIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the IPsec Phase-1 IKE Tunnel History
                Table.  The value of the index is a number which 
                begins at one and is incremented with each 
                tunnel that ends. The value of this object 
                will wrap at 2,147,483,647.
                ''',
                'ciketunhistindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikeTunHistActiveIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the previously active IPsec
                Phase-1 IKE Tunnel.
                ''',
                'ciketunhistactiveindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistActiveTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The length of time the IPsec Phase-1 IKE tunnel was been
                active in hundredths of seconds.
                ''',
                'ciketunhistactivetime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistAuthMethod', REFERENCE_ENUM_CLASS, 'IkeAuthMethod_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkeAuthMethod_Enum', 
                [], [], 
                '''                The authentication method used in IPsec Phase-1 IKE
                negotiations.
                ''',
                'ciketunhistauthmethod',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistDiffHellmanGrp', REFERENCE_ENUM_CLASS, 'DiffHellmanGrp_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'DiffHellmanGrp_Enum', 
                [], [], 
                '''                The Diffie Hellman Group used in IPsec Phase-1 IKE
                negotiations.
                ''',
                'ciketunhistdiffhellmangrp',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistEncryptAlgo', REFERENCE_ENUM_CLASS, 'EncryptAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EncryptAlgo_Enum', 
                [], [], 
                '''                The encryption algorithm used in IPsec Phase-1 IKE
                negotiations.
                ''',
                'ciketunhistencryptalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistHashAlgo', REFERENCE_ENUM_CLASS, 'IkeHashAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkeHashAlgo_Enum', 
                [], [], 
                '''                The hash algorithm used in IPsec Phase-1 IKE
                negotiations.
                ''',
                'ciketunhisthashalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistInDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped
                by this IPsec Phase-1
                 IKE Tunnel during receive processing.
                ''',
                'ciketunhistindroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistInNotifys', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of notifys received
                by this IPsec Phase-1
                 IKE Tunnel.
                ''',
                'ciketunhistinnotifys',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets
                received by this IPsec Phase-1
                 IKE Tunnel.
                ''',
                'ciketunhistinoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistInP2ExchgInvalids', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2
                exchanges received and
                 found to be invalid by this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunhistinp2exchginvalids',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistInP2ExchgRejects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2
                exchanges received and
                 rejected by this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunhistinp2exchgrejects',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistInP2Exchgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2
                exchanges received by
                 this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunhistinp2exchgs',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistInP2SaDelRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 security association
                delete requests received by this IPsec 
                Phase-1 IKE Tunnel.
                ''',
                'ciketunhistinp2sadelrequests',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received
                by this IPsec Phase-1
                 IKE Tunnel.
                ''',
                'ciketunhistinpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistLifeTime', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The negotiated LifeTime of the IPsec Phase-1 IKE Tunnel
                in seconds.
                ''',
                'ciketunhistlifetime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistLocalAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the local endpoint for the IPsec
                Phase-1 IKE Tunnel.
                ''',
                'ciketunhistlocaladdr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistLocalName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The DNS name of the local IP address for
                the IPsec Phase-1 IKE Tunnel. If the DNS 
                name associated with the local tunnel endpoint 
                is not known, then the value of this
                 object will be a NULL string.
                ''',
                'ciketunhistlocalname',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistNegoMode', REFERENCE_ENUM_CLASS, 'IkeNegoMode_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkeNegoMode_Enum', 
                [], [], 
                '''                The negotiation mode of the IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunhistnegomode',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistOutDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped
                by this IPsec Phase-1
                 IKE Tunnel during send processing.
                ''',
                'ciketunhistoutdroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistOutNotifys', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of notifys sent by this IPsec Phase-1
                IKE Tunnel.
                ''',
                'ciketunhistoutnotifys',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets sent by this IPsec Phase-1
                IKE Tunnel.
                ''',
                'ciketunhistoutoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistOutP2ExchgInvalids', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges sent and
                found to be invalid by this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunhistoutp2exchginvalids',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistOutP2ExchgRejects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges sent and
                rejected by this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunhistoutp2exchgrejects',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistOutP2Exchgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges sent by
                this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunhistoutp2exchgs',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistOutP2SaDelRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 security association
                delete requests sent by this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunhistoutp2sadelrequests',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets sent by this IPsec Phase-1
                IKE Tunnel.
                ''',
                'ciketunhistoutpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistPeerIntIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The internal index of the local-remote peer
                association.  This internal index is used to 
                uniquely identify multiple associations between 
                the local and remote peer.
                ''',
                'ciketunhistpeerintindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistPeerLocalType', REFERENCE_ENUM_CLASS, 'IkePeerType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkePeerType_Enum', 
                [], [], 
                '''                The type of local peer identity.  The local peer
                may be identified by:
                 1. an IP address, or
                 2. a host name.
                ''',
                'ciketunhistpeerlocaltype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistPeerLocalValue', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The value of the local peer identity.
                
                If the local peer type is an IP Address, then this
                is the IP Address used to identify the local peer.
                
                If the local peer type is a host name, then this is
                the host name used to identify the local peer.
                ''',
                'ciketunhistpeerlocalvalue',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistPeerRemoteType', REFERENCE_ENUM_CLASS, 'IkePeerType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkePeerType_Enum', 
                [], [], 
                '''                The type of remote peer identity.  The remote
                peer may be identified by:
                 1. an IP address, or
                 2. a host name.
                ''',
                'ciketunhistpeerremotetype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistPeerRemoteValue', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The value of the remote peer identity.
                
                If the remote peer type is an IP Address, then this
                is the IP Address used to identify the remote peer.
                
                If the remote peer type is a host name, then this is
                the host name used to identify the remote peer.
                ''',
                'ciketunhistpeerremotevalue',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistRemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the remote endpoint for the IPsec
                Phase-1 IKE Tunnel.
                ''',
                'ciketunhistremoteaddr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistRemoteName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The DNS name of the remote IP address of IPsec Phase-1
                IKE Tunnel. If the DNS name associated with the remote
                tunnel endpoint is not known, then the value of this
                object will be a NULL string.
                ''',
                'ciketunhistremotename',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistStartTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime in hundredths of seconds
                when the IPsec Phase-1 IKE tunnel was started.
                ''',
                'ciketunhiststarttime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistTermReason', REFERENCE_ENUM_CLASS, 'CikeTunHistTermReason_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable.CikeTunnelHistEntry.CikeTunHistTermReason_Enum', 
                [], [], 
                '''                The reason the IPsec Phase-1 IKE Tunnel was terminated.
                Possible reasons include:
                1 = other
                2 = normal termination
                3 = operator request
                4 = peer delete request was received
                5 = contact with peer was lost
                6 = local failure occurred.
                7 = operator initiated check point request
                ''',
                'ciketunhisttermreason',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistTotalRefreshes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of security associations
                refreshes performed.
                ''',
                'ciketunhisttotalrefreshes',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHistTotalSas', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of security associations
                used during the
                 life of the IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunhisttotalsas',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikeTunnelHistEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable',
            False, 
            [
            _MetaInfoClassMember('cikeTunnelHistEntry', REFERENCE_LIST, 'CikeTunnelHistEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable.CikeTunnelHistEntry', 
                [], [], 
                '''                Each entry contains the attributes
                associated with a previously active IPsec 
                Phase-1 IKE Tunnel.
                ''',
                'ciketunnelhistentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikeTunnelHistTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikeTunnelTable.CikeTunnelEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikeTunnelTable.CikeTunnelEntry',
            False, 
            [
            _MetaInfoClassMember('cikeTunIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the IPsec Phase-1 IKE Tunnel Table.
                The value of the index is a number which begins 
                at one and is incremented with each tunnel that 
                is created. The value of this object will 
                wrap at 2,147,483,647.
                ''',
                'ciketunindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cikeTunActiveTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The length of time the IPsec Phase-1 IKE tunnel has been
                active in hundredths of seconds.
                ''',
                'ciketunactivetime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunAuthMethod', REFERENCE_ENUM_CLASS, 'IkeAuthMethod_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkeAuthMethod_Enum', 
                [], [], 
                '''                The authentication method used in IPsec Phase-1 IKE
                negotiations.
                ''',
                'ciketunauthmethod',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunDiffHellmanGrp', REFERENCE_ENUM_CLASS, 'DiffHellmanGrp_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'DiffHellmanGrp_Enum', 
                [], [], 
                '''                The Diffie Hellman Group used in IPsec Phase-1 IKE
                negotiations.
                ''',
                'ciketundiffhellmangrp',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunEncryptAlgo', REFERENCE_ENUM_CLASS, 'EncryptAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EncryptAlgo_Enum', 
                [], [], 
                '''                The encryption algorithm used in IPsec Phase-1 IKE
                negotiations.
                ''',
                'ciketunencryptalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunHashAlgo', REFERENCE_ENUM_CLASS, 'IkeHashAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkeHashAlgo_Enum', 
                [], [], 
                '''                The hash algorithm used in IPsec Phase-1 IKE
                negotiations.
                ''',
                'ciketunhashalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunInDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped
                by this IPsec Phase-1 IKE Tunnel during 
                receive processing.
                ''',
                'ciketunindroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunInNotifys', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of notifys received by
                this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketuninnotifys',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets received by
                this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketuninoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunInP2ExchgInvalids', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2
                exchanges received and found to be invalid 
                by this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketuninp2exchginvalids',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunInP2ExchgRejects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges
                received and rejected by this IPsec Phase-1 
                Tunnel.
                ''',
                'ciketuninp2exchgrejects',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunInP2Exchgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2
                exchanges received by
                 this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketuninp2exchgs',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunInP2SaDelRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2
                security association delete requests received 
                by this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketuninp2sadelrequests',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received by
                this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketuninpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunLifeTime', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The negotiated LifeTime of the IPsec Phase-1 IKE Tunnel
                in seconds.
                ''',
                'ciketunlifetime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunLocalAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the local endpoint for the IPsec
                Phase-1 IKE Tunnel.
                ''',
                'ciketunlocaladdr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunLocalName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The DNS name of the local IP address for
                the IPsec Phase-1 IKE Tunnel. If the DNS 
                name associated with the local tunnel endpoint 
                is not known, then the value of this
                 object will be a NULL string.
                ''',
                'ciketunlocalname',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunLocalType', REFERENCE_ENUM_CLASS, 'IkePeerType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkePeerType_Enum', 
                [], [], 
                '''                The type of local peer identity.  The local
                peer may be identified by:
                 1. an IP address, or
                 2. a host name.
                ''',
                'ciketunlocaltype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunLocalValue', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The value of the local peer identity.
                
                If the local peer type is an IP Address, then this
                is the IP Address used to identify the local peer.
                
                If the local peer type is a host name, then this is
                the host name used to identify the local peer.
                ''',
                'ciketunlocalvalue',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunNegoMode', REFERENCE_ENUM_CLASS, 'IkeNegoMode_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkeNegoMode_Enum', 
                [], [], 
                '''                The negotiation mode of the IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunnegomode',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunOutDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped by this
                IPsec Phase-1 IKE Tunnel during send processing.
                ''',
                'ciketunoutdroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunOutNotifys', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of notifys sent by this
                IPsec Phase-1 Tunnel.
                ''',
                'ciketunoutnotifys',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets sent by this IPsec Phase-1
                IKE Tunnel.
                ''',
                'ciketunoutoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunOutP2ExchgInvalids', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges sent and
                found to be invalid by this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunoutp2exchginvalids',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunOutP2ExchgRejects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges sent and
                rejected by this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunoutp2exchgrejects',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunOutP2Exchgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 exchanges sent by
                this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunoutp2exchgs',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunOutP2SaDelRequests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of IPsec Phase-2 security association
                delete requests sent by this IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunoutp2sadelrequests',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets sent by this IPsec Phase-1
                IKE Tunnel.
                ''',
                'ciketunoutpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunRemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the remote endpoint for the IPsec
                Phase-1 IKE Tunnel.
                ''',
                'ciketunremoteaddr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunRemoteName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The DNS name of the remote IP address of IPsec Phase-1
                IKE Tunnel. If the DNS name associated with the remote
                tunnel endpoint is not known, then the value of this
                object will be a NULL string.
                ''',
                'ciketunremotename',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunRemoteType', REFERENCE_ENUM_CLASS, 'IkePeerType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'IkePeerType_Enum', 
                [], [], 
                '''                The type of remote peer identity.
                The remote peer may be identified by:
                 1. an IP address, or
                 2. a host name.
                ''',
                'ciketunremotetype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunRemoteValue', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The value of the remote peer identity.
                
                If the remote peer type is an IP Address, then this
                is the IP Address used to identify the remote peer.
                
                If the remote peer type is a host name, then 
                this is the host name used to identify the 
                remote peer.
                ''',
                'ciketunremotevalue',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunSaRefreshThreshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The security association refresh threshold in seconds.
                ''',
                'ciketunsarefreshthreshold',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunStatus', REFERENCE_ENUM_CLASS, 'TunnelStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TunnelStatus_Enum', 
                [], [], 
                '''                The status of the MIB table row.
                
                This object can be used to bring the tunnel down 
                by setting value of this object to destroy(2).
                
                This object cannot be used to create 
                a MIB table row.
                ''',
                'ciketunstatus',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunTotalRefreshes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of security associations
                refreshes performed.
                ''',
                'ciketuntotalrefreshes',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikeTunnelEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CikeTunnelTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CikeTunnelTable',
            False, 
            [
            _MetaInfoClassMember('cikeTunnelEntry', REFERENCE_LIST, 'CikeTunnelEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikeTunnelTable.CikeTunnelEntry', 
                [], [], 
                '''                Each entry contains the attributes associated with
                an active IPsec Phase-1 IKE Tunnel.
                ''',
                'ciketunnelentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cikeTunnelTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable.CipSecEndPtHistEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable.CipSecEndPtHistEntry',
            False, 
            [
            _MetaInfoClassMember('cipSecEndPtHistIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The number of the previously active
                Endpoint associated
                 with a IPsec Phase-2 Tunnel Table.  The value 
                 of this index is a number which begins at 
                 one and is incremented with each Endpoint 
                 associated with an IPsec Phase-2 Tunnel.
                 The value of this object will wrap at 2,147,483,647.
                ''',
                'cipsecendpthistindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cipSecEndPtHistActiveIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index  of the previously active Endpoint.
                ''',
                'cipsecendpthistactiveindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistLocalAddr1', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The local Endpoint's first IP address specification.
                
                If the local Endpoint type is single IP address, 
                then this is the value of the IP address.
                
                If the local Endpoint type is IP subnet, then this
                is the value of the subnet.
                
                If the local Endpoint type is IP address range, 
                then this is the value of beginning IP address of 
                the range.
                ''',
                'cipsecendpthistlocaladdr1',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistLocalAddr2', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The local Endpoint's second IP address specification.
                
                If the local Endpoint type is single IP address, 
                then this is the value of the IP address.
                
                If the local Endpoint type is IP subnet, then this
                is the value of the subnet mask.
                
                If the local Endpoint type is IP address range, 
                then this
                is the value of ending IP address of the range.
                ''',
                'cipsecendpthistlocaladdr2',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistLocalName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The DNS name of the local Endpoint.
                ''',
                'cipsecendpthistlocalname',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistLocalPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The port number of the local Endpoint's traffic.
                ''',
                'cipsecendpthistlocalport',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistLocalProtocol', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The protocol number of the local Endpoint's traffic.
                ''',
                'cipsecendpthistlocalprotocol',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistLocalType', REFERENCE_ENUM_CLASS, 'EndPtType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EndPtType_Enum', 
                [], [], 
                '''                The type of identity for the local Endpoint.
                Possible values are:
                1) a single IP address, or
                2) an IP address range, or
                3) an IP subnet.
                ''',
                'cipsecendpthistlocaltype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistRemoteAddr1', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The remote Endpoint's first IP address specification.
                
                If the remote Endpoint type is single IP address, 
                then this
                is the value of the IP address.
                
                If the remote Endpoint type is IP subnet, then this
                is the value of the subnet.
                
                If the remote Endpoint type is IP address range, 
                then this
                is the value of beginning IP address of the range.
                ''',
                'cipsecendpthistremoteaddr1',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistRemoteAddr2', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The remote Endpoint's second IP address specification.
                
                If the remote Endpoint type is single IP address, 
                then this
                is the value of the IP address.
                
                If the remote Endpoint type is IP subnet, then this
                is the value of the subnet mask.
                
                If the remote Endpoint type is IP address range, 
                then this
                is the value of ending IP address of the range.
                ''',
                'cipsecendpthistremoteaddr2',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistRemoteName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The DNS name of the remote Endpoint.
                ''',
                'cipsecendpthistremotename',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistRemotePort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The port number of the remote Endpoint's traffic.
                ''',
                'cipsecendpthistremoteport',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistRemoteProtocol', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The protocol number of the remote Endpoint's traffic.
                ''',
                'cipsecendpthistremoteprotocol',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistRemoteType', REFERENCE_ENUM_CLASS, 'EndPtType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EndPtType_Enum', 
                [], [], 
                '''                The type of identity for the remote Endpoint.
                Possible values are:
                1) a single IP address, or
                2) an IP address range, or
                3) an IP subnet.
                ''',
                'cipsecendpthistremotetype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistTunIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index  of the previously active IPsec
                Phase-2 Tunnel Table.
                ''',
                'cipsecendpthisttunindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecEndPtHistEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable',
            False, 
            [
            _MetaInfoClassMember('cipSecEndPtHistEntry', REFERENCE_LIST, 'CipSecEndPtHistEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable.CipSecEndPtHistEntry', 
                [], [], 
                '''                Each entry contains the attributes associated with
                a previously active IPsec Phase-2 Tunnel Endpoint.
                ''',
                'cipsecendpthistentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecEndPtHistTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable.CipSecEndPtEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable.CipSecEndPtEntry',
            False, 
            [
            _MetaInfoClassMember('cipSecEndPtIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The number of the Endpoint associated with the
                IPsec Phase-2 Tunnel Table.  The value of this
                index is a number which begins at one and 
                is incremented with each Endpoint associated 
                with an IPsec Phase-2 Tunnel.
                The value of this object will wrap at 2,147,483,647.
                ''',
                'cipsecendptindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cipSecTunIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'cipsectunindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cipSecEndPtLocalAddr1', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The local Endpoint's first IP address specification.
                
                If the local Endpoint type is single IP address, 
                then this is the value of the IP address.
                
                If the local Endpoint type is IP subnet, then this
                is the value of the subnet.
                
                If the local Endpoint type is IP address range, 
                then this is the value of beginning IP address 
                of the range.
                ''',
                'cipsecendptlocaladdr1',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtLocalAddr2', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The local Endpoint's second IP address specification.
                
                If the local Endpoint type is single IP address, 
                then this is the value of the IP address.
                
                If the local Endpoint type is IP subnet, then this
                is the value of the subnet mask.
                
                If the local Endpoint type is IP address range, 
                then this is the value of ending IP address 
                of the range.
                ''',
                'cipsecendptlocaladdr2',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtLocalName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The DNS name of the local Endpoint.
                ''',
                'cipsecendptlocalname',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtLocalPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The port number of the local Endpoint's traffic.
                ''',
                'cipsecendptlocalport',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtLocalProtocol', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The protocol number of the local Endpoint's traffic.
                ''',
                'cipsecendptlocalprotocol',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtLocalType', REFERENCE_ENUM_CLASS, 'EndPtType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EndPtType_Enum', 
                [], [], 
                '''                The type of identity for the local Endpoint.
                Possible values are:
                1) a single IP address, or
                2) an IP address range, or
                3) an IP subnet.
                ''',
                'cipsecendptlocaltype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtRemoteAddr1', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The remote Endpoint's first IP address specification.
                
                If the remote Endpoint type is single IP address, 
                then this is the value of the IP address.
                
                If the remote Endpoint type is IP subnet, then this
                is the value of the subnet.
                
                If the remote Endpoint type is IP address range, 
                then this is the value of beginning IP address 
                of the range.
                ''',
                'cipsecendptremoteaddr1',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtRemoteAddr2', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The remote Endpoint's second IP address specification.
                
                If the remote Endpoint type is single IP address, 
                then this is the value of the IP address.
                
                If the remote Endpoint type is IP subnet, then this
                is the value of the subnet mask.
                
                If the remote Endpoint type is IP address range, 
                then this is the value of ending IP address of 
                the range.
                ''',
                'cipsecendptremoteaddr2',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtRemoteName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The DNS name of the remote Endpoint.
                ''',
                'cipsecendptremotename',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtRemotePort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The port number of the remote Endpoint's traffic.
                ''',
                'cipsecendptremoteport',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtRemoteProtocol', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The protocol number of the remote Endpoint's traffic.
                ''',
                'cipsecendptremoteprotocol',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtRemoteType', REFERENCE_ENUM_CLASS, 'EndPtType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EndPtType_Enum', 
                [], [], 
                '''                The type of identity for the remote Endpoint.
                Possible values are:
                1) a single IP address, or
                2) an IP address range, or
                3) an IP subnet.
                ''',
                'cipsecendptremotetype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecEndPtEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable',
            False, 
            [
            _MetaInfoClassMember('cipSecEndPtEntry', REFERENCE_LIST, 'CipSecEndPtEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable.CipSecEndPtEntry', 
                [], [], 
                '''                An IPsec Phase-2 Tunnel Endpoint entry.
                ''',
                'cipsecendptentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecEndPtTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecFailGlobalCntl' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecFailGlobalCntl',
            False, 
            [
            _MetaInfoClassMember('cipSecFailTableSize', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The window size of the IPsec Phase-1 and Phase-2
                Failure Tables.
                
                The IPsec Phase-1 and Phase-2 Failure Tables are
                implemented as a sliding window in which only the
                last n entries are maintained.  This object is used
                specify the number of entries which will be 
                maintained in the IPsec Phase-1 and Phase-2 Failure 
                Tables.
                
                An implementation may choose suitable minimum and 
                maximum values for this element based on the local 
                policy and available resources. If an SNMP SET request 
                specifies a value outside this window for this element, 
                a BAD VALUE may be returned.
                ''',
                'cipsecfailtablesize',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecFailGlobalCntl',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecFailTable.CipSecFailEntry.CipSecFailReason_Enum' : _MetaInfoEnum('CipSecFailReason_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'other':'OTHER',
            'internalError':'INTERNALERROR',
            'peerEncodingError':'PEERENCODINGERROR',
            'proposalFailure':'PROPOSALFAILURE',
            'protocolUseFail':'PROTOCOLUSEFAIL',
            'nonExistentSa':'NONEXISTENTSA',
            'decryptFailure':'DECRYPTFAILURE',
            'encryptFailure':'ENCRYPTFAILURE',
            'inAuthFailure':'INAUTHFAILURE',
            'outAuthFailure':'OUTAUTHFAILURE',
            'compression':'COMPRESSION',
            'sysCapExceeded':'SYSCAPEXCEEDED',
            'peerDelRequest':'PEERDELREQUEST',
            'peerLost':'PEERLOST',
            'seqNumRollOver':'SEQNUMROLLOVER',
            'operRequest':'OPERREQUEST',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'CISCOIPSECFLOWMONITORMIB.CipSecFailTable.CipSecFailEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecFailTable.CipSecFailEntry',
            False, 
            [
            _MetaInfoClassMember('cipSecFailIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The IPsec Phase-2 Failure Table index.
                The value of the index is a number which 
                begins at one and is incremented with each 
                IPsec Phase-1 failure. The value
                of this object will wrap at 2,147,483,647.
                ''',
                'cipsecfailindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cipSecFailPktDstAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The packet's destination IP address.
                ''',
                'cipsecfailpktdstaddr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecFailPktSrcAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The packet's source IP address.
                ''',
                'cipsecfailpktsrcaddr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecFailReason', REFERENCE_ENUM_CLASS, 'CipSecFailReason_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecFailTable.CipSecFailEntry.CipSecFailReason_Enum', 
                [], [], 
                '''                The reason for the failure.  Possible reasons
                include:
                  1 = other
                  2 = internal error occurred
                  3 = peer encoding error
                  4 = proposal failure
                  5 = protocol use failure
                  6 = non-existent security association
                  7 = decryption failure
                  8 = encryption failure
                  9 = inbound authentication failure
                 10 = outbound authentication failure
                 11 = compression failure
                 12 = system capacity failure
                 13 = peer delete request was received
                 14 = contact with peer was lost
                 15 = sequence number rolled over
                 16 = operator requested termination.
                ''',
                'cipsecfailreason',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecFailSaSpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The security association SPI value.
                ''',
                'cipsecfailsaspi',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecFailTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime in hundredths of seconds
                at the time of the failure.
                ''',
                'cipsecfailtime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecFailTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The Phase-2 Tunnel index (cipSecTunIndex).
                ''',
                'cipsecfailtunnelindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecFailEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecFailTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecFailTable',
            False, 
            [
            _MetaInfoClassMember('cipSecFailEntry', REFERENCE_LIST, 'CipSecFailEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecFailTable.CipSecFailEntry', 
                [], [], 
                '''                Each entry contains the attributes associated with
                an IPsec Phase-1 failure.
                ''',
                'cipsecfailentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecFailTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecGlobalStats' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecGlobalStats',
            False, 
            [
            _MetaInfoClassMember('cipSecGlobalActiveTunnels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of currently active
                IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobalactivetunnels',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalHcInDecompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total number
                of decompressed octets received by all current 
                and previous IPsec Phase-2 Tunnels.  This value 
                is accumulated AFTER the packet is decompressed.
                 If compression is not being used, this value 
                 will match the value of cipSecGlobalHcInOctets.
                ''',
                'cipsecglobalhcindecompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalHcInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total number of
                octets received by all current and previous
                IPsec Phase-2 Tunnels. This value is accumulated
                BEFORE determining whether or not the packet
                should be decompressed.
                ''',
                'cipsecglobalhcinoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalHcOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total number
                of octets sent by all current and previous 
                IPsec Phase-2 Tunnels.  This value is accumulated 
                AFTER determining whether or not the packet should 
                be compressed.
                ''',
                'cipsecglobalhcoutoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalHcOutUncompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total number of
                uncompressed octets sent by all current and previous 
                IPsec Phase-2 Tunnels.  This value is accumulated 
                BEFORE the packet is compressed.  If compression is 
                not being used, this value will match the
                      value of cipSecGlobalHcOutOctets.
                ''',
                'cipsecglobalhcoutuncompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalInAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound authentication's
                which ended in failure by all current and previous 
                IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobalinauthfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalInAuths', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound authentication's
                performed by all current and previous IPsec 
                Phase-2 Tunnels.
                ''',
                'cipsecglobalinauths',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalInDecompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of decompressed octets received
                by all current and previous IPsec Phase-2 Tunnels.  
                This value is accumulated AFTER the packet is 
                decompressed. If compression is not being used, 
                this value will match the value of cipSecGlobalInOctets. 
                See also cipSecGlobalInDecompOctWraps
                 for the number of times this counter has wrapped.
                ''',
                'cipsecglobalindecompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalInDecompOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the global decompressed
                octets received counter
                 (cipSecGlobalInDecompOctets) has wrapped.
                ''',
                'cipsecglobalindecompoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalInDecryptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound decryption's
                which ended in failure by all current and 
                previous IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobalindecryptfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalInDecrypts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound decryption's
                performed by all current and previous IPsec 
                Phase-2 Tunnels.
                ''',
                'cipsecglobalindecrypts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalInDrops', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped
                during receive processing by all current and previous 
                IPsec Phase-2 Tunnels. This count does
                NOT include packets dropped due to 
                Anti-Replay processing.
                ''',
                'cipsecglobalindrops',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets received by all
                current and previous IPsec Phase-2 Tunnels. 
                This value is
                accumulated BEFORE determining whether or not
                the packet should be decompressed. See also
                cipSecGlobalInOctWraps for the number of times
                this counter has wrapped.
                ''',
                'cipsecglobalinoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalInOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the global octets received
                counter (cipSecGlobalInOctets) has wrapped.
                ''',
                'cipsecglobalinoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received
                by all current and previous
                 IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobalinpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalInReplayDrops', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped during
                receive processing due to Anti-Replay 
                processing by all current and previous IPsec
                 Phase-2 Tunnels.
                ''',
                'cipsecglobalinreplaydrops',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalNoSaFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of non-existent
                Security Association in failures which occurred 
                during processing of all current
                 and previous IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobalnosafails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalOutAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound authentication's
                which ended in failure
                 by all current and previous IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobaloutauthfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalOutAuths', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound authentication's
                performed by all current and previous IPsec 
                Phase-2 Tunnels.
                ''',
                'cipsecglobaloutauths',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalOutDrops', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped during send
                processing by all current and previous IPsec 
                Phase-2 Tunnels.
                ''',
                'cipsecglobaloutdrops',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalOutEncryptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound encryption's
                which ended in failure by all current and 
                previous IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobaloutencryptfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalOutEncrypts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound encryption's performed
                by all current and previous IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobaloutencrypts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets sent by all
                current and previous IPsec Phase-2 Tunnels.  
                This value is accumulated AFTER determining 
                whether or not the packet should be compressed.  
                See also cipSecGlobalOutOctWraps for the
                 number of times this counter has wrapped.
                ''',
                'cipsecglobaloutoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalOutOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the global octets sent counter
                (cipSecGlobalOutOctets) has wrapped.
                ''',
                'cipsecglobaloutoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets sent by all
                current and previous
                 IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobaloutpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalOutUncompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of uncompressed octets sent
                by all current and previous IPsec Phase-2 Tunnels.  
                This value is accumulated BEFORE the packet is 
                compressed. If compression is not being used, this 
                value will match the value of cipSecGlobalOutOctets. 
                See also cipSecGlobalOutDecompOctWraps for the number 
                of times this counter has wrapped.
                ''',
                'cipsecglobaloutuncompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalOutUncompOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the global uncompressed
                octets sent counter (cipSecGlobalOutUncompOctets) 
                has wrapped.
                ''',
                'cipsecglobaloutuncompoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalPreviousTunnels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of previously active
                IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobalprevioustunnels',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalProtocolUseFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of protocol use failures
                which occurred during processing of all current 
                and previously active IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobalprotocolusefails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalSysCapFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of system capacity failures
                which occurred during processing of all current 
                and previously active IPsec Phase-2 Tunnels.
                ''',
                'cipsecglobalsyscapfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecGlobalStats',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecHistGlobalCntl.CipSecHistCheckPoint_Enum' : _MetaInfoEnum('CipSecHistCheckPoint_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'ready':'READY',
            'checkPoint':'CHECKPOINT',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'CISCOIPSECFLOWMONITORMIB.CipSecHistGlobalCntl' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecHistGlobalCntl',
            False, 
            [
            _MetaInfoClassMember('cipSecHistCheckPoint', REFERENCE_ENUM_CLASS, 'CipSecHistCheckPoint_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecHistGlobalCntl.CipSecHistCheckPoint_Enum', 
                [], [], 
                '''                The current state of check point processing.
                
                This object will return ready when the agent is 
                ready to create on-demand history entries for 
                active IPsec Tunnels or checkPoint when the 
                agent is currently creating on-demand history 
                entries for active IPsec Tunnels.
                
                By setting this value to checkPoint, the agent 
                will create:
                a) an entry in the IPsec Phase-1 Tunnel History 
                   for each active IPsec Phase-1 Tunnel and
                b) an entry in the IPsec Phase-2 Tunnel History 
                   Table and an entry in the IPsec Phase-2 
                   Tunnel EndPoint History Table
                   for each active IPsec Phase-2 Tunnel.
                ''',
                'cipsechistcheckpoint',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecHistTableSize', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The window size of the IPsec Phase-1 and Phase-2
                History Tables.
                
                The IPsec Phase-1 and Phase-2 History Tables are
                implemented as a sliding window in which only the
                last n entries are maintained.  This object is used
                specify the number of entries which will be 
                maintained in the IPsec Phase-1 and 
                Phase-2 History Tables.
                
                An implementation may choose suitable minimum and 
                maximum values for this element based on the local 
                policy and available resources. If an SNMP SET request 
                specifies a value outside this window for this element, 
                a BAD VALUE may be returned.
                ''',
                'cipsechisttablesize',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecHistGlobalCntl',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecLevels' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecLevels',
            False, 
            [
            _MetaInfoClassMember('cipSecMibLevel', ATTRIBUTE, 'int' , None, None, 
                [(1, 4096)], [], 
                '''                The level of the IPsec MIB.
                ''',
                'cipsecmiblevel',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecLevels',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable.CipSecPhase2GWStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable.CipSecPhase2GWStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cmgwIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'cmgwindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cipSecPhase2GWActiveTunnels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of currently active
                IPsec Phase-2 Tunnels.
                ''',
                'cipsecphase2gwactivetunnels',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWInAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound authentication's
                which ended in failure by all current and previous 
                IPsec Phase-2 Tunnels.
                ''',
                'cipsecphase2gwinauthfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWInAuths', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound authentication's
                performed by all current and previous IPsec 
                Phase-2 Tunnels.
                ''',
                'cipsecphase2gwinauths',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWInDecompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of decompressed octets received
                by all current and previous IPsec Phase-2 Tunnels.  
                This value is accumulated AFTER the packet is 
                decompressed. If compression is not being used, 
                this value will match the value of cipSecGlobalInOctets. 
                See also cipSecGlobalInDecompOctWraps
                for the number of times this counter has wrapped.
                ''',
                'cipsecphase2gwindecompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWInDecompOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the global decompressed
                octets received counter (cipSecGlobalInDecompOctets) 
                has wrapped.
                ''',
                'cipsecphase2gwindecompoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWInDecryptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound decryption's
                which ended in failure by all current and 
                previous IPsec Phase-2 Tunnels.
                ''',
                'cipsecphase2gwindecryptfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWInDecrypts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound decryption's
                performed by all current and previous IPsec 
                Phase-2 Tunnels.
                ''',
                'cipsecphase2gwindecrypts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWInDrops', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped
                during receive processing by all current and previous 
                IPsec Phase-2 Tunnels. This count does NOT include 
                packets dropped due to Anti-Replay processing.
                ''',
                'cipsecphase2gwindrops',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets received by all
                current and previous IPsec Phase-2 Tunnels. 
                This value is accumulated BEFORE determining 
                whether or not the packet should be decompressed. 
                See also cipSecGlobalInOctWraps for the number
                of times this counter has wrapped.
                ''',
                'cipsecphase2gwinoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWInOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the global octets received
                counter (cipSecGlobalInOctets) has wrapped.
                ''',
                'cipsecphase2gwinoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received
                by all current and previous IPsec Phase-2 Tunnels.
                ''',
                'cipsecphase2gwinpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWInReplayDrops', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped during
                receive processing due to Anti-Replay 
                processing by all current and previous IPsec
                Phase-2 Tunnels.
                ''',
                'cipsecphase2gwinreplaydrops',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWNoSaFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of non-existent
                Security Association in failures which occurred 
                during processing of all current
                and previous IPsec Phase-2 Tunnels.
                ''',
                'cipsecphase2gwnosafails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWOutAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound authentication's
                which ended in failure
                by all current and previous IPsec Phase-2 Tunnels.
                ''',
                'cipsecphase2gwoutauthfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWOutAuths', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound authentication's
                performed by all current and previous IPsec 
                Phase-2 Tunnels.
                ''',
                'cipsecphase2gwoutauths',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWOutDrops', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped during send
                processing by all current and previous IPsec 
                Phase-2 Tunnels.
                ''',
                'cipsecphase2gwoutdrops',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWOutEncryptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound encryption's
                which ended in failure by all current and 
                previous IPsec Phase-2 Tunnels.
                ''',
                'cipsecphase2gwoutencryptfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWOutEncrypts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound encryption's performed
                by all current and previous IPsec Phase-2 Tunnels.
                ''',
                'cipsecphase2gwoutencrypts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets sent by all
                current and previous IPsec Phase-2 Tunnels.  
                This value is accumulated AFTER determining 
                whether or not the packet should be compressed.  
                See also cipSecGlobalOutOctWraps for the
                number of times this counter has wrapped.
                ''',
                'cipsecphase2gwoutoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWOutOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the global octets sent counter
                (cipSecGlobalOutOctets) has wrapped.
                ''',
                'cipsecphase2gwoutoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets sent by all
                current and previous IPsec Phase-2 
                Tunnels.
                ''',
                'cipsecphase2gwoutpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWOutUncompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of uncompressed octets sent
                by all current and previous IPsec Phase-2 Tunnels.  
                This value is accumulated BEFORE the packet is 
                compressed. If compression is not being used, this 
                value will match the value of cipSecGlobalOutOctets. 
                See also cipSecGlobalOutDecompOctWraps for the number 
                of times this counter has wrapped.
                ''',
                'cipsecphase2gwoutuncompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWOutUncompOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the global uncompressed
                octets sent counter (cipSecGlobalOutUncompOctets) 
                has wrapped.
                ''',
                'cipsecphase2gwoutuncompoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWPreviousTunnels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of previously active
                IPsec Phase-2 Tunnels.
                ''',
                'cipsecphase2gwprevioustunnels',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWProtocolUseFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of protocol use failures
                which occurred during processing of all current 
                and previously active IPsec Phase-2 Tunnels.
                ''',
                'cipsecphase2gwprotocolusefails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWSysCapFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of system capacity failures
                which occurred during processing of all current 
                and previously active IPsec Phase-2 Tunnels.
                ''',
                'cipsecphase2gwsyscapfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecPhase2GWStatsEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable',
            False, 
            [
            _MetaInfoClassMember('cipSecPhase2GWStatsEntry', REFERENCE_LIST, 'CipSecPhase2GWStatsEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable.CipSecPhase2GWStatsEntry', 
                [], [], 
                '''                Each entry contains the attributes of an Phase-2 IPsec stats
                information for the related gateway.
                
                There is only one entry for each gateway. The entry 
                is created when a gateway up and cannot be deleted.
                ''',
                'cipsecphase2gwstatsentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecPhase2GWStatsTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiDirection_Enum' : _MetaInfoEnum('CipSecSpiDirection_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'in':'IN',
            'out':'OUT',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiProtocol_Enum' : _MetaInfoEnum('CipSecSpiProtocol_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'ah':'AH',
            'esp':'ESP',
            'ipcomp':'IPCOMP',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiStatus_Enum' : _MetaInfoEnum('CipSecSpiStatus_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'active':'ACTIVE',
            'expiring':'EXPIRING',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry',
            False, 
            [
            _MetaInfoClassMember('cipSecSpiIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The number of the SPI associated with the
                Phase-2 Tunnel Table.  The value of this 
                index is a number which begins at one and is 
                incremented with each SPI associated with an 
                IPsec Phase-2 Tunnel.  The value of this 
                object will wrap at 2,147,483,647.
                ''',
                'cipsecspiindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cipSecTunIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'cipsectunindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cipSecSpiDirection', REFERENCE_ENUM_CLASS, 'CipSecSpiDirection_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiDirection_Enum', 
                [], [], 
                '''                The direction of the SPI.
                ''',
                'cipsecspidirection',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecSpiProtocol', REFERENCE_ENUM_CLASS, 'CipSecSpiProtocol_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiProtocol_Enum', 
                [], [], 
                '''                The protocol of the SPI.
                ''',
                'cipsecspiprotocol',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecSpiStatus', REFERENCE_ENUM_CLASS, 'CipSecSpiStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry.CipSecSpiStatus_Enum', 
                [], [], 
                '''                The status of the SPI.
                ''',
                'cipsecspistatus',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecSpiValue', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                The value of the SPI.
                ''',
                'cipsecspivalue',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecSpiEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecSpiTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecSpiTable',
            False, 
            [
            _MetaInfoClassMember('cipSecSpiEntry', REFERENCE_LIST, 'CipSecSpiEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry', 
                [], [], 
                '''                Each entry contains the attributes associated with
                active and expiring IPsec Phase-2 
                security associations.
                ''',
                'cipsecspientry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecSpiTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecTrapCntl' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecTrapCntl',
            False, 
            [
            _MetaInfoClassMember('cipSecTrapCntlIkeCertCrlFailure', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative
                state of sending the
                 IPsec IKE Phase-1 Certificate/CRL Failure TRAP
                ''',
                'cipsectrapcntlikecertcrlfailure',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIkeNoSa', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative
                state of sending the
                 IPsec IKE Phase-1 No Security Association TRAP
                ''',
                'cipsectrapcntlikenosa',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIkeProtocolFail', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative
                state of sending the
                 IPsec IKE Phase-1 Protocol Failure TRAP
                ''',
                'cipsectrapcntlikeprotocolfail',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIkeSysFailure', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state
                of sending the
                 IPsec IKE Phase-1 System Failure TRAP
                ''',
                'cipsectrapcntlikesysfailure',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIkeTunnelStart', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state of
                sending the IPsec IKE Phase-1 Tunnel Start TRAP
                ''',
                'cipsectrapcntliketunnelstart',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIkeTunnelStop', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state
                of sending the
                 IPsec IKE Phase-1 Tunnel Stop TRAP
                ''',
                'cipsectrapcntliketunnelstop',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIpSecEarlyTunTerm', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state
                of sending the IPsec
                 Phase-2 Early Tunnel Termination TRAP
                ''',
                'cipsectrapcntlipsecearlytunterm',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIpSecNoSa', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state
                of sending the IPsec
                 Phase-2  No Security Association TRAP
                ''',
                'cipsectrapcntlipsecnosa',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIpSecProtocolFail', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state
                of sending the IPsec
                 Phase-2 Protocol Failure TRAP
                ''',
                'cipsectrapcntlipsecprotocolfail',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIpSecSetUpFailure', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state
                of sending the IPsec
                 Phase-2 Set Up Failure TRAP
                ''',
                'cipsectrapcntlipsecsetupfailure',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIpSecSysFailure', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state
                of sending the IPsec
                 Phase-2 System Failure TRAP
                ''',
                'cipsectrapcntlipsecsysfailure',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIpSecTunnelStart', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state
                of sending the IPsec
                 Phase-2 Tunnel Start TRAP
                ''',
                'cipsectrapcntlipsectunnelstart',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntlIpSecTunnelStop', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative
                state of sending the IPsec
                 Phase-2 Tunnel Stop TRAP
                ''',
                'cipsectrapcntlipsectunnelstop',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecTrapCntl',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable.CipSecTunnelHistEntry.CipSecTunHistTermReason_Enum' : _MetaInfoEnum('CipSecTunHistTermReason_Enum', 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB',
        {
            'other':'OTHER',
            'normal':'NORMAL',
            'operRequest':'OPERREQUEST',
            'peerDelRequest':'PEERDELREQUEST',
            'peerLost':'PEERLOST',
            'seqNumRollOver':'SEQNUMROLLOVER',
            'checkPointReq':'CHECKPOINTREQ',
        }, 'CISCO-IPSEC-FLOW-MONITOR-MIB', _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB']),
    'CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable.CipSecTunnelHistEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable.CipSecTunnelHistEntry',
            False, 
            [
            _MetaInfoClassMember('cipSecTunHistIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the IPsec Phase-2 Tunnel History Table.
                The value of the index is a number which 
                begins at one and is incremented with each tunnel 
                that ends. The value
                of this object will wrap at 2,147,483,647.
                ''',
                'cipsectunhistindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cipSecTunHistActiveIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the previously active
                IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistactiveindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistActiveTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The length of time the IPsec Phase-2 Tunnel has been
                active in hundredths of seconds.
                ''',
                'cipsectunhistactivetime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistEncapMode', REFERENCE_ENUM_CLASS, 'EncapMode_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EncapMode_Enum', 
                [], [], 
                '''                The encapsulation mode used by the
                IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistencapmode',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistHcInDecompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total number of decompressed
                octets received by this IPsec Phase-2 Tunnel.  This value
                is accumulated AFTER the packet is decompressed. If
                compression is not being used, this value will match the
                value of cipSecTunHistHcInOctets.
                ''',
                'cipsectunhisthcindecompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistHcInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total number of octets
                received by this IPsec Phase-2 Tunnel.  This value is
                accumulated BEFORE determining whether or not 
                the packet should be decompressed.
                ''',
                'cipsectunhisthcinoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistHcOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total number of octets
                sent by this IPsec Phase-2 Tunnel.  This value 
                is accumulated AFTER determining whether or not 
                the packet should be
                compressed.
                ''',
                'cipsectunhisthcoutoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistHcOutUncompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total
                number of uncompressed octets sent by this 
                IPsec Phase-2 Tunnel.  This value is accumulated 
                BEFORE the packet is compressed. If compression
                is not being used, this value will match the value of
                cipSecTunHistHcOutOctets.
                ''',
                'cipsectunhisthcoutuncompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistIkeTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the associated IPsec Phase-1 Tunnel
                (cikeTunIndex in the cikeTunnelTable).
                ''',
                'cipsectunhistiketunnelindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound authentication's
                which ended in
                 failure by this IPsec Phase-2 Tunnel .
                ''',
                'cipsectunhistinauthfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInAuths', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound authentication's
                performed
                 by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistinauths',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInDecompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of decompressed octets received by this
                IPsec Phase-2 Tunnel.  This value is accumulated AFTER
                the packet is decompressed. If compression is not being
                used, this value will match the value of cipSecTunHistInOctets.
                See also cipSecTunInDecompOctWraps for the number of times
                this counter has wrapped.
                ''',
                'cipsectunhistindecompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInDecompOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the decompressed octets
                received counter (cipSecTunInDecompOctets) has wrapped.
                ''',
                'cipsectunhistindecompoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInDecryptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound decryption's
                which ended in failure
                 by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistindecryptfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInDecrypts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound decryption's performed
                by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistindecrypts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped during
                receive processing by this IPsec Phase-2 Tunnel. 
                This count does NOT include packets
                 dropped due to Anti-Replay processing.
                ''',
                'cipsectunhistindroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets received by this IPsec
                Phase-2 Tunnel.  This value is accumulated
                BEFORE determining whether or not the packet should 
                be decompressed.  See also cipSecTunInOctWraps for 
                the number of times this counter has wrapped.
                ''',
                'cipsectunhistinoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the octets received counter
                (cipSecTunInOctets) has wrapped.
                ''',
                'cipsectunhistinoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received by this
                IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistinpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInReplayDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped during
                receive processing due to Anti-Replay processing 
                by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistinreplaydroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInSaAhAuthAlgo', REFERENCE_ENUM_CLASS, 'AuthAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'AuthAlgo_Enum', 
                [], [], 
                '''                The authentication algorithm used by the inbound
                authentication header (AH) security association of
                the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistinsaahauthalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInSaDecompAlgo', REFERENCE_ENUM_CLASS, 'CompAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CompAlgo_Enum', 
                [], [], 
                '''                The decompression algorithm used by the inbound
                security association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistinsadecompalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInSaDiffHellmanGrp', REFERENCE_ENUM_CLASS, 'DiffHellmanGrp_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'DiffHellmanGrp_Enum', 
                [], [], 
                '''                The Diffie Hellman Group used by the inbound security
                association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistinsadiffhellmangrp',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInSaEncryptAlgo', REFERENCE_ENUM_CLASS, 'EncryptAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EncryptAlgo_Enum', 
                [], [], 
                '''                The encryption algorithm used by the inbound security
                association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistinsaencryptalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistInSaEspAuthAlgo', REFERENCE_ENUM_CLASS, 'AuthAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'AuthAlgo_Enum', 
                [], [], 
                '''                The authentication algorithm used by the inbound
                encapsulation security protocol (ESP) 
                security association of
                the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistinsaespauthalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistKeyType', REFERENCE_ENUM_CLASS, 'KeyType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'KeyType_Enum', 
                [], [], 
                '''                The type of key used by the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistkeytype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistLifeSize', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The negotiated LifeSize of the IPsec Phase-2 Tunnel in
                kilobytes.
                ''',
                'cipsectunhistlifesize',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistLifeTime', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The negotiated LifeTime of the IPsec Phase-2 Tunnel in
                seconds.
                ''',
                'cipsectunhistlifetime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistLocalAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the local endpoint for the IPsec
                Phase-2 Tunnel.
                ''',
                'cipsectunhistlocaladdr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound authentication's
                which ended in
                 failure by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistoutauthfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutAuths', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound authentication's performed
                by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistoutauths',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped
                during send processing
                 by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistoutdroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutEncryptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound encryption's
                which ended in failure
                 by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistoutencryptfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutEncrypts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound encryption's performed
                by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistoutencrypts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets sent by this IPsec
                Phase-2 Tunnel.  This value is accumulated
                AFTER determining whether or not the 
                packet should be
                compressed.  See also cipSecTunOutOctWraps for the
                number of times this counter has wrapped.
                ''',
                'cipsectunhistoutoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the octets sent counter
                (cipSecTunOutOctets) has wrapped.
                ''',
                'cipsectunhistoutoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets sent by this
                IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistoutpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutSaAhAuthAlgo', REFERENCE_ENUM_CLASS, 'AuthAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'AuthAlgo_Enum', 
                [], [], 
                '''                The authentication algorithm used by the outbound
                authentication header (AH) security association of
                the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistoutsaahauthalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutSaCompAlgo', REFERENCE_ENUM_CLASS, 'CompAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CompAlgo_Enum', 
                [], [], 
                '''                The compression algorithm used by the inbound
                security association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistoutsacompalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutSaDiffHellmanGrp', REFERENCE_ENUM_CLASS, 'DiffHellmanGrp_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'DiffHellmanGrp_Enum', 
                [], [], 
                '''                The Diffie Hellman Group used by the outbound security
                association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistoutsadiffhellmangrp',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutSaEncryptAlgo', REFERENCE_ENUM_CLASS, 'EncryptAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EncryptAlgo_Enum', 
                [], [], 
                '''                The encryption algorithm used by the outbound security
                association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistoutsaencryptalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutSaEspAuthAlgo', REFERENCE_ENUM_CLASS, 'AuthAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'AuthAlgo_Enum', 
                [], [], 
                '''                The authentication algorithm used by the inbound
                encapsulation security protocol (ESP) 
                security association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhistoutsaespauthalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutUncompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of uncompressed octets sent by this
                IPsec Phase-2 Tunnel.  This value is accumulated BEFORE
                the packet is compressed. If compression is not being
                used, this value will match the value of 
                cipSecTunHistOutOctets.  See also 
                cipSecTunOutDecompOctWraps for the number of times
                this counter has wrapped.
                ''',
                'cipsectunhistoutuncompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistOutUncompOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the uncompressed octets sent counter
                (cipSecTunOutUncompOctets) has wrapped.
                ''',
                'cipsectunhistoutuncompoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistRemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the remote endpoint for the IPsec
                Phase-2 Tunnel.
                ''',
                'cipsectunhistremoteaddr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistStartTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime in hundredths of seconds
                when the IPsec Phase-2 Tunnel was started.
                ''',
                'cipsectunhiststarttime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistTermReason', REFERENCE_ENUM_CLASS, 'CipSecTunHistTermReason_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable.CipSecTunnelHistEntry.CipSecTunHistTermReason_Enum', 
                [], [], 
                '''                The reason the IPsec Phase-2 Tunnel was terminated.
                Possible reasons include:
                1 = other
                2 = normal termination
                3 = operator request
                4 = peer delete request was received
                5 = contact with peer was lost
                6 = local failure occurred
                7 = operator initiated check point request
                ''',
                'cipsectunhisttermreason',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistTotalRefreshes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of security association refreshes
                performed.
                ''',
                'cipsectunhisttotalrefreshes',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHistTotalSas', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of security associations used
                during the
                 life of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunhisttotalsas',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecTunnelHistEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable',
            False, 
            [
            _MetaInfoClassMember('cipSecTunnelHistEntry', REFERENCE_LIST, 'CipSecTunnelHistEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable.CipSecTunnelHistEntry', 
                [], [], 
                '''                Each entry contains the attributes associated with
                a previously active IPsec Phase-2 Tunnel.
                ''',
                'cipsectunnelhistentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecTunnelHistTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable.CipSecTunnelEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable.CipSecTunnelEntry',
            False, 
            [
            _MetaInfoClassMember('cipSecTunIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the IPsec Phase-2 Tunnel Table.
                The value of the index is a number which begins 
                at one and is incremented with each tunnel that 
                is created. The value of this object will wrap 
                at 2,147,483,647.
                ''',
                'cipsectunindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', True),
            _MetaInfoClassMember('cipSecTunActiveTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The length of time the IPsec Phase-2
                Tunnel has been
                 active in hundredths of seconds.
                ''',
                'cipsectunactivetime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunCurrentSaInstances', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of security associations
                which are currently active or expiring.
                ''',
                'cipsectuncurrentsainstances',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunEncapMode', REFERENCE_ENUM_CLASS, 'EncapMode_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EncapMode_Enum', 
                [], [], 
                '''                The encapsulation mode used by the
                IPsec Phase-2 Tunnel.
                ''',
                'cipsectunencapmode',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunExpiredSaInstances', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of security associations
                which have expired.
                ''',
                'cipsectunexpiredsainstances',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHcInDecompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total number of decompressed
                octets received by this IPsec Phase-2 Tunnel.  This value
                is accumulated AFTER the packet is decompressed. If
                compression is not being used, this value will match the
                value of cipSecTunHcInOctets.
                ''',
                'cipsectunhcindecompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHcInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total number of octets
                received by this IPsec Phase-2 Tunnel.  This value is
                accumulated BEFORE determining whether or not the packet
                should be decompressed.
                ''',
                'cipsectunhcinoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHcOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total number of octets
                sent by this IPsec Phase-2 Tunnel.  This value is
                accumulated AFTER determining whether or not the 
                packet
                should be compressed.
                ''',
                'cipsectunhcoutoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunHcOutUncompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                A high capacity count of the total number
                of uncompressed octets sent by this IPsec 
                Phase-2 Tunnel.  This value is accumulated BEFORE 
                the packet is compressed. If compression
                 is not being used, this value will match the value
                 of cipSecTunHcOutOctets.
                ''',
                'cipsectunhcoutuncompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunIkeTunnelAlive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indicator which specifies whether or not the
                IPsec Phase-1 IKE Tunnel currently exists.
                ''',
                'cipsectuniketunnelalive',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunIkeTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the associated IPsec Phase-1
                IKE Tunnel.
                 (cikeTunIndex in the cikeTunnelTable)
                ''',
                'cipsectuniketunnelindex',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound authentication's
                which ended in
                 failure by this IPsec Phase-2 Tunnel .
                ''',
                'cipsectuninauthfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInAuths', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound
                authentication's performed by this 
                IPsec Phase-2 Tunnel.
                ''',
                'cipsectuninauths',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInDecompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of decompressed octets received
                by this IPsec Phase-2 Tunnel. This value is 
                accumulated AFTER the packet is decompressed. 
                If compression is not being
                 used, this value will match the value of 
                 cipSecTunInOctets.  See also cipSecTunInDecompOctWraps 
                 for the number of times
                 this counter has wrapped.
                ''',
                'cipsectunindecompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInDecompOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the decompressed
                octets received counter
                 (cipSecTunInDecompOctets) has wrapped.
                ''',
                'cipsectunindecompoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInDecryptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound decryption's
                which ended in failure
                 by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunindecryptfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInDecrypts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of inbound decryption's performed
                by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunindecrypts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped
                during receive processing by this IPsec Phase-2 
                Tunnel. This count does NOT include
                 packets dropped due to Anti-Replay processing.
                ''',
                'cipsectunindroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets received by this IPsec
                Phase-2 Tunnel.  This value is accumulated
                BEFORE determining whether or not the packet should be
                decompressed.  See also cipSecTunInOctWraps for the
                number of times this counter has wrapped.
                ''',
                'cipsectuninoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the octets received counter
                (cipSecTunInOctets) has wrapped.
                ''',
                'cipsectuninoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received
                by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectuninpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInReplayDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped during
                receive processing due to Anti-Replay processing 
                by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectuninreplaydroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInSaAhAuthAlgo', REFERENCE_ENUM_CLASS, 'AuthAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'AuthAlgo_Enum', 
                [], [], 
                '''                The authentication algorithm used by the inbound
                authentication header (AH) security association of
                the IPsec Phase-2 Tunnel.
                ''',
                'cipsectuninsaahauthalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInSaDecompAlgo', REFERENCE_ENUM_CLASS, 'CompAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CompAlgo_Enum', 
                [], [], 
                '''                The decompression algorithm used by the inbound
                security association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectuninsadecompalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInSaDiffHellmanGrp', REFERENCE_ENUM_CLASS, 'DiffHellmanGrp_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'DiffHellmanGrp_Enum', 
                [], [], 
                '''                The Diffie Hellman Group used
                by the inbound security association of the 
                IPsec Phase-2 Tunnel.
                ''',
                'cipsectuninsadiffhellmangrp',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInSaEncryptAlgo', REFERENCE_ENUM_CLASS, 'EncryptAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EncryptAlgo_Enum', 
                [], [], 
                '''                The encryption algorithm used by the inbound security
                association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectuninsaencryptalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunInSaEspAuthAlgo', REFERENCE_ENUM_CLASS, 'AuthAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'AuthAlgo_Enum', 
                [], [], 
                '''                The authentication algorithm used by the inbound
                encapsulation security protocol (ESP) security 
                association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectuninsaespauthalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunKeyType', REFERENCE_ENUM_CLASS, 'KeyType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'KeyType_Enum', 
                [], [], 
                '''                The type of key used by the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunkeytype',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunLifeSize', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The negotiated LifeSize of the
                IPsec Phase-2 Tunnel in kilobytes.
                ''',
                'cipsectunlifesize',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunLifeTime', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The negotiated LifeTime of the
                IPsec Phase-2 Tunnel in seconds.
                ''',
                'cipsectunlifetime',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunLocalAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the local endpoint for the IPsec
                Phase-2 Tunnel.
                ''',
                'cipsectunlocaladdr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound
                authentication's which ended in failure 
                by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunoutauthfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutAuths', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound authentication's performed
                by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunoutauths',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutDropPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets dropped during
                send processing by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunoutdroppkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutEncryptFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound encryption's
                which ended in failure by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunoutencryptfails',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutEncrypts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of outbound encryption's performed
                by this IPsec Phase-2 Tunnel.
                ''',
                'cipsectunoutencrypts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets sent by this IPsec
                Phase-2 Tunnel.  This value is accumulated
                AFTER determining whether or not the packet should 
                be compressed.  See also cipSecTunOutOctWraps for
                the number of times this counter has wrapped.
                ''',
                'cipsectunoutoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the out octets counter
                (cipSecTunOutOctets) has wrapped.
                ''',
                'cipsectunoutoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets sent by this
                IPsec Phase-2 Tunnel.
                ''',
                'cipsectunoutpkts',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutSaAhAuthAlgo', REFERENCE_ENUM_CLASS, 'AuthAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'AuthAlgo_Enum', 
                [], [], 
                '''                The authentication algorithm used by the outbound
                authentication header (AH) security association of
                the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunoutsaahauthalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutSaCompAlgo', REFERENCE_ENUM_CLASS, 'CompAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CompAlgo_Enum', 
                [], [], 
                '''                The compression algorithm used by the inbound
                security association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunoutsacompalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutSaDiffHellmanGrp', REFERENCE_ENUM_CLASS, 'DiffHellmanGrp_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'DiffHellmanGrp_Enum', 
                [], [], 
                '''                The Diffie Hellman Group used by the outbound security
                association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunoutsadiffhellmangrp',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutSaEncryptAlgo', REFERENCE_ENUM_CLASS, 'EncryptAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'EncryptAlgo_Enum', 
                [], [], 
                '''                The encryption algorithm used by the outbound security
                association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunoutsaencryptalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutSaEspAuthAlgo', REFERENCE_ENUM_CLASS, 'AuthAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'AuthAlgo_Enum', 
                [], [], 
                '''                The authentication algorithm used by the inbound
                encapsulation security protocol (ESP) 
                security association of the IPsec Phase-2 Tunnel.
                ''',
                'cipsectunoutsaespauthalgo',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutUncompOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of uncompressed octets sent
                by this IPsec Phase-2 Tunnel.  This value 
                is accumulated BEFORE the packet is compressed. 
                If compression is not being used, this value 
                will match the value of cipSecTunOutOctets.
                 See also cipSecTunOutDecompOctWraps for the 
                 number of times this counter has wrapped.
                ''',
                'cipsectunoutuncompoctets',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunOutUncompOctWraps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the uncompressed octets sent
                counter (cipSecTunOutUncompOctets) has wrapped.
                ''',
                'cipsectunoutuncompoctwraps',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunRemoteAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the remote endpoint for the IPsec
                Phase-2 Tunnel.
                ''',
                'cipsectunremoteaddr',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunSaLifeSizeThreshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The security association LifeSize refresh
                threshold in kilobytes.
                ''',
                'cipsectunsalifesizethreshold',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunSaLifeTimeThreshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The security association LifeTime refresh
                threshold in seconds.
                ''',
                'cipsectunsalifetimethreshold',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunStatus', REFERENCE_ENUM_CLASS, 'TunnelStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'TunnelStatus_Enum', 
                [], [], 
                '''                The status of the MIB table row.
                
                This object can be used to bring the tunnel down
                by setting value of this object to destroy(2).
                When the value is set to destroy(2), the SA
                bundle is destroyed and this row is deleted
                from this table.
                
                When this MIB value is queried, the value of
                active(1) is always returned, if the instance 
                exists.
                
                This object cannot be used to create a MIB 
                table row.
                ''',
                'cipsectunstatus',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunTotalRefreshes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of security
                association refreshes performed.
                ''',
                'cipsectuntotalrefreshes',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecTunnelEntry',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable',
            False, 
            [
            _MetaInfoClassMember('cipSecTunnelEntry', REFERENCE_LIST, 'CipSecTunnelEntry' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable.CipSecTunnelEntry', 
                [], [], 
                '''                Each entry contains the attributes
                associated with an active IPsec Phase-2 Tunnel.
                ''',
                'cipsectunnelentry',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'cipSecTunnelTable',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
    'CISCOIPSECFLOWMONITORMIB' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECFLOWMONITORMIB',
            False, 
            [
            _MetaInfoClassMember('cikeFailTable', REFERENCE_CLASS, 'CikeFailTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikeFailTable', 
                [], [], 
                '''                The IPsec Phase-1 Failure Table.
                This table is implemented as a sliding 
                window in which only the last n entries are 
                maintained.  The maximum number of entries
                is specified by the cipSecFailTableSize object.
                ''',
                'cikefailtable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeGlobalStats', REFERENCE_CLASS, 'CikeGlobalStats' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikeGlobalStats', 
                [], [], 
                '''                ''',
                'cikeglobalstats',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePeerCorrTable', REFERENCE_CLASS, 'CikePeerCorrTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable', 
                [], [], 
                '''                The IPsec Phase-1 Internet Key Exchange Peer
                Association to IPsec Phase-2 Tunnel
                Correlation Table. There is one entry in
                this table for each active IPsec Phase-2
                Tunnel.
                ''',
                'cikepeercorrtable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePeerTable', REFERENCE_CLASS, 'CikePeerTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikePeerTable', 
                [], [], 
                '''                The IPsec Phase-1 Internet Key Exchange Peer Table.
                There is one entry in this table for each IPsec
                Phase-1 IKE peer association which is currently
                associated with an active IPsec Phase-1 Tunnel.
                The IPsec Phase-1 IKE Tunnel associated with this
                IPsec Phase-1 IKE peer association may or may not
                be currently active.
                ''',
                'cikepeertable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikePhase1GWStatsTable', REFERENCE_CLASS, 'CikePhase1GWStatsTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable', 
                [], [], 
                '''                Phase-1 IKE stats information is included in this table.
                Each entry is related to a specific gateway which is 
                identified by 'cmgwIndex'.
                ''',
                'cikephase1gwstatstable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunnelHistTable', REFERENCE_CLASS, 'CikeTunnelHistTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable', 
                [], [], 
                '''                The IPsec Phase-1 Internet Key Exchange Tunnel
                History Table.  This table is implemented as a 
                sliding window in which only the last n entries 
                are maintained.  The maximum number of entries
                 is specified by the cipSecHistTableSize object.
                ''',
                'ciketunnelhisttable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cikeTunnelTable', REFERENCE_CLASS, 'CikeTunnelTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CikeTunnelTable', 
                [], [], 
                '''                The IPsec Phase-1 Internet Key Exchange Tunnel Table.
                There is one entry in this table for each active IPsec
                Phase-1 IKE Tunnel.
                ''',
                'ciketunneltable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtHistTable', REFERENCE_CLASS, 'CipSecEndPtHistTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable', 
                [], [], 
                '''                The IPsec Phase-2 Tunnel Endpoint History Table.
                This table is implemented as a 
                sliding window in which only the
                last n entries are maintained.  
                The maximum number of entries
                is specified by the cipSecHistTableSize object.
                ''',
                'cipsecendpthisttable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecEndPtTable', REFERENCE_CLASS, 'CipSecEndPtTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable', 
                [], [], 
                '''                The IPsec Phase-2 Tunnel Endpoint Table.
                This table contains an entry for each 
                active endpoint associated with an IPsec
                 Phase-2 Tunnel.
                ''',
                'cipsecendpttable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecFailGlobalCntl', REFERENCE_CLASS, 'CipSecFailGlobalCntl' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecFailGlobalCntl', 
                [], [], 
                '''                ''',
                'cipsecfailglobalcntl',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecFailTable', REFERENCE_CLASS, 'CipSecFailTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecFailTable', 
                [], [], 
                '''                The IPsec Phase-2 Failure Table.
                This table is implemented as a sliding window 
                in which only the last n entries are maintained.  
                The maximum number of entries
                is specified by the cipSecFailTableSize object.
                ''',
                'cipsecfailtable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecGlobalStats', REFERENCE_CLASS, 'CipSecGlobalStats' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecGlobalStats', 
                [], [], 
                '''                ''',
                'cipsecglobalstats',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecHistGlobalCntl', REFERENCE_CLASS, 'CipSecHistGlobalCntl' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecHistGlobalCntl', 
                [], [], 
                '''                ''',
                'cipsechistglobalcntl',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecLevels', REFERENCE_CLASS, 'CipSecLevels' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecLevels', 
                [], [], 
                '''                ''',
                'cipseclevels',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecPhase2GWStatsTable', REFERENCE_CLASS, 'CipSecPhase2GWStatsTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable', 
                [], [], 
                '''                Phase-2 IPsec stats information is included in this table.
                Each entry is related to a specific gateway which is 
                identified by 'cmgwIndex'
                ''',
                'cipsecphase2gwstatstable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecSpiTable', REFERENCE_CLASS, 'CipSecSpiTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecSpiTable', 
                [], [], 
                '''                The IPsec Phase-2 Security Protection Index Table.
                This table contains an entry for each active 
                and expiring security
                 association.
                ''',
                'cipsecspitable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTrapCntl', REFERENCE_CLASS, 'CipSecTrapCntl' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecTrapCntl', 
                [], [], 
                '''                ''',
                'cipsectrapcntl',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunnelHistTable', REFERENCE_CLASS, 'CipSecTunnelHistTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable', 
                [], [], 
                '''                The IPsec Phase-2 Tunnel History Table.
                This table is implemented as a sliding 
                window in which only the
                last n entries are maintained.  The maximum number 
                of entries
                is specified by the cipSecHistTableSize object.
                ''',
                'cipsectunnelhisttable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            _MetaInfoClassMember('cipSecTunnelTable', REFERENCE_CLASS, 'CipSecTunnelTable' , 'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB', 'CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable', 
                [], [], 
                '''                The IPsec Phase-2 Tunnel Table.
                There is one entry in this table for 
                each active IPsec Phase-2 Tunnel.
                ''',
                'cipsectunneltable',
                'CISCO-IPSEC-FLOW-MONITOR-MIB', False),
            ],
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            'CISCO-IPSEC-FLOW-MONITOR-MIB',
            _yang_ns._namespaces['CISCO-IPSEC-FLOW-MONITOR-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_FLOW_MONITOR_MIB'
        ),
    },
}
_meta_table['CISCOIPSECFLOWMONITORMIB.CikeFailTable.CikeFailEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CikeFailTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable.CikePeerCorrEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikePeerTable.CikePeerEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CikePeerTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable.CikePhase1GWStatsEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable.CikeTunnelHistEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikeTunnelTable.CikeTunnelEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CikeTunnelTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable.CipSecEndPtHistEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable.CipSecEndPtEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecFailTable.CipSecFailEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecFailTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable.CipSecPhase2GWStatsEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecSpiTable.CipSecSpiEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecSpiTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable.CipSecTunnelHistEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable.CipSecTunnelEntry']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikeFailTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikeGlobalStats']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikePeerCorrTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikePeerTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikePhase1GWStatsTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikeTunnelHistTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CikeTunnelTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecEndPtHistTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecEndPtTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecFailGlobalCntl']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecFailTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecGlobalStats']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecHistGlobalCntl']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecLevels']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecPhase2GWStatsTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecSpiTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTrapCntl']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTunnelHistTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
_meta_table['CISCOIPSECFLOWMONITORMIB.CipSecTunnelTable']['meta_info'].parent =_meta_table['CISCOIPSECFLOWMONITORMIB']['meta_info']
