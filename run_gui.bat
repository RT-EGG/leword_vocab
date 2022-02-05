@setlocal
@pushd %~dp0

call %~dp0venv\Scripts\activate
python scripts\run_gui.py
call deactivate

@popd
@endlocal

exit /b 0