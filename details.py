import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
import os
from datetime import datetime
from snippets import MyProc
from snippets import MyUser
from snippets import ProcList

JINJA_ENVIRONMENT= jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)

class Details(webapp2.RequestHandler):
    name = ""
    index= 0
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        global name
        name = self.request.get('name')

        # print(" the get name is " + name)
        global index
        index = int(self.request.get('index'))

        myproc_key=ndb.Key('MyProc', name)
        if(myproc_key!=None):
            myproc = myproc_key.get()

        else:
            myproc = MyProc(id=name)


        #
        # if action=='Search':
        #     geometry_checker = bool(self.request.get('geometry_checker'))
        #     tesselation_checker = bool(self.request.get('tessel_checker'))
        #     shader_checker = bool(self.request.get('shader_checker'))
        #     sparse_checker = bool(self.request.get('sparse_checker'))
        #     texture_checker = bool(self.request.get('texture_checker'))
        #     vertex_checker = bool(self.request.get('vertex_checker'))
        #
        #     query = myproc.query()
        #     if GeometryShader:
        #         query = query.filter(myproc.geometryShader == True).fetch()
        #     if tesselationShader:
        #         query = query.filter(myproc.tesselationShader == True).fetch()
        #     if shaderInt16:
        #         query = query.filter(myproc.shaderInt16 == True).fetch()
        #     if sparseBinding:
        #         query = query.filter(myproc.sparseBinding == True)
        #     if textureCompressionETC2:
        #         query = query.filter(myproc.textureCompressionETC2 == True)
        #     if vertexPipelineStoresAndAtomics:
        #         query = query.filter(myproc.vertexPipelineStoresAndAtomics == True)
        #
        template_values = {
            # 'query': query,
            'myproc':myproc
        }
        template = JINJA_ENVIRONMENT.get_template('details.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'

        action = self.request.get('update')
        if action == 'Update':

            print ("The name in post is  " + name)
            myproc_key = ndb.Key('MyProc', name)
            myproc = myproc_key.get()

            proc_name = self.request.get('proc_name')
            manufact_name = self.request.get('proc_manufacturer')
            information = self.request.get('proc_date')
            date1 = datetime.strptime(information,"%Y-%m-%d")
            geometry_string = self.request.get('proc_geometry_shader')
            if geometry_string=='True' or geometry_string =='TRUE' or geometry_string =='T':
                geometry_shader = True
            else :
                geometry_shader = False
            shader_string = self.request.get('proc_int16')
            if shader_string=='True' or shader_string =='TRUE' or shader_string =='T':
                shader_int = True
            else :
                shader_int = False
            sparse_string = self.request.get('proc_sparse')
            if sparse_string=='True' or sparse_string =='TRUE' or sparse_string =='T':
                sparse_binding = True
            else :
                sparse_binding = False

            tesselation_string = self.request.get('proc_Tess')
            if tesselation_string=='True' or tesselation_string =='TRUE' or tesselation_string =='T':
                tesselation_shader = True
            else :
                tesselation_shader = False

            texture_string = self.request.get('proc_texture')
            if texture_string=='True' or texture_string =='TRUE' or texture_string =='T':
                texture_compression = True
            else :
                texture_compression = False
            vertex_string = bool(self.request.get('proc_vert'))
            if vertex_string=='True' or vertex_string =='TRUE' or vertex_string =='T':
                vertex_pipe_line = True
            else :
                vertex_pipe_line = False

            ## If there are changes in the name of the processor this means that
            #there will be issue when we are trying to operate on the same object

            myproc.name = proc_name
            myproc.manufacturer = manufact_name
            myproc.date = date1
            myproc.geometryShader = geometry_shader
            myproc.shaderInt16 = shader_int
            myproc.sparseBinding = sparse_binding
            myproc.tesselationShader = tesselation_shader
            myproc.textureCompressionETC2 = texture_compression
            myproc.vertexPipelineStoresAndAtomics = vertex_pipe_line
            myproc.put()

            # proc_list_key = ndb.Key('ProcList','default')
            # proc_list = proc_list_key.get()
            # new_proc = MyProc(name = proc_name, manufacturer = manufact_name, date =date1, geometryShader = geometry_shader, tesselationShader=tesselation_shader, shaderInt16 = shader_int, sparseBinding=sparse_binding, textureCompressionETC2=texture_compression, vertexPipelineStoresAndAtomics=vertex_pipe_line)
            # proc_list.processor.append(new_proc)
            # del proc_list.processor[index]
            # proc_list.put()

        self.redirect('/edit')
