import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from snippets import MyProc
from snippets import ProcList

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape = True
)

class Compare(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        name = self.request.GET.get('value1')
        proc_name = name.split(',')
        # proc_list contains the list of all the objects that need to be compared


        myproc_list_key=ndb.Key('ProcList','default')
        myproc_list = myproc_list_key.get()

        myproc_list = ProcList(id='default')

        for i in proc_name:
            myproc_key = ndb.Key('MyProc',i)
            myproc= myproc_key.get()
            myproc_append = MyProc(name = myproc.name, manufacturer = myproc.manufacturer, date =myproc.date , geometryShader = myproc.geometryShader, tesselationShader=myproc.tesselationShader, shaderInt16 = myproc.shaderInt16, sparseBinding=myproc.sparseBinding , textureCompressionETC2=myproc.textureCompressionETC2, vertexPipelineStoresAndAtomics=myproc.vertexPipelineStoresAndAtomics)
            myproc_list.processor.append(myproc_append)
            myproc_list.put()
        template_values={
        'myproc_list': myproc_list.processor
        }
        template = JINJA_ENVIRONMENT.get_template('compare.html')
        self.response.write(template.render(template_values))
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'

        action=self.request.get('previous')
        if action=='PreviousPage':
            self.redirect('/edit')
