# Define paths
$ramlFilePath = "C:\jexxl-api\raml\api-doc.raml"
$themePath = "C:\jexxl-api\raml\raml2html-jexxl-theme"
$outputFilePath = "C:\jexxl-api\flaskapp\templates\api-doc.html"

# Run raml2html command
raml2html $ramlFilePath --theme $themePath -o $outputFilePath

# Check if the command was successful
if ($LASTEXITCODE -eq 0) {
    Write-Output "API documentation generated successfully."
} else {
    Write-Error "Failed to generate API documentation."
}
