# Tach - VS Code Extension


### Setup
1. Install the extension and you should see invalid imports highlighted as errors on save.
2. Navigate to the settings for the extension in `Extensions > Tach` to set arguments if needed. 
3. Run `Tach: Restart Server` from the command palette (`CMD+SHFT+P`) to restart the server.

If you run into any issues, let us know by either reaching out on [Discord](https://discord.gg/a58vW8dnmw) or submitting a [Github Issue](https://github.com/gauge-sh/tach/issues)!


### Known Issues
To diagnose an issue, use 'Output: Focus on Output View' in the VSCode Command Palette, and then select 'Tach' from the dropdown selector to see the logs.

- 'Project config root not found': this means you don't have a `tach.toml` in the ancestors of an open file. This should generally be in the root of your repo.
- 'ModuleNotFoundError: No module named 'tach.extension': this means your version of Python doesn't match the version which our bundled Tach expects, try adjusting the 'Import Strategy' for your Tach extension to 'useEnvironment' and see [this issue](https://github.com/gauge-sh/tach-vscode/issues/13)