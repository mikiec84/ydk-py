""" CISCO_IP_LOCAL_POOL_MIB 

This MIB defines the configuration and monitoring capabilities
relating to local IP pools.

Local IP pools have the following characteristics\:

\- An IP local pool consists of one or more IP address ranges.

\- An IP pool group consists of one or more IP local pools.

\- An IP local pool can only belong to one IP pool group.

\- IP local pools that belong to different groups can have
  overlapping addresses.

\- IP local pool names are unique even when they belong to
  different groups.

\- Addresses within an IP pool group can not overlap.

\- IP local pools without an explicit group name are considered
  members of the base system group.  In this MIB, the base
  system group is represented by a null IP pool group name.

This MIB defines objects that expose the relationship between
IP pool groups and IP local pools.  There exist other objects
that maintain statistics about the address usage of IP local
pools.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIPLOCALPOOLMIB(Entity):
    """
    
    
    .. attribute:: ciplocalpoolalloctable
    
    	This table lists all addresses that have been allocated out of an IP local pool.  Entries in this table are created when a remote peer allocates an address from one of the IP local pools in the cIpLocalPoolConfigTable.  Entries in this table are deleted when a remote peer deallocates an address from one of the IP local pool in the cIpLocalPoolConfigTable.  Entries in this table are uniquely indexed by the name of the IP local pool, and the allocated address, together with its address type
    	**type**\:   :py:class:`Ciplocalpoolalloctable <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolalloctable>`
    
    .. attribute:: ciplocalpoolconfig
    
    	
    	**type**\:   :py:class:`Ciplocalpoolconfig <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolconfig>`
    
    .. attribute:: ciplocalpoolconfigtable
    
    	This table manages the creation, modification, and deletion of IP local pools using the RowStatus textual convention.  An entry in this table defines an IP address range that is associated with an IP local pool.  A conceptual row in this table can not be modified while cIpLocalPoolRowStatus is set to 'active'.  Since IP local pool names are unique even when they belong to different groups, and addresses within a group can not overlap, a row in this table is uniquely indexed by the pool name, and by the low address of the IP local pool together with its address type
    	**type**\:   :py:class:`Ciplocalpoolconfigtable <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolconfigtable>`
    
    .. attribute:: ciplocalpoolgroupcontainstable
    
    	A table which exposes the container/'containee' relationships between local IP pools and IP pool groups.  Entries in this table are created or deleted as a by\-product of creating or deleting entries in the cIpLocalPoolConfigTable.  When an entry is created and activated in the cIpLocalPoolConfigTable table, an entry in this table will come into existence if it does not already exist.  When an entry is deleted in the cIpLocalPoolConfigTable table, if there is no other entry existing in that table with the same cIpLocalPoolGroupContainedIn and cIpLocalPoolName, the entry in this table with the respective cIpLocalPoolGroupName and cIpLocalPoolName indices will be removed
    	**type**\:   :py:class:`Ciplocalpoolgroupcontainstable <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolgroupcontainstable>`
    
    .. attribute:: ciplocalpoolgrouptable
    
    	This table provides statistics for configured IP pool groups.  Entries in this table are created as the result of adding a new IP pool group to the cIpLocalPoolConfigTable.  Entries in this table are deleted as the result of removing all IP local pools that are contained in an IP pool group in the cIpLocalPoolConfigTable.  An entry in this table is uniquely indexed by IP pool group name
    	**type**\:   :py:class:`Ciplocalpoolgrouptable <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolgrouptable>`
    
    .. attribute:: ciplocalpoolstatstable
    
    	A table providing statistics for each IP local pool.  Entries in this table are created as the result of adding a new IP local pool to the cIpLocalPoolConfigTable.  Entries in this table are deleted as the result of removing all the address ranges that are contained in an IP local pool in the cIpLocalPoolConfigTable.  Entries in this table are uniquely indexed by the name of the IP local pool
    	**type**\:   :py:class:`Ciplocalpoolstatstable <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolstatstable>`
    
    

    """

    _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
    _revision = '2007-11-12'

    def __init__(self):
        super(CISCOIPLOCALPOOLMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IP-LOCAL-POOL-MIB"
        self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"cIpLocalPoolAllocTable" : ("ciplocalpoolalloctable", CISCOIPLOCALPOOLMIB.Ciplocalpoolalloctable), "cIpLocalPoolConfig" : ("ciplocalpoolconfig", CISCOIPLOCALPOOLMIB.Ciplocalpoolconfig), "cIpLocalPoolConfigTable" : ("ciplocalpoolconfigtable", CISCOIPLOCALPOOLMIB.Ciplocalpoolconfigtable), "cIpLocalPoolGroupContainsTable" : ("ciplocalpoolgroupcontainstable", CISCOIPLOCALPOOLMIB.Ciplocalpoolgroupcontainstable), "cIpLocalPoolGroupTable" : ("ciplocalpoolgrouptable", CISCOIPLOCALPOOLMIB.Ciplocalpoolgrouptable), "cIpLocalPoolStatsTable" : ("ciplocalpoolstatstable", CISCOIPLOCALPOOLMIB.Ciplocalpoolstatstable)}
        self._child_list_classes = {}

        self.ciplocalpoolalloctable = CISCOIPLOCALPOOLMIB.Ciplocalpoolalloctable()
        self.ciplocalpoolalloctable.parent = self
        self._children_name_map["ciplocalpoolalloctable"] = "cIpLocalPoolAllocTable"
        self._children_yang_names.add("cIpLocalPoolAllocTable")

        self.ciplocalpoolconfig = CISCOIPLOCALPOOLMIB.Ciplocalpoolconfig()
        self.ciplocalpoolconfig.parent = self
        self._children_name_map["ciplocalpoolconfig"] = "cIpLocalPoolConfig"
        self._children_yang_names.add("cIpLocalPoolConfig")

        self.ciplocalpoolconfigtable = CISCOIPLOCALPOOLMIB.Ciplocalpoolconfigtable()
        self.ciplocalpoolconfigtable.parent = self
        self._children_name_map["ciplocalpoolconfigtable"] = "cIpLocalPoolConfigTable"
        self._children_yang_names.add("cIpLocalPoolConfigTable")

        self.ciplocalpoolgroupcontainstable = CISCOIPLOCALPOOLMIB.Ciplocalpoolgroupcontainstable()
        self.ciplocalpoolgroupcontainstable.parent = self
        self._children_name_map["ciplocalpoolgroupcontainstable"] = "cIpLocalPoolGroupContainsTable"
        self._children_yang_names.add("cIpLocalPoolGroupContainsTable")

        self.ciplocalpoolgrouptable = CISCOIPLOCALPOOLMIB.Ciplocalpoolgrouptable()
        self.ciplocalpoolgrouptable.parent = self
        self._children_name_map["ciplocalpoolgrouptable"] = "cIpLocalPoolGroupTable"
        self._children_yang_names.add("cIpLocalPoolGroupTable")

        self.ciplocalpoolstatstable = CISCOIPLOCALPOOLMIB.Ciplocalpoolstatstable()
        self.ciplocalpoolstatstable.parent = self
        self._children_name_map["ciplocalpoolstatstable"] = "cIpLocalPoolStatsTable"
        self._children_yang_names.add("cIpLocalPoolStatsTable")
        self._segment_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB"


    class Ciplocalpoolalloctable(Entity):
        """
        This table lists all addresses that have been allocated out of
        an IP local pool.
        
        Entries in this table are created when a remote peer allocates
        an address from one of the IP local pools in the
        cIpLocalPoolConfigTable.
        
        Entries in this table are deleted when a remote peer deallocates
        an address from one of the IP local pool in the
        cIpLocalPoolConfigTable.
        
        Entries in this table are uniquely indexed by the name of the IP
        local pool, and the allocated address, together with its address
        type.
        
        .. attribute:: ciplocalpoolallocentry
        
        	Each entry refers to conceptual row that associates an IP addresses with the interface where the request was received, and the user that requested the address
        	**type**\: list of    :py:class:`Ciplocalpoolallocentry <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolalloctable.Ciplocalpoolallocentry>`
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CISCOIPLOCALPOOLMIB.Ciplocalpoolalloctable, self).__init__()

            self.yang_name = "cIpLocalPoolAllocTable"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cIpLocalPoolAllocEntry" : ("ciplocalpoolallocentry", CISCOIPLOCALPOOLMIB.Ciplocalpoolalloctable.Ciplocalpoolallocentry)}

            self.ciplocalpoolallocentry = YList(self)
            self._segment_path = lambda: "cIpLocalPoolAllocTable"
            self._absolute_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPLOCALPOOLMIB.Ciplocalpoolalloctable, [], name, value)


        class Ciplocalpoolallocentry(Entity):
            """
            Each entry refers to conceptual row that associates an IP
            addresses with the interface where the request was received, and
            the user that requested the address.
            
            .. attribute:: ciplocalpoolname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..48
            
            	**refers to**\:  :py:class:`ciplocalpoolname <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry>`
            
            .. attribute:: ciplocalpoolallocaddrtype  <key>
            
            	This object specifies the address type of cIpLocalPoolAllocAddr
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ciplocalpoolallocaddr  <key>
            
            	This object specifies the allocated IP address.  The address type of this object is described by cIpLocalPoolAllocAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciplocalpoolallocifindex
            
            	This object indicates the interface from which the allocation message was sent.  In the case that the interface can not be determined, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciplocalpoolallocuser
            
            	This object indicates the user name of the person from whom the allocation message was sent.  In the case that the user name can not be determined, the value of this object will the null string
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
            _revision = '2007-11-12'

            def __init__(self):
                super(CISCOIPLOCALPOOLMIB.Ciplocalpoolalloctable.Ciplocalpoolallocentry, self).__init__()

                self.yang_name = "cIpLocalPoolAllocEntry"
                self.yang_parent_name = "cIpLocalPoolAllocTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciplocalpoolname = YLeaf(YType.str, "cIpLocalPoolName")

                self.ciplocalpoolallocaddrtype = YLeaf(YType.enumeration, "cIpLocalPoolAllocAddrType")

                self.ciplocalpoolallocaddr = YLeaf(YType.str, "cIpLocalPoolAllocAddr")

                self.ciplocalpoolallocifindex = YLeaf(YType.int32, "cIpLocalPoolAllocIfIndex")

                self.ciplocalpoolallocuser = YLeaf(YType.str, "cIpLocalPoolAllocUser")
                self._segment_path = lambda: "cIpLocalPoolAllocEntry" + "[cIpLocalPoolName='" + self.ciplocalpoolname.get() + "']" + "[cIpLocalPoolAllocAddrType='" + self.ciplocalpoolallocaddrtype.get() + "']" + "[cIpLocalPoolAllocAddr='" + self.ciplocalpoolallocaddr.get() + "']"
                self._absolute_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/cIpLocalPoolAllocTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPLOCALPOOLMIB.Ciplocalpoolalloctable.Ciplocalpoolallocentry, ['ciplocalpoolname', 'ciplocalpoolallocaddrtype', 'ciplocalpoolallocaddr', 'ciplocalpoolallocifindex', 'ciplocalpoolallocuser'], name, value)


    class Ciplocalpoolconfig(Entity):
        """
        
        
        .. attribute:: ciplocalpoolnotificationsenable
        
        	An indication of whether the notifications defined by the ciscoIpLocalPoolNotifGroup are enabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CISCOIPLOCALPOOLMIB.Ciplocalpoolconfig, self).__init__()

            self.yang_name = "cIpLocalPoolConfig"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.ciplocalpoolnotificationsenable = YLeaf(YType.boolean, "cIpLocalPoolNotificationsEnable")
            self._segment_path = lambda: "cIpLocalPoolConfig"
            self._absolute_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPLOCALPOOLMIB.Ciplocalpoolconfig, ['ciplocalpoolnotificationsenable'], name, value)


    class Ciplocalpoolconfigtable(Entity):
        """
        This table manages the creation, modification, and deletion
        of IP local pools using the RowStatus textual convention.  An
        entry in this table defines an IP address range that is
        associated with an IP local pool.
        
        A conceptual row in this table can not be modified while
        cIpLocalPoolRowStatus is set to 'active'.
        
        Since IP local pool names are unique even when they belong to
        different groups, and addresses within a group can not overlap,
        a row in this table is uniquely indexed by the pool name, and by
        the low address of the IP local pool together with its address
        type.
        
        .. attribute:: ciplocalpoolconfigentry
        
        	Each entry provides information about a particular IP local pool, including the number of free and used addresses and its priority
        	**type**\: list of    :py:class:`Ciplocalpoolconfigentry <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry>`
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CISCOIPLOCALPOOLMIB.Ciplocalpoolconfigtable, self).__init__()

            self.yang_name = "cIpLocalPoolConfigTable"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cIpLocalPoolConfigEntry" : ("ciplocalpoolconfigentry", CISCOIPLOCALPOOLMIB.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry)}

            self.ciplocalpoolconfigentry = YList(self)
            self._segment_path = lambda: "cIpLocalPoolConfigTable"
            self._absolute_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPLOCALPOOLMIB.Ciplocalpoolconfigtable, [], name, value)


        class Ciplocalpoolconfigentry(Entity):
            """
            Each entry provides information about a particular IP local
            pool, including the number of free and used addresses and its priority.
            
            .. attribute:: ciplocalpoolname  <key>
            
            	An arbitrary non\-empty string that uniquely identifies the IP local pool.  This name must be unique among all the local IP pools even when they belong to different pool groups
            	**type**\:  str
            
            	**length:** 1..48
            
            .. attribute:: ciplocalpooladdrtype  <key>
            
            	This object specifies the address type of cIpLocalPoolAddressLo and cIpLocalPoolAddressHi
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ciplocalpooladdresslo  <key>
            
            	This object specifies the first IP address of the range of IP addresses contained by this pool entry.  The address type of this object is described by cIpLocalPoolAddrType.  This address must be less than or equal to the address in cIpLocalPoolAddressHi
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciplocalpooladdresshi
            
            	This object specifies the last IP address of the range of IP addresses mapped by this pool entry.  The address type of this object is described by cIpLocalPoolAddrType.  If only a single address is being mapped, the value of this object is equal to the value of cIpLocalPoolAddressLo
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciplocalpoolfreeaddrs
            
            	The number of IP addresses available for use in the range of IP addresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolgroupcontainedin
            
            	This object relates an IP local pool to its IP pool group.  A null string indicates this IP local pool is not contained in a named IP pool group, but that it is contained in the base IP pool group.  An IP local pool can only belong to one IP pool group
            	**type**\:  str
            
            	**length:** 0..48
            
            .. attribute:: ciplocalpoolinuseaddrs
            
            	The number of IP addresses being used in the range of IP addresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolpriority
            
            	This object specifies priority of the IP local pool, where smaller value indicates the lower priority. The priority value is used in assigning IP Address  from local pools
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: ciplocalpoolrowstatus
            
            	This object facilitates the creation, or deletion of a conceptual row in this table
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
            _revision = '2007-11-12'

            def __init__(self):
                super(CISCOIPLOCALPOOLMIB.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry, self).__init__()

                self.yang_name = "cIpLocalPoolConfigEntry"
                self.yang_parent_name = "cIpLocalPoolConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciplocalpoolname = YLeaf(YType.str, "cIpLocalPoolName")

                self.ciplocalpooladdrtype = YLeaf(YType.enumeration, "cIpLocalPoolAddrType")

                self.ciplocalpooladdresslo = YLeaf(YType.str, "cIpLocalPoolAddressLo")

                self.ciplocalpooladdresshi = YLeaf(YType.str, "cIpLocalPoolAddressHi")

                self.ciplocalpoolfreeaddrs = YLeaf(YType.uint32, "cIpLocalPoolFreeAddrs")

                self.ciplocalpoolgroupcontainedin = YLeaf(YType.str, "cIpLocalPoolGroupContainedIn")

                self.ciplocalpoolinuseaddrs = YLeaf(YType.uint32, "cIpLocalPoolInUseAddrs")

                self.ciplocalpoolpriority = YLeaf(YType.uint32, "cIpLocalPoolPriority")

                self.ciplocalpoolrowstatus = YLeaf(YType.enumeration, "cIpLocalPoolRowStatus")
                self._segment_path = lambda: "cIpLocalPoolConfigEntry" + "[cIpLocalPoolName='" + self.ciplocalpoolname.get() + "']" + "[cIpLocalPoolAddrType='" + self.ciplocalpooladdrtype.get() + "']" + "[cIpLocalPoolAddressLo='" + self.ciplocalpooladdresslo.get() + "']"
                self._absolute_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/cIpLocalPoolConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPLOCALPOOLMIB.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry, ['ciplocalpoolname', 'ciplocalpooladdrtype', 'ciplocalpooladdresslo', 'ciplocalpooladdresshi', 'ciplocalpoolfreeaddrs', 'ciplocalpoolgroupcontainedin', 'ciplocalpoolinuseaddrs', 'ciplocalpoolpriority', 'ciplocalpoolrowstatus'], name, value)


    class Ciplocalpoolgroupcontainstable(Entity):
        """
        A table which exposes the container/'containee' relationships
        between local IP pools and IP pool groups.
        
        Entries in this table are created or deleted as a by\-product of
        creating or deleting entries in the cIpLocalPoolConfigTable.
        
        When an entry is created and activated in the
        cIpLocalPoolConfigTable table, an entry in this table will come
        into existence if it does not already exist.
        
        When an entry is deleted in the cIpLocalPoolConfigTable table,
        if there is no other entry existing in that table with the same
        cIpLocalPoolGroupContainedIn and cIpLocalPoolName, the entry in
        this table with the respective cIpLocalPoolGroupName and
        cIpLocalPoolName indices will be removed.
        
        .. attribute:: ciplocalpoolgroupcontainsentry
        
        	Each entry describes single container/'containee' relationship.  Pool names can only be associated with one group.  Pools carry implicit group identifiers because pool names can only be associated with one group.  An entry in this table describes such an association
        	**type**\: list of    :py:class:`Ciplocalpoolgroupcontainsentry <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry>`
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CISCOIPLOCALPOOLMIB.Ciplocalpoolgroupcontainstable, self).__init__()

            self.yang_name = "cIpLocalPoolGroupContainsTable"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cIpLocalPoolGroupContainsEntry" : ("ciplocalpoolgroupcontainsentry", CISCOIPLOCALPOOLMIB.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry)}

            self.ciplocalpoolgroupcontainsentry = YList(self)
            self._segment_path = lambda: "cIpLocalPoolGroupContainsTable"
            self._absolute_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPLOCALPOOLMIB.Ciplocalpoolgroupcontainstable, [], name, value)


        class Ciplocalpoolgroupcontainsentry(Entity):
            """
            Each entry describes single container/'containee'
            relationship.
            
            Pool names can only be associated with one group.  Pools carry
            implicit group identifiers because pool names can only be
            associated with one group.  An entry in this table describes
            such an association.
            
            .. attribute:: ciplocalpoolgroupname  <key>
            
            	A unique group name that identifies the IP pool group.  The null string represents the base IP pool group
            	**type**\:  str
            
            	**length:** 0..48
            
            .. attribute:: ciplocalpoolchildindex  <key>
            
            	The value of cIpLocalPoolName for the contained IP local pool
            	**type**\:  str
            
            	**length:** 1..48
            
            

            """

            _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
            _revision = '2007-11-12'

            def __init__(self):
                super(CISCOIPLOCALPOOLMIB.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry, self).__init__()

                self.yang_name = "cIpLocalPoolGroupContainsEntry"
                self.yang_parent_name = "cIpLocalPoolGroupContainsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciplocalpoolgroupname = YLeaf(YType.str, "cIpLocalPoolGroupName")

                self.ciplocalpoolchildindex = YLeaf(YType.str, "cIpLocalPoolChildIndex")
                self._segment_path = lambda: "cIpLocalPoolGroupContainsEntry" + "[cIpLocalPoolGroupName='" + self.ciplocalpoolgroupname.get() + "']" + "[cIpLocalPoolChildIndex='" + self.ciplocalpoolchildindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/cIpLocalPoolGroupContainsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPLOCALPOOLMIB.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry, ['ciplocalpoolgroupname', 'ciplocalpoolchildindex'], name, value)


    class Ciplocalpoolgrouptable(Entity):
        """
        This table provides statistics for configured IP pool groups.
        
        Entries in this table are created as the result of adding a new
        IP pool group to the cIpLocalPoolConfigTable.
        
        Entries in this table are deleted as the result of removing all
        IP local pools that are contained in an IP pool group in the
        cIpLocalPoolConfigTable.
        
        An entry in this table is uniquely indexed by IP pool group
        name.
        
        .. attribute:: ciplocalpoolgroupentry
        
        	Each entry provides information about a particular IP pool group and the number of free and used addresses in an IP pool group
        	**type**\: list of    :py:class:`Ciplocalpoolgroupentry <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry>`
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CISCOIPLOCALPOOLMIB.Ciplocalpoolgrouptable, self).__init__()

            self.yang_name = "cIpLocalPoolGroupTable"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cIpLocalPoolGroupEntry" : ("ciplocalpoolgroupentry", CISCOIPLOCALPOOLMIB.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry)}

            self.ciplocalpoolgroupentry = YList(self)
            self._segment_path = lambda: "cIpLocalPoolGroupTable"
            self._absolute_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPLOCALPOOLMIB.Ciplocalpoolgrouptable, [], name, value)


        class Ciplocalpoolgroupentry(Entity):
            """
            Each entry provides information about a particular IP pool
            group and the number of free and used addresses in an IP pool
            group.
            
            .. attribute:: ciplocalpoolgroupname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..48
            
            	**refers to**\:  :py:class:`ciplocalpoolgroupname <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry>`
            
            .. attribute:: ciplocalpoolgroupfreeaddrs
            
            	The number of IP addresses available for use in the IP pool group
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolgroupinuseaddrs
            
            	The number of IP addresses that have been allocated from the IP pool group
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
            _revision = '2007-11-12'

            def __init__(self):
                super(CISCOIPLOCALPOOLMIB.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry, self).__init__()

                self.yang_name = "cIpLocalPoolGroupEntry"
                self.yang_parent_name = "cIpLocalPoolGroupTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciplocalpoolgroupname = YLeaf(YType.str, "cIpLocalPoolGroupName")

                self.ciplocalpoolgroupfreeaddrs = YLeaf(YType.uint32, "cIpLocalPoolGroupFreeAddrs")

                self.ciplocalpoolgroupinuseaddrs = YLeaf(YType.uint32, "cIpLocalPoolGroupInUseAddrs")
                self._segment_path = lambda: "cIpLocalPoolGroupEntry" + "[cIpLocalPoolGroupName='" + self.ciplocalpoolgroupname.get() + "']"
                self._absolute_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/cIpLocalPoolGroupTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPLOCALPOOLMIB.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry, ['ciplocalpoolgroupname', 'ciplocalpoolgroupfreeaddrs', 'ciplocalpoolgroupinuseaddrs'], name, value)


    class Ciplocalpoolstatstable(Entity):
        """
        A table providing statistics for each IP local pool.
        
        Entries in this table are created as the result of adding a new
        IP local pool to the cIpLocalPoolConfigTable.
        
        Entries in this table are deleted as the result of removing all
        the address ranges that are contained in an IP local pool in the
        cIpLocalPoolConfigTable.
        
        Entries in this table are uniquely indexed by the name of the IP
        local pool.
        
        .. attribute:: ciplocalpoolstatsentry
        
        	Each entry provides statistical information about a particular IP local pool, and the total number of free and used addresses of all the ranges in an IP local pool
        	**type**\: list of    :py:class:`Ciplocalpoolstatsentry <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolstatstable.Ciplocalpoolstatsentry>`
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CISCOIPLOCALPOOLMIB.Ciplocalpoolstatstable, self).__init__()

            self.yang_name = "cIpLocalPoolStatsTable"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cIpLocalPoolStatsEntry" : ("ciplocalpoolstatsentry", CISCOIPLOCALPOOLMIB.Ciplocalpoolstatstable.Ciplocalpoolstatsentry)}

            self.ciplocalpoolstatsentry = YList(self)
            self._segment_path = lambda: "cIpLocalPoolStatsTable"
            self._absolute_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIPLOCALPOOLMIB.Ciplocalpoolstatstable, [], name, value)


        class Ciplocalpoolstatsentry(Entity):
            """
            Each entry provides statistical information about a particular
            IP local pool, and the total number of free and used addresses
            of all the ranges in an IP local pool.
            
            .. attribute:: ciplocalpoolname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..48
            
            	**refers to**\:  :py:class:`ciplocalpoolname <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry>`
            
            .. attribute:: ciplocalpoolpercentaddrthldhi
            
            	When the percentage of used addresses in an IP local pool is equal or exceeds this threshold value, a cilpPercentAddrUsedHiNotif notification will be generated. Once the notification is generated, it will be disarmed and it will not be generated again until the number of used addresses falls below the value indicated by cIpLocalPoolPercentAddrThldLo.  The value of this object should never be smaller than the value of cIpLocalPoolPercentAddrThldLo
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: ciplocalpoolpercentaddrthldlo
            
            	When the percentage of used addresses in an IP local pool falls below this threshold value, a cilpPercentAddrUsedLoNotif notification will be generated.  Once the notification is generated, it will be disarmed and it will not be generated again until the number of used addresses equals or exceeds the value indicated by cIpLocalPoolPercentAddrThldHi.  The value of this object should never be greater than the value of cIpLocalPoolPercentAddrThldHi
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: ciplocalpoolstatfreeaddrs
            
            	The number of IP addresses available for use in this IP local pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstathiwaterusedaddrs
            
            	This object contains the high water mark of used addresses in an IP local pool since pool creation, since the system was restarted, or since this object was reset, whichever occurred last.  This object can only be set to zero, and by doing so, it is reset to the value of cIpLocalPoolStatInUseAddrs.  Since the number of addresses in a pool can be reduced (e.g. by deleting one of its ranges), the value of this object may be greater than the sum of cIpLocalPoolStatFreeAddrs and cIpLocalPoolStatInUseAddrs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstatinuseaddrs
            
            	The number of IP addresses being used in this IP local pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstatinuseaddrthldhi
            
            	When the number of used addresses in an IP local pool is equal or exceeds this threshold value, a ciscoIpLocalPoolInUseAddrNoti notification will be generated. Once this notification is generated, it will be disarmed and it will not be generated again until the number of used address falls below the value indicated by cIpLocalPoolStatInUseAddrThldLo.  The value of this object should never be smaller than the value of cIpLocalPoolStatInUseAddrThldLo
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstatinuseaddrthldlo
            
            	When the number of used addresses in an IP local pool falls below this threshold value, the ciscoIpLocalPoolInUseAddrNoti notification will be rearmed.  The value of this object should never be greater than the value of cIpLocalPoolStatInUseAddrThldHi
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
            _revision = '2007-11-12'

            def __init__(self):
                super(CISCOIPLOCALPOOLMIB.Ciplocalpoolstatstable.Ciplocalpoolstatsentry, self).__init__()

                self.yang_name = "cIpLocalPoolStatsEntry"
                self.yang_parent_name = "cIpLocalPoolStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciplocalpoolname = YLeaf(YType.str, "cIpLocalPoolName")

                self.ciplocalpoolpercentaddrthldhi = YLeaf(YType.uint32, "cIpLocalPoolPercentAddrThldHi")

                self.ciplocalpoolpercentaddrthldlo = YLeaf(YType.uint32, "cIpLocalPoolPercentAddrThldLo")

                self.ciplocalpoolstatfreeaddrs = YLeaf(YType.uint32, "cIpLocalPoolStatFreeAddrs")

                self.ciplocalpoolstathiwaterusedaddrs = YLeaf(YType.uint32, "cIpLocalPoolStatHiWaterUsedAddrs")

                self.ciplocalpoolstatinuseaddrs = YLeaf(YType.uint32, "cIpLocalPoolStatInUseAddrs")

                self.ciplocalpoolstatinuseaddrthldhi = YLeaf(YType.uint32, "cIpLocalPoolStatInUseAddrThldHi")

                self.ciplocalpoolstatinuseaddrthldlo = YLeaf(YType.uint32, "cIpLocalPoolStatInUseAddrThldLo")
                self._segment_path = lambda: "cIpLocalPoolStatsEntry" + "[cIpLocalPoolName='" + self.ciplocalpoolname.get() + "']"
                self._absolute_path = lambda: "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/cIpLocalPoolStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIPLOCALPOOLMIB.Ciplocalpoolstatstable.Ciplocalpoolstatsentry, ['ciplocalpoolname', 'ciplocalpoolpercentaddrthldhi', 'ciplocalpoolpercentaddrthldlo', 'ciplocalpoolstatfreeaddrs', 'ciplocalpoolstathiwaterusedaddrs', 'ciplocalpoolstatinuseaddrs', 'ciplocalpoolstatinuseaddrthldhi', 'ciplocalpoolstatinuseaddrthldlo'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIPLOCALPOOLMIB()
        return self._top_entity
