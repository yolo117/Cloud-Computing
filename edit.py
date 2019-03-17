import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from datetime import datetime
import os
from snippets import MyProc
from snippets import ProcList


JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)

class Edit(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        error=''
        action1=self.request.get('compare')
        if action1=='Compare':
            selected_procs =self.request.get_all('select_processor')
            # print(str(len(selected_procs))+ " Number of entries")

            if len(selected_procs)>1:
                selected_procs_string = ','.join(selected_procs)

                self.redirect('/compare?value1=' + selected_procs_string)

            elif len(selected_procs)<=1:
                error='Select more than one processor to compare'
                # self.redirect('/edit')


        action=self.request.get("button")
        # print('-----------'+ action+" " + "--------" + self.request.get('button'))
        # print(self.request.get('select_processor'))
        if action =='Search':
            geometry_checker = bool(self.request.get("geometry_shader"))
            tesselation_checker = bool(self.request.get("tesselation_shader"))
            shader_checker = bool(self.request.get('shader_int16'))
            sparse_checker = bool(self.request.get('sparse_binding'))
            texture_checker = bool(self.request.get('texture_compressionETC2'))
            vertex_checker = bool(self.request.get('vertex_pipe_line'))
            # print(tesselation_checker)
            query = MyProc.query()

            if geometry_checker==True:
                query = query.filter(MyProc.geometryShader == True)

            if tesselation_checker==True:
                query = query.filter(MyProc.tesselationShader == True)

            if shader_checker==True:
                query = query.filter(MyProc.shaderInt16 == True)

            if sparse_checker==True:
                query = query.filter(MyProc.sparseBinding == True)

            if texture_checker==True:
                query = query.filter(MyProc.textureCompressionETC2 == True)

            if vertex_checker==True:
                query = query.filter(MyProc.vertexPipelineStoresAndAtomics == True)

            all_query = query.fetch()
            print(len(all_query))
            template_values = {
            'all_query':all_query,
            'error':error
            }
            template = JINJA_ENVIRONMENT.get_template('edit.html')
            self.response.write(template.render(template_values))
        else :
            query = MyProc.query().fetch()
            template_values = {
            'all_query':query,
            'error':error
            }
            template = JINJA_ENVIRONMENT.get_template('edit.html')
            self.response.write(template.render(template_values))


    # else :
    #     query = MyProc.query().fetch()
    #     template_values = {
    #     'all_query': query
    #     }
    #     template = JINJA_ENVIRONMENT.get_template('edit.html')
    #     self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'

        action = self.request.get('button')
        if action == 'Add':
            myproc_string = self.request.get('proc_name') # store the value of the string obtained from the form
            myproc_key = ndb.Key('MyProc',myproc_string)
            myproc = myproc_key.get()
            error = True
            # Template_values = {
            # 'error': error
            # 'processor': ProcList.processor
            # }


            if myproc != None:
                error = True


            else :
                proc_name = self.request.get('proc_name')
                manufact_name = self.request.get('proc_manufacturer')
                information = self.request.get('proc_date')
                date1 = datetime.strptime(information,"%Y-%m-%d")
                geometry_shader = bool(self.request.get('proc_geometry_shader'))
                print(self.request.get('proc_geometry_shader'))
                shader_int = bool(self.request.get('proc_int16'))
                sparse_binding = bool(self.request.get('proc_sparse'))
                tesselation_shader = bool(self.request.get('proc_Tess'))
                texture_compression = bool(self.request.get('proc_texture'))
                vertex_pipe_line = bool(self.request.get('proc_vert'))

                myproc = MyProc(id=myproc_string)
                print("the name of the string id is " + myproc_string)
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
                # proclist_key = ndb.Key('ProcList','default')
                # proc_list = proclist_key.get()
                # # new_proc = MyProc(name = proc_name, manufacturer = manufact_name, date =date1, geometryShader = geometry_shader, tesselationShader=tesselation_shader, shaderInt16 = shader_int, sparseBinding=sparse_binding, textureCompressionETC2=texture_compression, vertexPipelineStoresAndAtomics=vertex_pipe_line)
                # # proc_list.processor.append(new_proc)
                # # proc_list.put()






            self.redirect('/edit')
        elif action =='Cancel':
            self.redirect('/edit')



            # geometry_checker = bool(self.request.get('geometry_checker'))
            # tesselation_checker = bool(self.request.get('tessel_checker'))
            # shader_checker = bool(self.request.get('shader_checker'))
            # sparse_checker = bool(self.request.get('sparse_checker'))
            # texture_checker = bool(self.request.get('texture_checker'))
            # vertex_checker = bool(self.request.get('vertex_checker'))
            #
            # query = myproc.query()
            # if GeometryShader:
            #     query = query.filter(myproc.geometryShader == True)
            # if tesselationShader:
            #     query = query.filter(myproc.tesselationShader == True)
            # if shaderInt16:
            #     query = query.filter(myproc.shaderInt16 == True)
            # if sparseBinding:
            #     query = query.filter(myproc.sparseBinding == True)
            # if textureCompressionETC2:
            #     query = query.filter(myproc.textureCompressionETC2 == True)
            # if vertexPipelineStoresAndAtomics:
            #     query = query.filter(myproc.vertexPipelineStoresAndAtomics == True)
            #
            # template_values = {
            # 'query':query
            # }
            #
            # template = JINJA_ENVIRONMENT.get_template('edit.html')
            # self.response.write(template.render(template_values))
            # self.redirect('/edit')
