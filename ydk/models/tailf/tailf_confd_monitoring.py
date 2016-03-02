""" tailf_confd_monitoring 

This module defines status objects for monitoring of ConfD.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class ConfdState(object):
    """
    
    
    .. attribute:: cli
    
    	
    	**type**\: :py:class:`Cli <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Cli>`
    
    .. attribute:: daemon_status
    
    	
    	**type**\: :py:class:`DaemonStatus_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.DaemonStatus_Enum>`
    
    .. attribute:: epoll
    
    	Indicates whether an enhanced poll() function is used
    	**type**\: bool
    
    .. attribute:: ha
    
    	
    	**type**\: :py:class:`Ha <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Ha>`
    
    .. attribute:: internal
    
    	
    	**type**\: :py:class:`Internal <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal>`
    
    .. attribute:: loaded_data_models
    
    	
    	**type**\: :py:class:`LoadedDataModels <ydk.models.tailf.tailf_confd_monitoring.ConfdState.LoadedDataModels>`
    
    .. attribute:: netconf
    
    	
    	**type**\: :py:class:`Netconf <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Netconf>`
    
    .. attribute:: read_only_mode
    
    	
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: rest
    
    	
    	**type**\: :py:class:`Rest <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Rest>`
    
    .. attribute:: smp
    
    	
    	**type**\: :py:class:`Smp <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Smp>`
    
    .. attribute:: snmp
    
    	
    	**type**\: :py:class:`Snmp <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Snmp>`
    
    .. attribute:: upgrade_mode
    
    	Note that if the node is in upgrade mode, it is not possible to get any information from the system over NETCONF. The error\-app\-tag will be upgrade\-in\-progress.  Existing CLI sessions can get system information
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: version
    
    	Tail\-f product version number
    	**type**\: str
    
    .. attribute:: webui
    
    	
    	**type**\: :py:class:`Webui <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Webui>`
    
    

    """

    _prefix = 'tfcm'
    _revision = '2013-06-14'

    def __init__(self):
        self.cli = None
        self.daemon_status = None
        self.epoll = None
        self.ha = None
        self.internal = ConfdState.Internal()
        self.internal.parent = self
        self.loaded_data_models = ConfdState.LoadedDataModels()
        self.loaded_data_models.parent = self
        self.netconf = None
        self.read_only_mode = None
        self.rest = None
        self.smp = None
        self.snmp = None
        self.upgrade_mode = None
        self.version = None
        self.webui = None

    class DaemonStatus_Enum(Enum):
        """
        DaemonStatus_Enum

        """

        """

        The daemon is starting up.

        """
        STARTING = 0

        """

        The daemon is running in start phase 0.

        """
        PHASE0 = 1

        """

        The daemon is running in start phase 1.

        """
        PHASE1 = 2

        """

        The daemon is started.

        """
        STARTED = 3

        """

        The daemon is stopping.

        """
        STOPPING = 4


        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
            return meta._meta_table['ConfdState.DaemonStatus_Enum']



    class Cli(object):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the CLI server is listening on.  In addition to the SSH addresses listen below, the CLI can always be invoked through the daemons IPC port.  Note that other mechanisms can be put in front of the IPC port, e.g., an OpenSSH server.  Such mechanisms are not known to the daemon and not listed here
        	**type**\: :py:class:`Listen <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Cli.Listen>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            self.parent = None
            self.listen = ConfdState.Cli.Listen()
            self.listen.parent = self


        class Listen(object):
            """
            The transport addresses the CLI server is listening on.
            
            In addition to the SSH addresses listen below, the CLI can
            always be invoked through the daemons IPC port.
            
            Note that other mechanisms can be put in front of the IPC
            port, e.g., an OpenSSH server.  Such mechanisms are not
            known to the daemon and not listed here.
            
            .. attribute:: ssh
            
            	
            	**type**\: list of :py:class:`Ssh <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Cli.Listen.Ssh>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                self.parent = None
                self.ssh = YList()
                self.ssh.parent = self
                self.ssh.name = 'ssh'


            class Ssh(object):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of { str | str }
                
                .. attribute:: port
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.port = None

                @property
                def _common_path(self):

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:cli/tailf-confd-monitoring:listen/tailf-confd-monitoring:ssh'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ip is not None:
                        return True

                    if self.port is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Cli.Listen.Ssh']['meta_info']

            @property
            def _common_path(self):

                return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:cli/tailf-confd-monitoring:listen'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ssh is not None:
                    for child_ref in self.ssh:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                return meta._meta_table['ConfdState.Cli.Listen']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:cli'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.listen is not None and self.listen._has_data():
                return True

            if self.listen is not None and self.listen.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
            return meta._meta_table['ConfdState.Cli']['meta_info']


    class Ha(object):
        """
        
        
        .. attribute:: connected_slave
        
        	The node identifiers of the currently connected slaves
        	**type**\: list of str
        
        .. attribute:: master_node_id
        
        	The node identifier of this node's parent node. This is the HA cluster's master node unless relay slaves are used
        	**type**\: str
        
        .. attribute:: mode
        
        	The current HA mode of the node in the HA cluster
        	**type**\: :py:class:`Mode_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Ha.Mode_Enum>`
        
        .. attribute:: node_id
        
        	The node identifier of this node in the HA cluster
        	**type**\: str
        
        .. attribute:: pending_slave
        
        	The node identifiers of slaves with pending acknowledgement of synchronous replication
        	**type**\: list of str
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            self.parent = None
            self.connected_slave = []
            self.master_node_id = None
            self.mode = None
            self.node_id = None
            self.pending_slave = []

        class Mode_Enum(Enum):
            """
            Mode_Enum

            The current HA mode of the node in the HA cluster.

            """

            NONE = 0

            SLAVE = 1

            MASTER = 2

            RELAY_SLAVE = 3


            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                return meta._meta_table['ConfdState.Ha.Mode_Enum']


        @property
        def _common_path(self):

            return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:ha'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.connected_slave is not None:
                for child in self.connected_slave:
                    if child is not None:
                        return True

            if self.master_node_id is not None:
                return True

            if self.mode is not None:
                return True

            if self.node_id is not None:
                return True

            if self.pending_slave is not None:
                for child in self.pending_slave:
                    if child is not None:
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
            return meta._meta_table['ConfdState.Ha']['meta_info']


    class Internal(object):
        """
        
        
        .. attribute:: callpoints
        
        	
        	**type**\: :py:class:`Callpoints <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints>`
        
        .. attribute:: cdb
        
        	
        	**type**\: :py:class:`Cdb <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb>`
        
        

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            self.parent = None
            self.callpoints = ConfdState.Internal.Callpoints()
            self.callpoints.parent = self
            self.cdb = ConfdState.Internal.Cdb()
            self.cdb.parent = self

        class DatastoreName_Enum(Enum):
            """
            DatastoreName_Enum

            Name of one of the datastores implemented by CDB.

            """

            RUNNING = 0

            STARTUP = 1

            OPERATIONAL = 2


            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                return meta._meta_table['ConfdState.Internal.DatastoreName_Enum']



        class Callpoints(object):
            """
            
            
            .. attribute:: actionpoint
            
            	
            	**type**\: list of :py:class:`Actionpoint <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint>`
            
            .. attribute:: authentication_callback
            
            	
            	**type**\: :py:class:`AuthenticationCallback <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback>`
            
            .. attribute:: authorization_callbacks
            
            	
            	**type**\: :py:class:`AuthorizationCallbacks <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks>`
            
            .. attribute:: callpoint
            
            	
            	**type**\: list of :py:class:`Callpoint <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint>`
            
            .. attribute:: error_formatting_callback
            
            	
            	**type**\: list of :py:class:`ErrorFormattingCallback <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback>`
            
            .. attribute:: notification_stream_replay
            
            	
            	**type**\: list of :py:class:`NotificationStreamReplay <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay>`
            
            .. attribute:: snmp_inform_callback
            
            	
            	**type**\: list of :py:class:`SnmpInformCallback <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback>`
            
            .. attribute:: snmp_notification_subscription
            
            	
            	**type**\: list of :py:class:`SnmpNotificationSubscription <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription>`
            
            .. attribute:: typepoint
            
            	
            	**type**\: list of :py:class:`Typepoint <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint>`
            
            .. attribute:: validationpoint
            
            	
            	**type**\: list of :py:class:`Validationpoint <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                self.parent = None
                self.actionpoint = YList()
                self.actionpoint.parent = self
                self.actionpoint.name = 'actionpoint'
                self.authentication_callback = None
                self.authorization_callbacks = None
                self.callpoint = YList()
                self.callpoint.parent = self
                self.callpoint.name = 'callpoint'
                self.error_formatting_callback = YList()
                self.error_formatting_callback.parent = self
                self.error_formatting_callback.name = 'error_formatting_callback'
                self.notification_stream_replay = YList()
                self.notification_stream_replay.parent = self
                self.notification_stream_replay.name = 'notification_stream_replay'
                self.snmp_inform_callback = YList()
                self.snmp_inform_callback.parent = self
                self.snmp_inform_callback.name = 'snmp_inform_callback'
                self.snmp_notification_subscription = YList()
                self.snmp_notification_subscription.parent = self
                self.snmp_notification_subscription.name = 'snmp_notification_subscription'
                self.typepoint = YList()
                self.typepoint.parent = self
                self.typepoint.name = 'typepoint'
                self.validationpoint = YList()
                self.validationpoint.parent = self
                self.validationpoint.name = 'validationpoint'


            class Actionpoint(object):
                """
                
                
                .. attribute:: id
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Error_Enum>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of :py:class:`Range <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.daemon = ConfdState.Internal.Callpoints.Actionpoint.Daemon()
                    self.daemon.parent = self
                    self.error = None
                    self.file = None
                    self.path = None
                    self.range = YList()
                    self.range.parent = self
                    self.range.name = 'range'

                class Error_Enum(Enum):
                    """
                    Error_Enum

                    If this leaf exists, there is a problem
                    with the callpoint registration.

                    """

                    """

                    This value means that there is no registration
                    for the callpoint.

                    """
                    NOT_REGISTERED = 0

                    """

                    This value means that the callpoint does not exist,
                    but there is a registration for it.

                    """
                    UNKNOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Actionpoint.Error_Enum']



                class Daemon(object):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Daemon.Error_Enum>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.error = None
                        self.id = None
                        self.name = None

                    class Error_Enum(Enum):
                        """
                        Error_Enum

                        If this leaf exists, there is a problem
                        with the daemon registration.

                        """

                        """

                        This value means that the application daemon has not
                        completed the registration (with confd\_register\_done()).

                        """
                        PENDING = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.Actionpoint.Daemon.Error_Enum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.error is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Actionpoint.Daemon']['meta_info']


                class Range(object):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.daemon = ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon()
                        self.daemon.parent = self
                        self.default = None
                        self.lower = None
                        self.upper = None


                    class Daemon(object):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon.Error_Enum>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.error = None
                            self.id = None
                            self.name = None

                        class Error_Enum(Enum):
                            """
                            Error_Enum

                            If this leaf exists, there is a problem
                            with the daemon registration.

                            """

                            """

                            This value means that the application daemon has not
                            completed the registration (with confd\_register\_done()).

                            """
                            PENDING = 0


                            @staticmethod
                            def _meta_info():
                                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                                return meta._meta_table['ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon.Error_Enum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.error is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.daemon is not None and self.daemon._has_data():
                            return True

                        if self.daemon is not None and self.daemon.is_presence():
                            return True

                        if self.default is not None:
                            return True

                        if self.lower is not None:
                            return True

                        if self.upper is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Actionpoint.Range']['meta_info']

                @property
                def _common_path(self):
                    if self.id is None:
                        raise YPYDataValidationError('Key property id is None')

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:actionpoint[tailf-confd-monitoring:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.id is not None:
                        return True

                    if self.daemon is not None and self.daemon._has_data():
                        return True

                    if self.daemon is not None and self.daemon.is_presence():
                        return True

                    if self.error is not None:
                        return True

                    if self.file is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.range is not None:
                        for child_ref in self.range:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Callpoints.Actionpoint']['meta_info']


            class AuthenticationCallback(object):
                """
                
                
                .. attribute:: daemon
                
                	
                	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon>`
                
                .. attribute:: enabled
                
                	
                	**type**\: bool
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Error_Enum>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of :py:class:`Range <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Range>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.daemon = ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon()
                    self.daemon.parent = self
                    self.enabled = None
                    self.error = None
                    self.file = None
                    self.path = None
                    self.range = YList()
                    self.range.parent = self
                    self.range.name = 'range'

                class Error_Enum(Enum):
                    """
                    Error_Enum

                    If this leaf exists, there is a problem
                    with the callpoint registration.

                    """

                    """

                    This value means that there is no registration
                    for the callpoint.

                    """
                    NOT_REGISTERED = 0

                    """

                    This value means that the callpoint does not exist,
                    but there is a registration for it.

                    """
                    UNKNOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Error_Enum']



                class Daemon(object):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon.Error_Enum>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.error = None
                        self.id = None
                        self.name = None

                    class Error_Enum(Enum):
                        """
                        Error_Enum

                        If this leaf exists, there is a problem
                        with the daemon registration.

                        """

                        """

                        This value means that the application daemon has not
                        completed the registration (with confd\_register\_done()).

                        """
                        PENDING = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon.Error_Enum']


                    @property
                    def _common_path(self):

                        return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:authentication-callback/tailf-confd-monitoring:daemon'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.error is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon']['meta_info']


                class Range(object):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.daemon = ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon()
                        self.daemon.parent = self
                        self.default = None
                        self.lower = None
                        self.upper = None


                    class Daemon(object):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon.Error_Enum>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.error = None
                            self.id = None
                            self.name = None

                        class Error_Enum(Enum):
                            """
                            Error_Enum

                            If this leaf exists, there is a problem
                            with the daemon registration.

                            """

                            """

                            This value means that the application daemon has not
                            completed the registration (with confd\_register\_done()).

                            """
                            PENDING = 0


                            @staticmethod
                            def _meta_info():
                                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                                return meta._meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon.Error_Enum']


                        @property
                        def _common_path(self):

                            return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:authentication-callback/tailf-confd-monitoring:range/tailf-confd-monitoring:daemon'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.error is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon']['meta_info']

                    @property
                    def _common_path(self):

                        return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:authentication-callback/tailf-confd-monitoring:range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.daemon is not None and self.daemon._has_data():
                            return True

                        if self.daemon is not None and self.daemon.is_presence():
                            return True

                        if self.default is not None:
                            return True

                        if self.lower is not None:
                            return True

                        if self.upper is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Range']['meta_info']

                @property
                def _common_path(self):

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:authentication-callback'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.daemon is not None and self.daemon._has_data():
                        return True

                    if self.daemon is not None and self.daemon.is_presence():
                        return True

                    if self.enabled is not None:
                        return True

                    if self.error is not None:
                        return True

                    if self.file is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.range is not None:
                        for child_ref in self.range:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return True

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback']['meta_info']


            class AuthorizationCallbacks(object):
                """
                
                
                .. attribute:: daemon
                
                	
                	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon>`
                
                .. attribute:: enabled
                
                	
                	**type**\: bool
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Error_Enum>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of :py:class:`Range <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.daemon = ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon()
                    self.daemon.parent = self
                    self.enabled = None
                    self.error = None
                    self.file = None
                    self.path = None
                    self.range = YList()
                    self.range.parent = self
                    self.range.name = 'range'

                class Error_Enum(Enum):
                    """
                    Error_Enum

                    If this leaf exists, there is a problem
                    with the callpoint registration.

                    """

                    """

                    This value means that there is no registration
                    for the callpoint.

                    """
                    NOT_REGISTERED = 0

                    """

                    This value means that the callpoint does not exist,
                    but there is a registration for it.

                    """
                    UNKNOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Error_Enum']



                class Daemon(object):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon.Error_Enum>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.error = None
                        self.id = None
                        self.name = None

                    class Error_Enum(Enum):
                        """
                        Error_Enum

                        If this leaf exists, there is a problem
                        with the daemon registration.

                        """

                        """

                        This value means that the application daemon has not
                        completed the registration (with confd\_register\_done()).

                        """
                        PENDING = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon.Error_Enum']


                    @property
                    def _common_path(self):

                        return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:authorization-callbacks/tailf-confd-monitoring:daemon'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.error is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon']['meta_info']


                class Range(object):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.daemon = ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon()
                        self.daemon.parent = self
                        self.default = None
                        self.lower = None
                        self.upper = None


                    class Daemon(object):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon.Error_Enum>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.error = None
                            self.id = None
                            self.name = None

                        class Error_Enum(Enum):
                            """
                            Error_Enum

                            If this leaf exists, there is a problem
                            with the daemon registration.

                            """

                            """

                            This value means that the application daemon has not
                            completed the registration (with confd\_register\_done()).

                            """
                            PENDING = 0


                            @staticmethod
                            def _meta_info():
                                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                                return meta._meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon.Error_Enum']


                        @property
                        def _common_path(self):

                            return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:authorization-callbacks/tailf-confd-monitoring:range/tailf-confd-monitoring:daemon'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.error is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon']['meta_info']

                    @property
                    def _common_path(self):

                        return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:authorization-callbacks/tailf-confd-monitoring:range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.daemon is not None and self.daemon._has_data():
                            return True

                        if self.daemon is not None and self.daemon.is_presence():
                            return True

                        if self.default is not None:
                            return True

                        if self.lower is not None:
                            return True

                        if self.upper is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range']['meta_info']

                @property
                def _common_path(self):

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:authorization-callbacks'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.daemon is not None and self.daemon._has_data():
                        return True

                    if self.daemon is not None and self.daemon.is_presence():
                        return True

                    if self.enabled is not None:
                        return True

                    if self.error is not None:
                        return True

                    if self.file is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.range is not None:
                        for child_ref in self.range:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return True

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks']['meta_info']


            class Callpoint(object):
                """
                
                
                .. attribute:: id
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Error_Enum>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of :py:class:`Range <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.daemon = ConfdState.Internal.Callpoints.Callpoint.Daemon()
                    self.daemon.parent = self
                    self.error = None
                    self.file = None
                    self.path = None
                    self.range = YList()
                    self.range.parent = self
                    self.range.name = 'range'

                class Error_Enum(Enum):
                    """
                    Error_Enum

                    If this leaf exists, there is a problem
                    with the callpoint registration.

                    """

                    """

                    This value means that there is no registration
                    for the callpoint.

                    """
                    NOT_REGISTERED = 0

                    """

                    This value means that the callpoint does not exist,
                    but there is a registration for it.

                    """
                    UNKNOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Callpoint.Error_Enum']



                class Daemon(object):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Daemon.Error_Enum>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.error = None
                        self.id = None
                        self.name = None

                    class Error_Enum(Enum):
                        """
                        Error_Enum

                        If this leaf exists, there is a problem
                        with the daemon registration.

                        """

                        """

                        This value means that the application daemon has not
                        completed the registration (with confd\_register\_done()).

                        """
                        PENDING = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.Callpoint.Daemon.Error_Enum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.error is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Callpoint.Daemon']['meta_info']


                class Range(object):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.daemon = ConfdState.Internal.Callpoints.Callpoint.Range.Daemon()
                        self.daemon.parent = self
                        self.default = None
                        self.lower = None
                        self.upper = None


                    class Daemon(object):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Callpoint.Range.Daemon.Error_Enum>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.error = None
                            self.id = None
                            self.name = None

                        class Error_Enum(Enum):
                            """
                            Error_Enum

                            If this leaf exists, there is a problem
                            with the daemon registration.

                            """

                            """

                            This value means that the application daemon has not
                            completed the registration (with confd\_register\_done()).

                            """
                            PENDING = 0


                            @staticmethod
                            def _meta_info():
                                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                                return meta._meta_table['ConfdState.Internal.Callpoints.Callpoint.Range.Daemon.Error_Enum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.error is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.Callpoint.Range.Daemon']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.daemon is not None and self.daemon._has_data():
                            return True

                        if self.daemon is not None and self.daemon.is_presence():
                            return True

                        if self.default is not None:
                            return True

                        if self.lower is not None:
                            return True

                        if self.upper is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Callpoint.Range']['meta_info']

                @property
                def _common_path(self):
                    if self.id is None:
                        raise YPYDataValidationError('Key property id is None')

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:callpoint[tailf-confd-monitoring:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.id is not None:
                        return True

                    if self.daemon is not None and self.daemon._has_data():
                        return True

                    if self.daemon is not None and self.daemon.is_presence():
                        return True

                    if self.error is not None:
                        return True

                    if self.file is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.range is not None:
                        for child_ref in self.range:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Callpoints.Callpoint']['meta_info']


            class ErrorFormattingCallback(object):
                """
                
                
                .. attribute:: id
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Error_Enum>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of :py:class:`Range <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.daemon = ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon()
                    self.daemon.parent = self
                    self.error = None
                    self.file = None
                    self.path = None
                    self.range = YList()
                    self.range.parent = self
                    self.range.name = 'range'

                class Error_Enum(Enum):
                    """
                    Error_Enum

                    If this leaf exists, there is a problem
                    with the callpoint registration.

                    """

                    """

                    This value means that there is no registration
                    for the callpoint.

                    """
                    NOT_REGISTERED = 0

                    """

                    This value means that the callpoint does not exist,
                    but there is a registration for it.

                    """
                    UNKNOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Error_Enum']



                class Daemon(object):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon.Error_Enum>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.error = None
                        self.id = None
                        self.name = None

                    class Error_Enum(Enum):
                        """
                        Error_Enum

                        If this leaf exists, there is a problem
                        with the daemon registration.

                        """

                        """

                        This value means that the application daemon has not
                        completed the registration (with confd\_register\_done()).

                        """
                        PENDING = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon.Error_Enum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.error is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon']['meta_info']


                class Range(object):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.daemon = ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon()
                        self.daemon.parent = self
                        self.default = None
                        self.lower = None
                        self.upper = None


                    class Daemon(object):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon.Error_Enum>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.error = None
                            self.id = None
                            self.name = None

                        class Error_Enum(Enum):
                            """
                            Error_Enum

                            If this leaf exists, there is a problem
                            with the daemon registration.

                            """

                            """

                            This value means that the application daemon has not
                            completed the registration (with confd\_register\_done()).

                            """
                            PENDING = 0


                            @staticmethod
                            def _meta_info():
                                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                                return meta._meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon.Error_Enum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.error is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.daemon is not None and self.daemon._has_data():
                            return True

                        if self.daemon is not None and self.daemon.is_presence():
                            return True

                        if self.default is not None:
                            return True

                        if self.lower is not None:
                            return True

                        if self.upper is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range']['meta_info']

                @property
                def _common_path(self):
                    if self.id is None:
                        raise YPYDataValidationError('Key property id is None')

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:error-formatting-callback[tailf-confd-monitoring:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.id is not None:
                        return True

                    if self.daemon is not None and self.daemon._has_data():
                        return True

                    if self.daemon is not None and self.daemon.is_presence():
                        return True

                    if self.error is not None:
                        return True

                    if self.file is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.range is not None:
                        for child_ref in self.range:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback']['meta_info']


            class NotificationStreamReplay(object):
                """
                
                
                .. attribute:: name
                
                	Name of the notification stream
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Error_Enum>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of :py:class:`Range <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Range>`
                
                .. attribute:: replay_support
                
                	
                	**type**\: :py:class:`ReplaySupport_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.ReplaySupport_Enum>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.daemon = ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon()
                    self.daemon.parent = self
                    self.error = None
                    self.file = None
                    self.path = None
                    self.range = YList()
                    self.range.parent = self
                    self.range.name = 'range'
                    self.replay_support = None

                class Error_Enum(Enum):
                    """
                    Error_Enum

                    If this leaf exists, there is a problem
                    with the callpoint registration.

                    """

                    """

                    This value means that there is no registration
                    for the callpoint.

                    """
                    NOT_REGISTERED = 0

                    """

                    This value means that the callpoint does not exist,
                    but there is a registration for it.

                    """
                    UNKNOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Error_Enum']


                class ReplaySupport_Enum(Enum):
                    """
                    ReplaySupport_Enum

                    """

                    NONE = 0

                    BUILTIN = 1

                    EXTERNAL = 2


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.ReplaySupport_Enum']



                class Daemon(object):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon.Error_Enum>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.error = None
                        self.id = None
                        self.name = None

                    class Error_Enum(Enum):
                        """
                        Error_Enum

                        If this leaf exists, there is a problem
                        with the daemon registration.

                        """

                        """

                        This value means that the application daemon has not
                        completed the registration (with confd\_register\_done()).

                        """
                        PENDING = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon.Error_Enum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.error is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon']['meta_info']


                class Range(object):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.daemon = ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon()
                        self.daemon.parent = self
                        self.default = None
                        self.lower = None
                        self.upper = None


                    class Daemon(object):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon.Error_Enum>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.error = None
                            self.id = None
                            self.name = None

                        class Error_Enum(Enum):
                            """
                            Error_Enum

                            If this leaf exists, there is a problem
                            with the daemon registration.

                            """

                            """

                            This value means that the application daemon has not
                            completed the registration (with confd\_register\_done()).

                            """
                            PENDING = 0


                            @staticmethod
                            def _meta_info():
                                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                                return meta._meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon.Error_Enum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.error is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.daemon is not None and self.daemon._has_data():
                            return True

                        if self.daemon is not None and self.daemon.is_presence():
                            return True

                        if self.default is not None:
                            return True

                        if self.lower is not None:
                            return True

                        if self.upper is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Range']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:notification-stream-replay[tailf-confd-monitoring:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.name is not None:
                        return True

                    if self.daemon is not None and self.daemon._has_data():
                        return True

                    if self.daemon is not None and self.daemon.is_presence():
                        return True

                    if self.error is not None:
                        return True

                    if self.file is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.range is not None:
                        for child_ref in self.range:
                            if child_ref._has_data():
                                return True

                    if self.replay_support is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay']['meta_info']


            class SnmpInformCallback(object):
                """
                
                
                .. attribute:: id
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Error_Enum>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of :py:class:`Range <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.daemon = ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon()
                    self.daemon.parent = self
                    self.error = None
                    self.file = None
                    self.path = None
                    self.range = YList()
                    self.range.parent = self
                    self.range.name = 'range'

                class Error_Enum(Enum):
                    """
                    Error_Enum

                    If this leaf exists, there is a problem
                    with the callpoint registration.

                    """

                    """

                    This value means that there is no registration
                    for the callpoint.

                    """
                    NOT_REGISTERED = 0

                    """

                    This value means that the callpoint does not exist,
                    but there is a registration for it.

                    """
                    UNKNOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Error_Enum']



                class Daemon(object):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon.Error_Enum>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.error = None
                        self.id = None
                        self.name = None

                    class Error_Enum(Enum):
                        """
                        Error_Enum

                        If this leaf exists, there is a problem
                        with the daemon registration.

                        """

                        """

                        This value means that the application daemon has not
                        completed the registration (with confd\_register\_done()).

                        """
                        PENDING = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon.Error_Enum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.error is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon']['meta_info']


                class Range(object):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.daemon = ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon()
                        self.daemon.parent = self
                        self.default = None
                        self.lower = None
                        self.upper = None


                    class Daemon(object):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon.Error_Enum>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.error = None
                            self.id = None
                            self.name = None

                        class Error_Enum(Enum):
                            """
                            Error_Enum

                            If this leaf exists, there is a problem
                            with the daemon registration.

                            """

                            """

                            This value means that the application daemon has not
                            completed the registration (with confd\_register\_done()).

                            """
                            PENDING = 0


                            @staticmethod
                            def _meta_info():
                                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                                return meta._meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon.Error_Enum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.error is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.daemon is not None and self.daemon._has_data():
                            return True

                        if self.daemon is not None and self.daemon.is_presence():
                            return True

                        if self.default is not None:
                            return True

                        if self.lower is not None:
                            return True

                        if self.upper is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Range']['meta_info']

                @property
                def _common_path(self):
                    if self.id is None:
                        raise YPYDataValidationError('Key property id is None')

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:snmp-inform-callback[tailf-confd-monitoring:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.id is not None:
                        return True

                    if self.daemon is not None and self.daemon._has_data():
                        return True

                    if self.daemon is not None and self.daemon.is_presence():
                        return True

                    if self.error is not None:
                        return True

                    if self.file is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.range is not None:
                        for child_ref in self.range:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback']['meta_info']


            class SnmpNotificationSubscription(object):
                """
                
                
                .. attribute:: id
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Error_Enum>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of :py:class:`Range <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.daemon = ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon()
                    self.daemon.parent = self
                    self.error = None
                    self.file = None
                    self.path = None
                    self.range = YList()
                    self.range.parent = self
                    self.range.name = 'range'

                class Error_Enum(Enum):
                    """
                    Error_Enum

                    If this leaf exists, there is a problem
                    with the callpoint registration.

                    """

                    """

                    This value means that there is no registration
                    for the callpoint.

                    """
                    NOT_REGISTERED = 0

                    """

                    This value means that the callpoint does not exist,
                    but there is a registration for it.

                    """
                    UNKNOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Error_Enum']



                class Daemon(object):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon.Error_Enum>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.error = None
                        self.id = None
                        self.name = None

                    class Error_Enum(Enum):
                        """
                        Error_Enum

                        If this leaf exists, there is a problem
                        with the daemon registration.

                        """

                        """

                        This value means that the application daemon has not
                        completed the registration (with confd\_register\_done()).

                        """
                        PENDING = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon.Error_Enum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.error is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon']['meta_info']


                class Range(object):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.daemon = ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon()
                        self.daemon.parent = self
                        self.default = None
                        self.lower = None
                        self.upper = None


                    class Daemon(object):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon.Error_Enum>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.error = None
                            self.id = None
                            self.name = None

                        class Error_Enum(Enum):
                            """
                            Error_Enum

                            If this leaf exists, there is a problem
                            with the daemon registration.

                            """

                            """

                            This value means that the application daemon has not
                            completed the registration (with confd\_register\_done()).

                            """
                            PENDING = 0


                            @staticmethod
                            def _meta_info():
                                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                                return meta._meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon.Error_Enum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.error is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.daemon is not None and self.daemon._has_data():
                            return True

                        if self.daemon is not None and self.daemon.is_presence():
                            return True

                        if self.default is not None:
                            return True

                        if self.lower is not None:
                            return True

                        if self.upper is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range']['meta_info']

                @property
                def _common_path(self):
                    if self.id is None:
                        raise YPYDataValidationError('Key property id is None')

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:snmp-notification-subscription[tailf-confd-monitoring:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.id is not None:
                        return True

                    if self.daemon is not None and self.daemon._has_data():
                        return True

                    if self.daemon is not None and self.daemon.is_presence():
                        return True

                    if self.error is not None:
                        return True

                    if self.file is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.range is not None:
                        for child_ref in self.range:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription']['meta_info']


            class Typepoint(object):
                """
                
                
                .. attribute:: id
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Error_Enum>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of :py:class:`Range <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.daemon = ConfdState.Internal.Callpoints.Typepoint.Daemon()
                    self.daemon.parent = self
                    self.error = None
                    self.file = None
                    self.path = None
                    self.range = YList()
                    self.range.parent = self
                    self.range.name = 'range'

                class Error_Enum(Enum):
                    """
                    Error_Enum

                    If this leaf exists, there is a problem
                    with the callpoint registration.

                    """

                    """

                    This value means that there is no registration
                    for the callpoint.

                    """
                    NOT_REGISTERED = 0

                    """

                    This value means that the callpoint does not exist,
                    but there is a registration for it.

                    """
                    UNKNOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Typepoint.Error_Enum']



                class Daemon(object):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Daemon.Error_Enum>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.error = None
                        self.id = None
                        self.name = None

                    class Error_Enum(Enum):
                        """
                        Error_Enum

                        If this leaf exists, there is a problem
                        with the daemon registration.

                        """

                        """

                        This value means that the application daemon has not
                        completed the registration (with confd\_register\_done()).

                        """
                        PENDING = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.Typepoint.Daemon.Error_Enum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.error is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Typepoint.Daemon']['meta_info']


                class Range(object):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.daemon = ConfdState.Internal.Callpoints.Typepoint.Range.Daemon()
                        self.daemon.parent = self
                        self.default = None
                        self.lower = None
                        self.upper = None


                    class Daemon(object):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Typepoint.Range.Daemon.Error_Enum>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.error = None
                            self.id = None
                            self.name = None

                        class Error_Enum(Enum):
                            """
                            Error_Enum

                            If this leaf exists, there is a problem
                            with the daemon registration.

                            """

                            """

                            This value means that the application daemon has not
                            completed the registration (with confd\_register\_done()).

                            """
                            PENDING = 0


                            @staticmethod
                            def _meta_info():
                                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                                return meta._meta_table['ConfdState.Internal.Callpoints.Typepoint.Range.Daemon.Error_Enum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.error is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.Typepoint.Range.Daemon']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.daemon is not None and self.daemon._has_data():
                            return True

                        if self.daemon is not None and self.daemon.is_presence():
                            return True

                        if self.default is not None:
                            return True

                        if self.lower is not None:
                            return True

                        if self.upper is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Typepoint.Range']['meta_info']

                @property
                def _common_path(self):
                    if self.id is None:
                        raise YPYDataValidationError('Key property id is None')

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:typepoint[tailf-confd-monitoring:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.id is not None:
                        return True

                    if self.daemon is not None and self.daemon._has_data():
                        return True

                    if self.daemon is not None and self.daemon.is_presence():
                        return True

                    if self.error is not None:
                        return True

                    if self.file is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.range is not None:
                        for child_ref in self.range:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Callpoints.Typepoint']['meta_info']


            class Validationpoint(object):
                """
                
                
                .. attribute:: id
                
                	Callpoint id
                	**type**\: str
                
                .. attribute:: daemon
                
                	
                	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Daemon>`
                
                .. attribute:: error
                
                	If this leaf exists, there is a problem with the callpoint registration
                	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Error_Enum>`
                
                .. attribute:: file
                
                	The pathname of the shared object implementing the type for a typepoint
                	**type**\: str
                
                .. attribute:: path
                
                	The path of the list that a range registration pertains to
                	**type**\: str
                
                .. attribute:: range
                
                	
                	**type**\: list of :py:class:`Range <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Range>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.daemon = ConfdState.Internal.Callpoints.Validationpoint.Daemon()
                    self.daemon.parent = self
                    self.error = None
                    self.file = None
                    self.path = None
                    self.range = YList()
                    self.range.parent = self
                    self.range.name = 'range'

                class Error_Enum(Enum):
                    """
                    Error_Enum

                    If this leaf exists, there is a problem
                    with the callpoint registration.

                    """

                    """

                    This value means that there is no registration
                    for the callpoint.

                    """
                    NOT_REGISTERED = 0

                    """

                    This value means that the callpoint does not exist,
                    but there is a registration for it.

                    """
                    UNKNOWN = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Validationpoint.Error_Enum']



                class Daemon(object):
                    """
                    
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem with the daemon registration
                    	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Daemon.Error_Enum>`
                    
                    .. attribute:: id
                    
                    	The numerical id assigned to the application daemon that has registered for a callpoint
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	The name of the application daemon that has registered for a callpoint
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.error = None
                        self.id = None
                        self.name = None

                    class Error_Enum(Enum):
                        """
                        Error_Enum

                        If this leaf exists, there is a problem
                        with the daemon registration.

                        """

                        """

                        This value means that the application daemon has not
                        completed the registration (with confd\_register\_done()).

                        """
                        PENDING = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.Validationpoint.Daemon.Error_Enum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.error is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Validationpoint.Daemon']['meta_info']


                class Range(object):
                    """
                    
                    
                    .. attribute:: daemon
                    
                    	
                    	**type**\: :py:class:`Daemon <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon>`
                    
                    .. attribute:: default
                    
                    	If this leaf exists, this is a default registration \- in this case 'lower' and 'upper' do not exist
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: lower
                    
                    	The space\-separated set of keys that defines the lower endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    .. attribute:: upper
                    
                    	The space\-separated set of keys that defines the upper endpoint of the range for a non\-default registration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.daemon = ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon()
                        self.daemon.parent = self
                        self.default = None
                        self.lower = None
                        self.upper = None


                    class Daemon(object):
                        """
                        
                        
                        .. attribute:: error
                        
                        	If this leaf exists, there is a problem with the daemon registration
                        	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon.Error_Enum>`
                        
                        .. attribute:: id
                        
                        	The numerical id assigned to the application daemon that has registered for a callpoint
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	The name of the application daemon that has registered for a callpoint
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.error = None
                            self.id = None
                            self.name = None

                        class Error_Enum(Enum):
                            """
                            Error_Enum

                            If this leaf exists, there is a problem
                            with the daemon registration.

                            """

                            """

                            This value means that the application daemon has not
                            completed the registration (with confd\_register\_done()).

                            """
                            PENDING = 0


                            @staticmethod
                            def _meta_info():
                                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                                return meta._meta_table['ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon.Error_Enum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/tailf-confd-monitoring:daemon'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.error is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.name is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.daemon is not None and self.daemon._has_data():
                            return True

                        if self.daemon is not None and self.daemon.is_presence():
                            return True

                        if self.default is not None:
                            return True

                        if self.lower is not None:
                            return True

                        if self.upper is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Callpoints.Validationpoint.Range']['meta_info']

                @property
                def _common_path(self):
                    if self.id is None:
                        raise YPYDataValidationError('Key property id is None')

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints/tailf-confd-monitoring:validationpoint[tailf-confd-monitoring:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.id is not None:
                        return True

                    if self.daemon is not None and self.daemon._has_data():
                        return True

                    if self.daemon is not None and self.daemon.is_presence():
                        return True

                    if self.error is not None:
                        return True

                    if self.file is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.range is not None:
                        for child_ref in self.range:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Callpoints.Validationpoint']['meta_info']

            @property
            def _common_path(self):

                return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:callpoints'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.actionpoint is not None:
                    for child_ref in self.actionpoint:
                        if child_ref._has_data():
                            return True

                if self.authentication_callback is not None and self.authentication_callback._has_data():
                    return True

                if self.authentication_callback is not None and self.authentication_callback.is_presence():
                    return True

                if self.authorization_callbacks is not None and self.authorization_callbacks._has_data():
                    return True

                if self.authorization_callbacks is not None and self.authorization_callbacks.is_presence():
                    return True

                if self.callpoint is not None:
                    for child_ref in self.callpoint:
                        if child_ref._has_data():
                            return True

                if self.error_formatting_callback is not None:
                    for child_ref in self.error_formatting_callback:
                        if child_ref._has_data():
                            return True

                if self.notification_stream_replay is not None:
                    for child_ref in self.notification_stream_replay:
                        if child_ref._has_data():
                            return True

                if self.snmp_inform_callback is not None:
                    for child_ref in self.snmp_inform_callback:
                        if child_ref._has_data():
                            return True

                if self.snmp_notification_subscription is not None:
                    for child_ref in self.snmp_notification_subscription:
                        if child_ref._has_data():
                            return True

                if self.typepoint is not None:
                    for child_ref in self.typepoint:
                        if child_ref._has_data():
                            return True

                if self.validationpoint is not None:
                    for child_ref in self.validationpoint:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                return meta._meta_table['ConfdState.Internal.Callpoints']['meta_info']


        class Cdb(object):
            """
            
            
            .. attribute:: client
            
            	
            	**type**\: list of :py:class:`Client <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client>`
            
            .. attribute:: datastore
            
            	
            	**type**\: list of :py:class:`Datastore <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                self.parent = None
                self.client = YList()
                self.client.parent = self
                self.client.name = 'client'
                self.datastore = YList()
                self.datastore.parent = self
                self.datastore.name = 'datastore'


            class Client(object):
                """
                
                
                .. attribute:: datastore
                
                	The name of the datastore when 'type' = 'client'. The value 'pre\_commit\_running' is the 'pseudo' datastore representing 'running' before a commit
                	**type**\: one of { :py:class:`DatastoreName_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.DatastoreName_Enum>` | :py:class:`Datastore_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Datastore_Enum>` }
                
                .. attribute:: info
                
                	Additional information about the client obtained at connect time. If present, it consists of client PID and socket file descriptor number
                	**type**\: str
                
                .. attribute:: lock
                
                	Set when 'type' = 'client' and the client has requested or acquired a lock on the datastore. The 'pending\-read' and 'pending\-subscription' values indicate that the client has requested but not yet acquired the corresponding lock. A 'read' lock is never taken for the 'operational' datastore, a 'subscription' lock is never taken for any other datastore than 'operational'
                	**type**\: :py:class:`Lock_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Lock_Enum>`
                
                .. attribute:: name
                
                	The client name
                	**type**\: str
                
                .. attribute:: subscription
                
                	
                	**type**\: list of :py:class:`Subscription <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Subscription>`
                
                .. attribute:: type
                
                	The type of client\: 'inactive' is a client connection without any specific state. 'client' means that the client has an active session towards a datastore. A 'subscriber' has made one or more subscriptions. 'waiting' means that the client is waiting for completion of a call such as cdb\_wait\_start()
                	**type**\: :py:class:`Type_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Type_Enum>`
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.datastore = None
                    self.info = None
                    self.lock = None
                    self.name = None
                    self.subscription = YList()
                    self.subscription.parent = self
                    self.subscription.name = 'subscription'
                    self.type = None

                class Datastore_Enum(Enum):
                    """
                    Datastore_Enum

                    The name of the datastore when 'type' = 'client'. The value
                    'pre\_commit\_running' is the 'pseudo' datastore representing
                    'running' before a commit.

                    """

                    PRE_COMMIT_RUNNING = 9


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Cdb.Client.Datastore_Enum']


                class Lock_Enum(Enum):
                    """
                    Lock_Enum

                    Set when 'type' = 'client' and the client has requested or
                    acquired a lock on the datastore. The 'pending\-read' and
                    'pending\-subscription' values indicate that the client has
                    requested but not yet acquired the corresponding lock.
                    A 'read' lock is never taken for the 'operational' datastore,
                    a 'subscription' lock is never taken for any other datastore
                    than 'operational'.

                    """

                    READ = 0

                    SUBSCRIPTION = 1

                    PENDING_READ = 2

                    PENDING_SUBSCRIPTION = 3


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Cdb.Client.Lock_Enum']


                class Type_Enum(Enum):
                    """
                    Type_Enum

                    The type of client\: 'inactive' is a client connection without
                    any specific state. 'client' means that the client has an
                    active session towards a datastore. A 'subscriber' has made
                    one or more subscriptions. 'waiting' means that the client is
                    waiting for completion of a call such as cdb\_wait\_start().

                    """

                    INACTIVE = 0

                    CLIENT = 1

                    SUBSCRIBER = 2

                    WAITING = 3


                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Cdb.Client.Type_Enum']



                class Subscription(object):
                    """
                    
                    
                    .. attribute:: datastore
                    
                    	The name of the datastore for the subscription \- only 'running' and 'operational' can have subscriptions
                    	**type**\: :py:class:`DatastoreName_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.DatastoreName_Enum>`
                    
                    .. attribute:: error
                    
                    	If this leaf exists, there is a problem  with the subscription
                    	**type**\: :py:class:`Error_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Client.Subscription.Error_Enum>`
                    
                    .. attribute:: id
                    
                    	The subscription identifier for the subscription
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: path
                    
                    	The path that the subscription pertains to
                    	**type**\: str
                    
                    .. attribute:: priority
                    
                    	The priority of the subscription
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: twophase
                    
                    	Present if this is a 'twophase' subscription, i.e. notifications will be delivered at 'prepare' in addition to 'commit'. Only for the 'running' datastore
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.datastore = None
                        self.error = None
                        self.id = None
                        self.path = None
                        self.priority = None
                        self.twophase = None

                    class Error_Enum(Enum):
                        """
                        Error_Enum

                        If this leaf exists, there is a problem
                         with the subscription.

                        """

                        """

                        This value means that the subscribing client has not
                        completed the subscription (with cdb\_subscribe\_done()).

                        """
                        PENDING = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Cdb.Client.Subscription.Error_Enum']


                    @property
                    def _common_path(self):

                        return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:cdb/tailf-confd-monitoring:client/tailf-confd-monitoring:subscription'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.datastore is not None:
                            return True

                        if self.error is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.path is not None:
                            return True

                        if self.priority is not None:
                            return True

                        if self.twophase is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Cdb.Client.Subscription']['meta_info']

                @property
                def _common_path(self):

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:cdb/tailf-confd-monitoring:client'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.datastore is not None:
                        return True

                    if self.info is not None:
                        return True

                    if self.lock is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.subscription is not None:
                        for child_ref in self.subscription:
                            if child_ref._has_data():
                                return True

                    if self.type is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Cdb.Client']['meta_info']


            class Datastore(object):
                """
                
                
                .. attribute:: name
                
                	
                	**type**\: :py:class:`DatastoreName_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.DatastoreName_Enum>`
                
                .. attribute:: disk_size
                
                	The size of the file that is used for persistent storage for the datastore. Only present if 'filename' is present
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: filename
                
                	The pathname of the file that is used for persistent storage for the datastore. Not present for 'running' when 'startup' exists
                	**type**\: str
                
                .. attribute:: pending_notification_queue
                
                	Queues of notifications that have been generated but not yet delivered to subscribing clients. Not present for the 'startup' datastore
                	**type**\: list of :py:class:`PendingNotificationQueue <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue>`
                
                .. attribute:: pending_subscription_sync
                
                	Information pertaining to subscription notifications that have been delivered to, but not yet acknowledged by, subscribing clients. Not present for the 'startup' datastore
                	**type**\: :py:class:`PendingSubscriptionSync <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync>`
                
                .. attribute:: ram_size
                
                	The size of the in\-memory representation of the datastore
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: read_locks
                
                	The number of read locks on the datastore. Not present for the 'operational' data store
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: subscription_lock_set
                
                	Indicates whether a subscription lock is in effect for the 'operational' datastore
                	**type**\: bool
                
                .. attribute:: transaction_id
                
                	The id of the last committed transaction for the 'running' datastore, or the last update for the 'operational' datastore. For the 'operational' datastore, it is only present when HA is enabled
                	**type**\: str
                
                .. attribute:: waiting_for_replication_sync
                
                	Indicates whether synchronous replication from HA master to HA slave is in progress for the datastore. Not present for the 'operational' datastore
                	**type**\: bool
                
                .. attribute:: write_lock_set
                
                	Indicates whether a write lock is in effect for the datastore. Not present for the 'operational' datastore
                	**type**\: bool
                
                .. attribute:: write_queue
                
                	Number of pending write requests for the 'operational' datastore on a HA slave that is in the process of syncronizing with the master
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.disk_size = None
                    self.filename = None
                    self.pending_notification_queue = YList()
                    self.pending_notification_queue.parent = self
                    self.pending_notification_queue.name = 'pending_notification_queue'
                    self.pending_subscription_sync = None
                    self.ram_size = None
                    self.read_locks = None
                    self.subscription_lock_set = None
                    self.transaction_id = None
                    self.waiting_for_replication_sync = None
                    self.write_lock_set = None
                    self.write_queue = None


                class PendingNotificationQueue(object):
                    """
                    Queues of notifications that have been generated but not
                    yet delivered to subscribing clients. Not present for the
                    'startup' datastore.
                    
                    .. attribute:: notification
                    
                    	
                    	**type**\: list of :py:class:`Notification <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification>`
                    
                    

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.notification = YList()
                        self.notification.parent = self
                        self.notification.name = 'notification'


                    class Notification(object):
                        """
                        
                        
                        .. attribute:: client_name
                        
                        	The name of the client that is the recipient of the notification
                        	**type**\: str
                        
                        .. attribute:: priority
                        
                        	The priority of the subscriptions that generated the notification. Not present for the the 'operational' datastore
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: subscription_ids
                        
                        	The subscription identifiers for the subscriptions that generated the notification
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.client_name = None
                            self.priority = None
                            self.subscription_ids = []

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/tailf-confd-monitoring:notification'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.client_name is not None:
                                return True

                            if self.priority is not None:
                                return True

                            if self.subscription_ids is not None:
                                for child in self.subscription_ids:
                                    if child is not None:
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:pending-notification-queue'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.notification is not None:
                            for child_ref in self.notification:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue']['meta_info']


                class PendingSubscriptionSync(object):
                    """
                    Information pertaining to subscription notifications that have
                    been delivered to, but not yet acknowledged by, subscribing
                    clients. Not present for the 'startup' datastore.
                    
                    .. attribute:: notification
                    
                    	
                    	**type**\: list of :py:class:`Notification <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification>`
                    
                    .. attribute:: priority
                    
                    	The priority of the subscriptions that generated the notifications that are waiting for acknowledgement. Not present for the 'operational' datastore
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: time_remaining
                    
                    	The remaining time in seconds until subscribing clients that have not acknowledged their notifications are considered unresponsive and will be disconnected. See /confdConfig/cdb/clientTimeout in the confd.conf(5) manual page. The value 'infinity' means that no timeout has been configured in confd.conf
                    	**type**\: one of { int | :py:class:`TimeRemaining_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.TimeRemaining_Enum>` }
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'tfcm'
                    _revision = '2013-06-14'

                    def __init__(self):
                        self.parent = None
                        self.notification = YList()
                        self.notification.parent = self
                        self.notification.name = 'notification'
                        self.priority = None
                        self.time_remaining = None

                    class TimeRemaining_Enum(Enum):
                        """
                        TimeRemaining_Enum

                        The remaining time in seconds until subscribing clients
                        that have not acknowledged their notifications are
                        considered unresponsive and will be disconnected. See
                        /confdConfig/cdb/clientTimeout in the confd.conf(5) manual
                        page. The value 'infinity' means that no timeout has been
                        configured in confd.conf.

                        """

                        INFINITY = 0


                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.TimeRemaining_Enum']



                    class Notification(object):
                        """
                        
                        
                        .. attribute:: client_name
                        
                        	The name of the client that is the recipient of the notification
                        	**type**\: str
                        
                        .. attribute:: subscription_ids
                        
                        	The subscription identifiers for the subscriptions that generated the notification
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'tfcm'
                        _revision = '2013-06-14'

                        def __init__(self):
                            self.parent = None
                            self.client_name = None
                            self.subscription_ids = []

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/tailf-confd-monitoring:notification'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.client_name is not None:
                                return True

                            if self.subscription_ids is not None:
                                for child in self.subscription_ids:
                                    if child is not None:
                                        return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                            return meta._meta_table['ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/tailf-confd-monitoring:pending-subscription-sync'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.notification is not None:
                            for child_ref in self.notification:
                                if child_ref._has_data():
                                    return True

                        if self.priority is not None:
                            return True

                        if self.time_remaining is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return True

                    @staticmethod
                    def _meta_info():
                        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                        return meta._meta_table['ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync']['meta_info']

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:cdb/tailf-confd-monitoring:datastore[tailf-confd-monitoring:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.name is not None:
                        return True

                    if self.disk_size is not None:
                        return True

                    if self.filename is not None:
                        return True

                    if self.pending_notification_queue is not None:
                        for child_ref in self.pending_notification_queue:
                            if child_ref._has_data():
                                return True

                    if self.pending_subscription_sync is not None and self.pending_subscription_sync._has_data():
                        return True

                    if self.pending_subscription_sync is not None and self.pending_subscription_sync.is_presence():
                        return True

                    if self.ram_size is not None:
                        return True

                    if self.read_locks is not None:
                        return True

                    if self.subscription_lock_set is not None:
                        return True

                    if self.transaction_id is not None:
                        return True

                    if self.waiting_for_replication_sync is not None:
                        return True

                    if self.write_lock_set is not None:
                        return True

                    if self.write_queue is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Internal.Cdb.Datastore']['meta_info']

            @property
            def _common_path(self):

                return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal/tailf-confd-monitoring:cdb'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.client is not None:
                    for child_ref in self.client:
                        if child_ref._has_data():
                            return True

                if self.datastore is not None:
                    for child_ref in self.datastore:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                return meta._meta_table['ConfdState.Internal.Cdb']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:internal'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.callpoints is not None and self.callpoints._has_data():
                return True

            if self.callpoints is not None and self.callpoints.is_presence():
                return True

            if self.cdb is not None and self.cdb._has_data():
                return True

            if self.cdb is not None and self.cdb.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
            return meta._meta_table['ConfdState.Internal']['meta_info']


    class LoadedDataModels(object):
        """
        
        
        .. attribute:: data_model
        
        	This list contains all loaded YANG data modules.  This list is a superset of the 'schema' list defined in ietf\-netconf\-monitoring, which only lists modules exported through NETCONF
        	**type**\: list of :py:class:`DataModel <ydk.models.tailf.tailf_confd_monitoring.ConfdState.LoadedDataModels.DataModel>`
        
        

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            self.parent = None
            self.data_model = YList()
            self.data_model.parent = self
            self.data_model.name = 'data_model'


        class DataModel(object):
            """
            This list contains all loaded YANG data modules.
            
            This list is a superset of the 'schema' list defined in
            ietf\-netconf\-monitoring, which only lists modules exported
            through NETCONF.
            
            .. attribute:: name
            
            	The YANG module name
            	**type**\: str
            
            .. attribute:: exported_to
            
            	A list of the contexts (northbound interfaces) this module is exported to
            	**type**\: list of one of { list of :py:class:`ExportedTo_Enum <ydk.models.tailf.tailf_confd_monitoring.ConfdState.LoadedDataModels.DataModel.ExportedTo_Enum>` | list of str }
            
            .. attribute:: exported_to_all
            
            	This leaf is present if the module is exported to all northbound interfaces
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: namespace
            
            	The YANG module namespace
            	**type**\: str
            
            .. attribute:: prefix
            
            	The prefix defined in the YANG module
            	**type**\: str
            
            .. attribute:: revision
            
            	The YANG module revision
            	**type**\: str
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                self.parent = None
                self.name = None
                self.exported_to = []
                self.exported_to_all = None
                self.namespace = None
                self.prefix = None
                self.revision = None

            class ExportedTo_Enum(Enum):
                """
                ExportedTo_Enum

                A list of the contexts (northbound interfaces) this module
                is exported to.

                """

                NETCONF = 0

                CLI = 1

                WEBUI = 2

                REST = 3

                SNMP = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.LoadedDataModels.DataModel.ExportedTo_Enum']


            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYDataValidationError('Key property name is None')

                return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:loaded-data-models/tailf-confd-monitoring:data-model[tailf-confd-monitoring:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.name is not None:
                    return True

                if self.exported_to is not None:
                    for child in self.exported_to:
                        if child is not None:
                            return True

                if self.exported_to_all is not None:
                    return True

                if self.namespace is not None:
                    return True

                if self.prefix is not None:
                    return True

                if self.revision is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                return meta._meta_table['ConfdState.LoadedDataModels.DataModel']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:loaded-data-models'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.data_model is not None:
                for child_ref in self.data_model:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
            return meta._meta_table['ConfdState.LoadedDataModels']['meta_info']


    class Netconf(object):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the NETCONF server is listening on.  Note that other mechanisms can be put in front of the TCP addresses below, e.g., an OpenSSH server.  Such mechanisms are not known to the daemon and not listed here
        	**type**\: :py:class:`Listen <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Netconf.Listen>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            self.parent = None
            self.listen = ConfdState.Netconf.Listen()
            self.listen.parent = self


        class Listen(object):
            """
            The transport addresses the NETCONF server is listening on.
            
            Note that other mechanisms can be put in front of the TCP
            addresses below, e.g., an OpenSSH server.  Such mechanisms
            are not known to the daemon and not listed here.
            
            .. attribute:: ssh
            
            	
            	**type**\: list of :py:class:`Ssh <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Netconf.Listen.Ssh>`
            
            .. attribute:: tcp
            
            	
            	**type**\: list of :py:class:`Tcp <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Netconf.Listen.Tcp>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                self.parent = None
                self.ssh = YList()
                self.ssh.parent = self
                self.ssh.name = 'ssh'
                self.tcp = YList()
                self.tcp.parent = self
                self.tcp.name = 'tcp'


            class Ssh(object):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of { str | str }
                
                .. attribute:: port
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.port = None

                @property
                def _common_path(self):

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:netconf/tailf-confd-monitoring:listen/tailf-confd-monitoring:ssh'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ip is not None:
                        return True

                    if self.port is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Netconf.Listen.Ssh']['meta_info']


            class Tcp(object):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of { str | str }
                
                .. attribute:: port
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.port = None

                @property
                def _common_path(self):

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:netconf/tailf-confd-monitoring:listen/tailf-confd-monitoring:tcp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ip is not None:
                        return True

                    if self.port is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Netconf.Listen.Tcp']['meta_info']

            @property
            def _common_path(self):

                return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:netconf/tailf-confd-monitoring:listen'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ssh is not None:
                    for child_ref in self.ssh:
                        if child_ref._has_data():
                            return True

                if self.tcp is not None:
                    for child_ref in self.tcp:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                return meta._meta_table['ConfdState.Netconf.Listen']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:netconf'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.listen is not None and self.listen._has_data():
                return True

            if self.listen is not None and self.listen.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
            return meta._meta_table['ConfdState.Netconf']['meta_info']


    class Rest(object):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the REST server is listening on
        	**type**\: :py:class:`Listen <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Rest.Listen>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            self.parent = None
            self.listen = ConfdState.Rest.Listen()
            self.listen.parent = self


        class Listen(object):
            """
            The transport addresses the REST server is listening on.
            
            .. attribute:: ssl
            
            	
            	**type**\: list of :py:class:`Ssl <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Rest.Listen.Ssl>`
            
            .. attribute:: tcp
            
            	
            	**type**\: list of :py:class:`Tcp <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Rest.Listen.Tcp>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                self.parent = None
                self.ssl = YList()
                self.ssl.parent = self
                self.ssl.name = 'ssl'
                self.tcp = YList()
                self.tcp.parent = self
                self.tcp.name = 'tcp'


            class Ssl(object):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of { str | str }
                
                .. attribute:: port
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.port = None

                @property
                def _common_path(self):

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:rest/tailf-confd-monitoring:listen/tailf-confd-monitoring:ssl'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ip is not None:
                        return True

                    if self.port is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Rest.Listen.Ssl']['meta_info']


            class Tcp(object):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of { str | str }
                
                .. attribute:: port
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.port = None

                @property
                def _common_path(self):

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:rest/tailf-confd-monitoring:listen/tailf-confd-monitoring:tcp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ip is not None:
                        return True

                    if self.port is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Rest.Listen.Tcp']['meta_info']

            @property
            def _common_path(self):

                return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:rest/tailf-confd-monitoring:listen'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ssl is not None:
                    for child_ref in self.ssl:
                        if child_ref._has_data():
                            return True

                if self.tcp is not None:
                    for child_ref in self.tcp:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                return meta._meta_table['ConfdState.Rest.Listen']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:rest'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.listen is not None and self.listen._has_data():
                return True

            if self.listen is not None and self.listen.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
            return meta._meta_table['ConfdState.Rest']['meta_info']


    class Smp(object):
        """
        
        
        .. attribute:: number_of_threads
        
        	Number of threads used by the daemon
        	**type**\: int
        
        	**range:** 0..65535
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            self.parent = None
            self.number_of_threads = None

        @property
        def _common_path(self):

            return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:smp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.number_of_threads is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
            return meta._meta_table['ConfdState.Smp']['meta_info']


    class Snmp(object):
        """
        
        
        .. attribute:: engine_id
        
        	The local Engine ID specified as a list of colon\-specified hexadecimal octets e.g. '4F\:4C\:41\:71'
        	**type**\: str
        
        	**pattern:** ([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2}){4,31}
        
        .. attribute:: listen
        
        	The transport addresses the SNMP agent is listening on
        	**type**\: :py:class:`Listen <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Snmp.Listen>`
        
        .. attribute:: mib
        
        	MIBs loaded by the SNMP agent
        	**type**\: list of str
        
        .. attribute:: version
        
        	SNMP version used by the engine
        	**type**\: :py:class:`Version <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Snmp.Version>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            self.parent = None
            self.engine_id = None
            self.listen = ConfdState.Snmp.Listen()
            self.listen.parent = self
            self.mib = []
            self.version = ConfdState.Snmp.Version()
            self.version.parent = self


        class Listen(object):
            """
            The transport addresses the SNMP agent is listening on.
            
            .. attribute:: udp
            
            	
            	**type**\: list of :py:class:`Udp <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Snmp.Listen.Udp>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                self.parent = None
                self.udp = YList()
                self.udp.parent = self
                self.udp.name = 'udp'


            class Udp(object):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of { str | str }
                
                .. attribute:: port
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.port = None

                @property
                def _common_path(self):

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:snmp/tailf-confd-monitoring:listen/tailf-confd-monitoring:udp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ip is not None:
                        return True

                    if self.port is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Snmp.Listen.Udp']['meta_info']

            @property
            def _common_path(self):

                return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:snmp/tailf-confd-monitoring:listen'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.udp is not None:
                    for child_ref in self.udp:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                return meta._meta_table['ConfdState.Snmp.Listen']['meta_info']


        class Version(object):
            """
            SNMP version used by the engine.
            
            .. attribute:: v1
            
            	
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: v2c
            
            	
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: v3
            
            	
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                self.parent = None
                self.v1 = None
                self.v2c = None
                self.v3 = None

            @property
            def _common_path(self):

                return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:snmp/tailf-confd-monitoring:version'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.v1 is not None:
                    return True

                if self.v2c is not None:
                    return True

                if self.v3 is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                return meta._meta_table['ConfdState.Snmp.Version']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:snmp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.engine_id is not None:
                return True

            if self.listen is not None and self.listen._has_data():
                return True

            if self.listen is not None and self.listen.is_presence():
                return True

            if self.mib is not None:
                for child in self.mib:
                    if child is not None:
                        return True

            if self.version is not None and self.version._has_data():
                return True

            if self.version is not None and self.version.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
            return meta._meta_table['ConfdState.Snmp']['meta_info']


    class Webui(object):
        """
        
        
        .. attribute:: listen
        
        	The transport addresses the WebUI server is listening on
        	**type**\: :py:class:`Listen <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Webui.Listen>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'tfcm'
        _revision = '2013-06-14'

        def __init__(self):
            self.parent = None
            self.listen = ConfdState.Webui.Listen()
            self.listen.parent = self


        class Listen(object):
            """
            The transport addresses the WebUI server is listening on.
            
            .. attribute:: ssl
            
            	
            	**type**\: list of :py:class:`Ssl <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Webui.Listen.Ssl>`
            
            .. attribute:: tcp
            
            	
            	**type**\: list of :py:class:`Tcp <ydk.models.tailf.tailf_confd_monitoring.ConfdState.Webui.Listen.Tcp>`
            
            

            """

            _prefix = 'tfcm'
            _revision = '2013-06-14'

            def __init__(self):
                self.parent = None
                self.ssl = YList()
                self.ssl.parent = self
                self.ssl.name = 'ssl'
                self.tcp = YList()
                self.tcp.parent = self
                self.tcp.name = 'tcp'


            class Ssl(object):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of { str | str }
                
                .. attribute:: port
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.port = None

                @property
                def _common_path(self):

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:webui/tailf-confd-monitoring:listen/tailf-confd-monitoring:ssl'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ip is not None:
                        return True

                    if self.port is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Webui.Listen.Ssl']['meta_info']


            class Tcp(object):
                """
                
                
                .. attribute:: ip
                
                	
                	**type**\: one of { str | str }
                
                .. attribute:: port
                
                	
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'tfcm'
                _revision = '2013-06-14'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.port = None

                @property
                def _common_path(self):

                    return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:webui/tailf-confd-monitoring:listen/tailf-confd-monitoring:tcp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ip is not None:
                        return True

                    if self.port is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                    return meta._meta_table['ConfdState.Webui.Listen.Tcp']['meta_info']

            @property
            def _common_path(self):

                return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:webui/tailf-confd-monitoring:listen'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ssl is not None:
                    for child_ref in self.ssl:
                        if child_ref._has_data():
                            return True

                if self.tcp is not None:
                    for child_ref in self.tcp:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
                return meta._meta_table['ConfdState.Webui.Listen']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-confd-monitoring:confd-state/tailf-confd-monitoring:webui'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.listen is not None and self.listen._has_data():
                return True

            if self.listen is not None and self.listen.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
            return meta._meta_table['ConfdState.Webui']['meta_info']

    @property
    def _common_path(self):

        return '/tailf-confd-monitoring:confd-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cli is not None and self.cli._has_data():
            return True

        if self.cli is not None and self.cli.is_presence():
            return True

        if self.daemon_status is not None:
            return True

        if self.epoll is not None:
            return True

        if self.ha is not None and self.ha._has_data():
            return True

        if self.ha is not None and self.ha.is_presence():
            return True

        if self.internal is not None and self.internal._has_data():
            return True

        if self.internal is not None and self.internal.is_presence():
            return True

        if self.loaded_data_models is not None and self.loaded_data_models._has_data():
            return True

        if self.loaded_data_models is not None and self.loaded_data_models.is_presence():
            return True

        if self.netconf is not None and self.netconf._has_data():
            return True

        if self.netconf is not None and self.netconf.is_presence():
            return True

        if self.read_only_mode is not None:
            return True

        if self.rest is not None and self.rest._has_data():
            return True

        if self.rest is not None and self.rest.is_presence():
            return True

        if self.smp is not None and self.smp._has_data():
            return True

        if self.smp is not None and self.smp.is_presence():
            return True

        if self.snmp is not None and self.snmp._has_data():
            return True

        if self.snmp is not None and self.snmp.is_presence():
            return True

        if self.upgrade_mode is not None:
            return True

        if self.version is not None:
            return True

        if self.webui is not None and self.webui._has_data():
            return True

        if self.webui is not None and self.webui.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.tailf._meta import _tailf_confd_monitoring as meta
        return meta._meta_table['ConfdState']['meta_info']


