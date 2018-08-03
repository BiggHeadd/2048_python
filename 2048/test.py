import wx
import arrayTest

class Myframe(wx.Frame):
    PANEL_ORIG_POINT = wx.Point(15, 15)
    VALUE_COLOR_DEF = {
        0: "#CCC0B3",
        2: "#EEE4DA",
        4: "#EDE0C8",
        8: "#F2B179",
        16: "#F59563",
        32: "#F67C5F",
        64: "#F65E3B",
        128: "#EDCE72",
        256: "#EDCF72",
        512: "#EDCE72",
        1024: "#EDCF72",
        2048: "#EDCF72",
        4096: "#EDCF72",
        8192: "#EDCF72",
        16384: "#EDCF72",
        32768: "#EDCF72"
    }
    is_inited = False
    tile_values = arrayTest.init_array()
    array_pre = list()

    def __init__(self, title):
        super(Myframe, self).__init__(None, wx.ID_ANY, title=title, size=(500, 550))
        self.Bind(wx.EVT_PAINT, self.onPiant)
        self.Bind(wx.EVT_KEY_DOWN, self.on_key)
        self.Center()
        self.SetFocus()
        self.Show()



    def onPiant(self, event):
        self.draw_tiles()

    def draw_tiles(self):
        dc = wx.ClientDC(self)
        dc.SetBackground(wx.Brush("#FAF8EF"))
        dc.Clear()
        dc.SetBrush(wx.Brush("#C0B0A0"))
        dc.SetPen(wx.Pen("", 1, wx.TRANSPARENT))
        dc.DrawRoundedRectangle(self.PANEL_ORIG_POINT.x, self.PANEL_ORIG_POINT.y, 450, 450, 5)
        for row in range(4):
            for column in range(4):
                tile_value = self.tile_values[row][column]
                tile_color = self.VALUE_COLOR_DEF[tile_value]
                dc.SetBrush(wx.Brush(tile_color))
                dc.DrawRoundedRectangle(self.PANEL_ORIG_POINT.x + 110 * column + 10,
                                        self.PANEL_ORIG_POINT.y + 110 * row + 10, 100, 100, 5)
                dc.SetTextForeground("#707070")
                text_font = wx.Font(30, wx.SWISS, wx.NORMAL, wx.BOLD)
                dc.SetFont(text_font)
                if tile_value != 0:
                    size = dc.GetTextExtent(str(tile_value))
                    if size[0] > 100:
                        text_font = wx.Font(24, wx.SWISS, wx.NORMAL, wx.BOLD)
                        dc.SetFont(text_font)
                        size = dc.GetTextExtent(str(tile_value))
                    dc.DrawText(str(tile_value), self.PANEL_ORIG_POINT.x + 110 * column + 10 + (100 - size[0]) / 2,
                                self.PANEL_ORIG_POINT.y + 110 * row + 10 + (100 - size[1]) / 2)

    def test_update_tiles(self):
        self.tile_values = [[0, 2, 4, 8], [16, 32, 64, 128], [256, 512, 1024, 2048], [4096, 8192, 16384, 32768]]
        self.draw_tiles()


    def on_key(self, event):
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_UP:
            print("UP")
            self.tile_values = arrayTest.slide_up(self.tile_values)
            self.draw_tiles()
            if arrayTest.fail(self.tile_values):
                self.OnExit()
                self.tile_values = arrayTest.init_array()
            self.array_pre, self.tile_values = arrayTest.random_matrix(self.array_pre, self.tile_values)
        if key_code == wx.WXK_DOWN:
            print("DOWN")
            self.tile_values = arrayTest.slide_down(self.tile_values)
            self.draw_tiles()
            if arrayTest.fail(self.tile_values):
                self.OnExit()
                self.tile_values = arrayTest.init_array()
            self.array_pre, self.tile_values = arrayTest.random_matrix(self.array_pre, self.tile_values)

        if key_code == wx.WXK_LEFT:
            print("LEFT")
            self.tile_values = arrayTest.slide_left(self.tile_values)
            self.draw_tiles()
            if arrayTest.fail(self.tile_values):
                self.OnExit()
                self.tile_values = arrayTest.init_array()
            self.array_pre, self.tile_values = arrayTest.random_matrix(self.array_pre, self.tile_values)
        if key_code == wx.WXK_RIGHT:
            print("RIGHT")
            self.tile_values = arrayTest.slide_right(self.tile_values)
            self.draw_tiles()
            if arrayTest.fail(self.tile_values):
                self.OnExit()
                self.tile_values = arrayTest.init_array()
            self.array_pre, self.tile_values = arrayTest.random_matrix(self.array_pre, self.tile_values)

        if key_code == wx.WXK_SPACE:
            self.test_update_tiles()
            self.array_pre, self.tile_values = arrayTest.random_matrix(self.array_pre, self.tile_values)

    def OnExit(self):
        dlg = wx.MessageBox("GAME OVER", caption='Testing Complete', style=wx.OK | wx.ICON_INFORMATION)
class MyApp(wx.App):
    def OnInit(self):
        frame = Myframe("2048")
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()