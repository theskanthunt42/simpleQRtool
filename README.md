# simpleQRtool
A simple tool to en/decode QR code written in Python with Qt 5
<br>
New here, Write noob code, Kinda a remake from my another project but didn't work out.
<br>
Write just for fun and learn.
<br>
Can Make and Read QR Code with some options
<br>
(Thanks to various useful module and advice provided by the community)
<br>

### Task List
<br>

- [x] At least it works with decode/encode QR Codes
- [ ] More options in config.json
- [ ] Support more than PNG files
- [ ] Better Qt Interface(Scale, Stretch stuff like that)
- [x] Export using QFileDialog instead of just forcing output to Output/
- [x] Real tmp file using Tempfile
- [x] Check if is working on other platform like Windows
- [ ] Better overall stability
<br>

### Explainations
config.json:
        <br>
        Config some addtional setting other than GUI side provide, Like `background_color` And `color`... etc
        <br>
        `background_color` is for the `back_color` from `qrcode.QRCode.make_image`, defaults to `white`
        <br>
        And `color` if for the `fill_color` in `qrcode.QRCode.make_image`, defaults to `black`
        <br>
        `error_corrections` is for the `error_correction` from `qrcode.constants`, defaults to `0`
        <br>
        According to `constants.py`, You can set the value as:
        <br>
            # QR error correct levels
            <br>
            ERROR_CORRECT_L = 1
            <br>
            ERROR_CORRECT_M = 0
            <br>
            ERROR_CORRECT_Q = 3
            <br>
            ERROR_CORRECT_H = 2
        <br>
        `box_size`:
        <br>
        > controls how many pixels each "box" of QR code is. 
        > - https://pypi.org/project/qrcode/
        <br>
        Defaults to `10`
        <br>
        `border`:
        <br>
        > The border parameter controls how many boxes thick the border should be
        > - https://pypi.org/project/qrcode/
        <br>
        Defaults to `4`
    <br>
    Encoding section from the GUI:
        <br>
        You can use mutiple encoding method to generate QR Code with UTF-8(Defaulf) ASCII and Shift-JIS(Since I am a weeb, And its the only reason I add this)
        <br>
        But still not sure it's actually working or not.
<br>

### Requirements
python-qrcode(Or pyqrcode)
    <br>
    https://github.com/lincolnloop/python-qrcode
    <br>
    pyzbar
    <br>
    https://github.com/NaturalHistoryMuseum/pyzbar
    <br>
    PyQt5
    <br>
    https://pypi.org/project/PyQt5/
    <br>
    If still didn't work, Try install pillow Or...
    <br>
    It might just not working on anyother OS other than Linux
<br>

### For more
If I did anything wrong or u just wanna suggestions, Or I should del this, U can create a issues or contact me by using:
        the42game@rosehip.moe (Might wait for a long time till reply)
        <br>
        Or @the42game:chat.rosehip.moe on Matrix