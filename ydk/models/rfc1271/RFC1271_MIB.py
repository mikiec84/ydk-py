""" RFC1271_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class EntryStatus_Enum(Enum):
    """
    EntryStatus_Enum

    """

    VALID = 1

    CREATEREQUEST = 2

    UNDERCREATION = 3

    INVALID = 4


    @staticmethod
    def _meta_info():
        from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
        return meta._meta_table['EntryStatus_Enum']



class RFC1271MIB(object):
    """
    
    
    .. attribute:: alarmtable
    
    	A list of alarm entries
    	**type**\: :py:class:`AlarmTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.AlarmTable>`
    
    .. attribute:: buffercontroltable
    
    	A list of buffers control entries
    	**type**\: :py:class:`BufferControlTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.BufferControlTable>`
    
    .. attribute:: capturebuffertable
    
    	A list of packets captured off of a channel
    	**type**\: :py:class:`CaptureBufferTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.CaptureBufferTable>`
    
    .. attribute:: channeltable
    
    	A list of packet channel entries
    	**type**\: :py:class:`ChannelTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.ChannelTable>`
    
    .. attribute:: etherhistorytable
    
    	A list of Ethernet history entries
    	**type**\: :py:class:`EtherHistoryTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.EtherHistoryTable>`
    
    .. attribute:: etherstatstable
    
    	A list of Ethernet statistics entries
    	**type**\: :py:class:`EtherStatsTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.EtherStatsTable>`
    
    .. attribute:: eventtable
    
    	A list of events to be generated
    	**type**\: :py:class:`EventTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.EventTable>`
    
    .. attribute:: filtertable
    
    	A list of packet filter entries
    	**type**\: :py:class:`FilterTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.FilterTable>`
    
    .. attribute:: historycontroltable
    
    	A list of history control entries
    	**type**\: :py:class:`HistoryControlTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HistoryControlTable>`
    
    .. attribute:: hostcontroltable
    
    	A list of host table control entries
    	**type**\: :py:class:`HostControlTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HostControlTable>`
    
    .. attribute:: hosttable
    
    	A list of host entries
    	**type**\: :py:class:`HostTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HostTable>`
    
    .. attribute:: hosttimetable
    
    	A list of time\-ordered host table entries
    	**type**\: :py:class:`HostTimeTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HostTimeTable>`
    
    .. attribute:: hosttopncontroltable
    
    	A list of top N host control entries
    	**type**\: :py:class:`HostTopNControlTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HostTopNControlTable>`
    
    .. attribute:: hosttopntable
    
    	A list of top N host entries
    	**type**\: :py:class:`HostTopNTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HostTopNTable>`
    
    .. attribute:: logtable
    
    	A list of events that have been logged
    	**type**\: :py:class:`LogTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.LogTable>`
    
    .. attribute:: matrixcontroltable
    
    	A list of information entries for the traffic matrix on each interface
    	**type**\: :py:class:`MatrixControlTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.MatrixControlTable>`
    
    .. attribute:: matrixdstable
    
    	A list of traffic matrix entries indexed by destination and source MAC address
    	**type**\: :py:class:`MatrixDSTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.MatrixDSTable>`
    
    .. attribute:: matrixsdtable
    
    	A list of traffic matrix entries indexed by source and destination MAC address
    	**type**\: :py:class:`MatrixSDTable <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.MatrixSDTable>`
    
    

    """

    _prefix = 'rfc1271-mib'

    def __init__(self):
        self.alarmtable = RFC1271MIB.AlarmTable()
        self.alarmtable.parent = self
        self.buffercontroltable = RFC1271MIB.BufferControlTable()
        self.buffercontroltable.parent = self
        self.capturebuffertable = RFC1271MIB.CaptureBufferTable()
        self.capturebuffertable.parent = self
        self.channeltable = RFC1271MIB.ChannelTable()
        self.channeltable.parent = self
        self.etherhistorytable = RFC1271MIB.EtherHistoryTable()
        self.etherhistorytable.parent = self
        self.etherstatstable = RFC1271MIB.EtherStatsTable()
        self.etherstatstable.parent = self
        self.eventtable = RFC1271MIB.EventTable()
        self.eventtable.parent = self
        self.filtertable = RFC1271MIB.FilterTable()
        self.filtertable.parent = self
        self.historycontroltable = RFC1271MIB.HistoryControlTable()
        self.historycontroltable.parent = self
        self.hostcontroltable = RFC1271MIB.HostControlTable()
        self.hostcontroltable.parent = self
        self.hosttable = RFC1271MIB.HostTable()
        self.hosttable.parent = self
        self.hosttimetable = RFC1271MIB.HostTimeTable()
        self.hosttimetable.parent = self
        self.hosttopncontroltable = RFC1271MIB.HostTopNControlTable()
        self.hosttopncontroltable.parent = self
        self.hosttopntable = RFC1271MIB.HostTopNTable()
        self.hosttopntable.parent = self
        self.logtable = RFC1271MIB.LogTable()
        self.logtable.parent = self
        self.matrixcontroltable = RFC1271MIB.MatrixControlTable()
        self.matrixcontroltable.parent = self
        self.matrixdstable = RFC1271MIB.MatrixDSTable()
        self.matrixdstable.parent = self
        self.matrixsdtable = RFC1271MIB.MatrixSDTable()
        self.matrixsdtable.parent = self


    class AlarmTable(object):
        """
        A list of alarm entries.
        
        .. attribute:: alarmentry
        
        	A list of parameters that set up a periodic checking for alarm conditions
        	**type**\: list of :py:class:`AlarmEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.AlarmTable.AlarmEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.alarmentry = YList()
            self.alarmentry.parent = self
            self.alarmentry.name = 'alarmentry'


        class AlarmEntry(object):
            """
            A list of parameters that set up a periodic checking
            for alarm conditions.
            
            .. attribute:: alarmindex
            
            	An index that uniquely identifies an entry in the alarm table.  Each such entry defines a diagnostic sample at a particular interval for an object on the device
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: alarmfallingeventindex
            
            	The index of the eventEntry that is used when a falling threshold is crossed.  The eventEntry identified by a particular value of this index is the same as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In particular, if this value is zero, no associated event will be generated, as zero is not a valid event index.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: alarmfallingthreshold
            
            	A threshold for the sampled statistic.  When the current sampled value is less than or equal to this threshold, and the value at the last sampling interval was greater than this threshold, a single event will be generated. A single event will also be generated if the first sample after this entry becomes valid is less than or equal to this threshold and the associated alarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3).  After a falling event is generated, another such event will not be generated until the sampled value rises above this threshold and reaches the alarmRisingThreshold.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: alarminterval
            
            	The interval in seconds over which the data is sampled and compared with the rising and falling thresholds.  When setting this variable, care should be given to ensure that the variable being monitored will not exceed 2^31 \- 1 and roll over the alarmValue object during the interval.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: alarmowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: alarmrisingeventindex
            
            	The index of the eventEntry that is used when a rising threshold is crossed.  The eventEntry identified by a particular value of this index is the same as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In particular, if this value is zero, no associated event will be generated, as zero is not a valid event index.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: alarmrisingthreshold
            
            	A threshold for the sampled statistic.  When the current sampled value is greater than or equal to this threshold, and the value at the last sampling interval was less than this threshold, a single event will be generated. A single event will also be generated if the first sample after this entry becomes valid is greater than or equal to this threshold and the associated alarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3).  After a rising event is generated, another such event will not be generated until the sampled value falls below this threshold and reaches the alarmFallingThreshold.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: alarmsampletype
            
            	The method of sampling the selected variable and calculating the value to be compared against the thresholds.  If the value of this object is absoluteValue(1), the value of the selected variable will be compared directly with the thresholds at the end of the sampling interval.  If the value of this object is deltaValue(2), the value of the selected variable at the last sample will be subtracted from the current value, and the difference compared with the thresholds.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: :py:class:`AlarmSampleType_Enum <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.AlarmTable.AlarmEntry.AlarmSampleType_Enum>`
            
            .. attribute:: alarmstartupalarm
            
            	The alarm that may be sent when this entry is first set to valid.  If the first sample after this entry becomes valid is greater than or equal to the risingThreshold and alarmStartupAlarm is equal to risingAlarm(1) or risingOrFallingAlarm(3), then a single rising alarm will be generated.  If the first sample after this entry becomes valid is less than or equal to the fallingThreshold and alarmStartupAlarm is equal to fallingAlarm(2) or risingOrFallingAlarm(3), then a single falling alarm will be generated.  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: :py:class:`AlarmStartupAlarm_Enum <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.AlarmTable.AlarmEntry.AlarmStartupAlarm_Enum>`
            
            .. attribute:: alarmstatus
            
            	The status of this alarm entry
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.EntryStatus_Enum>`
            
            .. attribute:: alarmvalue
            
            	The value of the statistic during the last sampling period.  The value during the current sampling period is not made available until the period is completed
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: alarmvariable
            
            	The object identifier of the particular variable to be sampled.  Only variables that resolve to an ASN.1 primitive type of INTEGER (INTEGER, Counter, Gauge, or TimeTicks) may be sampled.  Because SNMP access control is articulated entirely in terms of the contents of MIB views, no access control mechanism exists that can restrict the value of this object to identify only those objects that exist in a particular MIB view.  Because there is thus no acceptable means of restricting the read access that could be obtained through the alarm mechanism, the probe must only grant write access to this object in those views that have read access to all objects on the probe.  During a set operation, if the supplied variable name is not available in the selected MIB view, a badValue error must be returned.  If at any time the variable name of an established alarmEntry is no longer available in the selected MIB view, the probe must change the status of this alarmEntry to invalid(4).  This object may not be modified if the associated alarmStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.alarmindex = None
                self.alarmfallingeventindex = None
                self.alarmfallingthreshold = None
                self.alarminterval = None
                self.alarmowner = None
                self.alarmrisingeventindex = None
                self.alarmrisingthreshold = None
                self.alarmsampletype = None
                self.alarmstartupalarm = None
                self.alarmstatus = None
                self.alarmvalue = None
                self.alarmvariable = None

            class AlarmSampleType_Enum(Enum):
                """
                AlarmSampleType_Enum

                The method of sampling the selected variable and
                calculating the value to be compared against the
                thresholds.  If the value of this object is
                absoluteValue(1), the value of the selected variable
                will be compared directly with the thresholds at the
                end of the sampling interval.  If the value of this
                object is deltaValue(2), the value of the selected
                variable at the last sample will be subtracted from
                the current value, and the difference compared with
                the thresholds.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).

                """

                ABSOLUTEVALUE = 1

                DELTAVALUE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                    return meta._meta_table['RFC1271MIB.AlarmTable.AlarmEntry.AlarmSampleType_Enum']


            class AlarmStartupAlarm_Enum(Enum):
                """
                AlarmStartupAlarm_Enum

                The alarm that may be sent when this entry is first
                set to valid.  If the first sample after this entry
                becomes valid is greater than or equal to the
                risingThreshold and alarmStartupAlarm is equal to
                risingAlarm(1) or risingOrFallingAlarm(3), then a
                single rising alarm will be generated.  If the first
                sample after this entry becomes valid is less than
                or equal to the fallingThreshold and
                alarmStartupAlarm is equal to fallingAlarm(2) or
                risingOrFallingAlarm(3), then a single falling
                alarm will be generated.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).

                """

                RISINGALARM = 1

                FALLINGALARM = 2

                RISINGORFALLINGALARM = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                    return meta._meta_table['RFC1271MIB.AlarmTable.AlarmEntry.AlarmStartupAlarm_Enum']


            @property
            def _common_path(self):
                if self.alarmindex is None:
                    raise YPYDataValidationError('Key property alarmindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:alarmTable/RFC1271-MIB:alarmEntry[RFC1271-MIB:alarmIndex = ' + str(self.alarmindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.alarmindex is not None:
                    return True

                if self.alarmfallingeventindex is not None:
                    return True

                if self.alarmfallingthreshold is not None:
                    return True

                if self.alarminterval is not None:
                    return True

                if self.alarmowner is not None:
                    return True

                if self.alarmrisingeventindex is not None:
                    return True

                if self.alarmrisingthreshold is not None:
                    return True

                if self.alarmsampletype is not None:
                    return True

                if self.alarmstartupalarm is not None:
                    return True

                if self.alarmstatus is not None:
                    return True

                if self.alarmvalue is not None:
                    return True

                if self.alarmvariable is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.AlarmTable.AlarmEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:alarmTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.alarmentry is not None:
                for child_ref in self.alarmentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.AlarmTable']['meta_info']


    class BufferControlTable(object):
        """
        A list of buffers control entries.
        
        .. attribute:: buffercontrolentry
        
        	A set of parameters that control the collection of a stream of packets that have matched filters
        	**type**\: list of :py:class:`BufferControlEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.BufferControlTable.BufferControlEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.buffercontrolentry = YList()
            self.buffercontrolentry.parent = self
            self.buffercontrolentry.name = 'buffercontrolentry'


        class BufferControlEntry(object):
            """
            A set of parameters that control the collection of
            a stream of packets that have matched filters.
            
            .. attribute:: buffercontrolindex
            
            	An index that uniquely identifies an entry in the bufferControl table.  The value of this index shall never be zero.  Each such entry defines one set of packets that is captured and controlled by one or more filters
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: buffercontrolcapturedpackets
            
            	The number of packets currently in this captureBuffer
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: buffercontrolcaptureslicesize
            
            	The maximum number of octets of each packet that will be saved in this capture buffer. For example, if a 1500 octet packet is received by the probe and this object is set to 500, then only 500 octets of the packet will be stored in the associated capture buffer.  If this variable is set to 0, the capture buffer will save as many octets as is possible.  This object may not be modified if the associated bufferControlStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: buffercontrolchannelindex
            
            	An index that identifies the channel that is the source of packets for this bufferControl table. The channel identified by a particular value of this index is the same as identified by the same value of the channelIndex object.  This object may not be modified if the associated bufferControlStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: buffercontroldownloadoffset
            
            	The offset of the first octet of each packet in this capture buffer that will be returned in an SNMP retrieval of that packet.  For example, if 500 octets of a packet have been stored in the associated capture buffer and this object is set to 100, then the captureBufferPacket object that contains the packet will contain bytes starting 100 octets into the packet
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: buffercontroldownloadslicesize
            
            	The maximum number of octets of each packet in this capture buffer that will be returned in an SNMP retrieval of that packet.  For example, if 500 octets of a packet have been stored in the associated capture buffer, the associated bufferControlDownloadOffset is 0, and this object is set to 100, then the captureBufferPacket object that contains the packet will contain only the first 100 octets of the packet.  A prudent manager will take into account possible interoperability or fragmentation problems that may occur if the download slice size is set too large. In particular, conformant SNMP implementations are not required to accept messages whose length exceeds 484 octets, although they are encouraged to support larger datagrams whenever feasible
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: buffercontrolfullaction
            
            	Controls the action of the buffer when it reaches the full status.  When in the lockWhenFull(1) state a packet is added to the buffer that fills the buffer, the bufferControlFullStatus will be set to full(2) and this buffer will stop capturing packets
            	**type**\: :py:class:`BufferControlFullAction_Enum <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.BufferControlTable.BufferControlEntry.BufferControlFullAction_Enum>`
            
            .. attribute:: buffercontrolfullstatus
            
            	This object shows whether the buffer has room to accept new packets or if it is full.  If the status is spaceAvailable(1), the buffer is accepting new packets normally.  If the status is full(2) and the associated bufferControlFullAction object is wrapWhenFull, the buffer is accepting new packets by deleting enough of the oldest packets to make room for new ones as they arrive.  Otherwise, if the status is full(2) and the bufferControlFullAction object is lockWhenFull, then the buffer has stopped collecting packets.  When this object is set to full(2) the probe must not later set it to spaceAvailable(1) except in the case of a significant gain in resources such as an increase of bufferControlOctetsGranted.  In particular, the wrap\-mode action of deleting old packets to make room for newly arrived packets must not affect the value of this object
            	**type**\: :py:class:`BufferControlFullStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.BufferControlTable.BufferControlEntry.BufferControlFullStatus_Enum>`
            
            .. attribute:: buffercontrolmaxoctetsgranted
            
            	The maximum number of octets that can be saved in this captureBuffer, including overhead. If this variable is \-1, the capture buffer will save as many octets as possible.  When the bufferControlMaxOctetsRequested object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular probe implementation and available resources.  However, if the request object has the special value of \-1, the probe must set this object to \-1.  The probe must not lower this value except as a result of a modification to the associated bufferControlMaxOctetsRequested object.  When this maximum number of octets is reached and a new packet is to be added to this capture buffer and the corresponding bufferControlFullAction is set to wrapWhenFull(2), enough of the oldest packets associated with this capture buffer shall be deleted by the agent so that the new packet can be added.  If the corresponding bufferControlFullAction is set to lockWhenFull(1), the new packet shall be discarded. In either case, the probe must set bufferControlFullStatus to full(2).  When the value of this object changes to a value less than the current value, entries are deleted from the captureBufferTable associated with this bufferControlEntry.  Enough of the oldest of these captureBufferEntries shall be deleted by the agent so that the number of octets used remains less than or equal to the new value of this object.  When the value of this object changes to a value greater than the current value, the number of associated captureBufferEntries may be allowed to grow
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: buffercontrolmaxoctetsrequested
            
            	The requested maximum number of octets to be saved in this captureBuffer, including any implementation\-specific overhead. If this variable is set to \-1, the capture buffer will save as many octets as is possible.  When this object is created or modified, the probe should set bufferControlMaxOctetsGranted as closely to this object as is possible for the particular probe implementation and available resources.  However, if the object has the special value of \-1, the probe must set bufferControlMaxOctetsGranted to \-1
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: buffercontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: buffercontrolstatus
            
            	The status of this buffer Control Entry
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.EntryStatus_Enum>`
            
            .. attribute:: buffercontrolturnontime
            
            	The value of sysUpTime when this capture buffer was first turned on
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.buffercontrolindex = None
                self.buffercontrolcapturedpackets = None
                self.buffercontrolcaptureslicesize = None
                self.buffercontrolchannelindex = None
                self.buffercontroldownloadoffset = None
                self.buffercontroldownloadslicesize = None
                self.buffercontrolfullaction = None
                self.buffercontrolfullstatus = None
                self.buffercontrolmaxoctetsgranted = None
                self.buffercontrolmaxoctetsrequested = None
                self.buffercontrolowner = None
                self.buffercontrolstatus = None
                self.buffercontrolturnontime = None

            class BufferControlFullAction_Enum(Enum):
                """
                BufferControlFullAction_Enum

                Controls the action of the buffer when it
                reaches the full status.  When in the lockWhenFull(1)
                state a packet is added to the buffer that
                fills the buffer, the bufferControlFullStatus will
                be set to full(2) and this buffer will stop capturing
                packets.

                """

                LOCKWHENFULL = 1

                WRAPWHENFULL = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                    return meta._meta_table['RFC1271MIB.BufferControlTable.BufferControlEntry.BufferControlFullAction_Enum']


            class BufferControlFullStatus_Enum(Enum):
                """
                BufferControlFullStatus_Enum

                This object shows whether the buffer has room to
                accept new packets or if it is full.
                
                If the status is spaceAvailable(1), the buffer is
                accepting new packets normally.  If the status is
                full(2) and the associated bufferControlFullAction
                object is wrapWhenFull, the buffer is accepting new
                packets by deleting enough of the oldest packets
                to make room for new ones as they arrive.  Otherwise,
                if the status is full(2) and the
                bufferControlFullAction object is lockWhenFull,
                then the buffer has stopped collecting packets.
                
                When this object is set to full(2) the probe must
                not later set it to spaceAvailable(1) except in the
                case of a significant gain in resources such as
                an increase of bufferControlOctetsGranted.  In
                particular, the wrap\-mode action of deleting old
                packets to make room for newly arrived packets
                must not affect the value of this object.

                """

                SPACEAVAILABLE = 1

                FULL = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                    return meta._meta_table['RFC1271MIB.BufferControlTable.BufferControlEntry.BufferControlFullStatus_Enum']


            @property
            def _common_path(self):
                if self.buffercontrolindex is None:
                    raise YPYDataValidationError('Key property buffercontrolindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:bufferControlTable/RFC1271-MIB:bufferControlEntry[RFC1271-MIB:bufferControlIndex = ' + str(self.buffercontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.buffercontrolindex is not None:
                    return True

                if self.buffercontrolcapturedpackets is not None:
                    return True

                if self.buffercontrolcaptureslicesize is not None:
                    return True

                if self.buffercontrolchannelindex is not None:
                    return True

                if self.buffercontroldownloadoffset is not None:
                    return True

                if self.buffercontroldownloadslicesize is not None:
                    return True

                if self.buffercontrolfullaction is not None:
                    return True

                if self.buffercontrolfullstatus is not None:
                    return True

                if self.buffercontrolmaxoctetsgranted is not None:
                    return True

                if self.buffercontrolmaxoctetsrequested is not None:
                    return True

                if self.buffercontrolowner is not None:
                    return True

                if self.buffercontrolstatus is not None:
                    return True

                if self.buffercontrolturnontime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.BufferControlTable.BufferControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:bufferControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.buffercontrolentry is not None:
                for child_ref in self.buffercontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.BufferControlTable']['meta_info']


    class CaptureBufferTable(object):
        """
        A list of packets captured off of a channel.
        
        .. attribute:: capturebufferentry
        
        	A packet captured off of an attached network
        	**type**\: list of :py:class:`CaptureBufferEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.CaptureBufferTable.CaptureBufferEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.capturebufferentry = YList()
            self.capturebufferentry.parent = self
            self.capturebufferentry.name = 'capturebufferentry'


        class CaptureBufferEntry(object):
            """
            A packet captured off of an attached network.
            
            .. attribute:: capturebuffercontrolindex
            
            	The index of the bufferControlEntry with which this packet is associated
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: capturebufferindex
            
            	An index that uniquely identifies an entry in the captureBuffer table associated with a particular bufferControlEntry.  This index will start at 1 and increase by one for each new packet added with the same captureBufferControlIndex
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: capturebufferpacketdata
            
            	The data inside the packet, starting at the beginning of the packet plus any offset specified in the associated bufferControlDownloadOffset, including any link level headers.  The length of the data in this object is the minimum of the length of the captured packet minus the offset, the length of the associated bufferControlCaptureSliceSize minus the offset, and the associated bufferControlDownloadSliceSize.  If this minimum is less than zero, this object shall have a length of zero
            	**type**\: str
            
            .. attribute:: capturebufferpacketid
            
            	An index that describes the order of packets that are received on a particular interface. The packetID of a packet captured on an interface is defined to be greater than the packetID's of all packets captured previously on the same interface.  As the captureBufferPacketID object has a maximum positive value of 2^31 \- 1, any captureBufferPacketID object shall have the value of the associated packet's packetID mod 2^31
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: capturebufferpacketlength
            
            	The actual length (off the wire) of the packet stored in this entry, including FCS octets
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: capturebufferpacketstatus
            
            	A value which indicates the error status of this packet.  The value of this object is defined in the same way as filterPacketStatus.  The value is a sum.  This sum initially takes the value zero.  Then, for each error, E, that has been discovered in this packet, 2 raised to a value representing E is added to the sum.  The errors defined for a packet captured off of an Ethernet interface are as follows\:      bit #    Error         0    Packet is longer than 1518 octets         1    Packet is shorter than 64 octets         2    Packet experienced a CRC or Alignment              error         3    First packet in this capture buffer after              it was detected that some packets were              not processed correctly.  For example, an Ethernet fragment would have a value of 6 (2^1 + 2^2).  As this MIB is expanded to new media types, this object will have other media\-specific errors defined
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: capturebufferpackettime
            
            	The number of milliseconds that had passed since this capture buffer was first turned on when this packet was captured
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.capturebuffercontrolindex = None
                self.capturebufferindex = None
                self.capturebufferpacketdata = None
                self.capturebufferpacketid = None
                self.capturebufferpacketlength = None
                self.capturebufferpacketstatus = None
                self.capturebufferpackettime = None

            @property
            def _common_path(self):
                if self.capturebuffercontrolindex is None:
                    raise YPYDataValidationError('Key property capturebuffercontrolindex is None')
                if self.capturebufferindex is None:
                    raise YPYDataValidationError('Key property capturebufferindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:captureBufferTable/RFC1271-MIB:captureBufferEntry[RFC1271-MIB:captureBufferControlIndex = ' + str(self.capturebuffercontrolindex) + '][RFC1271-MIB:captureBufferIndex = ' + str(self.capturebufferindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.capturebuffercontrolindex is not None:
                    return True

                if self.capturebufferindex is not None:
                    return True

                if self.capturebufferpacketdata is not None:
                    return True

                if self.capturebufferpacketid is not None:
                    return True

                if self.capturebufferpacketlength is not None:
                    return True

                if self.capturebufferpacketstatus is not None:
                    return True

                if self.capturebufferpackettime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.CaptureBufferTable.CaptureBufferEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:captureBufferTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.capturebufferentry is not None:
                for child_ref in self.capturebufferentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.CaptureBufferTable']['meta_info']


    class ChannelTable(object):
        """
        A list of packet channel entries.
        
        .. attribute:: channelentry
        
        	A set of parameters for a packet channel applied on a particular interface
        	**type**\: list of :py:class:`ChannelEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.ChannelTable.ChannelEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.channelentry = YList()
            self.channelentry.parent = self
            self.channelentry.name = 'channelentry'


        class ChannelEntry(object):
            """
            A set of parameters for a packet channel applied on a
            particular interface.
            
            .. attribute:: channelindex
            
            	An index that uniquely identifies an entry in the channel table.  Each such entry defines one channel, a logical data and event stream
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: channelaccepttype
            
            	This object controls the action of the filters associated with this channel.  If this object is equal to acceptMatched(1), packets will be accepted to this channel if they are accepted by both the packet data and packet status matches of an associated filter. If this object is equal to acceptFailed(2), packets will be accepted to this channel only if they fail either the packet data match or the packet status match of each of the associated filters. This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: :py:class:`ChannelAcceptType_Enum <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.ChannelTable.ChannelEntry.ChannelAcceptType_Enum>`
            
            .. attribute:: channeldatacontrol
            
            	This object controls the flow of data through this channel.  If this object is on(1), data, status and events flow through this channel.  If this object is off(2), data, status and events will not flow through this channel
            	**type**\: :py:class:`ChannelDataControl_Enum <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.ChannelTable.ChannelEntry.ChannelDataControl_Enum>`
            
            .. attribute:: channeldescription
            
            	A comment describing this channel
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: channeleventindex
            
            	The value of this object identifies the event that is configured to be generated when the associated channelDataControl is on and a packet is matched.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelEventIndex must be set to zero, a non\-existent event index.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: channeleventstatus
            
            	The event status of this channel.  If this channel is configured to generate events when packets are matched, a means of controlling the flow of those events is often needed.  When this object is equal to eventReady(1), a single event may be generated, after which this object will be set by the probe to eventFired(2).  While in the eventFired(2) state, no events will be generated until the object is modified to eventReady(1) (or eventAlwaysReady(3)).  The management station can thus easily respond to a notification of an event by re\-enabling this object.  If the management station wishes to disable this flow control and allow events to be generated at will, this object may be set to eventAlwaysReady(3).  Disabling the flow control is discouraged as it can result in high network traffic or other performance problems
            	**type**\: :py:class:`ChannelEventStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.ChannelTable.ChannelEntry.ChannelEventStatus_Enum>`
            
            .. attribute:: channelifindex
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device to which the associated filters are applied to allow data into this channel.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in [4,6].  The filters in this group are applied to all packets on the local network segment attached to the identified interface.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: channelmatches
            
            	The number of times this channel has matched a packet. Note that this object is updated even when channelDataControl is set to off
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: channelowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: channelstatus
            
            	The status of this channel entry
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.EntryStatus_Enum>`
            
            .. attribute:: channelturnoffeventindex
            
            	The value of this object identifies the event that is configured to turn the associated channelDataControl from on to off when the event is generated.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelTurnOffEventIndex must be set to zero, a non\-existent event index.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: channelturnoneventindex
            
            	The value of this object identifies the event that is configured to turn the associated channelDataControl from off to on when the event is generated.  The event identified by a particular value of this object is the same event as identified by the same value of the eventIndex object.  If there is no corresponding entry in the eventTable, then no association exists.  In fact, if no event is intended for this channel, channelTurnOnEventIndex must be set to zero, a non\-existent event index.  This object may not be modified if the associated channelStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.channelindex = None
                self.channelaccepttype = None
                self.channeldatacontrol = None
                self.channeldescription = None
                self.channeleventindex = None
                self.channeleventstatus = None
                self.channelifindex = None
                self.channelmatches = None
                self.channelowner = None
                self.channelstatus = None
                self.channelturnoffeventindex = None
                self.channelturnoneventindex = None

            class ChannelAcceptType_Enum(Enum):
                """
                ChannelAcceptType_Enum

                This object controls the action of the filters
                associated with this channel.  If this object is equal
                to acceptMatched(1), packets will be accepted to this
                channel if they are accepted by both the packet data
                and packet status matches of an associated filter. If
                this object is equal to acceptFailed(2), packets will
                be accepted to this channel only if they fail either
                the packet data match or the packet status match of
                each of the associated filters.
                This object may not be modified if the associated
                channelStatus object is equal to valid(1).

                """

                ACCEPTMATCHED = 1

                ACCEPTFAILED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                    return meta._meta_table['RFC1271MIB.ChannelTable.ChannelEntry.ChannelAcceptType_Enum']


            class ChannelDataControl_Enum(Enum):
                """
                ChannelDataControl_Enum

                This object controls the flow of data through this
                channel.  If this object is on(1), data, status and
                events flow through this channel.  If this object is
                off(2), data, status and events will not flow through
                this channel.

                """

                ON = 1

                OFF = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                    return meta._meta_table['RFC1271MIB.ChannelTable.ChannelEntry.ChannelDataControl_Enum']


            class ChannelEventStatus_Enum(Enum):
                """
                ChannelEventStatus_Enum

                The event status of this channel.
                
                If this channel is configured to generate events
                when packets are matched, a means of controlling
                the flow of those events is often needed.  When
                this object is equal to eventReady(1), a single
                event may be generated, after which this object
                will be set by the probe to eventFired(2).  While
                in the eventFired(2) state, no events will be
                generated until the object is modified to
                eventReady(1) (or eventAlwaysReady(3)).  The
                management station can thus easily respond to a
                notification of an event by re\-enabling this object.
                
                If the management station wishes to disable this
                flow control and allow events to be generated
                at will, this object may be set to
                eventAlwaysReady(3).  Disabling the flow control
                is discouraged as it can result in high network
                traffic or other performance problems.

                """

                EVENTREADY = 1

                EVENTFIRED = 2

                EVENTALWAYSREADY = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                    return meta._meta_table['RFC1271MIB.ChannelTable.ChannelEntry.ChannelEventStatus_Enum']


            @property
            def _common_path(self):
                if self.channelindex is None:
                    raise YPYDataValidationError('Key property channelindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:channelTable/RFC1271-MIB:channelEntry[RFC1271-MIB:channelIndex = ' + str(self.channelindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.channelindex is not None:
                    return True

                if self.channelaccepttype is not None:
                    return True

                if self.channeldatacontrol is not None:
                    return True

                if self.channeldescription is not None:
                    return True

                if self.channeleventindex is not None:
                    return True

                if self.channeleventstatus is not None:
                    return True

                if self.channelifindex is not None:
                    return True

                if self.channelmatches is not None:
                    return True

                if self.channelowner is not None:
                    return True

                if self.channelstatus is not None:
                    return True

                if self.channelturnoffeventindex is not None:
                    return True

                if self.channelturnoneventindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.ChannelTable.ChannelEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:channelTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.channelentry is not None:
                for child_ref in self.channelentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.ChannelTable']['meta_info']


    class EtherHistoryTable(object):
        """
        A list of Ethernet history entries.
        
        .. attribute:: etherhistoryentry
        
        	An historical sample of Ethernet statistics on a particular Ethernet interface.  This sample is associated with the historyControlEntry which set up the parameters for a regular collection of these samples
        	**type**\: list of :py:class:`EtherHistoryEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.EtherHistoryTable.EtherHistoryEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.etherhistoryentry = YList()
            self.etherhistoryentry.parent = self
            self.etherhistoryentry.name = 'etherhistoryentry'


        class EtherHistoryEntry(object):
            """
            An historical sample of Ethernet statistics on a
            particular Ethernet interface.  This sample is
            associated with the historyControlEntry which set
            up the parameters for a regular collection of these
            samples.
            
            .. attribute:: etherhistoryindex
            
            	The history of which this entry is a part.  The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: etherhistorysampleindex
            
            	An index that uniquely identifies the particular sample this entry represents among all samples associated with the same historyControlEntry. This index starts at 1 and increases by one as each new sample is taken
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: etherhistorybroadcastpkts
            
            	The number of good packets received during this sampling interval that were directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistorycollisions
            
            	The best estimate of the total number of collisions on this Ethernet segment during this interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistorycrcalignerrors
            
            	The number of packets received during this sampling interval that had a length (excluding framing bits but including FCS octets) between 64 and 1518 octets, inclusive, but were not an integral number of octets in length or had a bad Frame Check Sequence (FCS)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistorydropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources during this interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistoryfragments
            
            	The total number of packets received during this sampling interval that were not an integral number of octets in length or that had a bad Frame Check Sequence (FCS), and were less than 64 octets in length (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistoryjabbers
            
            	The number of packets received during this interval that were longer than 1518 octets (excluding framing bits but including FCS octets), and were not an integral number of octets in length or had a bad Frame Check Sequence (FCS)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistorymulticastpkts
            
            	The number of good packets received during this sampling interval that were directed to a multicast address.  Note that this number does not include packets addressed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistoryoctets
            
            	The total number of octets of data (including those in bad packets) received on the network (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistoryoversizepkts
            
            	The number of packets received during this interval that were longer than 1518 octets (excluding framing bits but including FCS octets) but were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistorypkts
            
            	The number of packets (including error packets) received during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistoryundersizepkts
            
            	The number of packets received during this interval that were less than 64 octets long (excluding framing bits but including FCS octets) and were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherhistoryutilization
            
            	The best estimate of the mean physical layer network utilization on this interface during this interval, in hundredths of a percent
            	**type**\: int
            
            	**range:** 0..10000
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.etherhistoryindex = None
                self.etherhistorysampleindex = None
                self.etherhistorybroadcastpkts = None
                self.etherhistorycollisions = None
                self.etherhistorycrcalignerrors = None
                self.etherhistorydropevents = None
                self.etherhistoryfragments = None
                self.etherhistoryintervalstart = None
                self.etherhistoryjabbers = None
                self.etherhistorymulticastpkts = None
                self.etherhistoryoctets = None
                self.etherhistoryoversizepkts = None
                self.etherhistorypkts = None
                self.etherhistoryundersizepkts = None
                self.etherhistoryutilization = None

            @property
            def _common_path(self):
                if self.etherhistoryindex is None:
                    raise YPYDataValidationError('Key property etherhistoryindex is None')
                if self.etherhistorysampleindex is None:
                    raise YPYDataValidationError('Key property etherhistorysampleindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:etherHistoryTable/RFC1271-MIB:etherHistoryEntry[RFC1271-MIB:etherHistoryIndex = ' + str(self.etherhistoryindex) + '][RFC1271-MIB:etherHistorySampleIndex = ' + str(self.etherhistorysampleindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.etherhistoryindex is not None:
                    return True

                if self.etherhistorysampleindex is not None:
                    return True

                if self.etherhistorybroadcastpkts is not None:
                    return True

                if self.etherhistorycollisions is not None:
                    return True

                if self.etherhistorycrcalignerrors is not None:
                    return True

                if self.etherhistorydropevents is not None:
                    return True

                if self.etherhistoryfragments is not None:
                    return True

                if self.etherhistoryintervalstart is not None:
                    return True

                if self.etherhistoryjabbers is not None:
                    return True

                if self.etherhistorymulticastpkts is not None:
                    return True

                if self.etherhistoryoctets is not None:
                    return True

                if self.etherhistoryoversizepkts is not None:
                    return True

                if self.etherhistorypkts is not None:
                    return True

                if self.etherhistoryundersizepkts is not None:
                    return True

                if self.etherhistoryutilization is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.EtherHistoryTable.EtherHistoryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:etherHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.etherhistoryentry is not None:
                for child_ref in self.etherhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.EtherHistoryTable']['meta_info']


    class EtherStatsTable(object):
        """
        A list of Ethernet statistics entries.
        
        .. attribute:: etherstatsentry
        
        	A collection of statistics kept for a particular Ethernet interface
        	**type**\: list of :py:class:`EtherStatsEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.EtherStatsTable.EtherStatsEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.etherstatsentry = YList()
            self.etherstatsentry.parent = self
            self.etherstatsentry.name = 'etherstatsentry'


        class EtherStatsEntry(object):
            """
            A collection of statistics kept for a particular
            Ethernet interface.
            
            .. attribute:: etherstatsindex
            
            	The value of this object uniquely identifies this etherStats entry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: etherstatsbroadcastpkts
            
            	The total number of good packets received that were directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatscollisions
            
            	The best estimate of the total number of collisions on this Ethernet segment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatscrcalignerrors
            
            	The total number of packets received that had a length (excluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but were not an integral number of octets in length or had a bad Frame Check Sequence (FCS)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsdatasource
            
            	This object identifies the source of the data that this etherStats entry is configured to analyze.  This source can be any ethernet interface on this device. In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in [4,6], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  This object may not be modified if the associated etherStatsStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: etherstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsfragments
            
            	The total number of packets received that were not an integral number of octets in length or that had a bad Frame Check Sequence (FCS), and were less than 64 octets in length (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsjabbers
            
            	The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets), and were not an integral number of octets in length or had a bad Frame Check Sequence (FCS)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsmulticastpkts
            
            	The total number of good packets received that were directed to a multicast address.  Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsoctets
            
            	The total number of octets of data (including those in bad packets) received on the network (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsoversizepkts
            
            	The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets) and were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: etherstatspkts
            
            	The total number of packets (including error packets) received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatspkts1024to1518octets
            
            	The total number of packets (including error packets) received that were between 1024 and 1518 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatspkts128to255octets
            
            	The total number of packets (including error packets) received that were between 128 and 255 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatspkts256to511octets
            
            	The total number of packets (including error packets) received that were between 256 and 511 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatspkts512to1023octets
            
            	The total number of packets (including error packets) received that were between 512 and 1023 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatspkts64octets
            
            	The total number of packets (including error packets) received that were 64 octets in length (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatspkts65to127octets
            
            	The total number of packets (including error packets) received that were between 65 and 127 octets in length inclusive (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: etherstatsstatus
            
            	The status of this etherStats entry
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.EntryStatus_Enum>`
            
            .. attribute:: etherstatsundersizepkts
            
            	The total number of packets received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.etherstatsindex = None
                self.etherstatsbroadcastpkts = None
                self.etherstatscollisions = None
                self.etherstatscrcalignerrors = None
                self.etherstatsdatasource = None
                self.etherstatsdropevents = None
                self.etherstatsfragments = None
                self.etherstatsjabbers = None
                self.etherstatsmulticastpkts = None
                self.etherstatsoctets = None
                self.etherstatsoversizepkts = None
                self.etherstatsowner = None
                self.etherstatspkts = None
                self.etherstatspkts1024to1518octets = None
                self.etherstatspkts128to255octets = None
                self.etherstatspkts256to511octets = None
                self.etherstatspkts512to1023octets = None
                self.etherstatspkts64octets = None
                self.etherstatspkts65to127octets = None
                self.etherstatsstatus = None
                self.etherstatsundersizepkts = None

            @property
            def _common_path(self):
                if self.etherstatsindex is None:
                    raise YPYDataValidationError('Key property etherstatsindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:etherStatsTable/RFC1271-MIB:etherStatsEntry[RFC1271-MIB:etherStatsIndex = ' + str(self.etherstatsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.etherstatsindex is not None:
                    return True

                if self.etherstatsbroadcastpkts is not None:
                    return True

                if self.etherstatscollisions is not None:
                    return True

                if self.etherstatscrcalignerrors is not None:
                    return True

                if self.etherstatsdatasource is not None:
                    return True

                if self.etherstatsdropevents is not None:
                    return True

                if self.etherstatsfragments is not None:
                    return True

                if self.etherstatsjabbers is not None:
                    return True

                if self.etherstatsmulticastpkts is not None:
                    return True

                if self.etherstatsoctets is not None:
                    return True

                if self.etherstatsoversizepkts is not None:
                    return True

                if self.etherstatsowner is not None:
                    return True

                if self.etherstatspkts is not None:
                    return True

                if self.etherstatspkts1024to1518octets is not None:
                    return True

                if self.etherstatspkts128to255octets is not None:
                    return True

                if self.etherstatspkts256to511octets is not None:
                    return True

                if self.etherstatspkts512to1023octets is not None:
                    return True

                if self.etherstatspkts64octets is not None:
                    return True

                if self.etherstatspkts65to127octets is not None:
                    return True

                if self.etherstatsstatus is not None:
                    return True

                if self.etherstatsundersizepkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.EtherStatsTable.EtherStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:etherStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.etherstatsentry is not None:
                for child_ref in self.etherstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.EtherStatsTable']['meta_info']


    class EventTable(object):
        """
        A list of events to be generated.
        
        .. attribute:: evententry
        
        	A set of parameters that describe an event to be generated when certain conditions are met
        	**type**\: list of :py:class:`EventEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.EventTable.EventEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.evententry = YList()
            self.evententry.parent = self
            self.evententry.name = 'evententry'


        class EventEntry(object):
            """
            A set of parameters that describe an event to be
            generated when certain conditions are met.
            
            .. attribute:: eventindex
            
            	An index that uniquely identifies an entry in the event table.  Each such entry defines one event that is to be generated when the appropriate conditions occur
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: eventcommunity
            
            	If an SNMP trap is to be sent, it will be sent to the SNMP community specified by this octet string. In the future this table will be extended to include the party security mechanism.  This object shall be set to a string of length zero if it is intended that that mechanism be used to specify the destination of the trap
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: eventdescription
            
            	A comment describing this event entry
            	**type**\: str
            
            	**range:** 0..127
            
            .. attribute:: eventlasttimesent
            
            	The value of sysUpTime at the time this event entry last generated an event.  If this entry has not generated any events, this value will be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: eventowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it.  If this object contains a string starting with 'monitor' and has associated entries in the log table, all connected management stations should retrieve those log entries, as they may have significance to all management stations connected to this device
            	**type**\: str
            
            .. attribute:: eventstatus
            
            	The status of this event entry.  If this object is not equal to valid(1), all associated log entries shall be deleted by the agent
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.EntryStatus_Enum>`
            
            .. attribute:: eventtype
            
            	The type of notification that the probe will make about this event.  In the case of log, an entry is made in the log table for each event.  In the case of snmp\-trap, an SNMP trap is sent to one or more management stations
            	**type**\: :py:class:`EventType_Enum <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.EventTable.EventEntry.EventType_Enum>`
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.eventindex = None
                self.eventcommunity = None
                self.eventdescription = None
                self.eventlasttimesent = None
                self.eventowner = None
                self.eventstatus = None
                self.eventtype = None

            class EventType_Enum(Enum):
                """
                EventType_Enum

                The type of notification that the probe will make
                about this event.  In the case of log, an entry is
                made in the log table for each event.  In the case of
                snmp\-trap, an SNMP trap is sent to one or more
                management stations.

                """

                NONE = 1

                LOG = 2

                SNMP_TRAP = 3

                LOG_AND_TRAP = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                    return meta._meta_table['RFC1271MIB.EventTable.EventEntry.EventType_Enum']


            @property
            def _common_path(self):
                if self.eventindex is None:
                    raise YPYDataValidationError('Key property eventindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:eventTable/RFC1271-MIB:eventEntry[RFC1271-MIB:eventIndex = ' + str(self.eventindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.eventindex is not None:
                    return True

                if self.eventcommunity is not None:
                    return True

                if self.eventdescription is not None:
                    return True

                if self.eventlasttimesent is not None:
                    return True

                if self.eventowner is not None:
                    return True

                if self.eventstatus is not None:
                    return True

                if self.eventtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.EventTable.EventEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:eventTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.evententry is not None:
                for child_ref in self.evententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.EventTable']['meta_info']


    class FilterTable(object):
        """
        A list of packet filter entries.
        
        .. attribute:: filterentry
        
        	A set of parameters for a packet filter applied on a particular interface
        	**type**\: list of :py:class:`FilterEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.FilterTable.FilterEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.filterentry = YList()
            self.filterentry.parent = self
            self.filterentry.name = 'filterentry'


        class FilterEntry(object):
            """
            A set of parameters for a packet filter applied on a
            particular interface.
            
            .. attribute:: filterindex
            
            	An index that uniquely identifies an entry in the filter table.  Each such entry defines one filter that is to be applied to every packet received on an interface
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: filterchannelindex
            
            	This object identifies the channel of which this filter is a part.  The filters identified by a particular value of this object are associated with the same channel as identified by the same value of the channelIndex object
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: filterowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: filterpktdata
            
            	The data that is to be matched with the input packet. For each packet received, this filter and the accompanying filterPktDataMask and filterPktDataNotMask will be adjusted for the offset.  The only bits relevant to this match algorithm are those that have the corresponding filterPktDataMask bit equal to one.  The following three rules are then applied to every packet\:  (1) If the packet is too short and does not have data     corresponding to part of the filterPktData, the     packet will fail this data match.  (2) For each relevant bit from the packet with the     corresponding filterPktDataNotMask bit set to     zero, if the bit from the packet is not equal to     the corresponding bit from the filterPktData,     then the packet will fail this data match.  (3) If for every relevant bit from the packet with the     corresponding filterPktDataNotMask bit set to one,     the bit from the packet is equal to the     corresponding bit from the filterPktData, then     the packet will fail this data match.  Any packets that have not failed any of the three matches above have passed this data match.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: str
            
            .. attribute:: filterpktdatamask
            
            	The mask that is applied to the match process. After adjusting this mask for the offset, only those bits in the received packet that correspond to bits set in this mask are relevant for further processing by the match algorithm.  The offset is applied to filterPktDataMask in the same way it is applied to the filter.  For the purposes of the matching algorithm, if the associated filterPktData object is longer than this mask, this mask is conceptually extended with '1' bits until it reaches the length of the filterPktData object. This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: str
            
            .. attribute:: filterpktdatanotmask
            
            	The inversion mask that is applied to the match process.  After adjusting this mask for the offset, those relevant bits in the received packet that correspond to bits cleared in this mask must all be equal to their corresponding bits in the filterPktData object for the packet to be accepted. In addition, at least one of those relevant bits in the received packet that correspond to bits set in this mask must be different to its corresponding bit in the filterPktData object.  For the purposes of the matching algorithm, if the associated filterPktData object is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the length of the filterPktData object.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: str
            
            .. attribute:: filterpktdataoffset
            
            	The offset from the beginning of each packet where a match of packet data will be attempted.  This offset is measured from the point in the physical layer packet after the framing bits, if any.  For example, in an Ethernet frame, this point is at the beginning of the destination MAC address.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: filterpktstatus
            
            	The status that is to be matched with the input packet.  The only bits relevant to this match algorithm are those that have the corresponding filterPktStatusMask bit equal to one.  The following two rules are then applied to every packet\:  (1) For each relevant bit from the packet status     with the corresponding filterPktStatusNotMask     bit set to zero, if the bit from the packet     status is not equal to the corresponding bit     from the filterPktStatus, then the packet will     fail this status match.  (2) If for every relevant bit from the packet status     with the corresponding filterPktStatusNotMask     bit set to one, the bit from the packet status     is equal to the corresponding bit from the     filterPktStatus, then the packet will fail     this status match.  Any packets that have not failed either of the two matches above have passed this status match.  The value of the packet status is a sum.  This sum initially takes the value zero.  Then, for each error, E, that has been discovered in this packet, 2 raised to a value representing E is added to the sum. The errors and the bits that represent them are dependent on the media type of the interface that this channel is receiving packets from.  The errors defined for a packet captured off of an Ethernet interface are as follows\:      bit #    Error         0    Packet is longer than 1518 octets         1    Packet is shorter than 64 octets         2    Packet experienced a CRC or Alignment              error  For example, an Ethernet fragment would have a value of 6 (2^1 + 2^2).  As this MIB is expanded to new media types, this object will have other media\-specific errors defined.  For the purposes of this status matching algorithm, if the packet status is longer than this object, filterPktStatus this object is conceptually extended with '0' bits until it reaches the size of the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: filterpktstatusmask
            
            	The mask that is applied to the status match process. Only those bits in the received packet that correspond to bits set in this mask are relevant for further processing by the status match algorithm.  For the purposes of the matching algorithm, if the associated filterPktStatus object is longer than this mask, this mask is conceptually extended with '1' bits until it reaches the size of the filterPktStatus.  In addition, if a packet status is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the size of the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: filterpktstatusnotmask
            
            	The inversion mask that is applied to the status match process.  Those relevant bits in the received packet status that correspond to bits cleared in this mask must all be equal to their corresponding bits in the filterPktStatus object for the packet to be accepted. In addition, at least one of those relevant bits in the received packet status that correspond to bits set in this mask must be different to its corresponding bit in the filterPktStatus object for the packet to be accepted.  For the purposes of the matching algorithm, if the associated filterPktStatus object or a packet status is longer than this mask, this mask is conceptually extended with '0' bits until it reaches the longer of the lengths of the filterPktStatus object and the packet status.  This object may not be modified if the associated filterStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: filterstatus
            
            	The status of this filter entry
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.EntryStatus_Enum>`
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.filterindex = None
                self.filterchannelindex = None
                self.filterowner = None
                self.filterpktdata = None
                self.filterpktdatamask = None
                self.filterpktdatanotmask = None
                self.filterpktdataoffset = None
                self.filterpktstatus = None
                self.filterpktstatusmask = None
                self.filterpktstatusnotmask = None
                self.filterstatus = None

            @property
            def _common_path(self):
                if self.filterindex is None:
                    raise YPYDataValidationError('Key property filterindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:filterTable/RFC1271-MIB:filterEntry[RFC1271-MIB:filterIndex = ' + str(self.filterindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.filterindex is not None:
                    return True

                if self.filterchannelindex is not None:
                    return True

                if self.filterowner is not None:
                    return True

                if self.filterpktdata is not None:
                    return True

                if self.filterpktdatamask is not None:
                    return True

                if self.filterpktdatanotmask is not None:
                    return True

                if self.filterpktdataoffset is not None:
                    return True

                if self.filterpktstatus is not None:
                    return True

                if self.filterpktstatusmask is not None:
                    return True

                if self.filterpktstatusnotmask is not None:
                    return True

                if self.filterstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.FilterTable.FilterEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:filterTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.filterentry is not None:
                for child_ref in self.filterentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.FilterTable']['meta_info']


    class HistoryControlTable(object):
        """
        A list of history control entries.
        
        .. attribute:: historycontrolentry
        
        	A list of parameters that set up a periodic sampling of statistics
        	**type**\: list of :py:class:`HistoryControlEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HistoryControlTable.HistoryControlEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.historycontrolentry = YList()
            self.historycontrolentry.parent = self
            self.historycontrolentry.name = 'historycontrolentry'


        class HistoryControlEntry(object):
            """
            A list of parameters that set up a periodic
            sampling of statistics.
            
            .. attribute:: historycontrolindex
            
            	An index that uniquely identifies an entry in the historyControl table.  Each such entry defines a set of samples at a particular interval for an interface on the device
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: historycontrolbucketsgranted
            
            	The number of discrete sampling intervals over which data shall be saved in the part of the media\-specific table associated with this historyControl entry.  When the associated historyControlBucketsRequested object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular probe implementation and available resources.  The probe must not lower this value except as a result of a modification to the associated historyControlBucketsRequested object.  There will be times when the actual number of buckets associated with this entry is less than the value of this object.  In this case, at the end of each sampling interval, a new bucket will be added to the media\-specific table.  When the number of buckets reaches the value of this object and a new bucket is to be added to the media\-specific table, the oldest bucket associated with this historyControlEntry shall be deleted by the agent so that the new bucket can be added.  When the value of this object changes to a value less than the current value, entries are deleted from the media\-specific table associated with this historyControlEntry.  Enough of the oldest of these entries shall be deleted by the agent so that their number remains less than or equal to the new value of this object.  When the value of this object changes to a value greater than the current value, the number of associated media\-specific entries may be allowed to grow
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: historycontrolbucketsrequested
            
            	The requested number of discrete time intervals over which data is to be saved in the part of the media\-specific table associated with this historyControl entry.  When this object is created or modified, the probe should set historyControlBucketsGranted as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: historycontroldatasource
            
            	This object identifies the source of the data for which historical data was collected and placed in a media\-specific table on behalf of this historyControlEntry.  This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in [4,6], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  This object may not be modified if the associated historyControlStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: historycontrolinterval
            
            	The interval in seconds over which the data is sampled for each bucket in the part of the media\-specific table associated with this historyControl entry.  This interval can be set to any number of seconds between 1 and 3600 (1 hour).  Because the counters in a bucket may overflow at their maximum value with no indication, a prudent manager will take into account the possibility of overflow in any of the associated counters.  It is important to consider the minimum time in which any counter could overflow on a particular media type and set the historyControlInterval object to a value less than this interval.  This is typically most important for the 'octets' counter in any media\-specific table.  For example, on an Ethernet network, the etherHistoryOctets counter could overflow in about one hour at the Ethernet's maximum utilization.  This object may not be modified if the associated historyControlStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..3600
            
            .. attribute:: historycontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: historycontrolstatus
            
            	The status of this historyControl entry.  Each instance of the media\-specific table associated with this historyControlEntry will be deleted by the agent if this historyControlEntry is not equal to valid(1)
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.EntryStatus_Enum>`
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.historycontrolindex = None
                self.historycontrolbucketsgranted = None
                self.historycontrolbucketsrequested = None
                self.historycontroldatasource = None
                self.historycontrolinterval = None
                self.historycontrolowner = None
                self.historycontrolstatus = None

            @property
            def _common_path(self):
                if self.historycontrolindex is None:
                    raise YPYDataValidationError('Key property historycontrolindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:historyControlTable/RFC1271-MIB:historyControlEntry[RFC1271-MIB:historyControlIndex = ' + str(self.historycontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.historycontrolindex is not None:
                    return True

                if self.historycontrolbucketsgranted is not None:
                    return True

                if self.historycontrolbucketsrequested is not None:
                    return True

                if self.historycontroldatasource is not None:
                    return True

                if self.historycontrolinterval is not None:
                    return True

                if self.historycontrolowner is not None:
                    return True

                if self.historycontrolstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.HistoryControlTable.HistoryControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:historyControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.historycontrolentry is not None:
                for child_ref in self.historycontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.HistoryControlTable']['meta_info']


    class HostControlTable(object):
        """
        A list of host table control entries.
        
        .. attribute:: hostcontrolentry
        
        	A list of parameters that set up the discovery of hosts on a particular interface and the collection of statistics about these hosts
        	**type**\: list of :py:class:`HostControlEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HostControlTable.HostControlEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.hostcontrolentry = YList()
            self.hostcontrolentry.parent = self
            self.hostcontrolentry.name = 'hostcontrolentry'


        class HostControlEntry(object):
            """
            A list of parameters that set up the discovery of
            hosts on a particular interface and the collection
            of statistics about these hosts.
            
            .. attribute:: hostcontrolindex
            
            	An index that uniquely identifies an entry in the hostControl table.  Each such entry defines a function that discovers hosts on a particular interface and places statistics about them in the hostTable and the hostTimeTable on behalf of this hostControlEntry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hostcontroldatasource
            
            	This object identifies the source of the data for this instance of the host function.  This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in [4,6], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  This object may not be modified if the associated hostControlStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: hostcontrollastdeletetime
            
            	The value of sysUpTime when the last entry was deleted from the portion of the hostTable associated with this hostControlEntry.  If no deletions have occurred, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: hostcontrolstatus
            
            	The status of this hostControl entry.  If this object is not equal to valid(1), all associated entries in the hostTable, hostTimeTable, and the hostTopNTable shall be deleted by the agent
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.EntryStatus_Enum>`
            
            .. attribute:: hostcontroltablesize
            
            	The number of hostEntries in the hostTable and the hostTimeTable associated with this hostControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.hostcontrolindex = None
                self.hostcontroldatasource = None
                self.hostcontrollastdeletetime = None
                self.hostcontrolowner = None
                self.hostcontrolstatus = None
                self.hostcontroltablesize = None

            @property
            def _common_path(self):
                if self.hostcontrolindex is None:
                    raise YPYDataValidationError('Key property hostcontrolindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:hostControlTable/RFC1271-MIB:hostControlEntry[RFC1271-MIB:hostControlIndex = ' + str(self.hostcontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.hostcontrolindex is not None:
                    return True

                if self.hostcontroldatasource is not None:
                    return True

                if self.hostcontrollastdeletetime is not None:
                    return True

                if self.hostcontrolowner is not None:
                    return True

                if self.hostcontrolstatus is not None:
                    return True

                if self.hostcontroltablesize is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.HostControlTable.HostControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:hostControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.hostcontrolentry is not None:
                for child_ref in self.hostcontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.HostControlTable']['meta_info']


    class HostTable(object):
        """
        A list of host entries.
        
        .. attribute:: hostentry
        
        	A collection of statistics for a particular host that has been discovered on an interface of this device
        	**type**\: list of :py:class:`HostEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HostTable.HostEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.hostentry = YList()
            self.hostentry.parent = self
            self.hostentry.name = 'hostentry'


        class HostEntry(object):
            """
            A collection of statistics for a particular host
            that has been discovered on an interface of this
            device.
            
            .. attribute:: hostaddress
            
            	The physical address of this host
            	**type**\: str
            
            .. attribute:: hostindex
            
            	The set of collected host statistics of which this entry is a part.  The set of hosts identified by a particular value of this index is associated with the hostControlEntry as identified by the same value of hostControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hostcreationorder
            
            	An index that defines the relative ordering of the creation time of hosts captured for a particular hostControlEntry.  This index shall be between 1 and N, where N is the value of the associated hostControlTableSize.  The ordering of the indexes is based on the order of each entry's insertion into the table, in which entries added earlier have a lower index value than entries added later.  It is important to note that the order for a particular entry may change as an (earlier) entry is deleted from the table.  Because this order may change, management stations should make use of the hostControlLastDeleteTime variable in the hostControlEntry associated with the relevant portion of the hostTable.  By observing this variable, the management station may detect the circumstances where a previous association between a value of hostCreationOrder and a hostEntry may no longer hold
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hostinoctets
            
            	The number of octets transmitted to this address since it was added to the hostTable (excluding framing bits but including FCS octets), except for those octets in packets that contained errors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostinpkts
            
            	The number of packets without errors transmitted to this address since it was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostoutbroadcastpkts
            
            	The number of good packets transmitted by this address that were directed to the broadcast address since this host was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostouterrors
            
            	The number of error packets transmitted by this address since this host was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostoutmulticastpkts
            
            	The number of good packets transmitted by this address that were directed to a multicast address since this host was added to the hostTable. Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostoutoctets
            
            	The number of octets transmitted by this address since it was added to the hostTable (excluding framing bits but including FCS octets), including those octets in packets that contained errors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hostoutpkts
            
            	The number of packets including errors transmitted by this address since it was added to the hostTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.hostaddress = None
                self.hostindex = None
                self.hostcreationorder = None
                self.hostinoctets = None
                self.hostinpkts = None
                self.hostoutbroadcastpkts = None
                self.hostouterrors = None
                self.hostoutmulticastpkts = None
                self.hostoutoctets = None
                self.hostoutpkts = None

            @property
            def _common_path(self):
                if self.hostaddress is None:
                    raise YPYDataValidationError('Key property hostaddress is None')
                if self.hostindex is None:
                    raise YPYDataValidationError('Key property hostindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:hostTable/RFC1271-MIB:hostEntry[RFC1271-MIB:hostAddress = ' + str(self.hostaddress) + '][RFC1271-MIB:hostIndex = ' + str(self.hostindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.hostaddress is not None:
                    return True

                if self.hostindex is not None:
                    return True

                if self.hostcreationorder is not None:
                    return True

                if self.hostinoctets is not None:
                    return True

                if self.hostinpkts is not None:
                    return True

                if self.hostoutbroadcastpkts is not None:
                    return True

                if self.hostouterrors is not None:
                    return True

                if self.hostoutmulticastpkts is not None:
                    return True

                if self.hostoutoctets is not None:
                    return True

                if self.hostoutpkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.HostTable.HostEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:hostTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.hostentry is not None:
                for child_ref in self.hostentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.HostTable']['meta_info']


    class HostTimeTable(object):
        """
        A list of time\-ordered host table entries.
        
        .. attribute:: hosttimeentry
        
        	A collection of statistics for a particular host that has been discovered on an interface of this device.  This collection includes the relative ordering of the creation time of this object
        	**type**\: list of :py:class:`HostTimeEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HostTimeTable.HostTimeEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.hosttimeentry = YList()
            self.hosttimeentry.parent = self
            self.hosttimeentry.name = 'hosttimeentry'


        class HostTimeEntry(object):
            """
            A collection of statistics for a particular host
            that has been discovered on an interface of this
            device.  This collection includes the relative
            ordering of the creation time of this object.
            
            .. attribute:: hosttimecreationorder
            
            	An index that uniquely identifies an entry in the hostTime table among those entries associated with the same hostControlEntry.  This index shall be between 1 and N, where N is the value of the associated hostControlTableSize.  The ordering of the indexes is based on the order of each entry's insertion into the table, in which entries added earlier have a lower index value than entries added later.  Thus the management station has the ability to learn of new entries added to this table without downloading the entire table.  It is important to note that the index for a particular entry may change as an (earlier) entry is deleted from the table.  Because this order may change, management stations should make use of the hostControlLastDeleteTime variable in the hostControlEntry associated with the relevant portion of the hostTimeTable.  By observing this variable, the management station may detect the circumstances where a download of the table may have missed entries, and where a previous association between a value of hostTimeCreationOrder and a hostTimeEntry may no longer hold
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hosttimeindex
            
            	The set of collected host statistics of which this entry is a part.  The set of hosts identified by a particular value of this index is associated with the hostControlEntry as identified by the same value of hostControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hosttimeaddress
            
            	The physical address of this host
            	**type**\: str
            
            .. attribute:: hosttimeinoctets
            
            	The number of octets transmitted to this address since it was added to the hostTimeTable (excluding framing bits but including FCS octets), except for those octets in packets that contained errors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hosttimeinpkts
            
            	The number of packets without errors transmitted to this address since it was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hosttimeoutbroadcastpkts
            
            	The number of good packets transmitted by this address that were directed to the broadcast address since this host was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hosttimeouterrors
            
            	The number of error packets transmitted by this address since this host was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hosttimeoutmulticastpkts
            
            	The number of good packets transmitted by this address that were directed to a multicast address since this host was added to the hostTimeTable. Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hosttimeoutoctets
            
            	The number of octets transmitted by this address since it was added to the hostTimeTable (excluding framing bits but including FCS octets), including those octets in packets that contained errors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hosttimeoutpkts
            
            	The number of packets including errors transmitted by this address since it was added to the hostTimeTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.hosttimecreationorder = None
                self.hosttimeindex = None
                self.hosttimeaddress = None
                self.hosttimeinoctets = None
                self.hosttimeinpkts = None
                self.hosttimeoutbroadcastpkts = None
                self.hosttimeouterrors = None
                self.hosttimeoutmulticastpkts = None
                self.hosttimeoutoctets = None
                self.hosttimeoutpkts = None

            @property
            def _common_path(self):
                if self.hosttimecreationorder is None:
                    raise YPYDataValidationError('Key property hosttimecreationorder is None')
                if self.hosttimeindex is None:
                    raise YPYDataValidationError('Key property hosttimeindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:hostTimeTable/RFC1271-MIB:hostTimeEntry[RFC1271-MIB:hostTimeCreationOrder = ' + str(self.hosttimecreationorder) + '][RFC1271-MIB:hostTimeIndex = ' + str(self.hosttimeindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.hosttimecreationorder is not None:
                    return True

                if self.hosttimeindex is not None:
                    return True

                if self.hosttimeaddress is not None:
                    return True

                if self.hosttimeinoctets is not None:
                    return True

                if self.hosttimeinpkts is not None:
                    return True

                if self.hosttimeoutbroadcastpkts is not None:
                    return True

                if self.hosttimeouterrors is not None:
                    return True

                if self.hosttimeoutmulticastpkts is not None:
                    return True

                if self.hosttimeoutoctets is not None:
                    return True

                if self.hosttimeoutpkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.HostTimeTable.HostTimeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:hostTimeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.hosttimeentry is not None:
                for child_ref in self.hosttimeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.HostTimeTable']['meta_info']


    class HostTopNControlTable(object):
        """
        A list of top N host control entries.
        
        .. attribute:: hosttopncontrolentry
        
        	A set of parameters that control the creation of a report of the top N hosts according to several metrics
        	**type**\: list of :py:class:`HostTopNControlEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HostTopNControlTable.HostTopNControlEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.hosttopncontrolentry = YList()
            self.hosttopncontrolentry.parent = self
            self.hosttopncontrolentry.name = 'hosttopncontrolentry'


        class HostTopNControlEntry(object):
            """
            A set of parameters that control the creation of a
            report of the top N hosts according to several
            metrics.
            
            .. attribute:: hosttopncontrolindex
            
            	An index that uniquely identifies an entry in the hostTopNControl table.  Each such entry defines one top N report prepared for one interface
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnduration
            
            	The number of seconds that this report has collected during the last sampling interval, or if this report is currently being collected, the number of seconds that this report is being collected during this sampling interval.  When the associated hostTopNTimeRemaining object is set, this object shall be set by the probe to the same value and shall not be modified until the next time the hostTopNTimeRemaining is set.  This value shall be zero if no reports have been requested for this hostTopNControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: hosttopngrantedsize
            
            	The maximum number of hosts in the top N table.  When the associated hostTopNRequestedSize object is created or modified, the probe should set this object as closely to the requested value as is possible for the particular implementation and available resources. The probe must not lower this value except as a result of a set to the associated hostTopNRequestedSize object.  Hosts with the highest value of hostTopNRate shall be placed in this table in decreasing order of this rate until there is no more room or until there are no more hosts
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: hosttopnhostindex
            
            	The host table for which a top N report will be prepared on behalf of this entry.  The host table identified by a particular value of this index is associated with the same host table as identified by the same value of hostIndex.  This object may not be modified if the associated hostTopNStatus object is equal to valid(1)
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: hosttopnratebase
            
            	The variable for each host that the hostTopNRate variable is based upon.  This object may not be modified if the associated hostTopNStatus object is equal to valid(1)
            	**type**\: :py:class:`HostTopNRateBase_Enum <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HostTopNControlTable.HostTopNControlEntry.HostTopNRateBase_Enum>`
            
            .. attribute:: hosttopnrequestedsize
            
            	The maximum number of hosts requested for the top N table.  When this object is created or modified, the probe should set hostTopNGrantedSize as closely to this object as is possible for the particular probe implementation and available resources
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: hosttopnstarttime
            
            	The value of sysUpTime when this top N report was last started.  In other words, this is the time that the associated hostTopNTimeRemaining object was modified to start the requested report
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hosttopnstatus
            
            	The status of this hostTopNControl entry. If this object is not equal to valid(1), all associated hostTopNEntries shall be deleted by the agent
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.EntryStatus_Enum>`
            
            .. attribute:: hosttopntimeremaining
            
            	The number of seconds left in the report currently being collected.  When this object is modified by the management station, a new collection is started, possibly aborting a currently running report.  The new value is used as the requested duration of this report, which is loaded into the associated hostTopNDuration object.  When this object is set to a non\-zero value, any associated hostTopNEntries shall be made inaccessible by the monitor.  While the value of this object is non\-zero, it decrements by one per second until it reaches zero.  During this time, all associated hostTopNEntries shall remain inaccessible.  At the time that this object decrements to zero, the report is made accessible in the hostTopNTable.  Thus, the hostTopN table needs to be created only at the end of the collection interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.hosttopncontrolindex = None
                self.hosttopnduration = None
                self.hosttopngrantedsize = None
                self.hosttopnhostindex = None
                self.hosttopnowner = None
                self.hosttopnratebase = None
                self.hosttopnrequestedsize = None
                self.hosttopnstarttime = None
                self.hosttopnstatus = None
                self.hosttopntimeremaining = None

            class HostTopNRateBase_Enum(Enum):
                """
                HostTopNRateBase_Enum

                The variable for each host that the hostTopNRate
                variable is based upon.
                
                This object may not be modified if the associated
                hostTopNStatus object is equal to valid(1).

                """

                HOSTTOPNINPKTS = 1

                HOSTTOPNOUTPKTS = 2

                HOSTTOPNINOCTETS = 3

                HOSTTOPNOUTOCTETS = 4

                HOSTTOPNOUTERRORS = 5

                HOSTTOPNOUTBROADCASTPKTS = 6

                HOSTTOPNOUTMULTICASTPKTS = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                    return meta._meta_table['RFC1271MIB.HostTopNControlTable.HostTopNControlEntry.HostTopNRateBase_Enum']


            @property
            def _common_path(self):
                if self.hosttopncontrolindex is None:
                    raise YPYDataValidationError('Key property hosttopncontrolindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:hostTopNControlTable/RFC1271-MIB:hostTopNControlEntry[RFC1271-MIB:hostTopNControlIndex = ' + str(self.hosttopncontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.hosttopncontrolindex is not None:
                    return True

                if self.hosttopnduration is not None:
                    return True

                if self.hosttopngrantedsize is not None:
                    return True

                if self.hosttopnhostindex is not None:
                    return True

                if self.hosttopnowner is not None:
                    return True

                if self.hosttopnratebase is not None:
                    return True

                if self.hosttopnrequestedsize is not None:
                    return True

                if self.hosttopnstarttime is not None:
                    return True

                if self.hosttopnstatus is not None:
                    return True

                if self.hosttopntimeremaining is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.HostTopNControlTable.HostTopNControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:hostTopNControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.hosttopncontrolentry is not None:
                for child_ref in self.hosttopncontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.HostTopNControlTable']['meta_info']


    class HostTopNTable(object):
        """
        A list of top N host entries.
        
        .. attribute:: hosttopnentry
        
        	A set of statistics for a host that is part of a top N report
        	**type**\: list of :py:class:`HostTopNEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.HostTopNTable.HostTopNEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.hosttopnentry = YList()
            self.hosttopnentry.parent = self
            self.hosttopnentry.name = 'hosttopnentry'


        class HostTopNEntry(object):
            """
            A set of statistics for a host that is part of a
            top N report.
            
            .. attribute:: hosttopnindex
            
            	An index that uniquely identifies an entry in the hostTopN table among those in the same report. This index is between 1 and N, where N is the number of entries in this table.  Increasing values of hostTopNIndex shall be assigned to entries with decreasing values of hostTopNRate until index N is assigned to the entry with the lowest value of hostTopNRate or there are no more hostTopNEntries
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnreport
            
            	This object identifies the top N report of which this entry is a part.  The set of hosts identified by a particular value of this object is part of the same report as identified by the same value of the hostTopNControlIndex object
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: hosttopnaddress
            
            	The physical address of this host
            	**type**\: str
            
            .. attribute:: hosttopnrate
            
            	The amount of change in the selected variable during this sampling interval.  The selected variable is this host's instance of the object selected by hostTopNRateBase
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.hosttopnindex = None
                self.hosttopnreport = None
                self.hosttopnaddress = None
                self.hosttopnrate = None

            @property
            def _common_path(self):
                if self.hosttopnindex is None:
                    raise YPYDataValidationError('Key property hosttopnindex is None')
                if self.hosttopnreport is None:
                    raise YPYDataValidationError('Key property hosttopnreport is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:hostTopNTable/RFC1271-MIB:hostTopNEntry[RFC1271-MIB:hostTopNIndex = ' + str(self.hosttopnindex) + '][RFC1271-MIB:hostTopNReport = ' + str(self.hosttopnreport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.hosttopnindex is not None:
                    return True

                if self.hosttopnreport is not None:
                    return True

                if self.hosttopnaddress is not None:
                    return True

                if self.hosttopnrate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.HostTopNTable.HostTopNEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:hostTopNTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.hosttopnentry is not None:
                for child_ref in self.hosttopnentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.HostTopNTable']['meta_info']


    class LogTable(object):
        """
        A list of events that have been logged.
        
        .. attribute:: logentry
        
        	A set of data describing an event that has been logged
        	**type**\: list of :py:class:`LogEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.LogTable.LogEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.logentry = YList()
            self.logentry.parent = self
            self.logentry.name = 'logentry'


        class LogEntry(object):
            """
            A set of data describing an event that has been
            logged.
            
            .. attribute:: logeventindex
            
            	The event entry that generated this log entry.  The log identified by a particular value of this index is associated with the same eventEntry as identified by the same value of eventIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: logindex
            
            	An index that uniquely identifies an entry in the log table amongst those generated by the same eventEntries.  These indexes are assigned beginning with 1 and increase by one with each new log entry.  The association between values of logIndex and logEntries is fixed for the lifetime of each logEntry. The agent may choose to delete the oldest instances of logEntry as required because of lack of memory.  It is an implementation\-specific matter as to when this deletion may occur
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: logdescription
            
            	An implementation dependent description of the event that activated this log entry
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: logtime
            
            	The value of sysUpTime when this log entry was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.logeventindex = None
                self.logindex = None
                self.logdescription = None
                self.logtime = None

            @property
            def _common_path(self):
                if self.logeventindex is None:
                    raise YPYDataValidationError('Key property logeventindex is None')
                if self.logindex is None:
                    raise YPYDataValidationError('Key property logindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:logTable/RFC1271-MIB:logEntry[RFC1271-MIB:logEventIndex = ' + str(self.logeventindex) + '][RFC1271-MIB:logIndex = ' + str(self.logindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.logeventindex is not None:
                    return True

                if self.logindex is not None:
                    return True

                if self.logdescription is not None:
                    return True

                if self.logtime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.LogTable.LogEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:logTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.logentry is not None:
                for child_ref in self.logentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.LogTable']['meta_info']


    class MatrixControlTable(object):
        """
        A list of information entries for the
        traffic matrix on each interface.
        
        .. attribute:: matrixcontrolentry
        
        	Information about a traffic matrix on a particular interface
        	**type**\: list of :py:class:`MatrixControlEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.MatrixControlTable.MatrixControlEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.matrixcontrolentry = YList()
            self.matrixcontrolentry.parent = self
            self.matrixcontrolentry.name = 'matrixcontrolentry'


        class MatrixControlEntry(object):
            """
            Information about a traffic matrix on a
            particular interface.
            
            .. attribute:: matrixcontrolindex
            
            	An index that uniquely identifies an entry in the matrixControl table.  Each such entry defines a function that discovers conversations on a particular interface and places statistics about them in the matrixSDTable and the matrixDSTable on behalf of this matrixControlEntry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: matrixcontroldatasource
            
            	This object identifies the source of the data from which this entry creates a traffic matrix. This source can be any interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in [4,6], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all packets on the local network segment attached to the identified interface.  This object may not be modified if the associated matrixControlStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: matrixcontrollastdeletetime
            
            	The value of sysUpTime when the last entry was deleted from the portion of the matrixSDTable or matrixDSTable associated with this matrixControlEntry. If no deletions have occurred, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: matrixcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: matrixcontrolstatus
            
            	The status of this matrixControl entry.  If this object is not equal to valid(1), all associated entries in the matrixSDTable and the matrixDSTable shall be deleted by the agent
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.rfc1271.RFC1271_MIB.EntryStatus_Enum>`
            
            .. attribute:: matrixcontroltablesize
            
            	The number of matrixSDEntries in the matrixSDTable for this interface.  This must also be the value of the number of entries in the matrixDSTable for this interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.matrixcontrolindex = None
                self.matrixcontroldatasource = None
                self.matrixcontrollastdeletetime = None
                self.matrixcontrolowner = None
                self.matrixcontrolstatus = None
                self.matrixcontroltablesize = None

            @property
            def _common_path(self):
                if self.matrixcontrolindex is None:
                    raise YPYDataValidationError('Key property matrixcontrolindex is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:matrixControlTable/RFC1271-MIB:matrixControlEntry[RFC1271-MIB:matrixControlIndex = ' + str(self.matrixcontrolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.matrixcontrolindex is not None:
                    return True

                if self.matrixcontroldatasource is not None:
                    return True

                if self.matrixcontrollastdeletetime is not None:
                    return True

                if self.matrixcontrolowner is not None:
                    return True

                if self.matrixcontrolstatus is not None:
                    return True

                if self.matrixcontroltablesize is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.MatrixControlTable.MatrixControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:matrixControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.matrixcontrolentry is not None:
                for child_ref in self.matrixcontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.MatrixControlTable']['meta_info']


    class MatrixDSTable(object):
        """
        A list of traffic matrix entries indexed by
        destination and source MAC address.
        
        .. attribute:: matrixdsentry
        
        	A collection of statistics for communications between two address on a particular interface
        	**type**\: list of :py:class:`MatrixDSEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.MatrixDSTable.MatrixDSEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.matrixdsentry = YList()
            self.matrixdsentry.parent = self
            self.matrixdsentry.name = 'matrixdsentry'


        class MatrixDSEntry(object):
            """
            A collection of statistics for communications between
            two address on a particular interface.
            
            .. attribute:: matrixdsdestaddress
            
            	The destination physical address
            	**type**\: str
            
            .. attribute:: matrixdsindex
            
            	The set of collected matrix statistics of which this entry is a part.  The set of matrix statistics identified by a particular value of this index is associated with the same matrixControlEntry as identified by the same value of matrixControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: matrixdssourceaddress
            
            	The source physical address
            	**type**\: str
            
            .. attribute:: matrixdserrors
            
            	The number of error packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: matrixdsoctets
            
            	The number of octets (excluding framing bits but including FCS octets) contained in all packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: matrixdspkts
            
            	The number of packets transmitted from the source address to the destination address (this number includes error packets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.matrixdsdestaddress = None
                self.matrixdsindex = None
                self.matrixdssourceaddress = None
                self.matrixdserrors = None
                self.matrixdsoctets = None
                self.matrixdspkts = None

            @property
            def _common_path(self):
                if self.matrixdsdestaddress is None:
                    raise YPYDataValidationError('Key property matrixdsdestaddress is None')
                if self.matrixdsindex is None:
                    raise YPYDataValidationError('Key property matrixdsindex is None')
                if self.matrixdssourceaddress is None:
                    raise YPYDataValidationError('Key property matrixdssourceaddress is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:matrixDSTable/RFC1271-MIB:matrixDSEntry[RFC1271-MIB:matrixDSDestAddress = ' + str(self.matrixdsdestaddress) + '][RFC1271-MIB:matrixDSIndex = ' + str(self.matrixdsindex) + '][RFC1271-MIB:matrixDSSourceAddress = ' + str(self.matrixdssourceaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.matrixdsdestaddress is not None:
                    return True

                if self.matrixdsindex is not None:
                    return True

                if self.matrixdssourceaddress is not None:
                    return True

                if self.matrixdserrors is not None:
                    return True

                if self.matrixdsoctets is not None:
                    return True

                if self.matrixdspkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.MatrixDSTable.MatrixDSEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:matrixDSTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.matrixdsentry is not None:
                for child_ref in self.matrixdsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.MatrixDSTable']['meta_info']


    class MatrixSDTable(object):
        """
        A list of traffic matrix entries indexed by
        source and destination MAC address.
        
        .. attribute:: matrixsdentry
        
        	A collection of statistics for communications between two addresses on a particular interface
        	**type**\: list of :py:class:`MatrixSDEntry <ydk.models.rfc1271.RFC1271_MIB.RFC1271MIB.MatrixSDTable.MatrixSDEntry>`
        
        

        """

        _prefix = 'rfc1271-mib'

        def __init__(self):
            self.parent = None
            self.matrixsdentry = YList()
            self.matrixsdentry.parent = self
            self.matrixsdentry.name = 'matrixsdentry'


        class MatrixSDEntry(object):
            """
            A collection of statistics for communications between
            two addresses on a particular interface.
            
            .. attribute:: matrixsddestaddress
            
            	The destination physical address
            	**type**\: str
            
            .. attribute:: matrixsdindex
            
            	The set of collected matrix statistics of which this entry is a part.  The set of matrix statistics identified by a particular value of this index is associated with the same matrixControlEntry as identified by the same value of matrixControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: matrixsdsourceaddress
            
            	The source physical address
            	**type**\: str
            
            .. attribute:: matrixsderrors
            
            	The number of error packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: matrixsdoctets
            
            	The number of octets (excluding framing bits but including FCS octets) contained in all packets transmitted from the source address to the destination address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: matrixsdpkts
            
            	The number of packets transmitted from the source address to the destination address (this number includes error packets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'rfc1271-mib'

            def __init__(self):
                self.parent = None
                self.matrixsddestaddress = None
                self.matrixsdindex = None
                self.matrixsdsourceaddress = None
                self.matrixsderrors = None
                self.matrixsdoctets = None
                self.matrixsdpkts = None

            @property
            def _common_path(self):
                if self.matrixsddestaddress is None:
                    raise YPYDataValidationError('Key property matrixsddestaddress is None')
                if self.matrixsdindex is None:
                    raise YPYDataValidationError('Key property matrixsdindex is None')
                if self.matrixsdsourceaddress is None:
                    raise YPYDataValidationError('Key property matrixsdsourceaddress is None')

                return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:matrixSDTable/RFC1271-MIB:matrixSDEntry[RFC1271-MIB:matrixSDDestAddress = ' + str(self.matrixsddestaddress) + '][RFC1271-MIB:matrixSDIndex = ' + str(self.matrixsdindex) + '][RFC1271-MIB:matrixSDSourceAddress = ' + str(self.matrixsdsourceaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.matrixsddestaddress is not None:
                    return True

                if self.matrixsdindex is not None:
                    return True

                if self.matrixsdsourceaddress is not None:
                    return True

                if self.matrixsderrors is not None:
                    return True

                if self.matrixsdoctets is not None:
                    return True

                if self.matrixsdpkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
                return meta._meta_table['RFC1271MIB.MatrixSDTable.MatrixSDEntry']['meta_info']

        @property
        def _common_path(self):

            return '/RFC1271-MIB:RFC1271-MIB/RFC1271-MIB:matrixSDTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.matrixsdentry is not None:
                for child_ref in self.matrixsdentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
            return meta._meta_table['RFC1271MIB.MatrixSDTable']['meta_info']

    @property
    def _common_path(self):

        return '/RFC1271-MIB:RFC1271-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.alarmtable is not None and self.alarmtable._has_data():
            return True

        if self.alarmtable is not None and self.alarmtable.is_presence():
            return True

        if self.buffercontroltable is not None and self.buffercontroltable._has_data():
            return True

        if self.buffercontroltable is not None and self.buffercontroltable.is_presence():
            return True

        if self.capturebuffertable is not None and self.capturebuffertable._has_data():
            return True

        if self.capturebuffertable is not None and self.capturebuffertable.is_presence():
            return True

        if self.channeltable is not None and self.channeltable._has_data():
            return True

        if self.channeltable is not None and self.channeltable.is_presence():
            return True

        if self.etherhistorytable is not None and self.etherhistorytable._has_data():
            return True

        if self.etherhistorytable is not None and self.etherhistorytable.is_presence():
            return True

        if self.etherstatstable is not None and self.etherstatstable._has_data():
            return True

        if self.etherstatstable is not None and self.etherstatstable.is_presence():
            return True

        if self.eventtable is not None and self.eventtable._has_data():
            return True

        if self.eventtable is not None and self.eventtable.is_presence():
            return True

        if self.filtertable is not None and self.filtertable._has_data():
            return True

        if self.filtertable is not None and self.filtertable.is_presence():
            return True

        if self.historycontroltable is not None and self.historycontroltable._has_data():
            return True

        if self.historycontroltable is not None and self.historycontroltable.is_presence():
            return True

        if self.hostcontroltable is not None and self.hostcontroltable._has_data():
            return True

        if self.hostcontroltable is not None and self.hostcontroltable.is_presence():
            return True

        if self.hosttable is not None and self.hosttable._has_data():
            return True

        if self.hosttable is not None and self.hosttable.is_presence():
            return True

        if self.hosttimetable is not None and self.hosttimetable._has_data():
            return True

        if self.hosttimetable is not None and self.hosttimetable.is_presence():
            return True

        if self.hosttopncontroltable is not None and self.hosttopncontroltable._has_data():
            return True

        if self.hosttopncontroltable is not None and self.hosttopncontroltable.is_presence():
            return True

        if self.hosttopntable is not None and self.hosttopntable._has_data():
            return True

        if self.hosttopntable is not None and self.hosttopntable.is_presence():
            return True

        if self.logtable is not None and self.logtable._has_data():
            return True

        if self.logtable is not None and self.logtable.is_presence():
            return True

        if self.matrixcontroltable is not None and self.matrixcontroltable._has_data():
            return True

        if self.matrixcontroltable is not None and self.matrixcontroltable.is_presence():
            return True

        if self.matrixdstable is not None and self.matrixdstable._has_data():
            return True

        if self.matrixdstable is not None and self.matrixdstable.is_presence():
            return True

        if self.matrixsdtable is not None and self.matrixsdtable._has_data():
            return True

        if self.matrixsdtable is not None and self.matrixsdtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.rfc1271._meta import _RFC1271_MIB as meta
        return meta._meta_table['RFC1271MIB']['meta_info']


