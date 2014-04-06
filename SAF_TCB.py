# TCB - Maya Transparency and Fast Camera Bookmarks
# Thanks to Jos Balcaen!

import maya.cmds as cmds
import maya.OpenMayaUI as mui
from PySide import QtGui
import shiboken
maya_window = (shiboken.wrapInstance(long(mui.MQtUtil.mainWindow()),QtGui.QWidget))
maya_window.setWindowOpacity(1.0)
viewport = (shiboken.wrapInstance(long(mui.MQtUtil.findLayout("MayaWindow|formLayout1|viewPanes")),QtGui.QWidget))
def opacity(value): maya_window.setWindowOpacity(value)
# Mac bag fix
def fix(self):
    import os
    if os.name == 'posix':
        viewport.hide()
        cmds.refresh()
        viewport.show()
    pass
fix
def CamSet1():
    if cmds.objExists('saveCam_1'): cmds.cameraView('saveCam_1',e=1,sc=1)
    if not cmds.objExists('saveCam_1'): cmds.cameraView(n='saveCam_1',ab=1)
def CamDel1(): 
    if cmds.objExists('saveCam_1'): cmds.delete("saveCam_1")
def CamSet2():
    if cmds.objExists('saveCam_2'): cmds.cameraView('saveCam_2',e=1,sc=1)
    if not cmds.objExists('saveCam_2'): cmds.cameraView(n='saveCam_2',ab=1)
def CamDel2(): 
    if cmds.objExists('saveCam_2'): cmds.delete("saveCam_2")
def CamSet3():
    if cmds.objExists('saveCam_3'): cmds.cameraView('saveCam_3',e=1,sc=1)
    if not cmds.objExists('saveCam_3'): cmds.cameraView(n='saveCam_3',ab=1)
def CamDel3(): 
    if cmds.objExists('saveCam_3'): cmds.delete("saveCam_3")
if (cmds.window('TCB', exists=True)):
        cmds.deleteUI('TCB')
cmds.window('TCB', t="TCB 1.1", s=0, tlb=1)
cmds.columnLayout()
cmds.floatSlider(min=0, max=1.0, v=1, dc=lambda x:opacity(x), cc=fix, w=200, h=20)
cmds.gridLayout(numberOfColumns=4,cellWidthHeight=(50, 20))
cmds.iconTextButton(st='iconAndTextHorizontal', i1='Bookmark.png', c='CamSet1()',dcc='CamDel1();CamSet1()', l='1', ann='Double Click For New Camera Bookmark')
cmds.iconTextButton(st='iconAndTextHorizontal', i1='Bookmark.png', c='CamSet2()',dcc='CamDel2();CamSet2()', l='2', ann='Double Click For New Camera Bookmark')
cmds.iconTextButton(st='iconAndTextHorizontal', i1='Bookmark.png', c='CamSet3()',dcc='CamDel3();CamSet3()', l='3', ann='Double Click For New Camera Bookmark')
cmds.iconTextButton(st='iconAndTextHorizontal', i1='Camera.png', c="cmds.viewSet(home=1,animate=cmds.optionVar(query='animateRollViewCompass'))",l='RES')
cmds.setParent()
cmds.showWindow('TCB')
#import SAF_TCB