function Run-Test([string]$Number) {
    $RootDir = "D:\GitRepos\coursera\course2\network_packet_processing_simulation"
    "$Number" | %{ type "$RootDir\tests\$_" } |  python "$RootDir\process_packages.py" > "D:\Output\$Number.txt"

    $Expected = "$RootDir\tests\$Number.a"
    $Actual = "D:\Output\$Number.txt"
    if(Compare-Object -ReferenceObject $(Get-Content $Expected) -DifferenceObject $(Get-Content $Actual)  -PassThru) {
    Write-Output "$Number=FAILED!"
}
Else {
    Write-Output "$Number=Success"
}
}

# 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 | %{ "{0:00}" -f $_} | %{ Run-Test $_ }