function Format-Files {
    Param($FileName)
    Write-Output "Running isort..."
    isort ./answers/$FileName
    Write-Output "Running black..."
    black ./answers/$FileName -l 100
    Write-Output "Running mypy..."
    mypy ./answers/$FileName --disallow-untyped-defs

}


$file = Read-Host -Prompt "Enter file name: "
Format-Files -FileName "$file.py"