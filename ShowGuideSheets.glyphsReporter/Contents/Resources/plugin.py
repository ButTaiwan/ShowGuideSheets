# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

RADIUS = 9

class ShowGuideSheets(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Guide Sheets',
			'zh-Hant': '稿紙',
			'zh-Hant-TW': '稿紙',
			'zh-Hans': '稿纸',
			'zh': '稿紙',
			'ja': '原稿用紙',
		})


	@objc.python_method
	def background(self, layer):
		script = layer.parent.script
		masterId = layer.associatedMasterId
		scale = self.getScale()
		if scale < 0.25: return

		guideGlyph = None
		if script is not None:
			guideGlyph = Glyphs.font.glyphs['_guide.' + script]
		if guideGlyph is None:
			guideGlyph = Glyphs.font.glyphs['_guide.any']
		if guideGlyph is None:
			return

		guideLayer = guideGlyph.layers[masterId]
		if guideLayer is None: return

		closedPaths = guideLayer.completeBezierPath.copy()
		opendPath = guideLayer.completeOpenBezierPath.copy()

		# show guides
		try:
			#color = NSColor.colorWithRed_green_blue_alpha_(0.1, 0.6, 0.8, 0.35)
			color = self.getColor(0.35)
			color.set()

			closedPaths.setLineWidth_(1.0 / scale)
			closedPaths.stroke()

			opendPath.setLineWidth_(1.0 / scale)
			opendPath.stroke()

			if guideLayer.annotations:
				for ann in guideLayer.annotations:
					if ann.type != TEXT: continue
					if ann.text is None: continue
					self.drawTextAtPoint(
							ann.text, ann.position, 
							fontSize = 10, 
							fontColor = color,
							align = "topleft",
						)
		
		except Exception as e:
			self.logToConsole( "showGuideSheets: %s\n" % str(e) )
			import traceback
			print(traceback.format_exc())

		# show on-path nodes
		if scale > 0.4:
			try:
				for path in layer.paths:
					for nodes in path.nodes:
						if closedPaths.isStrokeHitByPoint_padding_(nodes.position, .6): self.drawOnPathPoint(nodes.position, scale)
						if opendPath.isStrokeHitByPoint_padding_(nodes.position, .6): self.drawOnPathPoint(nodes.position, scale)
			
			except Exception as e:
				self.logToConsole( "showGuideSheetNodes: %s\n" % str(e) )
				import traceback
				print(traceback.format_exc())

	@objc.python_method
	def drawOnPathPoint(self, pos, scale):
		r = RADIUS * 1.0 / scale
		#NSColor.colorWithRed_green_blue_alpha_(0.1, 0.6, 0.8, 0.25).set()
		self.getColor(0.25).set()
		rect = NSRect(NSPoint(pos.x-r, pos.y-r), NSSize(r*2, r*2))
		circle = NSBezierPath.bezierPathWithRoundedRect_cornerRadius_(rect, r)
		circle.fill()

		NSColor.colorWithRed_green_blue_alpha_(1.0, 1.0, 1.0, 1.0).set()
		circle.setLineWidth_(1.0 / scale)
		circle.stroke()

	@objc.python_method
	def getColor(self, alpha):
		colorHex = Glyphs.font.customParameters["Guide Color"]

		try:
			r = int(colorHex[0:2], 16) / 256.0
			g = int(colorHex[2:4], 16) / 256.0
			b = int(colorHex[4:6], 16) / 256.0
			return NSColor.colorWithRed_green_blue_alpha_(r, g, b, alpha)
		except:
			return NSColor.colorWithRed_green_blue_alpha_(0.1, 0.6, 0.8, alpha)
		

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
