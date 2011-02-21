from zope.interface import implements
from collective.cdn.core.interfaces import ICDNProvider


class cdn(object):
    
    implements(ICDNProvider)
    
    
    def __init__(self,hostname=[],port=80,path=''):
        ''' Initialize
        '''
        self.hostname = hostname
        self.port = port
        self.path = path
        
    def process_url(self,url,relative_path=''):
        '''Given a base url we return an url pointing to 
           the hostname and path informed
           >>> obj = cdn()
           >>> obj.hostname = ['foo',]
           >>> obj.port = 80
           >>> obj.path = ''
           >>> assert obj.process_url('http://nohost/plone/') == 'http://foo/plone/'
           >>> assert obj.process_url('http://nohost:80/plone/') == 'http://foo/plone/'
           >>> assert obj.process_url('http://nohost:8080/plone/') == 'http://foo/plone/'
           >>> obj = cdn()
           >>> obj.hostname = ['bar',]
           >>> obj.port = 80
           >>> obj.path = 'somelongpath'
           >>> assert obj.process_url('http://nohost/plone/') == 'http://bar/somelongpath/plone/'
           >>> assert obj.process_url('http://nohost:80/plone/') == 'http://bar/somelongpath/plone/'
           >>> assert obj.process_url('http://nohost/plone/') == 'http://bar/somelongpath/plone/'
           >>> obj = cdn()
           >>> obj.hostname = ['foobar',]
           >>> obj.port = 8080
           >>> obj.path = 'shrtpth'
           >>> assert obj.process_url('http://nohost/plone/') == 'http://foobar:8080/shrtpth/plone/'
           >>> assert obj.process_url('http://nohost:80/plone/') == 'http://foobar:8080/shrtpth/plone/'
           >>> assert obj.process_url('http://nohost/plone/') == 'http://foobar:8080/shrtpth/plone/'           
        '''
        # splits url parts
        protocol,path = url.split('://')
        path = path.split('/')
        hostname = self.hostname[0]
        if not self.port in [80,]:
            hostname = '%s:%s' % (hostname, self.port)
        
        path[0] = hostname
        # add path, if supplied
        if self.path:
            path.insert(1,self.path)
        
        # join everything
        path = '/'.join(path)
        url = '%s://%s' % (protocol, path)
        return url