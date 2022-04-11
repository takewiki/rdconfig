import rdconfig.private as pv
# can access the private variable
# print(pv.__varName__)
# # the 2nd private var.
# print(pv.__varCaption)

# test the function
# pv.getName()
# pv.getCaption()
# pv.__getCaption()

# test object
# pvc = pv.Private()
# pvc.getName()
# class can protect the private function
pvc.__getCaption()


#conclution:class can protect the private function


