import rdconfig.glb as pg
#test for var
# print(pg.__varName__)
# print(pg.__varCaption)
# print(pg._varTitle)
# print(pg._varTag_)
#test for function
# pg.getCaption()
# pg._getTitle()
# pg.__getCaption()
#test for class
pic = pg.glb_testPrivate()
poc = pg.glb_testProtect()
poc.getTitle()
poc._getTitle()
pic.getName()
pic.__getCaption()





