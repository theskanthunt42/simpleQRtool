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
Task List:
<br>
- [x] At least it works with decode/encode QR Codes
- [ ] More options in config.json
- [ ] Better Qt Interface(Scale, Stretch stuff like that)
- [ ] Export using QFileDialog instead of just forcing output to Output/
- [ ] Real tmp file using Tempfile
- [ ] Check if is working on other platform like Windows
- [ ] Better overall stability
<br>
Explainations:
<br>
    config.json:
        <br>
        Config some addtional setting other than GUI side provide, Like ```
        background_color```And ```color```
        <br>
        ```background_color``` is for the ```back_color``` from ```qrcode.QRCode.make_image```
        <br>
        And ```color``` if for the ```fill_color``` in ```qrcode.QRCode.make_image```
        <br>
        Will add more later.
<br>
Requirements:
<br>
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