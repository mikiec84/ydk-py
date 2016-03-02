""" Cisco_IOS_XR_rgmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR rgmgr package configuration.

This module contains definitions
for the following management objects\:
  redundancy\-group\-manager\: Redundancy Group Manager
    Configuration

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class IccpMode_Enum(Enum):
    """
    IccpMode_Enum

    Iccp mode

    """

    """

    Run the ICCP group in Singleton mode

    """
    SINGLETON = 1


    @staticmethod
    def _meta_info():
        from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
        return meta._meta_table['IccpMode_Enum']



class RedundancyGroupManager(object):
    """
    Redundancy Group Manager Configuration
    
    .. attribute:: aps
    
    	MR\-APS groups
    	**type**\: :py:class:`Aps <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps>`
    
    .. attribute:: enable
    
    	Enable redundancy group manager
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: iccp
    
    	ICCP configuration
    	**type**\: :py:class:`Iccp <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp>`
    
    

    """

    _prefix = 'rgmgr-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        self.aps = RedundancyGroupManager.Aps()
        self.aps.parent = self
        self.enable = None
        self.iccp = RedundancyGroupManager.Iccp()
        self.iccp.parent = self


    class Aps(object):
        """
        MR\-APS groups
        
        .. attribute:: default_redundancy_group
        
        	Default SONET controller backup configuration
        	**type**\: :py:class:`DefaultRedundancyGroup <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.DefaultRedundancyGroup>`
        
        .. attribute:: groups
        
        	Redundancy Group Table
        	**type**\: :py:class:`Groups <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups>`
        
        

        """

        _prefix = 'rgmgr-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.default_redundancy_group = RedundancyGroupManager.Aps.DefaultRedundancyGroup()
            self.default_redundancy_group.parent = self
            self.groups = RedundancyGroupManager.Aps.Groups()
            self.groups.parent = self


        class DefaultRedundancyGroup(object):
            """
            Default SONET controller backup configuration
            
            .. attribute:: backup_interface_name
            
            	Backup interface name
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: next_hop_address
            
            	IPv4 address of remote peer
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'rgmgr-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.backup_interface_name = None
                self.next_hop_address = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:aps/Cisco-IOS-XR-rgmgr-cfg:default-redundancy-group'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.backup_interface_name is not None:
                    return True

                if self.next_hop_address is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                return meta._meta_table['RedundancyGroupManager.Aps.DefaultRedundancyGroup']['meta_info']


        class Groups(object):
            """
            Redundancy Group Table
            
            .. attribute:: group
            
            	Redundancy Group Configuration
            	**type**\: list of :py:class:`Group <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups.Group>`
            
            

            """

            _prefix = 'rgmgr-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.group = YList()
                self.group.parent = self
                self.group.name = 'group'


            class Group(object):
                """
                Redundancy Group Configuration
                
                .. attribute:: group_id
                
                	The redundancy group ID
                	**type**\: int
                
                	**range:** 1..32
                
                .. attribute:: controllers
                
                	Controller configuration
                	**type**\: :py:class:`Controllers <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups.Group.Controllers>`
                
                

                """

                _prefix = 'rgmgr-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.group_id = None
                    self.controllers = RedundancyGroupManager.Aps.Groups.Group.Controllers()
                    self.controllers.parent = self


                class Controllers(object):
                    """
                    Controller configuration
                    
                    .. attribute:: controller
                    
                    	none
                    	**type**\: list of :py:class:`Controller <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.controller = YList()
                        self.controller.parent = self
                        self.controller.name = 'controller'


                    class Controller(object):
                        """
                        none
                        
                        .. attribute:: controller_name
                        
                        	Controller Name
                        	**type**\: str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: backup_interface_name
                        
                        	Backup interface name
                        	**type**\: str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: next_hop_address
                        
                        	IPv4 address of remote peer
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'rgmgr-cfg'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.controller_name = None
                            self.backup_interface_name = None
                            self.next_hop_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.controller_name is None:
                                raise YPYDataValidationError('Key property controller_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:controller[Cisco-IOS-XR-rgmgr-cfg:controller-name = ' + str(self.controller_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.controller_name is not None:
                                return True

                            if self.backup_interface_name is not None:
                                return True

                            if self.next_hop_address is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                            return meta._meta_table['RedundancyGroupManager.Aps.Groups.Group.Controllers.Controller']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:controllers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.controller is not None:
                            for child_ref in self.controller:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                        return meta._meta_table['RedundancyGroupManager.Aps.Groups.Group.Controllers']['meta_info']

                @property
                def _common_path(self):
                    if self.group_id is None:
                        raise YPYDataValidationError('Key property group_id is None')

                    return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:aps/Cisco-IOS-XR-rgmgr-cfg:groups/Cisco-IOS-XR-rgmgr-cfg:group[Cisco-IOS-XR-rgmgr-cfg:group-id = ' + str(self.group_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.group_id is not None:
                        return True

                    if self.controllers is not None and self.controllers._has_data():
                        return True

                    if self.controllers is not None and self.controllers.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                    return meta._meta_table['RedundancyGroupManager.Aps.Groups.Group']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:aps/Cisco-IOS-XR-rgmgr-cfg:groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.group is not None:
                    for child_ref in self.group:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                return meta._meta_table['RedundancyGroupManager.Aps.Groups']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:aps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.default_redundancy_group is not None and self.default_redundancy_group._has_data():
                return True

            if self.default_redundancy_group is not None and self.default_redundancy_group.is_presence():
                return True

            if self.groups is not None and self.groups._has_data():
                return True

            if self.groups is not None and self.groups.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
            return meta._meta_table['RedundancyGroupManager.Aps']['meta_info']


    class Iccp(object):
        """
        ICCP configuration
        
        .. attribute:: iccp_groups
        
        	Redundancy Group Table Configuration
        	**type**\: :py:class:`IccpGroups <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups>`
        
        

        """

        _prefix = 'rgmgr-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.iccp_groups = RedundancyGroupManager.Iccp.IccpGroups()
            self.iccp_groups.parent = self


        class IccpGroups(object):
            """
            Redundancy Group Table Configuration
            
            .. attribute:: iccp_group
            
            	Redundancy Group Configuration
            	**type**\: list of :py:class:`IccpGroup <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup>`
            
            

            """

            _prefix = 'rgmgr-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.iccp_group = YList()
                self.iccp_group.parent = self
                self.iccp_group.name = 'iccp_group'


            class IccpGroup(object):
                """
                Redundancy Group Configuration
                
                .. attribute:: group_number
                
                	The redundancy icc group number
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: backbones
                
                	ICCP backbone configuration
                	**type**\: :py:class:`Backbones <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones>`
                
                .. attribute:: isolation_recovery_delay
                
                	ICCP isolation recovery delay
                	**type**\: int
                
                	**range:** 30..600
                
                .. attribute:: members
                
                	ICCP member configuration
                	**type**\: :py:class:`Members <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members>`
                
                .. attribute:: mode
                
                	ICCP mode
                	**type**\: :py:class:`IccpMode_Enum <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.IccpMode_Enum>`
                
                .. attribute:: nv_satellite
                
                	nV Satellite configuration
                	**type**\: :py:class:`NvSatellite <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite>`
                
                

                """

                _prefix = 'rgmgr-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.group_number = None
                    self.backbones = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones()
                    self.backbones.parent = self
                    self.isolation_recovery_delay = None
                    self.members = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members()
                    self.members.parent = self
                    self.mode = None
                    self.nv_satellite = RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite()
                    self.nv_satellite.parent = self


                class Backbones(object):
                    """
                    ICCP backbone configuration
                    
                    .. attribute:: backbone
                    
                    	ICCP backbone interface configuration
                    	**type**\: list of :py:class:`Backbone <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.backbone = YList()
                        self.backbone.parent = self
                        self.backbone.name = 'backbone'


                    class Backbone(object):
                        """
                        ICCP backbone interface configuration
                        
                        .. attribute:: backbone_name
                        
                        	none
                        	**type**\: str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'rgmgr-cfg'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.backbone_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.backbone_name is None:
                                raise YPYDataValidationError('Key property backbone_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:backbone[Cisco-IOS-XR-rgmgr-cfg:backbone-name = ' + str(self.backbone_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.backbone_name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                            return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones.Backbone']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:backbones'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.backbone is not None:
                            for child_ref in self.backbone:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                        return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Backbones']['meta_info']


                class Members(object):
                    """
                    ICCP member configuration
                    
                    .. attribute:: member
                    
                    	ICCP member configuration
                    	**type**\: list of :py:class:`Member <ydk.models.rgmgr.Cisco_IOS_XR_rgmgr_cfg.RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member>`
                    
                    

                    """

                    _prefix = 'rgmgr-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.member = YList()
                        self.member.parent = self
                        self.member.name = 'member'


                    class Member(object):
                        """
                        ICCP member configuration
                        
                        .. attribute:: neighbor_address
                        
                        	Neighbor IP address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'rgmgr-cfg'
                        _revision = '2015-07-30'

                        def __init__(self):
                            self.parent = None
                            self.neighbor_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.neighbor_address is None:
                                raise YPYDataValidationError('Key property neighbor_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:member[Cisco-IOS-XR-rgmgr-cfg:neighbor-address = ' + str(self.neighbor_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.neighbor_address is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                            return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members.Member']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-rgmgr-cfg:members'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.member is not None:
                            for child_ref in self.member:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                        return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.Members']['meta_info']


                class NvSatellite(object):
                    """
                    nV Satellite configuration
                    
                    .. attribute:: system_mac
                    
                    	Optional identifier for this system
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    

                    """

                    _prefix = 'icpe-infra-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.system_mac = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-icpe-infra-cfg:nv-satellite'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.system_mac is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                        return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup.NvSatellite']['meta_info']

                @property
                def _common_path(self):
                    if self.group_number is None:
                        raise YPYDataValidationError('Key property group_number is None')

                    return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:iccp/Cisco-IOS-XR-rgmgr-cfg:iccp-groups/Cisco-IOS-XR-rgmgr-cfg:iccp-group[Cisco-IOS-XR-rgmgr-cfg:group-number = ' + str(self.group_number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.group_number is not None:
                        return True

                    if self.backbones is not None and self.backbones._has_data():
                        return True

                    if self.backbones is not None and self.backbones.is_presence():
                        return True

                    if self.isolation_recovery_delay is not None:
                        return True

                    if self.members is not None and self.members._has_data():
                        return True

                    if self.members is not None and self.members.is_presence():
                        return True

                    if self.mode is not None:
                        return True

                    if self.nv_satellite is not None and self.nv_satellite._has_data():
                        return True

                    if self.nv_satellite is not None and self.nv_satellite.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                    return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups.IccpGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:iccp/Cisco-IOS-XR-rgmgr-cfg:iccp-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.iccp_group is not None:
                    for child_ref in self.iccp_group:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
                return meta._meta_table['RedundancyGroupManager.Iccp.IccpGroups']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager/Cisco-IOS-XR-rgmgr-cfg:iccp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.iccp_groups is not None and self.iccp_groups._has_data():
                return True

            if self.iccp_groups is not None and self.iccp_groups.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
            return meta._meta_table['RedundancyGroupManager.Iccp']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-rgmgr-cfg:redundancy-group-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.aps is not None and self.aps._has_data():
            return True

        if self.aps is not None and self.aps.is_presence():
            return True

        if self.enable is not None:
            return True

        if self.iccp is not None and self.iccp._has_data():
            return True

        if self.iccp is not None and self.iccp.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.rgmgr._meta import _Cisco_IOS_XR_rgmgr_cfg as meta
        return meta._meta_table['RedundancyGroupManager']['meta_info']


