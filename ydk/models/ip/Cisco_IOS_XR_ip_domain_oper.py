""" Cisco_IOS_XR_ip_domain_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-domain package operational data.

This module contains definitions
for the following management objects\:
  ip\-domain\: Domain server and host data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class ServerDomainLkup_Enum(Enum):
    """
    ServerDomainLkup_Enum

    Domain look up

    """

    """

    Static mapping

    """
    STATIC_MAPPING = 0

    """

    Domain service

    """
    DOMAIN_SERVICE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
        return meta._meta_table['ServerDomainLkup_Enum']



class HostAddressBase_Identity(object):
    """
    Base identity for Host\-address
    
    

    """

    _prefix = 'Cisco-IOS-XR-ip-domain-oper'
    _revision = '2015-09-29'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
        return meta._meta_table['HostAddressBase_Identity']['meta_info']


class IpDomain(object):
    """
    Domain server and host data
    
    .. attribute:: vrfs
    
    	List of VRFs
    	**type**\: :py:class:`Vrfs <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs>`
    
    

    """

    _prefix = 'ip-domain-oper'
    _revision = '2015-09-29'

    def __init__(self):
        self.vrfs = IpDomain.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        List of VRFs
        
        .. attribute:: vrf
        
        	VRF instance
        	**type**\: list of :py:class:`Vrf <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-domain-oper'
        _revision = '2015-09-29'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            VRF instance
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: hosts
            
            	List of domain hosts
            	**type**\: :py:class:`Hosts <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Hosts>`
            
            .. attribute:: server
            
            	Domain server data
            	**type**\: :py:class:`Server <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Server>`
            
            

            """

            _prefix = 'ip-domain-oper'
            _revision = '2015-09-29'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.hosts = IpDomain.Vrfs.Vrf.Hosts()
                self.hosts.parent = self
                self.server = IpDomain.Vrfs.Vrf.Server()
                self.server.parent = self


            class Hosts(object):
                """
                List of domain hosts
                
                .. attribute:: host
                
                	IP domain\-name, lookup style, nameservers for specific host
                	**type**\: list of :py:class:`Host <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Hosts.Host>`
                
                

                """

                _prefix = 'ip-domain-oper'
                _revision = '2015-09-29'

                def __init__(self):
                    self.parent = None
                    self.host = YList()
                    self.host.parent = self
                    self.host.name = 'host'


                class Host(object):
                    """
                    IP domain\-name, lookup style, nameservers for
                    specific host
                    
                    .. attribute:: host_name
                    
                    	Hostname
                    	**type**\: str
                    
                    .. attribute:: af_name
                    
                    	Address type
                    	**type**\: :py:class:`HostAddressBase_Identity <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.HostAddressBase_Identity>`
                    
                    .. attribute:: age
                    
                    	Age in hours
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: host_address
                    
                    	Host address list
                    	**type**\: list of :py:class:`HostAddress <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress>`
                    
                    .. attribute:: host_alias_list
                    
                    	Host alias
                    	**type**\: :py:class:`HostAliasList <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList>`
                    
                    

                    """

                    _prefix = 'ip-domain-oper'
                    _revision = '2015-09-29'

                    def __init__(self):
                        self.parent = None
                        self.host_name = None
                        self.af_name = None
                        self.age = None
                        self.host_address = YList()
                        self.host_address.parent = self
                        self.host_address.name = 'host_address'
                        self.host_alias_list = IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList()
                        self.host_alias_list.parent = self


                    class HostAddress(object):
                        """
                        Host address list
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\: :py:class:`HostAddressBase_Identity <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.HostAddressBase_Identity>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-domain-oper'
                        _revision = '2015-09-29'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-oper:host-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
                            return meta._meta_table['IpDomain.Vrfs.Vrf.Hosts.Host.HostAddress']['meta_info']


                    class HostAliasList(object):
                        """
                        Host alias
                        
                        .. attribute:: host_alias
                        
                        	Host alias list
                        	**type**\: list of str
                        
                        	**range:** 0..256
                        
                        

                        """

                        _prefix = 'ip-domain-oper'
                        _revision = '2015-09-29'

                        def __init__(self):
                            self.parent = None
                            self.host_alias = []

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-oper:host-alias-list'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.host_alias is not None:
                                for child in self.host_alias:
                                    if child is not None:
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
                            return meta._meta_table['IpDomain.Vrfs.Vrf.Hosts.Host.HostAliasList']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.host_name is None:
                            raise YPYDataValidationError('Key property host_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-oper:host[Cisco-IOS-XR-ip-domain-oper:host-name = ' + str(self.host_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.host_name is not None:
                            return True

                        if self.af_name is not None:
                            return True

                        if self.age is not None:
                            return True

                        if self.host_address is not None:
                            for child_ref in self.host_address:
                                if child_ref._has_data():
                                    return True

                        if self.host_alias_list is not None and self.host_alias_list._has_data():
                            return True

                        if self.host_alias_list is not None and self.host_alias_list.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
                        return meta._meta_table['IpDomain.Vrfs.Vrf.Hosts.Host']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-oper:hosts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.host is not None:
                        for child_ref in self.host:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
                    return meta._meta_table['IpDomain.Vrfs.Vrf.Hosts']['meta_info']


            class Server(object):
                """
                Domain server data
                
                .. attribute:: domain
                
                	Domain list
                	**type**\: list of str
                
                	**range:** 0..256
                
                .. attribute:: domain_lookup
                
                	Domain lookup
                	**type**\: :py:class:`ServerDomainLkup_Enum <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.ServerDomainLkup_Enum>`
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\: str
                
                	**range:** 0..256
                
                .. attribute:: server_address
                
                	Server address list
                	**type**\: list of :py:class:`ServerAddress <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.IpDomain.Vrfs.Vrf.Server.ServerAddress>`
                
                

                """

                _prefix = 'ip-domain-oper'
                _revision = '2015-09-29'

                def __init__(self):
                    self.parent = None
                    self.domain = []
                    self.domain_lookup = None
                    self.domain_name = None
                    self.server_address = YList()
                    self.server_address.parent = self
                    self.server_address.name = 'server_address'


                class ServerAddress(object):
                    """
                    Server address list
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\: :py:class:`HostAddressBase_Identity <ydk.models.ip.Cisco_IOS_XR_ip_domain_oper.HostAddressBase_Identity>`
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	IPv6 address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-domain-oper'
                    _revision = '2015-09-29'

                    def __init__(self):
                        self.parent = None
                        self.af_name = None
                        self.ipv4_address = None
                        self.ipv6_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-oper:server-address'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.af_name is not None:
                            return True

                        if self.ipv4_address is not None:
                            return True

                        if self.ipv6_address is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
                        return meta._meta_table['IpDomain.Vrfs.Vrf.Server.ServerAddress']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-domain-oper:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.domain is not None:
                        for child in self.domain:
                            if child is not None:
                                return True

                    if self.domain_lookup is not None:
                        return True

                    if self.domain_name is not None:
                        return True

                    if self.server_address is not None:
                        for child_ref in self.server_address:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
                    return meta._meta_table['IpDomain.Vrfs.Vrf.Server']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYDataValidationError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ip-domain-oper:ip-domain/Cisco-IOS-XR-ip-domain-oper:vrfs/Cisco-IOS-XR-ip-domain-oper:vrf[Cisco-IOS-XR-ip-domain-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.vrf_name is not None:
                    return True

                if self.hosts is not None and self.hosts._has_data():
                    return True

                if self.hosts is not None and self.hosts.is_presence():
                    return True

                if self.server is not None and self.server._has_data():
                    return True

                if self.server is not None and self.server.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
                return meta._meta_table['IpDomain.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-domain-oper:ip-domain/Cisco-IOS-XR-ip-domain-oper:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
            return meta._meta_table['IpDomain.Vrfs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-domain-oper:ip-domain'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.vrfs is not None and self.vrfs._has_data():
            return True

        if self.vrfs is not None and self.vrfs.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
        return meta._meta_table['IpDomain']['meta_info']


class Ipv4_Identity(HostAddressBase_Identity):
    """
    IPv4 family address
    
    

    """

    _prefix = 'Cisco-IOS-XR-ip-domain-oper'
    _revision = '2015-09-29'

    def __init__(self):
        HostAddressBase_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
        return meta._meta_table['Ipv4_Identity']['meta_info']


class Ipv6_Identity(HostAddressBase_Identity):
    """
    IPv6 family address
    
    

    """

    _prefix = 'Cisco-IOS-XR-ip-domain-oper'
    _revision = '2015-09-29'

    def __init__(self):
        HostAddressBase_Identity.__init__(self)
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_domain_oper as meta
        return meta._meta_table['Ipv6_Identity']['meta_info']


