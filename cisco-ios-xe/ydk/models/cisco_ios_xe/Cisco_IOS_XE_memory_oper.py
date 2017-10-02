""" Cisco_IOS_XE_memory_oper 

This module contains a collection of YANG definitions for
monitoring memory in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MemoryStatistics(Entity):
    """
    Data nodes for All Memory Pool Statistics.
    
    .. attribute:: memory_statistic
    
    	The list of software memory pools in the system
    	**type**\: list of    :py:class:`MemoryStatistic <ydk.models.cisco_ios_xe.Cisco_IOS_XE_memory_oper.MemoryStatistics.MemoryStatistic>`
    
    

    """

    _prefix = 'memory-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(MemoryStatistics, self).__init__()
        self._top_entity = None

        self.yang_name = "memory-statistics"
        self.yang_parent_name = "Cisco-IOS-XE-memory-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"memory-statistic" : ("memory_statistic", MemoryStatistics.MemoryStatistic)}

        self.memory_statistic = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-memory-oper:memory-statistics"

    def __setattr__(self, name, value):
        self._perform_setattr(MemoryStatistics, [], name, value)


    class MemoryStatistic(Entity):
        """
        The list of software memory pools in the system.
        
        .. attribute:: name  <key>
        
        	The name of the memory pool
        	**type**\:  str
        
        .. attribute:: free_memory
        
        	Total free memory in the pool (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: highest_usage
        
        	Historical highest memory usage (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: lowest_usage
        
        	Historical lowest memory usage (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: total_memory
        
        	Total memory in the pool (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: used_memory
        
        	Total used memory in the pool (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        

        """

        _prefix = 'memory-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(MemoryStatistics.MemoryStatistic, self).__init__()

            self.yang_name = "memory-statistic"
            self.yang_parent_name = "memory-statistics"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.name = YLeaf(YType.str, "name")

            self.free_memory = YLeaf(YType.uint64, "free-memory")

            self.highest_usage = YLeaf(YType.uint64, "highest-usage")

            self.lowest_usage = YLeaf(YType.uint64, "lowest-usage")

            self.total_memory = YLeaf(YType.uint64, "total-memory")

            self.used_memory = YLeaf(YType.uint64, "used-memory")
            self._segment_path = lambda: "memory-statistic" + "[name='" + self.name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-memory-oper:memory-statistics/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MemoryStatistics.MemoryStatistic, ['name', 'free_memory', 'highest_usage', 'lowest_usage', 'total_memory', 'used_memory'], name, value)

    def clone_ptr(self):
        self._top_entity = MemoryStatistics()
        return self._top_entity
