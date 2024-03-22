from handleobjects import PythonSE

PythonSEInstance = PythonSE()


class TestCases:
    def test_handleinputandradio(self):
        PythonSEInstance.HandleInputandRadio()

    def test_handledropdown(self):
        PythonSEInstance.HandleDropdown()

    def test_handlemultidropdown(self):
        PythonSEInstance.HandleMultiDropdown()

    def test_handlebootstrapdropdown(self):
        PythonSEInstance.HandleBootstrapDropdown()

    def test_handleautosuggestion(self):
        PythonSEInstance.HandleAutoSuggestion()

    def test_handlehiddenitems(self):
        PythonSEInstance.HandleHiddenItems()

    def test_handledialogalerts(self):
        PythonSEInstance.HandleDialogAlerts()

    def test_handleframesiframes(self):
        PythonSEInstance.HandleFramesiFrames()

    def test_handlewebtablepagination(self):
        PythonSEInstance.HandleWebTablePagination()

    def test_handledatepickers(self):
        PythonSEInstance.HandleDatePickers()

    def test_handlemouseactions(self):
        PythonSEInstance.HandleMouseActions()

    def test_handlekeyboardactions(self):
        PythonSEInstance.HandleKeyboardActions()

    def test_handleuploadfiles(self):
        PythonSEInstance.HandleUploadFiles()

    def test_handlepageswindows(self):
        PythonSEInstance.HandlePagesWindows()

    def test_handlemultiplepageswindows(self):
        PythonSEInstance.HandleMultiplePagesWindows()

    def test_handlecapturescreen(self):
        PythonSEInstance.HandleCaptureScreen()

    def test_handleusingclass(self):
        PythonSEInstance.HandleUsingClass()

    def test_executionend(self):
        PythonSEInstance.ExecutionEnd()

# to execute > terminal > pytest .\tests\test_handleobjects.py --html=.\reports\report1.html
