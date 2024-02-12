function Test-IfNotCI($IfTrue)
{
    If ($null -eq $env:CI)
    {
        If ($IfTrue -is "ScriptBlock")
        {
            &$IfTrue
        }
        Else
        {
            $IfTrue
        }
    }
}
