import wx
from logicas.longitud import convertir_longitud
from logicas.peso import convertir_peso
from logicas.temperatura import convertir_temperatura
from logicas.datos import convertir_datos


class PanelUnaVariable(wx.Panel):

    def convertidor(self, event):
        valor = self.textbox.GetValue()
        opcion = self.destino
        
        if self.destino == "":
            self.resultado.SetLabel("Seleccione una unidad de destino")
            return

        if self.origen == "":
            self.resultado.SetLabel("Seleccione una unidad de origen")
            return

        if opcion in {"Centimetros" ,"Pulgadas", "Pies", "Yardas"}:
            resultado = convertir_longitud(valor, self.origen, opcion)

        elif opcion in {"Gramos", "Kilogramos", "Libras", "Toneladas", "Onzas"}:
            resultado = convertir_peso(valor, self.origen, opcion)
        
        elif opcion in {"Celsius", "Fahrenheit", "Kelvin"}:
            resultado = convertir_temperatura(valor, self.origen, opcion)

        elif opcion in {"Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"}:
            resultado = convertir_datos(valor, self.origen, opcion) 

        else:
            self.resultado.SetLabel("seleccione una opcion")
            return
            
        self.resultado.SetLabel(f"{resultado:g} {opcion}")
   

    def __init__(self, parent):
        super().__init__(parent)        
        
        # === NUEVOS CONTROLES EN EL PANEL ===
        self.label_magnitud = wx.StaticText(self, label="Magnitud:")
        self.combo_magnitud = wx.Choice(
            self, 
            choices=["Seleccionar...", "Longitud", "Peso", "Temperatura", "Datos Informáticos"]
        )
        self.combo_magnitud.SetSelection(0)

        self.label_destino_combo = wx.StaticText(self, label="Unidad Destino:")
        self.combo_destino = wx.Choice(self, choices=[])
        # ===================================

        self.textbox = wx.SpinCtrlDouble(
            self, value="0.00", size=(120,40), min=-1000000, max=1000000, inc=0.01
        )
        self.textbox.SetDigits(2)

        self.label = wx.StaticText(self, label="Seleccione una unidad de origen e ingrese un valor")
        self.label_destino = wx.StaticText(self, label="Destino: Ninguno")

        self.boton1 = wx.Button(self, label='Convertir', size=(100,40))
        self.boton_limpiar = wx.Button(self, label='Limpiar', size=(60,40))
        self.boton_volver = wx.Button(self, label="Volver", size=(100,40))
        
        self.combo_origen = wx.ComboBox(self, choices=[], style=wx.CB_READONLY)
                    
        self.resultado = wx.StaticText(self, label="")
        self.destino = ""
        self.origen = ""

        # Distribución con Sizers
        sizer_ppal = wx.BoxSizer(wx.VERTICAL)
        fila_selectores = wx.BoxSizer(wx.HORIZONTAL) # Nueva fila para magnitudes y destinos
        fila_datos = wx.BoxSizer(wx.HORIZONTAL)
        fila_botones = wx.BoxSizer(wx.HORIZONTAL)

        # Añadimos los nuevos componentes a su fila superior
        fila_selectores.Add(self.label_magnitud, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        fila_selectores.Add(self.combo_magnitud, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        fila_selectores.Add(self.label_destino_combo, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        fila_selectores.Add(self.combo_destino, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)

        fila_datos.Add(wx.StaticText(self, label="Origen:"), 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        fila_datos.Add(self.combo_origen, 1, wx.ALL | wx.CENTER, 10)
        fila_datos.Add(self.textbox, 1, wx.ALL | wx.CENTER, 10)
        
        fila_botones.Add(self.boton1, 1, wx.ALL | wx.CENTER, 10)
        fila_botones.Add(self.boton_limpiar, 1, wx.ALL | wx.CENTER, 10)

        sizer_ppal.Add(self.label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_ppal.Add(self.label_destino, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        
        # Insertamos las filas organizadas
        sizer_ppal.Add(fila_selectores, 0, wx.ALIGN_CENTER)
        sizer_ppal.Add(fila_datos, 0, wx.ALIGN_CENTER)
        sizer_ppal.Add(fila_botones, 0, wx.ALIGN_CENTER)
        
        sizer_ppal.Add(self.resultado, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)
        sizer_ppal.AddStretchSpacer()
        sizer_ppal.Add(self.boton_volver, 0, wx.ALL | wx.ALIGN_RIGHT, 10)

        self.SetSizer(sizer_ppal)
        
        # Enlaces de eventos
        self.boton1.Bind(wx.EVT_BUTTON, self.convertidor)
        self.boton_limpiar.Bind(wx.EVT_BUTTON, self.limpiar)
        self.boton_volver.Bind(wx.EVT_BUTTON, self.volver)
        self.combo_origen.Bind(wx.EVT_COMBOBOX, self.seleccionar_origen)
        
        # Binds para los nuevos menús interactivos del panel
        self.combo_magnitud.Bind(wx.EVT_CHOICE, self.on_cambiar_magnitud)
        self.combo_destino.Bind(wx.EVT_CHOICE, self.on_seleccionar_destino)

    def on_cambiar_magnitud(self, event):
        """Se ejecuta al elegir Longitud, Peso, etc. Llena el combo de Destino"""
        magnitud = self.combo_magnitud.GetStringSelection()
        self.combo_destino.Clear()
        self.combo_origen.Clear()
        self.destino = ""
        self.origen = ""
        self.label_destino.SetLabel("Destino: Ninguno")

        if magnitud == "Longitud":
            self.combo_destino.SetItems(["Centimetros", "Pies", "Pulgadas", "Yardas"])
        elif magnitud == "Peso":
            self.combo_destino.SetItems(["Gramos", "Kilogramos", "Libras", "Toneladas", "Onzas"])
        elif magnitud == "Temperatura":
            self.combo_destino.SetItems(["Celsius", "Fahrenheit", "Kelvin"])
        elif magnitud == "Datos Informáticos":
            self.combo_destino.SetItems(["Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"])

    def on_seleccionar_destino(self, event):
        """Se ejecuta al elegir la unidad Destino. Auto-llena las opciones de Origen descartando el duplicado"""
        self.destino = self.combo_destino.GetStringSelection()
        self.label_destino.SetLabel(f"Destino: {self.destino}")
        magnitud = self.combo_magnitud.GetStringSelection()
        
        # Lista base de opciones según la magnitud seleccionada
        opciones = []
        if magnitud == "Longitud":
            opciones = ["Centimetros", "Pies", "Pulgadas", "Yardas"]
        elif magnitud == "Peso":
            opciones = ["Gramos", "Kilogramos", "Libras", "Toneladas", "Onzas"]
        elif magnitud == "Temperatura":
            opciones = ["Celsius", "Fahrenheit", "Kelvin"]
        elif magnitud == "Datos Informáticos":
            opciones = ["Bits", "Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"]

        # Filtramos para que la unidad origen no sea igual a la unidad destino
        opciones_filtradas = [o for o in opciones if o != self.destino]
        
        self.combo_origen.Clear()
        self.combo_origen.AppendItems(opciones_filtradas)
        self.combo_origen.SetSelection(0)
        self.origen = self.combo_origen.GetValue()

    def seleccionar_origen(self, event):
        self.origen = self.combo_origen.GetValue()

    def limpiar(self, event):
        self.textbox.SetValue(0.0)
        self.resultado.SetLabel("")
        self.destino = ""
        self.origen = ""
        self.combo_origen.Clear()
        self.combo_destino.Clear()
        self.label_destino.SetLabel("Destino: Ninguno") 
        if event:
            self.combo_magnitud.SetSelection(0)

    def volver(self, event):
        ventana = self.GetParent()
        if ventana.parent:
            ventana.parent.Show()
        ventana.Close()     
    

class VentanaUnaVariable(wx.Frame):

    def __init__(self, parent = None):
        super().__init__(parent, title='convertidor de unidades', size=(750, 450)) # Ajuste leve de tamaño
        self.parent = parent
        self.panel = PanelUnaVariable(self)

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        self.menu_salir = file_menu.Append(wx.ID_EXIT , "salir")
        
        # Submenús clásicos de arriba
        menu_longitud = wx.Menu()
        self.long_cm = menu_longitud.Append(wx.ID_ANY, "Centimetros")
        self.long_pies = menu_longitud.Append(wx.ID_ANY, "Pies")       
        self.long_pulgadas = menu_longitud.Append(wx.ID_ANY, "Pulgadas")
        self.long_yardas = menu_longitud.Append(wx.ID_ANY, "Yardas")

        menu_peso = wx.Menu()
        self.m_gr = menu_peso.Append(wx.ID_ANY, "Gramos")
        self.m_kg = menu_peso.Append(wx.ID_ANY, "Kilogramos")
        self.m_lb = menu_peso.Append(wx.ID_ANY, "Libras")
        self.m_tone = menu_peso.Append(wx.ID_ANY, "Toneladas")
        self.m_onzas = menu_peso.Append(wx.ID_ANY, "Onzas")

        menu_temp = wx.Menu()
        self.temp_c = menu_temp.Append(wx.ID_ANY, "Celsius")
        self.temp_f = menu_temp.Append(wx.ID_ANY, "Fahrenheit")
        self.temp_k = menu_temp.Append(wx.ID_ANY, "Kelvin")

        menu_datos = wx.Menu()
        self.datos_bit = menu_datos.Append(wx.ID_ANY, "Bits")
        self.datos_byt = menu_datos.Append(wx.ID_ANY, "Bytes")
        self.datos_kb = menu_datos.Append(wx.ID_ANY, "Kilobytes")
        self.datos_mb = menu_datos.Append(wx.ID_ANY, "Megabytes")
        self.datos_gb = menu_datos.Append(wx.ID_ANY, "Gigabytes")
        self.datos_tb = menu_datos.Append(wx.ID_ANY, "Terabytes")

        menu_convertir = wx.Menu()
        menu_convertir.AppendSubMenu(menu_longitud, "longitud")
        menu_convertir.AppendSubMenu(menu_peso, "peso")
        menu_convertir.AppendSubMenu(menu_temp, "temperatura")
        menu_convertir.AppendSubMenu(menu_datos, "datos informaticos")

        menu_bar.Append(file_menu, "archivo")
        menu_bar.Append(menu_convertir, "convertir")
        self.SetMenuBar(menu_bar)
        
        self.Bind(wx.EVT_MENU, self.salir, self.menu_salir)
        
        # Enlaces de barras de menú (Sincronizan los nuevos combos en pantalla)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Longitud", "Centimetros"), self.long_cm)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Longitud", "Pies"), self.long_pies)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Longitud", "Pulgadas"), self.long_pulgadas)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Longitud", "Yardas"), self.long_yardas)

        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Peso", "Gramos"), self.m_gr)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Peso", "Kilogramos"), self.m_kg)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Peso", "Libras"), self.m_lb)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Peso", "Toneladas"), self.m_tone)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Peso", "Onzas"), self.m_onzas)

        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Temperatura", "Celsius"), self.temp_c)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Temperatura", "Fahrenheit"), self.temp_f)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Temperatura", "Kelvin"), self.temp_k)

        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Datos Informáticos", "Bits"), self.datos_bit)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Datos Informáticos", "Bytes"), self.datos_byt)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Datos Informáticos", "Kilobytes"), self.datos_kb)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Datos Informáticos", "Megabytes"), self.datos_mb)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Datos Informáticos", "Gigabytes"), self.datos_gb)
        self.Bind(wx.EVT_MENU, lambda e: self.forzar_seleccion_pantalla("Datos Informáticos", "Terabytes"), self.datos_tb)

        self.Bind(wx.EVT_CLOSE, self.al_cerrar)
        self.Show()

    def forzar_seleccion_pantalla(self, magnitud, destino):
        """Asistente para que al usar el menú clásico superior se actualice la vista del panel"""
        self.panel.combo_magnitud.SetStringSelection(magnitud)
        self.panel.on_cambiar_magnitud(None)
        self.panel.combo_destino.SetStringSelection(destino)
        self.panel.on_seleccionar_destino(None)

    def salir(self, event):
        if self.parent:
            self.parent.Show()
        self.Close()

    def al_cerrar(self, event):
        if self.parent:
            self.parent.Show()
        event.Skip()    


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = VentanaUnaVariable()
    app.MainLoop()