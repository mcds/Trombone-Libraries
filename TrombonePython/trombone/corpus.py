import urllib
import urllib2
import json

class TromboneCorpus:
    trombone_url = 'http://localhost:8080/voyeur/trombone'
    
    def __init__(self, id=None):
        self.id = id

    def load(self, input):
        json = self.get_json({'input': input})
        self.id = json['corpus']['@id']

    def get(self, query, tool=None, outputFormat=None, template=None):
        if self.id:
            query['corpus'] = self.id
        if tool:
            query['tool'] = tool
        if outputFormat:
            query['outputFormat'] = outputFormat
        if template:
            query['template'] = template
        url = self.trombone_url+'?'+urllib.urlencode(query)
        print url
        connection =  urllib2.urlopen(url)
        result = connection.read();
        return result

    def get_json(self, query, tool=None):
        result = self.get(query, tool)
        return json.loads(result)
