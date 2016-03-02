


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable.CContextMappingBridgeDomainEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable.CContextMappingBridgeDomainEntry',
            False, 
            [
            _MetaInfoClassMember('cContextMappingVacmContextName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'ccontextmappingvacmcontextname',
                'CISCO-CONTEXT-MAPPING-MIB', True),
            _MetaInfoClassMember('cContextMappingBridgeDomainIdentifier', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of an instance of this object identifies
                the bridge domain to which the SNMP context is 
                mapped to.
                ''',
                'ccontextmappingbridgedomainidentifier',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingBridgeDomainRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object facilitates the creation, modification, or
                deletion of a conceptual row in this table.
                ''',
                'ccontextmappingbridgedomainrowstatus',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingBridgeDomainStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                The storage type for this conceptual row.
                
                Conceptual rows having the value 'permanent' need not
                allow write-access to any columnar objects in the row.
                ''',
                'ccontextmappingbridgedomainstoragetype',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            ],
            'CISCO-CONTEXT-MAPPING-MIB',
            'cContextMappingBridgeDomainEntry',
            _yang_ns._namespaces['CISCO-CONTEXT-MAPPING-MIB'],
        'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB'
        ),
    },
    'CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable' : {
        'meta_info' : _MetaInfoClass('CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable',
            False, 
            [
            _MetaInfoClassMember('cContextMappingBridgeDomainEntry', REFERENCE_LIST, 'CContextMappingBridgeDomainEntry' , 'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB', 'CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable.CContextMappingBridgeDomainEntry', 
                [], [], 
                '''                Information relating to a single mapping of
                cContextMappingVacmContextName to the 
                corresponding bridge domain.
                
                To create a row in this table, a manager must set
                cContextMappingBridgeDomainRowStatus to either 
                'createAndGo' or 'createAndWait'.
                
                To delete a row in this table, a manager must set
                cContextMappingBridgeDomainRowStatus to 'destroy'.
                ''',
                'ccontextmappingbridgedomainentry',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            ],
            'CISCO-CONTEXT-MAPPING-MIB',
            'cContextMappingBridgeDomainTable',
            _yang_ns._namespaces['CISCO-CONTEXT-MAPPING-MIB'],
        'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB'
        ),
    },
    'CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable.CContextMappingBridgeInstanceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable.CContextMappingBridgeInstanceEntry',
            False, 
            [
            _MetaInfoClassMember('cContextMappingVacmContextName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'ccontextmappingvacmcontextname',
                'CISCO-CONTEXT-MAPPING-MIB', True),
            _MetaInfoClassMember('cContextMappingBridgeInstName', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                The object identifies the name given to bridge
                instance to which the SNMP context is mapped to.
                
                Value of this object cannot be changed when the 
                RowStatus object in the same row is 'active'.
                
                This is typically a human-readable string. This is
                the same ASCII string used in the router's console
                interface to refer to this bridge instance.
                
                When the value of this object is a zero length
                string, it indicates that the SNMP context is
                independent of any bridge instances.
                ''',
                'ccontextmappingbridgeinstname',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingBridgeInstRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object facilitates the creation, modification, or
                deletion of a conceptual row in this table.
                ''',
                'ccontextmappingbridgeinstrowstatus',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingBridgeInstStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                The storage type for this conceptual row.
                
                Value of this object cannot be changed when the 
                RowStatus object in the same row is 'active'.
                
                Conceptual rows having the value 'permanent' need not
                allow write-access to any columnar objects in the row.
                ''',
                'ccontextmappingbridgeinststoragetype',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            ],
            'CISCO-CONTEXT-MAPPING-MIB',
            'cContextMappingBridgeInstanceEntry',
            _yang_ns._namespaces['CISCO-CONTEXT-MAPPING-MIB'],
        'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB'
        ),
    },
    'CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable' : {
        'meta_info' : _MetaInfoClass('CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable',
            False, 
            [
            _MetaInfoClassMember('cContextMappingBridgeInstanceEntry', REFERENCE_LIST, 'CContextMappingBridgeInstanceEntry' , 'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB', 'CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable.CContextMappingBridgeInstanceEntry', 
                [], [], 
                '''                Information relating to a single mapping of
                cContextMappingVacmContextName to the 
                corresponding bridge instance.
                
                To create a row in this table, a manager must set
                cContextMappingBridgeInstRowStatus to either 
                'createAndGo' or 'createAndWait'.
                
                To delete a row in this table, a manager must set
                cContextMappingBridgeInstRowStatus to 'destroy'.
                ''',
                'ccontextmappingbridgeinstanceentry',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            ],
            'CISCO-CONTEXT-MAPPING-MIB',
            'cContextMappingBridgeInstanceTable',
            _yang_ns._namespaces['CISCO-CONTEXT-MAPPING-MIB'],
        'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB'
        ),
    },
    'CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable.CContextMappingLicenseGroupEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable.CContextMappingLicenseGroupEntry',
            False, 
            [
            _MetaInfoClassMember('cContextMappingVacmContextName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'ccontextmappingvacmcontextname',
                'CISCO-CONTEXT-MAPPING-MIB', True),
            _MetaInfoClassMember('cContextMappingLicenseGroupName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The value of an instance of this object identifies
                the name given to the Group to which the SNMP context
                is mapped.
                
                Feature sets from all groups will be combined to form 
                universal image. User can configure multiple groups as needed.
                
                For example: In Next generation ISRs will use
                the universal image package level licensing model
                for its licensing need. Each group has
                the feature set needed for that specific technology.
                Feature sets from different groups are combined to 
                form universal image and each feature set for a group 
                can be enabled using a valid license key. There will 
                be a base level ipbase package in which the router 
                boots with out any license key.
                
                The following are the different Technology Groups.
                1.crypto
                2.data
                3.ip
                4.legacy
                5.novpn-security
                6.security
                7.uc
                ''',
                'ccontextmappinglicensegroupname',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingLicenseGroupRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object facilitates the creation, modification, or
                deletion of a conceptual row in this table.
                ''',
                'ccontextmappinglicensegrouprowstatus',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingLicenseGroupStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                The storage type for this conceptual row.
                
                Conceptual rows having the value 'permanent' need not
                allow write-access to any columnar objects in the row.
                ''',
                'ccontextmappinglicensegroupstoragetype',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            ],
            'CISCO-CONTEXT-MAPPING-MIB',
            'cContextMappingLicenseGroupEntry',
            _yang_ns._namespaces['CISCO-CONTEXT-MAPPING-MIB'],
        'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB'
        ),
    },
    'CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable' : {
        'meta_info' : _MetaInfoClass('CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable',
            False, 
            [
            _MetaInfoClassMember('cContextMappingLicenseGroupEntry', REFERENCE_LIST, 'CContextMappingLicenseGroupEntry' , 'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB', 'CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable.CContextMappingLicenseGroupEntry', 
                [], [], 
                '''                Information relating to a single mapping of
                CContextMappingVacmContextName to the
                corresponding License Group.
                ''',
                'ccontextmappinglicensegroupentry',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            ],
            'CISCO-CONTEXT-MAPPING-MIB',
            'cContextMappingLicenseGroupTable',
            _yang_ns._namespaces['CISCO-CONTEXT-MAPPING-MIB'],
        'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB'
        ),
    },
    'CISCOCONTEXTMAPPINGMIB.CContextMappingTable.CContextMappingEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCONTEXTMAPPINGMIB.CContextMappingTable.CContextMappingEntry',
            False, 
            [
            _MetaInfoClassMember('cContextMappingVacmContextName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The vacmContextName given to the SNMP context.
                
                This is a human readable name identifying a particular
                SNMP VACM context at a particular SNMP entity.
                The empty contextName (zero length) represents the
                default context.
                ''',
                'ccontextmappingvacmcontextname',
                'CISCO-CONTEXT-MAPPING-MIB', True),
            _MetaInfoClassMember('cContextMappingProtoInstName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The value of an instance of this object identifies
                the name given to the protocol instance to which the
                SNMP context is mapped to.
                
                This is typically a human-readable string. This is
                the same ASCII string used in the router's console
                interface to refer to this protocol instance.
                
                When the value of this object is the zero length
                string it indicates that the SNMP context is independent
                of any protocol instance.
                ''',
                'ccontextmappingprotoinstname',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object facilitates the creation, modification, or
                deletion of a conceptual row in this table.
                ''',
                'ccontextmappingrowstatus',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                The storage type for this conceptual row.
                
                Conceptual rows having the value 'permanent' need not
                allow write-access to any columnar objects in the row.
                ''',
                'ccontextmappingstoragetype',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingTopologyName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The value of an instance of this object identifies
                the name given to the topology to which the SNMP
                context is mapped to.
                
                This is typically a human-readable string. This is
                the same ASCII string used in the router's console
                interface to refer to this topology.
                
                When the value of this object is the zero length
                string it indicates that the SNMP context is independent
                of any topology.
                ''',
                'ccontextmappingtopologyname',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The value of an instance of this object identifies
                the name given to the VRF to which the SNMP context
                is mapped to.
                
                This is typically a human-readable string. This is
                the same ASCII string used in the router's console
                interface to refer to this VRF.
                
                When the value of this object is the zero length
                string it indicates that the SNMP context is independent
                of any VRF.
                ''',
                'ccontextmappingvrfname',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            ],
            'CISCO-CONTEXT-MAPPING-MIB',
            'cContextMappingEntry',
            _yang_ns._namespaces['CISCO-CONTEXT-MAPPING-MIB'],
        'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB'
        ),
    },
    'CISCOCONTEXTMAPPINGMIB.CContextMappingTable' : {
        'meta_info' : _MetaInfoClass('CISCOCONTEXTMAPPINGMIB.CContextMappingTable',
            False, 
            [
            _MetaInfoClassMember('cContextMappingEntry', REFERENCE_LIST, 'CContextMappingEntry' , 'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB', 'CISCOCONTEXTMAPPINGMIB.CContextMappingTable.CContextMappingEntry', 
                [], [], 
                '''                Information relating to a single mapping of
                cContextMappingVacmContextName to the corresponding VRF,
                the corresponding topology, and the corresponding routing
                protocol instance.
                ''',
                'ccontextmappingentry',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            ],
            'CISCO-CONTEXT-MAPPING-MIB',
            'cContextMappingTable',
            _yang_ns._namespaces['CISCO-CONTEXT-MAPPING-MIB'],
        'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB'
        ),
    },
    'CISCOCONTEXTMAPPINGMIB' : {
        'meta_info' : _MetaInfoClass('CISCOCONTEXTMAPPINGMIB',
            False, 
            [
            _MetaInfoClassMember('cContextMappingBridgeDomainTable', REFERENCE_CLASS, 'CContextMappingBridgeDomainTable' , 'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB', 'CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable', 
                [], [], 
                '''                This table contains information on which
                cContextMappingVacmContextName is mapped to
                which bridge domain.
                
                A Bridge Domain is one of the means by which it is possible 
                to define an Ethernet broadcast domain on a bridging device. 
                A network can have multiple broadcast domains configured.
                This table helps the network management personnel to find 
                out the  details of various broadcast domains configured 
                in the network.
                
                An entry need to exist in cContextMappingTable, to create 
                an entry in this table.
                ''',
                'ccontextmappingbridgedomaintable',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingBridgeInstanceTable', REFERENCE_CLASS, 'CContextMappingBridgeInstanceTable' , 'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB', 'CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable', 
                [], [], 
                '''                This table contains information on mapping between
                cContextMappingVacmContextName and bridge instance.
                
                Bridge instance is an instance of a physical or logical 
                bridge which has unique bridge-id.
                
                If an entry is deleted from cContextMappingTable, the
                corresponding entry in this table will also get deleted.
                
                If an entry needs to be created in this table, the
                corresponding entry must exist in cContextMappingTable.
                ''',
                'ccontextmappingbridgeinstancetable',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingLicenseGroupTable', REFERENCE_CLASS, 'CContextMappingLicenseGroupTable' , 'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB', 'CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable', 
                [], [], 
                '''                This table contains information on which
                cContextMappingVacmContextName is mapped to
                which License Group.
                Group level licensing is used where each
                Technology Package is enabled via a License.
                ''',
                'ccontextmappinglicensegrouptable',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            _MetaInfoClassMember('cContextMappingTable', REFERENCE_CLASS, 'CContextMappingTable' , 'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB', 'CISCOCONTEXTMAPPINGMIB.CContextMappingTable', 
                [], [], 
                '''                This table contains information on which
                cContextMappingVacmContextName is mapped to
                which VRF, topology, and routing protocol instance.
                
                This table is indexed by SNMP VACM context.
                
                Configuring a row in this table for an SNMP context
                does not require that the context be already defined,
                i.e., a row can be created in this table for a context
                before the corresponding row is created in RFC 3415's
                vacmContextTable.
                
                To create a row in this table, a manager must set
                cContextMappingRowStatus to either 'createAndGo' or
                'createAndWait'.
                
                To delete a row in this table, a manager must set
                cContextMappingRowStatus to 'destroy'.
                ''',
                'ccontextmappingtable',
                'CISCO-CONTEXT-MAPPING-MIB', False),
            ],
            'CISCO-CONTEXT-MAPPING-MIB',
            'CISCO-CONTEXT-MAPPING-MIB',
            _yang_ns._namespaces['CISCO-CONTEXT-MAPPING-MIB'],
        'ydk.models.context.CISCO_CONTEXT_MAPPING_MIB'
        ),
    },
}
_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable.CContextMappingBridgeDomainEntry']['meta_info'].parent =_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable']['meta_info']
_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable.CContextMappingBridgeInstanceEntry']['meta_info'].parent =_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable']['meta_info']
_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable.CContextMappingLicenseGroupEntry']['meta_info'].parent =_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable']['meta_info']
_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingTable.CContextMappingEntry']['meta_info'].parent =_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingTable']['meta_info']
_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeDomainTable']['meta_info'].parent =_meta_table['CISCOCONTEXTMAPPINGMIB']['meta_info']
_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingBridgeInstanceTable']['meta_info'].parent =_meta_table['CISCOCONTEXTMAPPINGMIB']['meta_info']
_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingLicenseGroupTable']['meta_info'].parent =_meta_table['CISCOCONTEXTMAPPINGMIB']['meta_info']
_meta_table['CISCOCONTEXTMAPPINGMIB.CContextMappingTable']['meta_info'].parent =_meta_table['CISCOCONTEXTMAPPINGMIB']['meta_info']
