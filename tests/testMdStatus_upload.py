#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mdlCpEcsMdpy

import mdlCpEcsMdpy

# 按单号同步

res=mdlCpEcsMdpy.materialStatus_upload(token="9B6F803F-9D37-41A2-BDA0-70A7179AF0F3",FNumber="K86-10015S-H")

print(res)

res=mdlCpEcsMdpy.customerStatus_upload(token="9B6F803F-9D37-41A2-BDA0-70A7179AF0F3",FNumber="C15276")

print(res)

res=mdlCpEcsMdpy.supplierStatus_upload(token="9B6F803F-9D37-41A2-BDA0-70A7179AF0F3",FNumber="S00085")

print(res)