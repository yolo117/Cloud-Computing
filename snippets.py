from google.appengine.ext import ndb

class MyProc(ndb.Model):
    name = ndb.StringProperty()
    manufacturer = ndb.StringProperty()
    date = ndb.DateProperty()
    geometryShader = ndb.BooleanProperty()
    tesselationShader = ndb.BooleanProperty()
    shaderInt16  =  ndb.BooleanProperty()
    sparseBinding = ndb.BooleanProperty()
    textureCompressionETC2 = ndb.BooleanProperty()
    vertexPipelineStoresAndAtomics = ndb.BooleanProperty()


class MyUser(ndb.Model):
    name = ndb.StringProperty()

class ProcList(ndb.Model):
    processor = ndb.StructuredProperty(MyProc, repeated=True)
