# roadanalysis

A tool to analyse the roadrecon output and directly search for interesting information & paths.
Sometimes it is not that comfortable to search through plain users & groups. Therefore it's nice to have a tool to do the job for you and grab important information.

It needs the input, e.g. `roadrecon.db`, of the roadtools gather/dump and will process it.

## Usage

```cmd
roadanalysis get-membershiprules
# if the file / path is not current directory and named "roadrecon.db"
roadanalysis get-membershiprules roadoutput.db
```
