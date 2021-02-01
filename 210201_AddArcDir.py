import rhinoscriptsyntax as rs  

def AddArcDir(ptStart, ptEnd, vecDir):
    vecBase = rs.PointSubstract(ptEnd, ptStart)
    if rs.VectorLength(vecBase) == 0: return

