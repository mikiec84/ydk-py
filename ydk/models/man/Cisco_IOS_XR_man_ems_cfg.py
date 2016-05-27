""" Cisco_IOS_XR_man_ems_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-ems package configuration.

This module contains definitions
for the following management objects\:
  grpc\: GRPC configruation

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class Grpc(object):
    """
    GRPC configruation
    
    .. attribute:: tls
    
    	Transport Layer Security (TLS)
    	**type**\: :py:class:`Tls <ydk.models.man.Cisco_IOS_XR_man_ems_cfg.Grpc.Tls>`
    
    .. attribute:: port
    
    	Server listening port
    	**type**\: int
    
    	**range:** 57344..57999
    
    .. attribute:: enable
    
    	Enable GRPC
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: max_request_per_user
    
    	Maximum concurrent requests per user
    	**type**\: int
    
    	**range:** 1..32
    
    .. attribute:: address_family
    
    	Address family identifier type
    	**type**\: str
    
    .. attribute:: max_request_total
    
    	Maximum concurrent requests in total
    	**type**\: int
    
    	**range:** 1..256
    
    

    """

    _prefix = 'man-ems-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.tls = Grpc.Tls()
        self.tls.parent = self
        self.port = None
        self.enable = None
        self.max_request_per_user = None
        self.address_family = None
        self.max_request_total = None


    class Tls(object):
        """
        Transport Layer Security (TLS)
        
        .. attribute:: trustpoint
        
        	Trustpoint Name
        	**type**\: str
        
        .. attribute:: enable
        
        	Enable TLS
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        

        """

        _prefix = 'man-ems-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.trustpoint = None
            self.enable = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-man-ems-cfg:grpc/Cisco-IOS-XR-man-ems-cfg:tls'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.trustpoint is not None:
                return True

            if self.enable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.man._meta import _Cisco_IOS_XR_man_ems_cfg as meta
            return meta._meta_table['Grpc.Tls']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-man-ems-cfg:grpc'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.tls is not None and self.tls._has_data():
            return True

        if self.port is not None:
            return True

        if self.enable is not None:
            return True

        if self.max_request_per_user is not None:
            return True

        if self.address_family is not None:
            return True

        if self.max_request_total is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.man._meta import _Cisco_IOS_XR_man_ems_cfg as meta
        return meta._meta_table['Grpc']['meta_info']


