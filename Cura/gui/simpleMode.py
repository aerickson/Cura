__copyright__ = "Copyright (C) 2013 David Braam - Released under terms of the AGPLv3 License"

import wx

from Cura.util import profile
from Cura.util.simpleModeSettings import SimpleModeSettings
import cPickle as pickle

class simpleModePanel(wx.Panel):
	"Main user interface window for Quickprint mode"
	def __init__(self, parent, callback):
		super(simpleModePanel, self).__init__(parent)
		self._callback = callback

		#toolsMenu = wx.Menu()
		#i = toolsMenu.Append(-1, 'Switch to Normal mode...')
		#self.Bind(wx.EVT_MENU, self.OnNormalSwitch, i)
		#self.menubar.Insert(1, toolsMenu, 'Normal mode')

		printTypePanel = wx.Panel(self)
		self.printTypeHigh = wx.RadioButton(printTypePanel, -1, _("High quality print"), style=wx.RB_GROUP)
		self.printTypeNormal = wx.RadioButton(printTypePanel, -1, _("Normal quality print"))
		self.printTypeLow = wx.RadioButton(printTypePanel, -1, _("Fast low quality print"))
		self.printTypeJoris = wx.RadioButton(printTypePanel, -1, _("Thin walled cup or vase"))
		self.printTypeJoris.Hide()

		printMaterialPanel = wx.Panel(self)
		if profile.getMachineSetting('machine_type') == 'lulzbot_mini' or profile.getMachineSetting('machine_type') == 'lulzbot_TAZ_5' or profile.getMachineSetting('machine_type') == 'lulzbot_TAZ_4':
			self.printMaterialHIPS = wx.RadioButton(printMaterialPanel, -1, _('HIPS'), style=wx.RB_GROUP)
			self.printMaterialABS = wx.RadioButton(printMaterialPanel, -1, _('ABS'))
		else:
			self.printMaterialABS = wx.RadioButton(printMaterialPanel, -1, _('ABS'), style=wx.RB_GROUP)
		self.printMaterialPLA = wx.RadioButton(printMaterialPanel, -1, _('PLA'))
		if profile.getMachineSetting('gcode_flavor') == 'UltiGCode':
			printMaterialPanel.Show(False)
		
		self.printSupport = wx.CheckBox(self, -1, _("Print support structure"))
		self.printBrim = wx.CheckBox(self, -1, _("Print Brim"))

		sizer = wx.GridBagSizer()
		self.SetSizer(sizer)

		sb = wx.StaticBox(printTypePanel, label=_("Select a quickprint profile:"))
		boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		boxsizer.Add(self.printTypeHigh)
		boxsizer.Add(self.printTypeNormal)
		boxsizer.Add(self.printTypeLow)
		boxsizer.Add(self.printTypeJoris, border=5, flag=wx.TOP)
		printTypePanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		printTypePanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		sizer.Add(printTypePanel, (0,0), flag=wx.EXPAND)

		sb = wx.StaticBox(printMaterialPanel, label=_("Material:"))
		boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		if profile.getMachineSetting('machine_type') == 'lulzbot_mini' or profile.getMachineSetting('machine_type') == 'lulzbot_TAZ_5' or profile.getMachineSetting('machine_type') == 'lulzbot_TAZ_4':
			boxsizer.Add(self.printMaterialHIPS)
		boxsizer.Add(self.printMaterialABS)
		boxsizer.Add(self.printMaterialPLA)
		printMaterialPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		printMaterialPanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		sizer.Add(printMaterialPanel, (1,0), flag=wx.EXPAND)

		sb = wx.StaticBox(self, label=_("Other:"))
		boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		boxsizer.Add(self.printSupport)
		boxsizer.Add(self.printBrim)
		sizer.Add(boxsizer, (2,0), flag=wx.EXPAND)

		self.printTypeNormal.SetValue(True)
		if profile.getMachineSetting('machine_type') == 'lulzbot_mini' or profile.getMachineSetting('machine_type') == 'lulzbot_TAZ_5' or profile.getMachineSetting('machine_type') == 'lulzbot_TAZ_4':
			self.printMaterialHIPS.SetValue(True)
		else:
			self.printMaterialPLA.SetValue(True)

		self.printTypeHigh.Bind(wx.EVT_RADIOBUTTON, lambda e: self._callback())
		self.printTypeNormal.Bind(wx.EVT_RADIOBUTTON, lambda e: self._callback())
		self.printTypeLow.Bind(wx.EVT_RADIOBUTTON, lambda e: self._callback())
		#self.printTypeJoris.Bind(wx.EVT_RADIOBUTTON, lambda e: self._callback())

		self.printMaterialPLA.Bind(wx.EVT_RADIOBUTTON, lambda e: self._callback())
		self.printMaterialABS.Bind(wx.EVT_RADIOBUTTON, lambda e: self._callback())
		if profile.getMachineSetting('machine_type') == 'lulzbot_mini' or profile.getMachineSetting('machine_type') == 'lulzbot_TAZ_5' or profile.getMachineSetting('machine_type') == 'lulzbot_TAZ_4':
			self.printMaterialHIPS.Bind(wx.EVT_RADIOBUTTON, lambda e: self._callback())

		self.printSupport.Bind(wx.EVT_CHECKBOX, lambda e: self._callback())
		self.printBrim.Bind(wx.EVT_CHECKBOX, lambda e: self._callback())

		self.loadSettings()

	def getSavedSettings(self):
		try:
			return pickle.loads(str(profile.getProfileSetting('simpleModeSettings')))
		except:
			return {}

	def loadSettings(self):
		settings = self.getSavedSettings()
		for item in settings.keys():
			if hasattr(self, item):
				getattr(self, item).SetValue(settings[item])

	def saveSettings(self):
		settings = {}
		settingItems = ['printTypeHigh', 'printTypeNormal', 'printTypeLow', 'printTypeJoris',
						'printMaterialHIPS', 'printMaterialABS', 'printMaterialPLA',
						'printSupport', 'printBrim']

		for item in settingItems:
			if hasattr(self, item):
				settings[item] = getattr(self, item).GetValue()

		profile.putProfileSetting('simpleModeSettings', pickle.dumps(settings))

	def setupSlice(self):
		self.saveSettings()

		put = profile.setTempOverride
		get = profile.getProfileSetting
		for setting in profile.settingsList:
			if not setting.isProfile():
				continue
			profile.setTempOverride(setting.getName(), setting.getDefault())

		settings = SimpleModeSettings.getSimpleSettings(self)
		for setting in settings:
			put(setting[0], setting[1])


	def updateProfileToControls(self):
		pass
