


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'WanphyLanMode_Enum' : _MetaInfoEnum('WanphyLanMode_Enum', 'ydk.models.wanphy.Cisco_IOS_XR_wanphy_ui_cfg',
        {
            'on':'ON',
        }, 'Cisco-IOS-XR-wanphy-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-wanphy-ui-cfg']),
    'WanphyWanMode_Enum' : _MetaInfoEnum('WanphyWanMode_Enum', 'ydk.models.wanphy.Cisco_IOS_XR_wanphy_ui_cfg',
        {
            'on':'ON',
        }, 'Cisco-IOS-XR-wanphy-ui-cfg', _yang_ns._namespaces['Cisco-IOS-XR-wanphy-ui-cfg']),
}
