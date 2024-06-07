# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *

# connect to host
Connect("localhost")

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# set active view
SetActiveView(None)

CreateLayout('Layout #1')

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [844, 545]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 0
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(0, renderView1)

# create a new 'OpenFOAMReader'
smarthomecasefoam = OpenFOAMReader(FileName='/wop/cases/smarthome.case/smarthome.case.foam')
smarthomecasefoam.MeshRegions = ['internalMesh', 'heater/internalMesh', 'fluid/internalMesh']
smarthomecasefoam.CellArrays = ['G', 'T', 'U', 'a', 'alphat', 'k', 'nut', 'omega', 'p', 'p_rgh', 'qr', 'rho']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# show data in view
smarthomecasefoamDisplay = Show(smarthomecasefoam, renderView1)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# trace defaults for the display properties.
smarthomecasefoamDisplay.Representation = 'Surface'
smarthomecasefoamDisplay.ColorArrayName = ['POINTS', 'p']
smarthomecasefoamDisplay.LookupTable = pLUT
smarthomecasefoamDisplay.OSPRayScaleArray = 'p'
smarthomecasefoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
smarthomecasefoamDisplay.SelectOrientationVectors = 'U'
smarthomecasefoamDisplay.ScaleFactor = 0.4153845973312855
smarthomecasefoamDisplay.SelectScaleArray = 'p'
smarthomecasefoamDisplay.GlyphType = 'Arrow'
smarthomecasefoamDisplay.GlyphTableIndexArray = 'p'
smarthomecasefoamDisplay.GaussianRadius = 0.020769229866564275
smarthomecasefoamDisplay.SetScaleArray = ['POINTS', 'p']
smarthomecasefoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
smarthomecasefoamDisplay.OpacityArray = ['POINTS', 'p']
smarthomecasefoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
smarthomecasefoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
smarthomecasefoamDisplay.SelectionCellLabelFontFile = ''
smarthomecasefoamDisplay.SelectionPointLabelFontFile = ''
smarthomecasefoamDisplay.PolarAxes = 'PolarAxesRepresentation'
smarthomecasefoamDisplay.ScalarOpacityFunction = pPWF
smarthomecasefoamDisplay.ScalarOpacityUnitDistance = 0.314955081977079

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
smarthomecasefoamDisplay.DataAxesGrid.XTitleFontFile = ''
smarthomecasefoamDisplay.DataAxesGrid.YTitleFontFile = ''
smarthomecasefoamDisplay.DataAxesGrid.ZTitleFontFile = ''
smarthomecasefoamDisplay.DataAxesGrid.XLabelFontFile = ''
smarthomecasefoamDisplay.DataAxesGrid.YLabelFontFile = ''
smarthomecasefoamDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
smarthomecasefoamDisplay.PolarAxes.PolarAxisTitleFontFile = ''
smarthomecasefoamDisplay.PolarAxes.PolarAxisLabelFontFile = ''
smarthomecasefoamDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
smarthomecasefoamDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
smarthomecasefoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on smarthomecasefoamDisplay
smarthomecasefoamDisplay.Opacity = 0.9

# Properties modified on smarthomecasefoamDisplay
smarthomecasefoamDisplay.Opacity = 0.8

# Properties modified on smarthomecasefoamDisplay
smarthomecasefoamDisplay.Opacity = 0.7

# Properties modified on smarthomecasefoamDisplay
smarthomecasefoamDisplay.Opacity = 0.6

# Properties modified on smarthomecasefoamDisplay
smarthomecasefoamDisplay.Opacity = 0.5

# Properties modified on smarthomecasefoamDisplay
smarthomecasefoamDisplay.Opacity = 0.4

# create a new 'Contour'
contour1 = Contour(Input=smarthomecasefoam)
contour1.ContourBy = ['POINTS', 'p']
contour1.Isosurfaces = [100020.23828125]
contour1.PointMergeMethod = 'Uniform Binning'

# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'T']
contour1.Isosurfaces = [290.0, 295.0]

# show data in view
contour1Display = Show(contour1, renderView1)

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = [None, '']
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = -2.0000000000000002e+298
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.GaussianRadius = -1e+297
contour1Display.SetScaleArray = [None, '']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = [None, '']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.SelectionCellLabelFontFile = ''
contour1Display.SelectionPointLabelFontFile = ''
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display.DataAxesGrid.XTitleFontFile = ''
contour1Display.DataAxesGrid.YTitleFontFile = ''
contour1Display.DataAxesGrid.ZTitleFontFile = ''
contour1Display.DataAxesGrid.XLabelFontFile = ''
contour1Display.DataAxesGrid.YLabelFontFile = ''
contour1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display.PolarAxes.PolarAxisTitleFontFile = ''
contour1Display.PolarAxes.PolarAxisLabelFontFile = ''
contour1Display.PolarAxes.LastRadialAxisTextFontFile = ''
contour1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour1Display
contour1Display.SetScaleArray = [None, 'G']

# Properties modified on contour1Display
contour1Display.OpacityArray = [None, 'G']

# Properties modified on contour1Display
contour1Display.OSPRayScaleArray = 'G'

# set scalar coloring
ColorBy(contour1Display, ('CELLS', 'T'))

# rescale color and/or opacity maps used to include current data range
contour1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')

# set scalar coloring using an separate color/opacity maps
ColorBy(contour1Display, ('CELLS', 'T'), True)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(tLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
contour1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# get separate color transfer function/color map for 'T'
separate_contour1Display_TLUT = GetColorTransferFunction('T', contour1Display, separate=True)

# get separate opacity transfer function/opacity map for 'T'
separate_contour1Display_TPWF = GetOpacityTransferFunction('T', contour1Display, separate=True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
separate_contour1Display_TLUT.ApplyPreset('jet', True)

animationScene1.GoToFirst()

# current camera placement for renderView1
renderView1.CameraPosition = [7.27117159849462, 11.250597809201299, 5.062494148085477]
renderView1.CameraFocalPoint = [1.5000000000000004, 1.9999999068677419, 1.5000000000000009]
renderView1.CameraViewUp = [-0.12772825750066827, -0.2860398947205462, 0.9496666103765583]
renderView1.CameraParallelScale = 2.9687723207585077

# save animation
SaveAnimation('./video.avi', renderView1, ImageResolution=[844, 544],
    FrameWindow=[0, 123])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [7.27117159849462, 11.250597809201299, 5.062494148085477]
renderView1.CameraFocalPoint = [1.5000000000000004, 1.9999999068677419, 1.5000000000000009]
renderView1.CameraViewUp = [-0.12772825750066827, -0.2860398947205462, 0.9496666103765583]
renderView1.CameraParallelScale = 2.9687723207585077

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
