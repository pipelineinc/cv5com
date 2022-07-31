import win32com.client as win32

def safeDispatch(clsid):
    try:
        return win32.Dispatch(clsid)
    except Exception as e:
        print(e)
        return None
