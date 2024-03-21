import handleobjects

handleobjectsinstance = handleobjects


class TestCases:
    def test_handleinputandradio(self):
        handleobjectsinstance.HandleInputandRadio()

    def test_handledropdown(self):
        handleobjectsinstance.HandleDropdown()

    def test_handlemultidropdown(self):
        handleobjectsinstance.HandleMultiDropdown()

    def test_handlebootstrapdropdown(self):
        handleobjectsinstance.HandleBootstrapDropdown()

    def test_handleautosuggestion(self):
        handleobjectsinstance.HandleAutoSuggestion()

    def test_handlehiddenitems(self):
        handleobjectsinstance.HandleHiddenItems()

    def test_handledialogalerts(self):
        handleobjectsinstance.HandleDialogAlerts()

    def test_handleframesiframes(self):
        handleobjectsinstance.HandleFramesiFrames()

    def test_handlewebtablepagination(self):
        handleobjectsinstance.HandleWebTablePagination()

    def test_handledatepickers(self):
        handleobjectsinstance.HandleDatePickers()

    def test_handlemouseactions(self):
        handleobjectsinstance.HandleMouseActions()

    def test_handlekeyboardactions(self):
        handleobjectsinstance.HandleKeyboardActions()

    def test_handleuploadfiles(self):
        handleobjectsinstance.HandleUploadFiles()

    def test_handlepageswindows(self):
        handleobjectsinstance.HandlePagesWindows()

    def test_handlemultiplepageswindows(self):
        handleobjectsinstance.HandleMultiplePagesWindows()

    def test_handlecapturescreen(self):
        handleobjectsinstance.HandleCaptureScreen()

    def test_handleusingclass(self):
        handleobjectsinstance.HandleUsingClass()

    def test_executionend(self):
        handleobjectsinstance.ExecutionEnd()

# to execute > terminal > pytest .\tests\test_handleobjects.py --html=.\reports\report1.html
