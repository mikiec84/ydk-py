""" Cisco_IOS_XR_asr9k_qos_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-qos package configuration.

This module contains definitions
for the following management objects\:
  qos\: Global QOS configuration.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class QosFieldNotSupported_Enum(Enum):
    """
    QosFieldNotSupported_Enum

    Qos field not supported

    """

    """

    Dummy data type leave unspecified

    """
    NOT_SUPPORTED = 0


    @staticmethod
    def _meta_info():
        from ydk.models.asr9k._meta import _Cisco_IOS_XR_asr9k_qos_cfg as meta
        return meta._meta_table['QosFieldNotSupported_Enum']


class QosPolicyAccount_Enum(Enum):
    """
    QosPolicyAccount_Enum

    Qos policy account

    """

    """

    No account turn off preference

    """
    NO_PREFERENCE = 0

    """

    Turn on layer 2 accounting

    """
    LAYER2 = 1

    """

    Turn off layer 2 accounting

    """
    NO_LAYER2 = 2

    """

    User defined accounting

    """
    USER_DEFINED = 4

    """

    Turn on layer 1 accounting

    """
    LAYER1 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.asr9k._meta import _Cisco_IOS_XR_asr9k_qos_cfg as meta
        return meta._meta_table['QosPolicyAccount_Enum']


class Qosl2DataLink_Enum(Enum):
    """
    Qosl2DataLink_Enum

    Qosl2 data link

    """

    """

    ATM adaption layer AAL5

    """
    AAL5 = 0


    @staticmethod
    def _meta_info():
        from ydk.models.asr9k._meta import _Cisco_IOS_XR_asr9k_qos_cfg as meta
        return meta._meta_table['Qosl2DataLink_Enum']


class Qosl2Encap_Enum(Enum):
    """
    Qosl2Encap_Enum

    Qosl2 encap

    """

    """

    snap\-pppoa encap used between the DSLAM and CPE

    """
    SNAP_PPPOA = 1

    """

    mux\-pppoa encap used between the DSLAM and CPE

    """
    MUX_PPPOA = 2

    """

    snap\-1483routed encap used between the DSLAM
    and CPE

    """
    SNAP1483_ROUTED = 3

    """

    mux\-1483routed encap used between the DSLAM and
    CPE

    """
    MUX1483_ROUTED = 4

    """

    snap\-rbe encap used between the DSLAM and CPE

    """
    SNAP_RBE = 5

    """

    snap\-dot1q\-rbe encap used between the DSLAM and
    CPE

    """
    SNAP_DOT1QRBE = 6

    """

    mux\-rbe encap used between the DSLAM and CPE

    """
    MUX_RBE = 7

    """

    mux\-dot1q\-rbe encap used between the DSLAM and
    CPE

    """
    MUX_DOT1QRBE = 8


    @staticmethod
    def _meta_info():
        from ydk.models.asr9k._meta import _Cisco_IOS_XR_asr9k_qos_cfg as meta
        return meta._meta_table['Qosl2Encap_Enum']



class Qos(object):
    """
    Global QOS configuration.
    
    .. attribute:: fabric_service_policy
    
    	Name of the fabric service policy
    	**type**\: str
    
    	**range:** 0..63
    
    

    """

    _prefix = 'asr9k-qos-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.fabric_service_policy = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-qos-cfg:qos'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.fabric_service_policy is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.asr9k._meta import _Cisco_IOS_XR_asr9k_qos_cfg as meta
        return meta._meta_table['Qos']['meta_info']


