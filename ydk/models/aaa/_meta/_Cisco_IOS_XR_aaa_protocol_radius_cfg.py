


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'AaaAuthentication_Enum' : _MetaInfoEnum('AaaAuthentication_Enum', 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg',
        {
            'all':'ALL',
            'any':'ANY',
            'session-key':'SESSION_KEY',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaConfig_Enum' : _MetaInfoEnum('AaaConfig_Enum', 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg',
        {
            'false':'FALSE',
            'true':'TRUE',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaAction_Enum' : _MetaInfoEnum('AaaAction_Enum', 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg',
        {
            'accept':'ACCEPT',
            'reject':'REJECT',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaDscpValue_Enum' : _MetaInfoEnum('AaaDscpValue_Enum', 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg',
        {
            'af11':'AF11',
            'af12':'AF12',
            'af13':'AF13',
            'af21':'AF21',
            'af22':'AF22',
            'af23':'AF23',
            'af31':'AF31',
            'af32':'AF32',
            'af33':'AF33',
            'af41':'AF41',
            'af42':'AF42',
            'af43':'AF43',
            'cs1':'CS1',
            'cs2':'CS2',
            'cs3':'CS3',
            'cs4':'CS4',
            'cs5':'CS5',
            'cs6':'CS6',
            'cs7':'CS7',
            'default':'DEFAULT',
            'ef':'EF',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaSelectKey_Enum' : _MetaInfoEnum('AaaSelectKey_Enum', 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg',
        {
            'server-key':'SERVER_KEY',
            'session-key':'SESSION_KEY',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
}
