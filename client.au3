
;~ _HTTP_Upload ( string $sURL , string $sFilePath , string $sFileField , string $sPostData = '' , string $sFilename = Default)

#include <HTTP.au3>
$sURL = 'http://localhost:3005/upload'
$sFilePath = 'gohan.png'

;~ $test = _HTTP_Upload("http://mysite/index.php", @ScriptDir & "\myFile.txt", "uploadinput", "pwd=123&filename=" & URLEncode("test.txt") )
$sFileField = 'Images'
$x = _HTTP_Upload($sURL,$sFilePath,$sFileField)


MsgBox(0,0,$x)